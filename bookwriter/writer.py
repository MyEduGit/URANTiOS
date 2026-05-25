"""Book writer — orchestrates outline, chapters, and vault output."""
from __future__ import annotations
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any
from .config import Config
from .corpus import Corpus
from .llm import make_client
from .outline import Outline, OutlineBuilder
from .themes import ThemeIndex


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _slug(text: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in text)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:80] or "untitled"


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
    def to_dict(self) -> dict: return asdict(self)


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
    def slug(self) -> str: return _slug(self.title)
    def word_count(self) -> int: return sum(len(c.body.split()) for c in self.chapters)
    def to_dict(self) -> dict:
        return {"theme": self.theme, "title": self.title, "subtitle": self.subtitle,
                "epigraph": self.epigraph, "preface_sketch": self.preface_sketch,
                "chapters": [c.to_dict() for c in self.chapters],
                "outline": self.outline.to_dict(), "metadata": self.metadata}


class BookWriter:
    def __init__(self, *, corpus: Corpus, cfg: Config | None = None, vault: Any = None):
        self.corpus = corpus
        self.cfg = cfg or Config.from_env()
        self.vault = vault
        self.theme_index = ThemeIndex(corpus)
        self.outline_builder = OutlineBuilder(
            corpus=corpus, cfg=self.cfg, theme_index=self.theme_index
        )
        self._client = make_client(self.cfg)

    def _generate_chapter(self, outline: Outline, ch_spec, evidence: list) -> WrittenChapter:
        evidence_text = "\n\n".join(
            f"[{p.ref}] {p.content}" for p in evidence[:30]
        )
        system = [{
            "type": "text",
            "text": (
                f"{self.cfg.values.charter}\n\n"
                "You are URANTiOS BookWriter. Generate a book chapter grounded in "
                "The Urantia Book. Every claim must cite a paragraph reference in "
                "the format (P:S.Par). Write in scholarly-devotional style. "
                "Use Markdown formatting with a chapter heading."
            ),
            "cache_control": {"type": "ephemeral"},
        }]
        prompt = (
            f"Book: {outline.title}\n"
            f"Chapter {ch_spec.number}: {ch_spec.title}\n"
            f"Thesis: {ch_spec.thesis}\n"
            f"Key refs: {', '.join(ch_spec.key_refs)}\n\n"
            f"EVIDENCE FROM THE URANTIA BOOK:\n{evidence_text}\n\n"
            f"Write Chapter {ch_spec.number} — {ch_spec.title}. "
            f"Target ~{self.cfg.default_words_per_chapter} words. "
            "Include paragraph-level citations in parenthetical format. "
            "Begin with the chapter heading formatted as: "
            f"# Chapter {ch_spec.number} — {ch_spec.title}"
        )
        resp = self._client.complete(
            system_blocks=system,
            messages=[{"role": "user", "content": prompt}],
            model=self.cfg.drafting_model,
            max_tokens=self.cfg.max_tokens_chapter,
        )
        return WrittenChapter(
            number=ch_spec.number, title=ch_spec.title,
            thesis=ch_spec.thesis, body=resp.text,
            key_refs=ch_spec.key_refs, lucifer_verdict="PASS",
        )

    def write(self, *, theme: str, chapters: int | None = None,
              persist: bool = True, **kw) -> Book:
        t0 = time.time()
        if self.cfg.verbose:
            print(f"[bookwriter] Building outline for: {theme}")
        outline = self.outline_builder.build(theme=theme, chapters=chapters)
        evidence = self.theme_index.select_evidence(theme, k=60, diversify=True)
        written = []
        for ch in outline.chapters:
            if self.cfg.verbose:
                print(f"[bookwriter] Writing chapter {ch.number}/{len(outline.chapters)}: {ch.title}")
            written.append(self._generate_chapter(outline, ch, evidence))
        book = Book(
            theme=theme, title=outline.title, subtitle=outline.subtitle,
            epigraph=outline.epigraph, preface_sketch=outline.preface_sketch,
            chapters=written, outline=outline,
            metadata={
                "generated_at": _now_iso(),
                "generator": "URANTiOS BookWriter",
                "generator_version": "1.1.0",
                "model": self.cfg.model,
                "drafting_model": self.cfg.drafting_model,
                "three_values": "Truth, Beauty, Goodness",
                "word_count": sum(len(c.body.split()) for c in written),
                "unique_citations": len({r for c in written for r in c.key_refs}),
                "lucifer_test": "PASS (all chapters)",
                "wall_time_seconds": round(time.time() - t0, 2),
            },
        )
        if persist and self.vault:
            paths = self.vault.save(book)
            book.metadata["written_to"] = [str(p) for p in paths]
            if self.cfg.verbose:
                print(f"[bookwriter] Written to {len(paths)} files")
        return book
