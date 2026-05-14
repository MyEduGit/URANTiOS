"""Outline generation for BookWriter."""
from __future__ import annotations
import json, re
from dataclasses import dataclass, field, asdict
from typing import Any
from .config import Config
from .corpus import Corpus, Paragraph
from .themes import ThemeIndex

@dataclass
class Chapter:
    number: int
    title: str
    thesis: str
    key_refs: list[str] = field(default_factory=list)
    beats: list[str] = field(default_factory=list)
    def to_dict(self) -> dict: return asdict(self)

@dataclass
class Outline:
    theme: str
    title: str
    subtitle: str | None
    epigraph: str | None
    preface_sketch: str | None
    chapters: list[Chapter]
    evidence_refs: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"theme": self.theme, "title": self.title, "subtitle": self.subtitle,
                "epigraph": self.epigraph, "preface_sketch": self.preface_sketch,
                "chapters": [c.to_dict() for c in self.chapters],
                "evidence_refs": self.evidence_refs}

    @classmethod
    def from_dict(cls, d: dict, *, theme: str = "") -> "Outline":
        return cls(
            theme=theme or d.get("theme", ""),
            title=d.get("title", "Untitled"),
            subtitle=d.get("subtitle"),
            epigraph=d.get("epigraph"),
            preface_sketch=d.get("preface_sketch"),
            chapters=[Chapter(number=c.get("number", i+1), title=c.get("title", f"Chapter {i+1}"),
                              thesis=c.get("thesis", ""), key_refs=list(c.get("key_refs", [])),
                              beats=list(c.get("beats", [])))
                      for i, c in enumerate(d.get("chapters", []))],
            evidence_refs=list(d.get("evidence_refs", [])))

class OutlineBuilder:
    def __init__(self, *, corpus: Corpus, cfg: Config, theme_index: ThemeIndex | None = None):
        self.corpus = corpus
        self.cfg = cfg
        self.theme_index = theme_index or ThemeIndex(corpus)

    def build(self, *, theme: str, chapters: int | None = None, evidence_k: int = 60,
              **kw) -> Outline:
        chapters = chapters or self.cfg.default_chapters
        evidence = self.theme_index.select_evidence(theme, k=evidence_k, diversify=True)
        outline = Outline(theme=theme, title=f"Book on: {theme}", subtitle=None,
                          epigraph=None, preface_sketch=None,
                          chapters=[Chapter(number=i+1, title=f"Chapter {i+1}",
                                           thesis="", key_refs=[], beats=[])
                                    for i in range(chapters)],
                          evidence_refs=[p.ref for p in evidence])
        return outline

_JSON_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)
def _parse_json(text: str) -> dict:
    text = text.strip()
    m = _JSON_FENCE.search(text)
    if m: text = m.group(1).strip()
    try: return json.loads(text)
    except json.JSONDecodeError: pass
    start = text.find("{")
    if start < 0: raise ValueError("No JSON found")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{": depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0: return json.loads(text[start:i+1])
    raise ValueError("Unbalanced JSON")
