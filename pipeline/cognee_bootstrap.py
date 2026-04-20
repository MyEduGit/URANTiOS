#!/usr/bin/env python3
"""
Cognee Bootstrap — URANTiOS Knowledge Graph Ingestion
Loads all 197 Urantia Book papers (Foreword + Papers 1-196) into Cognee's
knowledge graph for semantic search and recall.

UrantiOS governed — Truth, Beauty, Goodness

Usage:
    python3 cognee_bootstrap.py                    # Ingest all papers
    python3 cognee_bootstrap.py --papers 0-10      # Ingest papers 0 through 10
    python3 cognee_bootstrap.py --papers 0,1,196   # Ingest specific papers
    python3 cognee_bootstrap.py --verify            # Verify graph with test query
"""
import asyncio
import json
import os
import sys
import argparse
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "urantia-book"
DATASET_NAME = "urantia_book"


def find_paper_files():
    """Find all Doc*.json files in the urantia-book directory."""
    if not BOOK_DIR.exists():
        print(f"ERROR: Urantia Book directory not found at {BOOK_DIR}")
        sys.exit(1)
    files = sorted(BOOK_DIR.glob("Doc*.json"))
    if not files:
        print(f"ERROR: No Doc*.json files found in {BOOK_DIR}")
        sys.exit(1)
    return files


def parse_paper_range(spec):
    """Parse a paper specification like '0-10' or '0,1,196' into a set of ints."""
    indices = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            indices.update(range(int(lo), int(hi) + 1))
        else:
            indices.add(int(part))
    return indices


def paper_to_text(paper_data):
    """Convert a paper JSON object into readable text for Cognee ingestion."""
    title = paper_data.get("paper_title", "Untitled")
    author = paper_data.get("author", "Unknown")
    index = paper_data.get("paper_index", "?")
    lines = [
        f"Paper {index}: {title}",
        f"Author: {author}",
        "",
    ]
    for section in paper_data.get("sections", []):
        section_ref = section.get("section_ref", "")
        section_title = section.get("section_title", "")
        if section_title:
            lines.append(f"## {section_ref} — {section_title}")
        elif section_ref:
            lines.append(f"## {section_ref}")
        lines.append("")
        for par in section.get("pars", []):
            content = par.get("par_content", "")
            ref = par.get("par_ref", "")
            if content:
                lines.append(f"[{ref}] {content}")
                lines.append("")
    return "\n".join(lines)


async def ingest_papers(paper_files, verbose=True):
    """Ingest papers into Cognee's knowledge graph."""
    import cognee

    total = len(paper_files)
    succeeded = 0
    failed = 0

    for i, fpath in enumerate(paper_files, 1):
        with open(fpath) as f:
            paper_data = json.load(f)

        paper_index = paper_data.get("paper_index", "?")
        paper_title = paper_data.get("paper_title", "Untitled")
        text = paper_to_text(paper_data)

        if verbose:
            label = "Foreword" if paper_index == 0 else f"Paper {paper_index}"
            print(f"  [{i}/{total}] {label}: {paper_title} ({len(text)} chars)...")

        try:
            await cognee.remember(
                text,
                dataset_name=DATASET_NAME,
            )
            succeeded += 1
        except Exception as e:
            failed += 1
            print(f"  ERROR ingesting Paper {paper_index}: {e}")

    return succeeded, failed


async def verify_graph():
    """Run a test query against the Cognee knowledge graph."""
    import cognee

    print("\nVerification query: 'What is the Universal Father?'")
    results = await cognee.recall(
        "What is the Universal Father?",
        datasets=[DATASET_NAME],
        top_k=3,
    )
    if results:
        print(f"  Found {len(results)} results.")
        for j, r in enumerate(results, 1):
            snippet = str(r)[:200]
            print(f"  [{j}] {snippet}...")
        return True
    else:
        print("  No results returned. Graph may need an LLM API key for cognify.")
        return False


async def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap Cognee with Urantia Book papers"
    )
    parser.add_argument(
        "--papers",
        type=str,
        default=None,
        help="Paper range: '0-10' or '0,1,196'. Default: all papers.",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Run a test query after ingestion.",
    )
    args = parser.parse_args()

    print("=" * 57)
    print("  Cognee Bootstrap — URANTiOS Knowledge Graph")
    print("=" * 57)
    print()

    all_files = find_paper_files()
    print(f"Found {len(all_files)} papers in {BOOK_DIR}")

    # Filter to requested papers
    if args.papers:
        wanted = parse_paper_range(args.papers)
        paper_files = []
        for f in all_files:
            # Extract index from filename like Doc000.json
            stem = f.stem  # e.g. Doc000
            idx = int(stem.replace("Doc", ""))
            if idx in wanted:
                paper_files.append(f)
        print(f"Filtered to {len(paper_files)} papers: {args.papers}")
    else:
        paper_files = all_files
        print("Ingesting all papers.")

    print()
    print("Ingesting into Cognee knowledge graph...")
    print(f"  Dataset: {DATASET_NAME}")
    print()

    succeeded, failed = await ingest_papers(paper_files)

    print()
    print(f"Ingestion complete: {succeeded} succeeded, {failed} failed.")

    if args.verify:
        await verify_graph()

    print()
    print("=" * 57)
    print("  UrantiOS governed — Truth, Beauty, Goodness")
    print("=" * 57)


if __name__ == "__main__":
    asyncio.run(main())
