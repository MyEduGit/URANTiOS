"""Corpus loader for The Urantia Book (197 papers, 14,596 paragraphs)."""
from __future__ import annotations
import json, re
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Iterator
from .config import DEFAULT_CORPUS_DIR

REF_RE = re.compile(r"^(\d+):(\d+)\.(\d+)$")

@dataclass(frozen=True)
class Citation:
    paper: int
    section: int
    paragraph: int

    @classmethod
    def parse(cls, ref: str) -> "Citation":
        m = REF_RE.match(ref.strip())
        if not m:
            raise ValueError(f"Not a Urantia Book reference: {ref!r}")
        return cls(int(m.group(1)), int(m.group(2)), int(m.group(3)))

    def __str__(self) -> str:
        return f"{self.paper}:{self.section}.{self.paragraph}"

    @property
    def obsidian_link(self) -> str:
        return f"UB-{self.paper:03d}-{self.section:02d}-{self.paragraph:03d}"

@dataclass
class Paragraph:
    ref: str
    pageref: str
    content: str
    @property
    def citation(self) -> Citation:
        return Citation.parse(self.ref)

@dataclass
class Section:
    index: int
    ref: str
    title: str | None
    paragraphs: list[Paragraph]
    def __iter__(self) -> Iterator[Paragraph]:
        return iter(self.paragraphs)
    def find(self, paragraph_index: int) -> Paragraph | None:
        for p in self.paragraphs:
            if p.citation.paragraph == paragraph_index:
                return p
        return None

@dataclass
class Paper:
    index: int
    title: str | None
    sections: list[Section]
    @property
    def is_foreword(self) -> bool:
        return self.index == 0
    def __iter__(self) -> Iterator[Section]:
        return iter(self.sections)
    def find_section(self, section_index: int) -> Section | None:
        for s in self.sections:
            if s.index == section_index:
                return s
        return None
    def paragraphs(self) -> Iterator[Paragraph]:
        for s in self.sections:
            yield from s.paragraphs
    @cached_property
    def text(self) -> str:
        return "\n\n".join(p.content for p in self.paragraphs())

@dataclass
class Corpus:
    papers: list[Paper] = field(default_factory=list)
    source_dir: Path | None = None

    @classmethod
    def load(cls, corpus_dir: Path | str = DEFAULT_CORPUS_DIR) -> "Corpus":
        root = Path(corpus_dir).expanduser()
        files = sorted(root.glob("Doc*.json"))
        if not files:
            raise FileNotFoundError(f"No Doc*.json in {root}")
        return cls(papers=[cls._load_paper(f) for f in files], source_dir=root)

    @staticmethod
    def _load_paper(path: Path) -> Paper:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        sections = []
        for s in data.get("sections", []):
            paras = [
                Paragraph(ref=p["par_ref"], pageref=p.get("par_pageref", ""), content=p["par_content"])
                for p in s.get("pars", [])
            ]
            sections.append(Section(index=s["section_index"], ref=s["section_ref"],
                                    title=s.get("section_title"), paragraphs=paras))
        return Paper(index=data["paper_index"], title=data.get("paper_title"), sections=sections)

    def __len__(self) -> int:
        return len(self.papers)
    def __iter__(self) -> Iterator[Paper]:
        return iter(self.papers)

    def paper(self, index: int) -> Paper:
        for p in self.papers:
            if p.index == index:
                return p
        raise KeyError(f"No paper {index}")

    def paragraph(self, ref: str | Citation) -> Paragraph:
        c = ref if isinstance(ref, Citation) else Citation.parse(str(ref))
        section = self.paper(c.paper).find_section(c.section)
        if section is None:
            raise KeyError(f"No section {c.paper}:{c.section}")
        para = section.find(c.paragraph)
        if para is None:
            raise KeyError(f"No paragraph {c}")
        return para

    def paragraphs(self) -> Iterator[Paragraph]:
        for paper in self.papers:
            yield from paper.paragraphs()

    def search(self, query: str, *, limit: int = 50) -> list[Paragraph]:
        needle = query.lower()
        out = []
        for p in self.paragraphs():
            if needle in p.content.lower():
                out.append(p)
                if len(out) >= limit:
                    break
        return out

    def stats(self) -> dict[str, int]:
        n_p = sum(1 for _ in self.paragraphs())
        n_c = sum(len(p.content) for p in self.paragraphs())
        return {"papers": len(self.papers),
                "sections": sum(len(p.sections) for p in self.papers),
                "paragraphs": n_p, "characters": n_c, "approx_tokens": n_c // 4}

    def excerpt(self, refs) -> str:
        lines = []
        for r in refs:
            try:
                p = self.paragraph(r)
                lines.append(f"[{p.ref}] {p.content}")
            except KeyError:
                lines.append(f"[{r}] (not found)")
        return "\n\n".join(lines)
