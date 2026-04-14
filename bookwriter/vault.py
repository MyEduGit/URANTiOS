"""
MultiVault — write the same book to multiple destinations.

Each destination is an ``ObsidianVault``-like object (anything with a
``.save(book) -> list[Path]`` method). This lets a single generation
populate:

  • The local Obsidian vault on disk.
  • The PhD-Triune-Monism repo (as a companion artifact).
  • A flat archive directory for backup.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Protocol

from .obsidian import ObsidianRenderer, ObsidianVault
from .writer import Book


class VaultDestination(Protocol):
    def save(self, book: Book) -> list[Path]:  # noqa: D401
        ...


@dataclass
class MultiVault:
    destinations: list[VaultDestination]

    @classmethod
    def from_paths(
        cls,
        paths: Iterable[Path | str],
        *,
        renderer: ObsidianRenderer | None = None,
    ) -> "MultiVault":
        renderer = renderer or ObsidianRenderer()
        dests: list[VaultDestination] = []
        for p in paths:
            path = Path(p).expanduser()
            if path:
                dests.append(ObsidianVault(root=path, renderer=renderer))
        return cls(destinations=dests)

    def save(self, book: Book) -> list[Path]:
        written: list[Path] = []
        for dest in self.destinations:
            written.extend(dest.save(book))
        return written
