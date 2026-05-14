"""CLI entry point: python -m bookwriter {stats,evidence,write}"""
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

def main(argv=None):
    p = argparse.ArgumentParser(prog="bookwriter")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("stats")
    s.add_argument("--corpus", default=None)
    e = sub.add_parser("evidence")
    e.add_argument("--theme", required=True)
    e.add_argument("-k", type=int, default=20)
    e.add_argument("--corpus", default=None)
    args = p.parse_args(argv)
    {"stats": cmd_stats, "evidence": cmd_evidence}[args.cmd](args)
    return 0
