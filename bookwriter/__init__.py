"""
URANTiOS BookWriter — automated book generation from The Urantia Book.

Governed by UrantiOS: Truth, Beauty, Goodness.

Public API:
    from bookwriter import BookWriter, Corpus, ObsidianVault

    corpus  = Corpus.load()
    vault   = ObsidianVault("~/Obsidian/UrantiaBooks")
    writer  = BookWriter(corpus=corpus, vault=vault)
    book    = writer.write(theme="The Bestowal Career of Michael of Nebadon",
                           chapters=12, style="scholarly-devotional")
"""
from .corpus import Corpus, Paper, Section, Paragraph, Citation
from .outline import Outline, Chapter, OutlineBuilder
from .writer import BookWriter, Book, WrittenChapter
from .obsidian import ObsidianRenderer, ObsidianVault
from .vault import MultiVault, VaultDestination
from .config import Config, ThreeValues
from .themes import ThemeIndex

__version__ = "1.0.0"
__all__ = [
    "BookWriter",
    "Book",
    "WrittenChapter",
    "Corpus",
    "Paper",
    "Section",
    "Paragraph",
    "Citation",
    "Outline",
    "Chapter",
    "OutlineBuilder",
    "ObsidianRenderer",
    "ObsidianVault",
    "MultiVault",
    "VaultDestination",
    "Config",
    "ThreeValues",
    "ThemeIndex",
]
