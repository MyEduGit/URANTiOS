"""Tests that run against the real Urantia Book JSON corpus.

These tests are intentionally dependency-free (stdlib only) so they
work without pytest installed. Run:

    python -m bookwriter.tests.test_corpus
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from bookwriter import Corpus, Citation, ThemeIndex
from bookwriter.obsidian import (
    ObsidianRenderer,
    linkify_citations,
    extract_citations,
)
from bookwriter.outline import _parse_json
from bookwriter.writer import BookWriter, Book, WrittenChapter
from bookwriter.config import Config


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        print(f"FAIL: {msg}")
        sys.exit(1)


def test_citation_roundtrip() -> None:
    c = Citation.parse("120:4.5")
    _assert(c.paper == 120 and c.section == 4 and c.paragraph == 5, "parse")
    _assert(str(c) == "120:4.5", "str roundtrip")
    _assert(c.obsidian_link == "UB-120-04-005", "obsidian link shape")


def test_corpus_load() -> None:
    corpus = Corpus.load()
    stats = corpus.stats()
    _assert(stats["papers"] == 197, f"expected 197 papers, got {stats['papers']}")
    _assert(stats["paragraphs"] > 10_000, "paragraph count sane")
    # Paragraph lookup
    p = corpus.paragraph("0:0.1")
    _assert("Urantia" in p.content, "paragraph content looks right")


def test_search() -> None:
    corpus = Corpus.load()
    hits = corpus.search("Michael of Nebadon", limit=5)
    _assert(len(hits) > 0, "substring search returns results")


def test_theme_index() -> None:
    corpus = Corpus.load()
    idx = ThemeIndex(corpus)
    ev = idx.select_evidence("faith of Jesus", k=10)
    _assert(len(ev) == 10, f"expected 10 evidence paragraphs, got {len(ev)}")
    # Diversification should give us paragraphs from multiple papers
    papers = {p.citation.paper for p in ev}
    _assert(len(papers) > 1, "diversified evidence spans multiple papers")


def test_outline_parser_tolerates_fences() -> None:
    wrapped = "```json\n" + json.dumps({"title": "x", "chapters": []}) + "\n```"
    out = _parse_json(wrapped)
    _assert(out["title"] == "x", "parses fenced JSON")


def test_citation_regex_and_linkify() -> None:
    text = "As the papers teach (120:4.5), Michael bestowed himself on Urantia (0:1.1)."
    refs = extract_citations(text)
    _assert(refs == ["120:4.5", "0:1.1"], f"extract refs: {refs}")
    linked = linkify_citations(text)
    _assert("[[UB-120-04-005|120:4.5]]" in linked, "linkify ub-120")
    _assert("[[UB-000-01-001|0:1.1]]" in linked, "linkify foreword")


def test_renderer_produces_expected_files() -> None:
    # Build a fake, tiny Book object and render it
    outline_dict = {
        "title": "Test Book",
        "subtitle": "A tiny one",
        "epigraph": "In the minds of the mortals of Urantia… (0:0.1)",
        "preface_sketch": "This is a preface.",
        "chapters": [
            {
                "number": 1,
                "title": "Intro",
                "thesis": "We begin.",
                "key_refs": ["0:0.1"],
                "beats": ["open", "middle", "close"],
            }
        ],
    }
    from bookwriter.outline import Outline

    outline = Outline.from_dict(outline_dict, theme="test")
    book = Book(
        theme="test",
        title="Test Book",
        subtitle="A tiny one",
        epigraph="In the minds of the mortals of Urantia… (0:0.1)",
        preface_sketch="This is a preface.",
        chapters=[
            WrittenChapter(
                number=1,
                title="Intro",
                thesis="We begin.",
                body="# Chapter 1 — Intro\n\nAs (0:0.1) teaches, mortals are often confused.",
                key_refs=["0:0.1"],
            )
        ],
        outline=outline,
        metadata={"generated_at": "2026-01-01T00:00:00Z"},
    )
    renderer = ObsidianRenderer()
    files = renderer.render_book(book)
    _assert(any(k.startswith("00 - ") for k in files), "has cover file")
    _assert(any(k.startswith("01 - ") for k in files), "has ch 1 file")
    _assert("_outline.md" in files, "has outline")
    _assert("_meta.json" in files, "has meta")
    # Cover links into ch1
    cover = files[next(k for k in files if k.startswith("00 - "))]
    _assert("Chapter 1" in cover, "cover lists chapter 1")


def test_writer_end_to_end_dry_run(tmp_dir: Path) -> None:
    cfg = Config.from_env()
    cfg.dry_run = True
    cfg.default_chapters = 3
    cfg.verbose = False
    cfg.enable_lucifer_test = False
    cfg.output_dir = tmp_dir

    corpus = Corpus.load()
    from bookwriter.obsidian import ObsidianVault

    vault = ObsidianVault(root=tmp_dir)
    writer = BookWriter(corpus=corpus, cfg=cfg, vault=vault)
    book = writer.write(theme="Truth, Beauty, Goodness", chapters=3, evidence_k=15)
    _assert(len(book.chapters) == 3, "dry-run produces 3 chapters")
    # vault written
    files = list((tmp_dir / "Books" / book.slug).glob("*"))
    _assert(len(files) >= 5, f"vault has files, got {len(files)}")


def main() -> None:
    import tempfile

    test_citation_roundtrip()
    test_corpus_load()
    test_search()
    test_theme_index()
    test_outline_parser_tolerates_fences()
    test_citation_regex_and_linkify()
    test_renderer_produces_expected_files()
    with tempfile.TemporaryDirectory() as tmp:
        test_writer_end_to_end_dry_run(Path(tmp))
    print("All tests passed.")


if __name__ == "__main__":
    main()
