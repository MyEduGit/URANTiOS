"""
CLI entry point for the BookWriter.

Usage:

  # write a full book end-to-end
  python -m bookwriter write \\
      --theme "The Bestowal Career of Michael of Nebadon" \\
      --chapters 12 \\
      --vault ~/Obsidian/UrantiaBooks \\
      --vault /home/user/PhD-Triune-Monism/07_Generated_Books

  # generate only an outline (JSON)
  python -m bookwriter outline --theme "The Three Absolutes"

  # corpus sanity-check
  python -m bookwriter stats

  # preview theme-selected evidence (no API cost)
  python -m bookwriter evidence --theme "faith of Jesus" -k 20
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .config import Config
from .corpus import Corpus
from .obsidian import ObsidianRenderer, ObsidianVault
from .outline import OutlineBuilder
from .themes import ThemeIndex
from .vault import MultiVault
from .writer import BookWriter


# ---------------------------------------------------------------------------

def _cfg_from_args(args: argparse.Namespace) -> Config:
    cfg = Config.from_env()
    if args.model:
        cfg.model = args.model
    if args.drafting_model:
        cfg.drafting_model = args.drafting_model
    if args.revisions is not None:
        cfg.revision_passes = args.revisions
    if args.no_lucifer:
        cfg.enable_lucifer_test = False
    if args.no_cache:
        cfg.enable_prompt_cache = False
    if args.dry_run:
        cfg.dry_run = True
    if args.quiet:
        cfg.verbose = False
    if args.seed is not None:
        cfg.seed = args.seed
    if args.corpus:
        cfg.corpus_dir = Path(args.corpus).expanduser()
    return cfg


def _common_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--corpus", type=str, default=None,
                   help="Path to urantia-book/ directory")
    p.add_argument("--model", default=None)
    p.add_argument("--drafting-model", default=None)
    p.add_argument("--revisions", type=int, default=None)
    p.add_argument("--no-lucifer", action="store_true")
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("--dry-run", action="store_true",
                   help="Do not call the API; emit deterministic placeholder")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--seed", type=int, default=None)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_stats(args: argparse.Namespace) -> int:
    cfg = _cfg_from_args(args)
    corpus = Corpus.load(cfg.corpus_dir)
    print(json.dumps(corpus.stats(), indent=2))
    return 0


def cmd_evidence(args: argparse.Namespace) -> int:
    cfg = _cfg_from_args(args)
    corpus = Corpus.load(cfg.corpus_dir)
    index = ThemeIndex(corpus)
    paras = index.select_evidence(args.theme, k=args.k, diversify=not args.nodiv)
    for p in paras:
        snippet = p.content[:140].replace("\n", " ")
        print(f"[{p.ref}] {snippet}…")
    return 0


def cmd_outline(args: argparse.Namespace) -> int:
    cfg = _cfg_from_args(args)
    corpus = Corpus.load(cfg.corpus_dir)
    builder = OutlineBuilder(corpus=corpus, cfg=cfg)
    outline = builder.build(
        theme=args.theme,
        chapters=args.chapters,
        style=args.style,
        voice=args.voice,
        audience=args.audience,
    )
    out = json.dumps(outline.to_dict(), indent=2)
    if args.out:
        Path(args.out).expanduser().write_text(out, encoding="utf-8")
        print(f"Outline → {args.out}")
    else:
        print(out)
    return 0


def cmd_write(args: argparse.Namespace) -> int:
    cfg = _cfg_from_args(args)
    corpus = Corpus.load(cfg.corpus_dir)

    # Collect vault destinations: --vault (repeatable) + output_dir default
    vault_paths: list[Path] = []
    for v in args.vault or []:
        vault_paths.append(Path(v).expanduser())
    if not vault_paths:
        # default to <repo>/artifacts/books
        vault_paths.append(cfg.output_dir)

    renderer = ObsidianRenderer(
        wikilinks=cfg.wikilinks,
        dataview_frontmatter=cfg.dataview_frontmatter,
    )
    multi = MultiVault.from_paths(vault_paths, renderer=renderer)

    writer = BookWriter(corpus=corpus, cfg=cfg, vault=multi)
    book = writer.write(
        theme=args.theme,
        chapters=args.chapters,
        style=args.style,
        voice=args.voice,
        audience=args.audience,
        words_per_chapter=args.words,
        evidence_k=args.evidence_k,
        persist=True,
    )

    print(
        json.dumps(
            {
                "title": book.title,
                "slug": book.slug,
                "chapters": len(book.chapters),
                "word_count": book.word_count(),
                "written_to": book.metadata.get("written_to", []),
                "model": book.metadata.get("model"),
                "wall_time_seconds": book.metadata.get("wall_time_seconds"),
            },
            indent=2,
        )
    )
    return 0


# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="bookwriter",
        description="URANTiOS BookWriter — write books from The Urantia Book.",
    )
    sub = p.add_subparsers(dest="command", required=True)

    # stats
    p_stats = sub.add_parser("stats", help="Print corpus statistics")
    _common_args(p_stats)
    p_stats.set_defaults(func=cmd_stats)

    # evidence
    p_ev = sub.add_parser("evidence", help="Preview theme-selected paragraphs")
    _common_args(p_ev)
    p_ev.add_argument("--theme", required=True)
    p_ev.add_argument("-k", type=int, default=20)
    p_ev.add_argument("--nodiv", action="store_true",
                      help="Disable (paper,section) diversification")
    p_ev.set_defaults(func=cmd_evidence)

    # outline
    p_ol = sub.add_parser("outline", help="Generate a book outline (JSON)")
    _common_args(p_ol)
    p_ol.add_argument("--theme", required=True)
    p_ol.add_argument("--chapters", type=int, default=None)
    p_ol.add_argument("--style", default=None)
    p_ol.add_argument("--voice", default="a scholar who has also knelt")
    p_ol.add_argument("--audience", default="spiritually curious adults")
    p_ol.add_argument("--out", default=None, help="Path to write outline JSON")
    p_ol.set_defaults(func=cmd_outline)

    # write
    p_w = sub.add_parser("write", help="Write a full book end-to-end")
    _common_args(p_w)
    p_w.add_argument("--theme", required=True)
    p_w.add_argument("--chapters", type=int, default=None)
    p_w.add_argument("--words", type=int, default=None,
                     help="Target words per chapter")
    p_w.add_argument("--style", default=None)
    p_w.add_argument("--voice", default="a scholar who has also knelt")
    p_w.add_argument("--audience", default="spiritually curious adults")
    p_w.add_argument("--evidence-k", type=int, default=60)
    p_w.add_argument(
        "--vault",
        action="append",
        default=None,
        help="Obsidian vault root. Repeat for multiple destinations.",
    )
    p_w.set_defaults(func=cmd_write)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
