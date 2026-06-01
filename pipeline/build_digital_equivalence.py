#!/usr/bin/env python3
"""Scaffold the URANTiOS digital-equivalence mapping, Foreword-first.

Implements Phase 1 of the URANTiOS meta prompt: process the Foreword
paragraph-by-paragraph into structured digital equivalents. For each Foreword
paragraph this creates one note pre-filled with:

  - the canonical locator (paper / section / paragraph)
  - the verbatim text, transcluded from the source note (never duplicated)
  - the empty output contract: semantic extraction, digital-equivalence mapping,
    OS artifact emission, alignment & safety, integration delta, confidence ledger

Plus an index note with a per-section progress checklist.

  obsidian/Digital Equivalence/
    Foreword — Digital Equivalence.md   Index + progress checklist (regenerated)
    Foreword/<locator>.md               One note per paragraph — created once,
                                        NEVER overwritten (your mapping is safe)

Run from the repo root:

    python3 pipeline/build_digital_equivalence.py
"""
from __future__ import annotations

from pathlib import Path

from build_obsidian_vault import REPO, block_id, load_papers, paper_filename

VAULT = REPO / "obsidian"
DE_DIR = VAULT / "Digital Equivalence"
FOREWORD_DIR = DE_DIR / "Foreword"


def locator_slug(par_ref: str) -> str:
    """`0:2.2` -> `0.2.2` (safe, readable filename stem)."""
    return par_ref.replace(":", ".")


def render_paragraph_scaffold(paper: dict, section: dict, par: dict) -> str:
    ref = par.get("par_ref", "")
    page = par.get("par_pageref", "")
    sec_idx = section.get("section_index", 0)
    sec_title = (section.get("section_title") or "").strip()
    source_note = paper_filename(paper["_index"], paper["_title"])[:-3]
    bid = block_id(ref)

    L: list[str] = []
    L.append("---")
    L.append(f'locator: "{ref}"')
    L.append(f"paper: {paper['_index']}")
    L.append(f"section: {sec_idx}")
    if sec_title:
        L.append(f'section_title: "{sec_title}"')
    if page:
        L.append(f'page: "{page}"')
    L.append("tags:")
    L.append("  - urantios")
    L.append("  - digital-equivalence")
    L.append("  - foreword")
    L.append("status: todo            # todo | in-progress | done | needs-review")
    L.append("textual_confidence: 0   # 0.0–1.0")
    L.append("mapping_confidence: 0   # 0.0–1.0")
    L.append("requires_human_review: true")
    L.append("---")
    L.append("")
    head = sec_title if sec_title else f"Section {sec_idx}"
    L.append(f"# Foreword {ref} — Digital Equivalent")
    L.append("")
    L.append(f"**Locator:** Foreword · {head} · ¶ `{ref}`"
             + (f" · p.{page}" if page else ""))
    L.append("")
    L.append("> [[Foreword — Digital Equivalence|↑ Foreword DE Index]]  ·  "
             f"[[{source_note}#^{bid}|source paragraph]]")
    L.append("")
    L.append("## Paragraph (verbatim)")
    L.append(f"![[{source_note}#^{bid}]]")
    L.append("")
    L.append("## Semantic Extraction")
    L.append("*3–10 core claims.*")
    L.append("- ")
    L.append("")
    L.append("## Digital Equivalence Mapping")
    L.append("- **Entities:** ")
    L.append("- **Relations:** *(subject → predicate → object)*")
    L.append("- **Axioms:** ")
    L.append("- **Constraints:** ")
    L.append("- **State transitions:** *(from → event → to)*")
    L.append("- **Governance rules:** ")
    L.append("- **Interfaces:** *(name · inputs · outputs)*")
    L.append("")
    L.append("## OS Artifact Emission")
    L.append("- **Ontology patch:** ")
    L.append("- **Policy patch:** ")
    L.append("- **Protocol patch:** ")
    L.append("- **Memory patch:** ")
    L.append("- **Tests:** *(≥2 assertions tied to this paragraph)*")
    L.append("  - [ ] ")
    L.append("  - [ ] ")
    L.append("")
    L.append("## Alignment & Safety")
    L.append("- **Misinterpretation risks:** ")
    L.append("- **Dogma-drift risks:** ")
    L.append("- **Mitigations:** ")
    L.append("")
    L.append("## Integration Delta")
    L.append("*What changed in the cumulative URANTiOS architecture. "
             "Backward compatibility: compatible | conditional | breaking.*")
    L.append("- ")
    L.append("")
    L.append("## Confidence Ledger")
    L.append("*Mirror the frontmatter once mapped; set `requires_human_review` and a reason.*")
    L.append("")
    return "\n".join(L)


def render_index(foreword: dict, par_paths: list[tuple[dict, dict, Path]]) -> str:
    L: list[str] = []
    L.append("---")
    L.append("tags:")
    L.append("  - urantios")
    L.append("  - digital-equivalence")
    L.append("  - moc")
    L.append("---")
    L.append("")
    L.append("# Foreword — Digital Equivalence")
    L.append("")
    L.append("> [[URANTiOS — Home|↑ Home]]  ·  [[Foreword — Definitions Map|Definitions Map]]")
    L.append("")
    L.append("> [!info] Phase 1 of the URANTiOS build")
    L.append("> Process the Foreword **one paragraph at a time** into a structured")
    L.append("> digital equivalent. Each paragraph below has its own note with the full")
    L.append("> output contract. Check it off here as you complete it; the source text")
    L.append("> is transcluded into each note so you never re-type or alter canon.")
    L.append("")
    total = len(par_paths)
    L.append(f"**{total} paragraphs** across {len(foreword.get('sections', []))} sections.")
    L.append("")

    by_section: dict[int, list[tuple[dict, dict, Path]]] = {}
    for paper, section, path in par_paths:
        by_section.setdefault(section.get("section_index", 0), []).append((paper, section, path))

    for section in foreword.get("sections", []):
        sidx = section.get("section_index", 0)
        rows = by_section.get(sidx, [])
        if not rows:
            continue
        title = (section.get("section_title") or "").strip() or "Introduction"
        L.append(f"## {title}")
        L.append("")
        for paper, sec, path in rows:
            stem = path.stem
            # par_ref lives in the section's pars; recover it from the stem.
            ref = stem.replace(".", ":", 1)
            L.append(f"- [ ] [[{stem}|{ref}]]")
        L.append("")
    return "\n".join(L)


def main() -> None:
    FOREWORD_DIR.mkdir(parents=True, exist_ok=True)
    papers = load_papers()
    foreword = next((p for p in papers if p["_index"] == 0), None)
    if foreword is None:
        raise SystemExit("Foreword (Doc000) not found.")

    created = 0
    par_paths: list[tuple[dict, dict, Path]] = []
    for section in foreword.get("sections", []):
        for par in section.get("pars", []):
            ref = par.get("par_ref", "")
            if not (par.get("par_content") or "").strip():
                continue
            path = FOREWORD_DIR / f"{locator_slug(ref)}.md"
            par_paths.append((foreword, section, path))
            if not path.exists():
                path.write_text(
                    render_paragraph_scaffold(foreword, section, par), encoding="utf-8"
                )
                created += 1

    (DE_DIR / "Foreword — Digital Equivalence.md").write_text(
        render_index(foreword, par_paths), encoding="utf-8"
    )

    print(f"Digital Equivalence (Foreword) at: {FOREWORD_DIR}")
    print(f"  Paragraph scaffolds: {len(par_paths)}  (created: {created}, "
          f"existing preserved: {len(par_paths) - created})")


if __name__ == "__main__":
    main()
