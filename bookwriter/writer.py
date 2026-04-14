"""
Chapter writer and book assembler.

``BookWriter.write(theme=...)`` is the single high-level entry point:
  1. Build the evidence set with the ``ThemeIndex``.
  2. Generate an outline via ``OutlineBuilder``.
  3. For each chapter: draft → (optional) Lucifer critique → revise.
  4. Assemble the ``Book`` object.
  5. Hand off to a vault for persistence.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Config
from .corpus import Corpus, Paragraph
from .llm import ClaudeClient, DryRunClient, make_client
from .outline import Outline, OutlineBuilder, _system_blocks
from .prompts import (
    CHAPTER_INSTRUCTIONS,
    LUCIFER_CRITIQUE_INSTRUCTIONS,
    REVISION_INSTRUCTIONS,
)
from .themes import ThemeIndex


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug(text: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in text)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:80] or "untitled"


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass
class WrittenChapter:
    number: int
    title: str
    thesis: str
    body: str
    key_refs: list[str] = field(default_factory=list)
    critique: str | None = None
    revision_count: int = 0
    lucifer_verdict: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Book:
    theme: str
    title: str
    subtitle: str | None
    epigraph: str | None
    preface_sketch: str | None
    chapters: list[WrittenChapter]
    outline: Outline
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def slug(self) -> str:
        return _slug(self.title)

    def word_count(self) -> int:
        return sum(len(c.body.split()) for c in self.chapters)

    def to_dict(self) -> dict[str, Any]:
        return {
            "theme": self.theme,
            "title": self.title,
            "subtitle": self.subtitle,
            "epigraph": self.epigraph,
            "preface_sketch": self.preface_sketch,
            "chapters": [c.to_dict() for c in self.chapters],
            "outline": self.outline.to_dict(),
            "metadata": self.metadata,
        }


# ---------------------------------------------------------------------------
# Writer
# ---------------------------------------------------------------------------

class BookWriter:
    """Top-level orchestrator."""

    def __init__(
        self,
        *,
        corpus: Corpus,
        cfg: Config | None = None,
        theme_index: ThemeIndex | None = None,
        client: ClaudeClient | DryRunClient | None = None,
        vault: Any | None = None,   # MultiVault or ObsidianVault
    ):
        self.corpus = corpus
        self.cfg = cfg or Config.from_env()
        self.theme_index = theme_index or ThemeIndex(corpus)
        self.client = client or make_client(self.cfg)
        self.vault = vault
        self.outline_builder = OutlineBuilder(
            corpus=corpus,
            cfg=self.cfg,
            theme_index=self.theme_index,
            client=self.client,
        )

    # ------------------------------------------------------------------
    def write(
        self,
        *,
        theme: str,
        chapters: int | None = None,
        style: str | None = None,
        audience: str = "spiritually curious adults",
        voice: str = "a scholar who has also knelt",
        words_per_chapter: int | None = None,
        evidence_k: int = 60,
        persist: bool = True,
    ) -> Book:
        """Write an entire book end-to-end."""
        t0 = time.time()
        self._log(f"— Writing book on theme: {theme!r}")
        self._log(f"— Corpus stats: {self.corpus.stats()}")

        # Outline -------------------------------------------------------
        outline = self.outline_builder.build(
            theme=theme,
            chapters=chapters,
            style=style,
            audience=audience,
            voice=voice,
            words_per_chapter=words_per_chapter,
            evidence_k=evidence_k,
        )
        self._log(
            f"— Outline ready: {outline.title!r} "
            f"({len(outline.chapters)} chapters, "
            f"{len(outline.evidence_refs)} evidence paragraphs)"
        )

        # Shared evidence: reuse the outline's evidence set (same for all
        # chapters → prompt cache hit).
        evidence = [self.corpus.paragraph(ref) for ref in outline.evidence_refs]
        system_blocks = _system_blocks(self.cfg, evidence)

        # Chapters ------------------------------------------------------
        written: list[WrittenChapter] = []
        for ch in outline.chapters:
            self._log(f"  • Drafting chapter {ch.number}: {ch.title}")
            wc = self._write_chapter(
                outline=outline,
                chapter=ch,
                system_blocks=system_blocks,
                style=style or self.cfg.default_style,
                voice=voice,
                words=words_per_chapter or self.cfg.default_words_per_chapter,
            )
            written.append(wc)

        book = Book(
            theme=theme,
            title=outline.title,
            subtitle=outline.subtitle,
            epigraph=outline.epigraph,
            preface_sketch=outline.preface_sketch,
            chapters=written,
            outline=outline,
            metadata={
                "generated_at": _now_iso(),
                "generator": "URANTiOS BookWriter",
                "generator_version": "1.0.0",
                "model": self.cfg.model,
                "drafting_model": self.cfg.drafting_model,
                "revision_passes": self.cfg.revision_passes,
                "lucifer_test": self.cfg.enable_lucifer_test,
                "word_count_estimate": sum(
                    len(c.body.split()) for c in written
                ),
                "wall_time_seconds": round(time.time() - t0, 2),
                "three_values": asdict(self.cfg.values),
            },
        )

        if persist and self.vault is not None:
            written_paths = self.vault.save(book)
            book.metadata["written_to"] = [str(p) for p in written_paths]
            self._log(f"— Persisted to {len(written_paths)} location(s)")

        self._log(
            f"— Done. {book.word_count():,} words in "
            f"{book.metadata['wall_time_seconds']}s."
        )
        return book

    # ------------------------------------------------------------------
    def _write_chapter(
        self,
        *,
        outline: Outline,
        chapter,
        system_blocks: list[dict[str, Any]],
        style: str,
        voice: str,
        words: int,
    ) -> WrittenChapter:
        user = CHAPTER_INSTRUCTIONS.format(
            number=chapter.number,
            book_title=outline.title,
            title=chapter.title,
            thesis=chapter.thesis,
            beats="\n".join(f"  - {b}" for b in chapter.beats),
            key_refs="\n".join(f"  - ({r})" for r in chapter.key_refs),
            words=words,
            voice=voice,
            style=style,
        )
        resp = self.client.complete(
            system_blocks=system_blocks,
            messages=[{"role": "user", "content": user}],
            model=self.cfg.drafting_model,
            max_tokens=self.cfg.max_tokens_chapter,
            thinking_budget=self.cfg.thinking_budget_chapter,
        )
        body = resp.text.strip()

        wc = WrittenChapter(
            number=chapter.number,
            title=chapter.title,
            thesis=chapter.thesis,
            body=body,
            key_refs=list(chapter.key_refs),
        )

        # Revision pass -------------------------------------------------
        for _ in range(self.cfg.revision_passes):
            if not self.cfg.enable_lucifer_test:
                break
            critique = self._lucifer_test(wc.body, system_blocks)
            wc.critique = critique
            wc.lucifer_verdict = _extract_verdict(critique)
            if wc.lucifer_verdict == "PASS":
                break
            # Revise
            rev_user = REVISION_INSTRUCTIONS.format(
                critique=critique, chapter_text=wc.body
            )
            rev = self.client.complete(
                system_blocks=system_blocks,
                messages=[{"role": "user", "content": rev_user}],
                model=self.cfg.model,   # use the stronger model for revision
                max_tokens=self.cfg.max_tokens_chapter,
                thinking_budget=self.cfg.thinking_budget_chapter,
            )
            wc.body = rev.text.strip()
            wc.revision_count += 1
        return wc

    def _lucifer_test(self, chapter_text: str, system_blocks) -> str:
        user = LUCIFER_CRITIQUE_INSTRUCTIONS.format(chapter_text=chapter_text)
        resp = self.client.complete(
            system_blocks=system_blocks,
            messages=[{"role": "user", "content": user}],
            model=self.cfg.model,
            max_tokens=1500,
            thinking_budget=0,
        )
        return resp.text.strip()

    # ------------------------------------------------------------------
    def _log(self, msg: str) -> None:
        if self.cfg.verbose:
            print(msg)


# ---------------------------------------------------------------------------

def _extract_verdict(critique: str) -> str | None:
    upper = critique.upper()
    for verdict in ("PASS", "REVISE", "FAIL"):
        if verdict in upper:
            return verdict
    return None
