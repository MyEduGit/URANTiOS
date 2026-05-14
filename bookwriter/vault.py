"""MultiVault — write the same book to multiple destinations."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from .obsidian import ObsidianRenderer, ObsidianVault
from .writer import Book

@dataclass
class MultiVault:
    destinations: list
    @classmethod
    def from_paths(cls, paths, *, renderer=None):
        renderer = renderer or ObsidianRenderer()
        return cls([ObsidianVault(root=Path(p).expanduser(), renderer=renderer) for p in paths])
    def save(self, book: Book) -> list[Path]:
        written = []
        for d in self.destinations:
            written.extend(d.save(book))
        return written
