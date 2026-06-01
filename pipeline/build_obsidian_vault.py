#!/usr/bin/env python3
"""Build an Obsidian vault from The Urantia Book JSON papers + the URANTiOS soul spec.

Produces a self-contained, navigable vault under ``obsidian/`` at the repo root:

  obsidian/
    URANTiOS — Home.md      Map of Content: all 197 papers grouped by Part
    Papers/                 One note per paper, with per-paragraph block IDs
    Soul/                   The URANTiOS v2.0 specification (the OS kernel)

Every paragraph gets an Obsidian block ID derived from its canonical reference
(``1:0.1`` -> ``^p1-0-1``) so any single paragraph can be linked or transcluded
from anywhere in the vault. Run from the repo root:

    python3 pipeline/build_obsidian_vault.py
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BOOK_DIR = REPO / "urantia-book"
SOUL_DIR = REPO / "soul"
VAULT = REPO / "obsidian"
PAPERS_DIR = VAULT / "Papers"
SOUL_VAULT_DIR = VAULT / "Soul"

# The Urantia Book's canonical four-part structure (Foreword == paper 0).
PARTS = [
    ("Foreword", 0, 0),
    ("Part I — The Central and Superuniverses", 1, 31),
    ("Part II — The Local Universe", 32, 56),
    ("Part III — The History of Urantia", 57, 119),
    ("Part IV — The Life and Teachings of Jesus", 120, 196),
]


def part_for(paper_index: int) -> str:
    for name, lo, hi in PARTS:
        if lo <= paper_index <= hi:
            return name
    return "Unknown"


def block_id(par_ref: str) -> str:
    """`1:0.1` -> `p1-0-1` (Obsidian block IDs allow [A-Za-z0-9-])."""
    return "p" + re.sub(r"[^A-Za-z0-9]+", "-", par_ref).strip("-")


def paper_filename(idx: int, title: str) -> str:
    safe = re.sub(r'[\\/:*?"<>|]+', "", title).strip()
    return f"Paper {idx:03d} — {safe}.md"


def wikilink(paper: dict, display: str) -> str:
    note = paper_filename(paper["_index"], paper["_title"])[:-3]
    return f"[[{note}|{display}]]"


def nav_display(paper: dict) -> str:
    return "Foreword" if paper["_index"] == 0 else f"Paper {paper['_index']}: {paper['_title']}"


def load_papers() -> list[dict]:
    papers = []
    for path in sorted(BOOK_DIR.glob("Doc*.json")):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        idx = data.get("paper_index", int(re.sub(r"\D", "", path.stem)))
        title = data.get("paper_title") or ("Foreword" if idx == 0 else f"Paper {idx}")
        data["_index"] = idx
        data["_title"] = title.strip()
        papers.append(data)
    papers.sort(key=lambda d: d["_index"])
    return papers


def render_paper(paper: dict, prev: dict | None, nxt: dict | None) -> str:
    idx = paper["_index"]
    title = paper["_title"]
    author = (paper.get("author") or "").strip()
    part = part_for(idx)

    lines: list[str] = []
    # YAML frontmatter
    lines.append("---")
    lines.append(f"paper: {idx}")
    lines.append(f'title: "{title}"')
    if author:
        lines.append(f'author: "{author}"')
    lines.append(f'part: "{part}"')
    lines.append("tags:")
    lines.append("  - urantia-book")
    lines.append(f"  - paper/{idx:03d}")
    lines.append(f'aliases:')
    lines.append(f'  - "Paper {idx}"')
    lines.append("---")
    lines.append("")

    lines.append(f"# {('Foreword' if idx == 0 else f'Paper {idx}')} — {title}")
    lines.append("")
    meta = [f"**Part:** {part}"]
    if author:
        meta.append(f"**Author:** {author}")
    lines.append("  ·  ".join(meta))
    lines.append("")
    lines.append("> [[URANTiOS — Home|↑ Home]]")
    lines.append("")

    for section in paper.get("sections", []):
        sec_ref = section.get("section_ref", "")
        sec_title = (section.get("section_title") or "").strip()
        sec_idx = section.get("section_index", 0)
        # Section 0 is the paper's introductory text — no heading needed.
        # section_title (when present) already carries its own number, e.g.
        # "1. The Father's Name", so it is used verbatim.
        if sec_idx:
            heading = sec_title if sec_title else f"{sec_idx}. Section {sec_idx}"
            lines.append(f"## {heading}")
            lines.append("")
        for par in section.get("pars", []):
            ref = par.get("par_ref", "")
            page = par.get("par_pageref", "")
            content = (par.get("par_content") or "").replace("\r", " ").strip()
            if not content:
                continue
            lines.append(content)
            tag = f"`{ref}`"
            if page:
                tag += f" · p.{page}"
            lines.append(f"{tag} ^{block_id(ref)}")
            lines.append("")

    # Footer navigation
    lines.append("---")
    nav = []
    if prev is not None:
        nav.append("← " + wikilink(prev, nav_display(prev)))
    nav.append("[[URANTiOS — Home|Home]]")
    if nxt is not None:
        nav.append(wikilink(nxt, nav_display(nxt)) + " →")
    lines.append("  ·  ".join(nav))
    lines.append("")
    return "\n".join(lines)


def render_home(papers: list[dict]) -> str:
    lines: list[str] = []
    lines.append("---")
    lines.append("tags:")
    lines.append("  - urantios")
    lines.append("  - moc")
    lines.append("---")
    lines.append("")
    lines.append("# URANTiOS — Home")
    lines.append("")
    lines.append("**An AI Operating System derived from The Urantia Book's cosmology.**")
    lines.append("")
    lines.append("Three Values: **Truth · Beauty · Goodness**")
    lines.append("")
    lines.append("- ⭐ **[[Foreword — Definitions Map|Start here — Foreword Definitions Map]]** — the term/concept mapping for the whole book")
    lines.append("- 📚 [[Urantipedia — Home|Urantipedia]] — encyclopedia of concepts examined from every angle")
    lines.append("- 🛠 [[Foreword — Digital Equivalence|Foreword Digital Equivalence]] — Phase 1: the Foreword mapped paragraph-by-paragraph into URANTiOS")
    lines.append("- 🧠 [[URANTiOS v2.0 Specification|The Soul — URANTiOS v2.0 kernel spec]]")
    lines.append(f"- 📖 The Urantia Book — {len(papers)} papers, fully linked below")
    lines.append("")
    lines.append("> [!tip] How this vault works")
    lines.append("> Every paragraph has a block ID. Link any single paragraph from anywhere")
    lines.append("> with `[[Paper 001 — The Universal Father#^p1-0-1]]`. Build your")
    lines.append("> digital-equivalence notes on top of the source without ever altering it.")
    lines.append("")

    by_part: dict[str, list[dict]] = {}
    for p in papers:
        by_part.setdefault(part_for(p["_index"]), []).append(p)

    for name, _lo, _hi in PARTS:
        group = by_part.get(name, [])
        if not group:
            continue
        lines.append(f"## {name}")
        lines.append("")
        for p in group:
            fn = paper_filename(p["_index"], p["_title"])[:-3]
            label = "Foreword" if p["_index"] == 0 else f"Paper {p['_index']:03d} — {p['_title']}"
            lines.append(f"- [[{fn}|{label}]]")
        lines.append("")
    return "\n".join(lines)


def render_foreword_map(foreword: dict) -> str:
    """The Foreword defines the terms and concepts used across the whole book.

    This note is the canonical entry point: it links to each definition section
    so the digital-equivalence mapping can begin where the book itself begins.
    """
    note = paper_filename(foreword["_index"], foreword["_title"])[:-3]
    lines: list[str] = []
    lines.append("---")
    lines.append("tags:")
    lines.append("  - urantios")
    lines.append("  - foreword")
    lines.append("  - definitions")
    lines.append("  - moc")
    lines.append("---")
    lines.append("")
    lines.append("# Foreword — Definitions Map")
    lines.append("")
    lines.append("> [[URANTiOS — Home|↑ Home]]  ·  [[" + note + "|Read the full Foreword]]")
    lines.append("")
    lines.append("> [!important] Start here")
    lines.append("> The Foreword is the definitional root of The Urantia Book — it fixes the")
    lines.append("> meaning of every key term (Deity, God, the Absolutes, personality, the")
    lines.append("> Supreme) before the papers use them. Map these definitions into URANTiOS")
    lines.append("> first; everything downstream inherits from them.")
    lines.append("")
    for section in foreword.get("sections", []):
        title = (section.get("section_title") or "").strip()
        if not title:
            continue
        n_pars = len(section.get("pars", []))
        lines.append(f"- [[{note}#{title}|{title}]]  ·  {n_pars} ¶")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    # Only refresh the directories this script owns. Anything else in the vault
    # (e.g. authored Urantipedia entries, the user's own notes) is preserved.
    for owned in (PAPERS_DIR, SOUL_VAULT_DIR):
        if owned.exists():
            shutil.rmtree(owned)
    PAPERS_DIR.mkdir(parents=True)
    SOUL_VAULT_DIR.mkdir(parents=True)

    papers = load_papers()

    for i, paper in enumerate(papers):
        prev = papers[i - 1] if i > 0 else None
        nxt = papers[i + 1] if i < len(papers) - 1 else None
        fn = paper_filename(paper["_index"], paper["_title"])
        (PAPERS_DIR / fn).write_text(render_paper(paper, prev, nxt), encoding="utf-8")

    (VAULT / "URANTiOS — Home.md").write_text(render_home(papers), encoding="utf-8")

    foreword = next((p for p in papers if p["_index"] == 0), None)
    if foreword is not None:
        (VAULT / "Foreword — Definitions Map.md").write_text(
            render_foreword_map(foreword), encoding="utf-8"
        )

    # Bring the soul spec into the vault (kept in sync on each build).
    soul_src = SOUL_DIR / "URANTiOS_v2.md"
    if soul_src.exists():
        dest = SOUL_VAULT_DIR / "URANTiOS v2.0 Specification.md"
        body = soul_src.read_text(encoding="utf-8")
        front = "---\ntags:\n  - urantios\n  - soul\n  - kernel\n---\n\n> [[URANTiOS — Home|↑ Home]]\n\n"
        dest.write_text(front + body, encoding="utf-8")

    total_pars = sum(
        len(s.get("pars", [])) for p in papers for s in p.get("sections", [])
    )
    print(f"Vault built at: {VAULT}")
    print(f"  Papers: {len(papers)}")
    print(f"  Paragraphs (block-linkable): {total_pars}")
    print(f"  Home MOC + soul spec included")


if __name__ == "__main__":
    main()
