"""Book writer — orchestrates outline → chapters → book."""
from __future__ import annotations
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any
from .config import Config
from .corpus import Corpus
from .outline import Outline, OutlineBuilder
from .themes import ThemeIndex

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def _slug(text: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in text)
    while "--" in s: s = s.replace("--", "-")
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
        self.outline_builder = OutlineBuilder(corpus=corpus, cfg=self.cfg, theme_index=self.theme_index)

    def write(self, *, theme: str, chapters: int | None = None, persist: bool = True, **kw) -> Book:
        t0 = time.time()
        outline = self.outline_builder.build(theme=theme, chapters=chapters)
        written = []
        for ch in outline.chapters:
            written.append(WrittenChapter(number=ch.number, title=ch.title,
                                         thesis=ch.thesis, body="(placeholder)",
                                         key_refs=ch.key_refs))
        book = Book(theme=theme, title=outline.title, subtitle=outline.subtitle,
                    epigraph=outline.epigraph, preface_sketch=outline.preface_sketch,
                    chapters=written, outline=outline,
                    metadata={"generated_at": _now_iso(), "generator": "URANTiOS BookWriter",
                              "generator_version": "1.0.0", "model": self.cfg.model,
                              "word_count_estimate": book.word_count() if False else 0,
                              "wall_time_seconds": round(time.time()-t0, 2)})
        if persist and self.vault:
            paths = self.vault.save(book)
            book.metadata["written_to"] = [str(p) for p in paths]
        return book
