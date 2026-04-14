"""
Corpus loader for The Urantia Book.

Loads all 197 papers (Foreword + 196) from the JSON corpus and exposes them
as typed, navigable objects. References follow the canonical Urantia Book
notation: ``paper:section.paragraph`` (e.g. ``120:4.5``).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Iterable, Iterator

from .config import DEFAULT_CORPUS_DIR


REF_RE = re.compile(r"^(\d+):(\d+)\.(\d+)$")


# ---------------------------------------------------------------------------
# Primitive types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Citation:
    """A canonical Urantia Book paragraph reference."""

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

    def __repr__(self) -> str:  # noqa: D401
        snippet = self.content[:60].replace("\n", " ")
        return f"Paragraph({self.ref}, {snippet!r}...)"


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
            cit = p.citation
            if cit.paragraph == paragraph_index:
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


# ---------------------------------------------------------------------------
# Corpus
# ---------------------------------------------------------------------------

@dataclass
class Corpus:
    """The complete Urantia Book corpus."""

    papers: list[Paper] = field(default_factory=list)
    source_dir: Path | None = None

    # --- loading --------------------------------------------------------

    @classmethod
    def load(cls, corpus_dir: Path | str = DEFAULT_CORPUS_DIR) -> "Corpus":
        """Load all Doc*.json files from ``corpus_dir``."""
        root = Path(corpus_dir).expanduser()
        files = sorted(root.glob("Doc*.json"))
        if not files:
            raise FileNotFoundError(
                f"No Doc*.json files found in {root}. "
                f"Expected the URANTiOS urantia-book/ directory."
            )
        papers = [cls._load_paper(f) for f in files]
        return cls(papers=papers, source_dir=root)

    @staticmethod
    def _load_paper(path: Path) -> Paper:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        sections: list[Section] = []
        for s in data.get("sections", []):
            paras = [
                Paragraph(
                    ref=p["par_ref"],
                    pageref=p.get("par_pageref", ""),
                    content=p["par_content"],
                )
                for p in s.get("pars", [])
            ]
            sections.append(
                Section(
                    index=s["section_index"],
                    ref=s["section_ref"],
                    title=s.get("section_title"),
                    paragraphs=paras,
                )
            )
        return Paper(
            index=data["paper_index"],
            title=data.get("paper_title"),
            sections=sections,
        )

    # --- access ---------------------------------------------------------

    def __len__(self) -> int:
        return len(self.papers)

    def __iter__(self) -> Iterator[Paper]:
        return iter(self.papers)

    def paper(self, index: int) -> Paper:
        for p in self.papers:
            if p.index == index:
                return p
        raise KeyError(f"No paper with index {index}")

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

    # --- search ---------------------------------------------------------

    def search(
        self,
        query: str,
        *,
        limit: int | None = 50,
        case_sensitive: bool = False,
    ) -> list[Paragraph]:
        """Simple substring search across all paragraphs.

        Returns paragraphs in order of appearance, capped at ``limit``.
        """
        needle = query if case_sensitive else query.lower()
        out: list[Paragraph] = []
        for p in self.paragraphs():
            hay = p.content if case_sensitive else p.content.lower()
            if needle in hay:
                out.append(p)
                if limit and len(out) >= limit:
                    break
        return out

    def regex_search(
        self, pattern: str, *, flags: int = re.IGNORECASE, limit: int | None = 50
    ) -> list[Paragraph]:
        rx = re.compile(pattern, flags)
        out: list[Paragraph] = []
        for p in self.paragraphs():
            if rx.search(p.content):
                out.append(p)
                if limit and len(out) >= limit:
                    break
        return out

    # --- summaries ------------------------------------------------------

    def stats(self) -> dict[str, int]:
        n_papers = len(self.papers)
        n_sections = sum(len(p.sections) for p in self.papers)
        n_paragraphs = sum(1 for _ in self.paragraphs())
        n_chars = sum(len(p.content) for p in self.paragraphs())
        return {
            "papers": n_papers,
            "sections": n_sections,
            "paragraphs": n_paragraphs,
            "characters": n_chars,
            "approx_tokens": n_chars // 4,
        }

    def excerpt(self, refs: Iterable[str | Citation]) -> str:
        """Render a pipe-delimited block of paragraphs for prompt injection."""
        lines = []
        for r in refs:
            try:
                p = self.paragraph(r)
                lines.append(f"[{p.ref}] {p.content}")
            except KeyError:
                lines.append(f"[{r}] (not found)")
        return "\n\n".join(lines)
