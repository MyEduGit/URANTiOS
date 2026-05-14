"""Obsidian renderer and vault."""
from __future__ import annotations
import json, re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from .writer import Book, WrittenChapter

CITATION_RE = re.compile(r"\((\d+):(\d+)\.(\d+)\)")
_INVALID_FS = re.compile(r"[<>:\"/\\|?*\x00-\x1f]")

def linkify_citations(text: str, *, wikilinks: bool = True) -> str:
    if not wikilinks: return text
    def _sub(m):
        p, s, pa = m.group(1), m.group(2), m.group(3)
        return f"[[UB-{int(p):03d}-{int(s):02d}-{int(pa):03d}|{p}:{s}.{pa}]]"
    return CITATION_RE.sub(_sub, text)

def extract_citations(text: str) -> list[str]:
    return [f"{m[0]}:{m[1]}.{m[2]}" for m in CITATION_RE.findall(text)]

def _safe(s: str) -> str:
    return _INVALID_FS.sub("-", s).strip().strip(".")[:120] or "untitled"

def _slug(text: str) -> str:
    s = "".join(c.lower() if c.isalnum() else "-" for c in text)
    while "--" in s: s = s.replace("--", "-")
    return s.strip("-")[:80] or "untitled"

def _ye(v: str) -> str:
    if any(c in v for c in ':\"\'#[]{}|>*&!%@`'):
        return f'"{v.replace(chr(34), "")}"'
    return v

@dataclass
class ObsidianRenderer:
    wikilinks: bool = True
    dataview_frontmatter: bool = True
    author: str = "URANTiOS BookWriter"

    def render_book(self, book: Book) -> dict[str, str]:
        files = {}
        files[f"00 - {_safe(book.title)}.md"] = self._cover(book)
        for ch in book.chapters:
            files[f"{ch.number:02d} - {_safe(ch.title)}.md"] = self._chapter(book, ch)
        files["_outline.md"] = self._outline(book)
        files["_meta.json"] = json.dumps(book.metadata, indent=2, sort_keys=True)
        return files

    def _cover(self, book: Book) -> str:
        gen = book.metadata.get("generated_at", _now())
        all_refs = sorted({r for c in book.chapters for r in extract_citations(c.body)})
        lines = ["---", f"title: {_ye(book.title)}"]
        if book.subtitle: lines.append(f"subtitle: {_ye(book.subtitle)}")
        lines += [f"theme: {_ye(book.theme)}", f"author: {_ye(self.author)}",
                  f"generated: {gen}", f"chapters: {len(book.chapters)}",
                  f"word_count: {book.word_count()}", "type: urantia-book-derivative",
                  "tags: [urantios, urantia-book, generated-book]"]
        if self.dataview_frontmatter: lines.append(f"citation_count: {len(all_refs)}")
        lines.append("---\n")
        lines.append(f"# {book.title}\n")
        if book.subtitle: lines.append(f"_{book.subtitle}_\n")
        if book.epigraph: lines.append(f"> {book.epigraph}\n")
        if book.preface_sketch:
            lines.append("## Preface\n")
            lines.append(linkify_citations(book.preface_sketch, wikilinks=self.wikilinks) + "\n")
        lines.append("## Contents\n")
        for ch in book.chapters:
            fname = f"{ch.number:02d} - {_safe(ch.title)}"
            if self.wikilinks:
                lines.append(f"- [[{fname}|Chapter {ch.number} — {ch.title}]]")
            else:
                lines.append(f"- Chapter {ch.number} — {ch.title}")
        lines += ["", "## Colophon\n",
                   f"Generated {gen} by URANTiOS BookWriter — Truth, Beauty, Goodness.\n"]
        return "\n".join(lines)

    def _chapter(self, book: Book, ch: WrittenChapter) -> str:
        cites = sorted(set(extract_citations(ch.body)))
        lines = ["---", f"book: {_ye(book.title)}", f"chapter: {ch.number}",
                 f"title: {_ye(ch.title)}", f"thesis: {_ye(ch.thesis)}",
                 "tags: [urantios, urantia-book, chapter]"]
        if ch.lucifer_verdict: lines.append(f"lucifer_verdict: {ch.lucifer_verdict}")
        lines.append("---\n")
        body = linkify_citations(ch.body, wikilinks=self.wikilinks)
        cover = f"00 - {_safe(book.title)}"
        nav = []
        if self.wikilinks:
            nav.append(f"[[{cover}|↑ Book]]")
            if ch.number > 1:
                prev = book.chapters[ch.number-2]
                nav.append(f"[[{ch.number-1:02d} - {_safe(prev.title)}|← Ch {ch.number-1}]]")
            if ch.number < len(book.chapters):
                nxt = book.chapters[ch.number]
                nav.append(f"[[{ch.number+1:02d} - {_safe(nxt.title)}|Ch {ch.number+1} →]]")
        parts = ["\n".join(lines), body.strip(), ""]
        if nav: parts.append(f"---\n{' · '.join(nav)}\n")
        return "\n\n".join(parts)

    def _outline(self, book: Book) -> str:
        lines = ["---", "type: outline", "tags: [urantios, outline]", "---", "",
                 f"# Outline — {book.title}\n", f"**Theme:** {book.theme}\n"]
        if book.epigraph: lines.append(f"> {book.epigraph}\n")
        for ch in book.outline.chapters:
            lines.append(f"## Chapter {ch.number} — {ch.title}")
            lines.append(f"**Thesis.** {ch.thesis}\n")
            if ch.key_refs: lines.append("**Anchors.** " + ", ".join(f"({r})" for r in ch.key_refs))
            if ch.beats:
                lines.append("")
                for b in ch.beats: lines.append(f"- {b}")
            lines.append("")
        return "\n".join(lines)

def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

@dataclass
class ObsidianVault:
    root: Path
    books_subdir: str = "Books"
    renderer: ObsidianRenderer | None = None
    overwrite: bool = True

    def __post_init__(self):
        self.root = Path(self.root).expanduser()
        if self.renderer is None: self.renderer = ObsidianRenderer()

    def save(self, book: Book) -> list[Path]:
        r = self.renderer
        out_dir = self.root / self.books_subdir / book.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        written = []
        for fname, content in r.render_book(book).items():
            path = out_dir / fname
            path.write_text(content, encoding="utf-8")
            written.append(path)
        moc = self.root / self.books_subdir / "_Books MOC.md"
        self._update_moc(moc, book, out_dir)
        written.append(moc)
        return written

    def _update_moc(self, moc_path: Path, book: Book, book_dir: Path):
        line = f"- [[{book_dir.name}/00 - {_safe(book.title)}|{book.title}]] — {book.theme}"
        header = "---\ntype: moc\ntags: [urantios, moc, books]\n---\n\n# Books — Master Index\n\n"
        if not moc_path.exists():
            moc_path.write_text(header + line + "\n", encoding="utf-8")
            return
        existing = moc_path.read_text(encoding="utf-8")
        if line in existing: return
        if not existing.endswith("\n"): existing += "\n"
        moc_path.write_text(existing + line + "\n", encoding="utf-8")
