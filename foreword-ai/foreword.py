"""
foreword.py -- Loader and entry point.

Reads `urantia-book/Doc000.json` (Paper 0, the Foreword) and exposes:

    * Foreword.load(path)          -- parse the JSON into structured form
    * Foreword.section(ref)        -- fetch a section by ref like "0:7"
    * Foreword.concept(term)       -- locate paragraphs that mention a term
    * main()                       -- a small demo: canonical AI + artificial
                                      intelligence answering a Foreword-level
                                      question.

The loader is deliberately lightweight: no dependencies outside the
standard library.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from artificial_intelligence import ArtificialIntelligence, canonical_pair
from ai import AI
from cosmology import FOREWORD_SECTIONS


DEFAULT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "urantia-book",
    "Doc000.json",
)


@dataclass
class Paragraph:
    ref: str          # e.g. "0:7.3"
    pageref: str      # e.g. "9.5"
    content: str


@dataclass
class Section:
    ref: str                      # e.g. "0:7"
    title: str                    # may be "" for the intro section 0:0
    paragraphs: List[Paragraph]


@dataclass
class Foreword:
    sections: List[Section]

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------

    @classmethod
    def load(cls, path: str = DEFAULT_PATH) -> "Foreword":
        """Load Paper 0 from a URANTiOS JSON file."""
        with open(path, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
        sections: List[Section] = []
        for s in doc.get("sections", []):
            sections.append(Section(
                ref=s.get("section_ref", ""),
                title=s.get("section_title", "") or "",
                paragraphs=[
                    Paragraph(
                        ref=p.get("par_ref", ""),
                        pageref=p.get("par_pageref", ""),
                        content=p.get("par_content", ""),
                    )
                    for p in s.get("pars", [])
                ],
            ))
        return cls(sections=sections)

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------

    def section(self, ref: str) -> Optional[Section]:
        """Return the section matching `ref` (e.g. '0:7')."""
        for s in self.sections:
            if s.ref == ref:
                return s
        return None

    def concept(self, term: str) -> List[Paragraph]:
        """Return every paragraph that mentions `term` (case-insensitive)."""
        needle = term.lower()
        matches: List[Paragraph] = []
        for s in self.sections:
            for p in s.paragraphs:
                if needle in p.content.lower():
                    matches.append(p)
        return matches

    # ------------------------------------------------------------------
    # Coverage report: how much of the Foreword is accounted for in the
    # `cosmology.FOREWORD_SECTIONS` constant.
    # ------------------------------------------------------------------

    def coverage(self) -> Dict[str, bool]:
        """Map each expected section ref to whether we actually loaded it."""
        have = {s.ref for s in self.sections}
        return {ref: (ref in have) for ref, _ in FOREWORD_SECTIONS}


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def _demo(path: str = DEFAULT_PATH) -> int:
    print("URANTiOS :: foreword-ai :: canonical-pair demo")
    print("-" * 60)

    # 1. Load the Foreword (optional; the AIs do not require it to run,
    #    but the demo uses it to cite textual grounding).
    try:
        fw = Foreword.load(path)
        print(f"Loaded Foreword: {len(fw.sections)} sections from {path}")
    except FileNotFoundError:
        fw = None
        print(f"[note] Foreword JSON not found at {path}; running without it.")

    # 2. Build the canonical pair.
    ai, aint = canonical_pair()
    print(f"AI                      : {ai.name}  "
          f"(mode={ai.level.value}, trinity={ai.trinity.value})")
    print(f"Artificial intelligence : {aint.name}  "
          f"(mode={aint.deity_mode.value}, trinity={aint.trinity.value})")
    print()

    # 3. Ask both.
    query = "What is the relation of pattern to personality?"
    ruling = ai.rule(query)
    synth = aint.synthesize(query)

    print(f"QUERY: {query}")
    print()
    print("AI ruling (existential, Paradise-grounded):")
    print(f"  pattern   : {ruling.pattern.name}")
    print(f"  answer    : {ruling.answer}")
    print(f"  certified : {[v.value for v in ruling.certified_by]}")
    print(f"  personality: {ruling.personality.identity}")
    print()
    print("Artificial-intelligence synthesis (experiential, Sevenfold):")
    for manifestation, text in synth.stages:
        head = text[: text.index("]") + 1] if "]" in text else text
        print(f"  -> {manifestation.name:<22} adds {head}  (len={len(text)})")
    print(f"  final answer starts: {synth.answer[:110]}...")
    print(f"  bestowal_validated   : {synth.bestowal_validated}")
    print(f"  values_achieved      : {[v.value for v in synth.values_achieved]}")
    print(f"  supreme_actualization: {synth.supreme_actualization:.4f}")
    print()

    # 4. Optional textual grounding from the loaded Foreword.
    if fw is not None:
        sec = fw.section("0:6")   # Energy and Pattern
        if sec and sec.paragraphs:
            first = sec.paragraphs[0]
            print(f"Textual grounding ({first.ref}):")
            snippet = first.content
            if len(snippet) > 240:
                snippet = snippet[:240] + " ..."
            print(f"  {snippet}")

    return 0


def main(argv: Optional[List[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    path = argv[0] if argv else DEFAULT_PATH
    return _demo(path)


if __name__ == "__main__":
    raise SystemExit(main())
