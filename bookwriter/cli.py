"""CLI entry point: python -m bookwriter {stats,evidence,write,daily}"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from .config import Config
from .corpus import Corpus
from .themes import ThemeIndex
from .obsidian import ObsidianVault
from .vault import MultiVault
from .writer import BookWriter


def cmd_stats(args):
    corpus = Corpus.load(args.corpus or Config.from_env().corpus_dir)
    print(json.dumps(corpus.stats(), indent=2))


def cmd_evidence(args):
    corpus = Corpus.load(args.corpus or Config.from_env().corpus_dir)
    idx = ThemeIndex(corpus)
    for p in idx.select_evidence(args.theme, k=args.k):
        print(f"[{p.ref}] {p.content[:140].replace(chr(10),' ')}…")


def cmd_write(args):
    cfg = Config.from_env(dry_run=args.dry_run)
    corpus = Corpus.load(args.corpus or cfg.corpus_dir)
    vaults = None
    if args.vault:
        vaults = MultiVault.from_paths(args.vault)
    elif cfg.obsidian_vault_dirs:
        vaults = MultiVault.from_paths(cfg.obsidian_vault_dirs)
    writer = BookWriter(corpus=corpus, cfg=cfg, vault=vaults)
    book = writer.write(theme=args.theme, chapters=args.chapters)
    print(json.dumps({
        "title": book.title,
        "chapters": len(book.chapters),
        "words": book.word_count(),
        "slug": book.slug,
        "metadata": book.metadata,
    }, indent=2))


def cmd_daily(args):
    from .daily import DailyPublisher
    publisher = DailyPublisher.from_env()
    result = publisher.run(dry_run=args.dry_run, force_theme=args.theme)
    print(json.dumps(result, indent=2))


def main(argv=None):
    p = argparse.ArgumentParser(prog="bookwriter")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("stats")
    s.add_argument("--corpus", default=None)

    e = sub.add_parser("evidence")
    e.add_argument("--theme", required=True)
    e.add_argument("-k", type=int, default=20)
    e.add_argument("--corpus", default=None)

    w = sub.add_parser("write")
    w.add_argument("--theme", required=True)
    w.add_argument("--chapters", type=int, default=None)
    w.add_argument("--vault", action="append", default=None)
    w.add_argument("--dry-run", action="store_true")
    w.add_argument("--corpus", default=None)

    d = sub.add_parser("daily")
    d.add_argument("--dry-run", action="store_true")
    d.add_argument("--theme", default=None)

    args = p.parse_args(argv)
    {"stats": cmd_stats, "evidence": cmd_evidence,
     "write": cmd_write, "daily": cmd_daily}[args.cmd](args)
    return 0
