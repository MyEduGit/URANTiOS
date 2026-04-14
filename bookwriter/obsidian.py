"""
Obsidian renderer and vault.

Produces a folder-per-book structure that Obsidian (and most Markdown
tools) read natively:

    <vault>/
      Books/
        <slug>/
          00 - <Title>.md           ← book cover + TOC (MOC)
          01 - <Chapter 1 title>.md
          02 - ...
          _meta.json                ← generation metadata
          _outline.md               ← the raw outline
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .writer import Book, WrittenChapter


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_FRONTMATTER_SAFE_RE = re.compile(r"[\r\n]+")


def _yaml_escape(value: str) -> str:
    """Minimal YAML string escape — good enough for Obsidian frontmatter."""
    v = _FRONTMATTER_SAFE_RE.sub(" ", value).strip()
    if any(c in v for c in ":\"'#[]{}|>*&!%@`"):
        v = v.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{v}"'
    return v


def _yaml_list(values: Iterable[str]) -> str:
    items = list(values)
    if not items:
        return "[]"
    return "[" + ", ".join(_yaml_escape(v) for v in items) + "]"


def _slug(text: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in text)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:80] or "untitled"


# ---------------------------------------------------------------------------
# Citation linkification
# ---------------------------------------------------------------------------

# Matches in-prose Urantia-Book citations like (120:4.5) or (0:1.1).
CITATION_RE = re.compile(r"\((\d+):(\d+)\.(\d+)\)")


def linkify_citations(text: str, *, wikilinks: bool = True) -> str:
    """Turn (120:4.5) into [[UB-120-04-005|120:4.5]] (or a plain ref)."""
    if not wikilinks:
        return text

    def _sub(m: re.Match[str]) -> str:
        paper, section, para = m.group(1), m.group(2), m.group(3)
        target = f"UB-{int(paper):03d}-{int(section):02d}-{int(para):03d}"
        label = f"{paper}:{section}.{para}"
        return f"[[{target}|{label}]]"

    return CITATION_RE.sub(_sub, text)


def extract_citations(text: str) -> list[str]:
    return [f"{m[0]}:{m[1]}.{m[2]}" for m in CITATION_RE.findall(text)]


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------

@dataclass
class ObsidianRenderer:
    wikilinks: bool = True
    dataview_frontmatter: bool = True
    author: str = "URANTiOS BookWriter"

    def render_book(self, book: Book) -> dict[str, str]:
        """Return a mapping ``filename -> content`` for the book's files."""
        files: dict[str, str] = {}

        # Cover / MOC --------------------------------------------------
        files[f"00 - {_safe_filename(book.title)}.md"] = self._render_cover(book)

        # Chapters -----------------------------------------------------
        for ch in book.chapters:
            fname = f"{ch.number:02d} - {_safe_filename(ch.title)}.md"
            files[fname] = self._render_chapter(book, ch)

        # Outline (raw) ------------------------------------------------
        files["_outline.md"] = self._render_outline(book)
        files["_meta.json"] = json.dumps(book.metadata, indent=2, sort_keys=True)

        return files

    # --- cover / MOC ---------------------------------------------------
    def _render_cover(self, book: Book) -> str:
        gen = book.metadata.get("generated_at") or datetime.now(
            timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        all_refs = sorted({
            r for c in book.chapters for r in extract_citations(c.body)
        })

        fm_lines = [
            "---",
            f"title: {_yaml_escape(book.title)}",
        ]
        if book.subtitle:
            fm_lines.append(f"subtitle: {_yaml_escape(book.subtitle)}")
        fm_lines += [
            f"theme: {_yaml_escape(book.theme)}",
            f"author: {_yaml_escape(self.author)}",
            f"generated: {gen}",
            f"chapters: {len(book.chapters)}",
            f"word_count_estimate: {book.word_count()}",
            "type: urantia-book-derivative",
            "tags: [urantios, urantia-book, generated-book]",
        ]
        if self.dataview_frontmatter:
            fm_lines.append(f"citation_count: {len(all_refs)}")
        fm_lines.append("---\n")

        lines = ["\n".join(fm_lines)]
        lines.append(f"# {book.title}\n")
        if book.subtitle:
            lines.append(f"_{book.subtitle}_\n")
        if book.epigraph:
            lines.append(f"> {book.epigraph}\n")
        if book.preface_sketch:
            lines.append("## Preface\n")
            lines.append(
                linkify_citations(book.preface_sketch, wikilinks=self.wikilinks)
                + "\n"
            )
        lines.append("## Contents\n")
        for ch in book.chapters:
            fname = f"{ch.number:02d} - {_safe_filename(ch.title)}"
            if self.wikilinks:
                lines.append(f"- [[{fname}|Chapter {ch.number} — {ch.title}]]")
            else:
                lines.append(f"- Chapter {ch.number} — {ch.title}")
        lines.append("")
        lines.append("## Source references\n")
        lines.append(
            "Every claim in this book is anchored to The Urantia Book. "
            "All cited paragraphs:\n"
        )
        if all_refs:
            per_line = 6
            for i in range(0, len(all_refs), per_line):
                chunk = all_refs[i : i + per_line]
                if self.wikilinks:
                    lines.append(
                        ", ".join(
                            f"[[UB-{int(r.split(':')[0]):03d}-"
                            f"{int(r.split(':')[1].split('.')[0]):02d}-"
                            f"{int(r.split('.')[1]):03d}|{r}]]"
                            for r in chunk
                        )
                    )
                else:
                    lines.append(", ".join(chunk))
        lines.append("")
        lines.append(
            "## Colophon\n\n"
            f"Generated {gen} by URANTiOS BookWriter under the governance "
            "of the Three Values — Truth, Beauty, Goodness.\n"
        )
        return "\n".join(lines)

    # --- chapter -------------------------------------------------------
    def _render_chapter(self, book: Book, ch: WrittenChapter) -> str:
        cites = extract_citations(ch.body)
        uniq = sorted(set(cites))

        fm_lines = [
            "---",
            f"book: {_yaml_escape(book.title)}",
            f"chapter: {ch.number}",
            f"title: {_yaml_escape(ch.title)}",
            f"thesis: {_yaml_escape(ch.thesis)}",
            f"citations: {_yaml_list(uniq)}",
            "tags: [urantios, urantia-book, chapter]",
        ]
        if ch.lucifer_verdict:
            fm_lines.append(f"lucifer_verdict: {ch.lucifer_verdict}")
        if ch.revision_count:
            fm_lines.append(f"revisions: {ch.revision_count}")
        fm_lines.append("---\n")

        body = linkify_citations(ch.body, wikilinks=self.wikilinks)
        cover_name = f"00 - {_safe_filename(book.title)}"
        nav_prev = None
        nav_next = None
        if ch.number > 1:
            nav_prev = ch.number - 1
        if ch.number < len(book.chapters):
            nav_next = ch.number + 1

        nav_parts = []
        if self.wikilinks:
            nav_parts.append(f"[[{cover_name}|↑ Book]]")
            if nav_prev:
                prev_ch = book.chapters[nav_prev - 1]
                nav_parts.append(
                    f"[[{nav_prev:02d} - {_safe_filename(prev_ch.title)}|← Ch {nav_prev}]]"
                )
            if nav_next:
                next_ch = book.chapters[nav_next - 1]
                nav_parts.append(
                    f"[[{nav_next:02d} - {_safe_filename(next_ch.title)}|Ch {nav_next} →]]"
                )
        nav = " · ".join(nav_parts)

        parts = ["\n".join(fm_lines), body.strip(), ""]
        if nav:
            parts.append(f"---\n{nav}\n")
        return "\n\n".join(parts)

    # --- outline -------------------------------------------------------
    def _render_outline(self, book: Book) -> str:
        lines = ["---", "type: outline", "tags: [urantios, outline]", "---", ""]
        lines.append(f"# Outline — {book.title}\n")
        if book.subtitle:
            lines.append(f"_{book.subtitle}_\n")
        lines.append(f"**Theme:** {book.theme}\n")
        if book.epigraph:
            lines.append(f"> {book.epigraph}\n")
        if book.preface_sketch:
            lines.append(f"**Preface sketch.** {book.preface_sketch}\n")
        for ch in book.outline.chapters:
            lines.append(f"## Chapter {ch.number} — {ch.title}")
            lines.append(f"**Thesis.** {ch.thesis}\n")
            if ch.key_refs:
                lines.append(
                    "**Anchors.** "
                    + ", ".join(f"({r})" for r in ch.key_refs)
                )
            if ch.beats:
                lines.append("")
                for b in ch.beats:
                    lines.append(f"- {b}")
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Vault
# ---------------------------------------------------------------------------

_INVALID_FS_CHARS_RE = re.compile(r"[<>:\"/\\|?*\x00-\x1f]")


def _safe_filename(s: str) -> str:
    cleaned = _INVALID_FS_CHARS_RE.sub("-", s).strip().strip(".")
    return cleaned[:120] or "untitled"


@dataclass
class ObsidianVault:
    """Persist books to an Obsidian-compatible folder tree."""

    root: Path
    books_subdir: str = "Books"
    renderer: ObsidianRenderer | None = None
    overwrite: bool = True

    def __post_init__(self) -> None:
        self.root = Path(self.root).expanduser()
        if self.renderer is None:
            self.renderer = ObsidianRenderer()

    def save(self, book: Book) -> list[Path]:
        renderer = self.renderer
        assert renderer is not None
        out_dir = self.root / self.books_subdir / book.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        for fname, content in renderer.render_book(book).items():
            path = out_dir / fname
            if path.exists() and not self.overwrite:
                continue
            path.write_text(content, encoding="utf-8")
            written.append(path)

        # Ensure a top-level Books MOC exists and is up to date
        moc_path = self.root / self.books_subdir / "_Books MOC.md"
        self._append_to_moc(moc_path, book, out_dir)
        written.append(moc_path)
        return written

    def _append_to_moc(self, moc_path: Path, book: Book, book_dir: Path) -> None:
        line = (
            f"- [[{book_dir.name}/00 - {_safe_filename(book.title)}|"
            f"{book.title}]] — {book.theme}"
        )
        header = (
            "---\ntype: moc\ntags: [urantios, moc, books]\n---\n\n"
            "# Books — Master Index\n\n"
            "Every book generated by URANTiOS BookWriter is listed here.\n\n"
        )
        if not moc_path.exists():
            moc_path.write_text(header + line + "\n", encoding="utf-8")
            return
        existing = moc_path.read_text(encoding="utf-8")
        if line in existing:
            return
        if not existing.endswith("\n"):
            existing += "\n"
        moc_path.write_text(existing + line + "\n", encoding="utf-8")
