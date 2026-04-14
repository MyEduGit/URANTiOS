"""
Example: write a book end-to-end from Python.

Run:
    python examples/write_book.py
"""
from __future__ import annotations

import os
from pathlib import Path

from bookwriter import BookWriter, Corpus, ObsidianVault, MultiVault, Config


def main() -> None:
    cfg = Config.from_env()
    # If no API key is present, stay safe with a dry run so the example
    # still produces files to inspect.
    if not os.environ.get("ANTHROPIC_API_KEY"):
        cfg.dry_run = True
        cfg.default_chapters = 3

    corpus = Corpus.load(cfg.corpus_dir)

    home = Path.home()
    vaults = MultiVault.from_paths(
        [
            home / "Obsidian" / "UrantiaBooks",          # personal vault
            Path("/home/user/PhD-Triune-Monism/07_Generated_Books"),
        ]
    )

    writer = BookWriter(corpus=corpus, cfg=cfg, vault=vaults)
    book = writer.write(
        theme="The Bestowal Career of Michael of Nebadon",
        chapters=12,
        style="scholarly-devotional",
        voice="a scholar who has also knelt",
        audience="spiritually curious adults",
    )

    print("\n=== Done ===")
    print(f"Title       : {book.title}")
    print(f"Chapters    : {len(book.chapters)}")
    print(f"Word count  : {book.word_count():,}")
    print(f"Written to  : {book.metadata.get('written_to', [])}")


if __name__ == "__main__":
    main()
