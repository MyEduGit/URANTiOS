"""
Outline generation.

The ``OutlineBuilder`` takes a theme and produces a structured book
outline (title, epigraph, chapters, beats, citation anchors) by calling
Claude against a carefully selected evidence set from the corpus.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from typing import Any

from .config import Config
from .corpus import Corpus, Paragraph
from .llm import ClaudeClient, DryRunClient, make_client
from .prompts import OUTLINE_INSTRUCTIONS, SYSTEM_PREAMBLE
from .themes import ThemeIndex


@dataclass
class Chapter:
    number: int
    title: str
    thesis: str
    key_refs: list[str] = field(default_factory=list)
    beats: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Outline:
    theme: str
    title: str
    subtitle: str | None
    epigraph: str | None
    preface_sketch: str | None
    chapters: list[Chapter]
    evidence_refs: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "theme": self.theme,
            "title": self.title,
            "subtitle": self.subtitle,
            "epigraph": self.epigraph,
            "preface_sketch": self.preface_sketch,
            "chapters": [c.to_dict() for c in self.chapters],
            "evidence_refs": self.evidence_refs,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any], *, theme: str | None = None) -> "Outline":
        return cls(
            theme=theme or d.get("theme", ""),
            title=d.get("title", "Untitled"),
            subtitle=d.get("subtitle"),
            epigraph=d.get("epigraph"),
            preface_sketch=d.get("preface_sketch"),
            chapters=[
                Chapter(
                    number=c.get("number", i + 1),
                    title=c.get("title", f"Chapter {i+1}"),
                    thesis=c.get("thesis", ""),
                    key_refs=list(c.get("key_refs", [])),
                    beats=list(c.get("beats", [])),
                )
                for i, c in enumerate(d.get("chapters", []))
            ],
            evidence_refs=list(d.get("evidence_refs", [])),
        )


# ---------------------------------------------------------------------------

class OutlineBuilder:
    def __init__(
        self,
        *,
        corpus: Corpus,
        cfg: Config,
        theme_index: ThemeIndex | None = None,
        client: ClaudeClient | DryRunClient | None = None,
    ):
        self.corpus = corpus
        self.cfg = cfg
        self.theme_index = theme_index or ThemeIndex(corpus)
        self.client = client or make_client(cfg)

    # ------------------------------------------------------------------
    def build(
        self,
        *,
        theme: str,
        chapters: int | None = None,
        style: str | None = None,
        audience: str = "spiritually curious adults",
        voice: str = "a scholar who has also knelt",
        words_per_chapter: int | None = None,
        evidence_k: int = 60,
    ) -> Outline:
        chapters = chapters or self.cfg.default_chapters
        style = style or self.cfg.default_style
        words_per_chapter = words_per_chapter or self.cfg.default_words_per_chapter

        evidence = self.theme_index.select_evidence(
            theme, k=evidence_k, diversify=True
        )
        system_blocks = _system_blocks(self.cfg, evidence)

        user = OUTLINE_INSTRUCTIONS.format(
            theme=theme,
            style=style,
            audience=audience,
            chapters=chapters,
            words_per_chapter=words_per_chapter,
            voice=voice,
        )

        resp = self.client.complete(
            system_blocks=system_blocks,
            messages=[{"role": "user", "content": user}],
            model=self.cfg.model,
            max_tokens=self.cfg.max_tokens_outline,
            thinking_budget=self.cfg.thinking_budget_outline,
        )

        data = _parse_json(resp.text)
        outline = Outline.from_dict(data, theme=theme)
        outline.evidence_refs = [p.ref for p in evidence]
        return outline


# ---------------------------------------------------------------------------
# Shared: system blocks with prompt caching
# ---------------------------------------------------------------------------

def _system_blocks(cfg: Config, evidence: list[Paragraph]) -> list[dict[str, Any]]:
    """Construct the Anthropic system prompt as an array of blocks.

    We cache:
      1. The preamble (Three Values + authorial principles) — small, stable.
      2. The evidence set — potentially large per book but stable across
         all chapter calls for that book.
    """
    preamble = SYSTEM_PREAMBLE.format(charter=cfg.values.charter)

    evidence_text = "EVIDENCE SET — selected paragraphs from The Urantia Book:\n\n" + "\n\n".join(
        f"[{p.ref}] {p.content}" for p in evidence
    )

    blocks: list[dict[str, Any]] = [
        {"type": "text", "text": preamble},
        {"type": "text", "text": evidence_text},
    ]

    if cfg.enable_prompt_cache:
        # Cache both the preamble and the evidence — the big win is on
        # evidence, which is identical across every chapter call.
        blocks[0]["cache_control"] = {"type": "ephemeral"}
        blocks[1]["cache_control"] = {"type": "ephemeral"}

    return blocks


# ---------------------------------------------------------------------------

_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)


def _parse_json(text: str) -> dict[str, Any]:
    """Extract the first JSON object from ``text``.

    Tolerates stray code fences or surrounding prose; falls back to a
    brace-balancing scan if direct parse fails.
    """
    text = text.strip()
    # Fenced?
    m = _JSON_FENCE_RE.search(text)
    if m:
        text = m.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Brace-balancing fallback
    start = text.find("{")
    if start < 0:
        raise ValueError(f"No JSON object found in model output: {text[:200]!r}")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                candidate = text[start : i + 1]
                return json.loads(candidate)
    raise ValueError("Unbalanced JSON braces in model output")
