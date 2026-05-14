# URANTiOS BookWriter

**An automated book-writing app that composes full-length books grounded in The Urantia Book, and stores them as Obsidian-ready Markdown vaults.**

Governed by URANTiOS. Three Values: **Truth · Beauty · Goodness**.

---

## What it does

Given a theme (e.g. *"The Bestowal Career of Michael of Nebadon"*), the BookWriter:

1. **Selects evidence** — a TF-IDF-weighted, paper-diversified slate of ~60 paragraphs from the 14,596-paragraph Urantia Book corpus.
2. **Plans the book** — a JSON outline with title, subtitle, epigraph, preface sketch, and per-chapter (thesis, beats, citation anchors).
3. **Drafts each chapter** — prose with inline `(paper:section.paragraph)` citations, anchored in the evidence set.
4. **Audits with the Lucifer Test** — every chapter is critiqued against four audit questions, then revised if it doesn't `PASS`.
5. **Renders to Obsidian** — one folder per book with a cover / MOC, per-chapter files, wikilink navigation, Dataview-friendly frontmatter, an outline, and a `_meta.json` provenance record.
6. **Fans out to multiple vaults** — same book written to your Obsidian vault, your PhD vault, and an archive directory in one pass.

Prompt caching is enabled by default: the preamble and the entire evidence set are cached once per book, so chapter calls are cheap.

---

## Quick start

```bash
cd URANTiOS
pip install -e .              # installs the `bookwriter` CLI
export ANTHROPIC_API_KEY=sk-ant-...

# Sanity-check the corpus
bookwriter stats

# Preview which paragraphs would be cited for a theme
bookwriter evidence --theme "faith of Jesus" -k 20

# Generate just an outline (cheap — ~1 API call)
bookwriter outline --theme "The Three Absolutes" --out outline.json

# Write a full book, storing it in two vaults
bookwriter write \
  --theme "The Bestowal Career of Michael of Nebadon" \
  --chapters 12 \
  --words 4500 \
  --vault ~/Obsidian/UrantiaBooks \
  --vault /home/user/PhD-Triune-Monism/07_Generated_Books
```

No API key? Run with `--dry-run` — the pipeline will use a deterministic offline stub so you can exercise the full path and inspect the output format.

---

## Architecture

```
bookwriter/
├── __init__.py        # public API
├── config.py          # Config + ThreeValues charter
├── corpus.py          # loads 197 papers; Citation/Paper/Section/Paragraph
├── themes.py          # TF-IDF theme index + diversified evidence selection
├── llm.py             # Claude client (real + DryRun) with prompt caching
├── outline.py         # OutlineBuilder — JSON outline from evidence
├── writer.py          # BookWriter — orchestrates outline → draft → audit → revise
├── obsidian.py        # ObsidianRenderer + ObsidianVault (Markdown + MOC)
├── vault.py           # MultiVault — write to several destinations
├── cli.py             # `bookwriter` CLI
├── prompts/           # all prompt templates
└── tests/             # stdlib-only smoke tests
```

### Data flow

```
        theme
          │
          ▼
  ┌───────────────┐      ┌───────────────┐
  │  ThemeIndex   │◄────►│    Corpus     │   (197 papers, 14,596 paragraphs)
  └──────┬────────┘      └───────────────┘
         │  top-k evidence paragraphs
         ▼
  ┌───────────────┐
  │ OutlineBuilder│   one API call — extended thinking — JSON out
  └──────┬────────┘
         │  Outline (chapters, beats, refs)
         ▼
  ┌───────────────┐
  │  BookWriter   │   per chapter:
  │               │     draft → Lucifer critique → revise if needed
  └──────┬────────┘
         │  Book
         ▼
  ┌───────────────┐
  │   MultiVault  │───► ObsidianVault #1 (local vault)
  │               │───► ObsidianVault #2 (PhD repo)
  │               │───► ObsidianVault #3 (archive)
  └───────────────┘
```

### Obsidian output

A generated book appears at `<vault>/Books/<slug>/`:

```
Books/
├── _Books MOC.md                              ← auto-updated master index
└── the-bestowal-career-of-michael-of-nebadon/
    ├── 00 - The Bestowal Career....md          ← cover + TOC + colophon
    ├── 01 - The Sovereign Son of Nebadon.md
    ├── 02 - ...
    ├── _outline.md                             ← the raw outline
    └── _meta.json                              ← generation provenance
```

Every `(120:4.5)` in prose is linkified to `[[UB-120-04-005|120:4.5]]`, so a paragraph-per-file Urantia Book vault lights up every citation as a backlink.

---

## The Lucifer Test

Before a chapter leaves the writer, it is audited:

1. Are there any unsupported doctrinal claims?
2. Are there citations that could not exist in the Urantia Book's numbering?
3. Has style overrun substance?
4. Does the chapter serve the reader's growth?

Verdict is one of `PASS` / `REVISE` / `FAIL`. A `REVISE` triggers a revision pass (configurable via `--revisions`).

Disable with `--no-lucifer` if you want raw drafts.

---

## Configuration

Every flag can be set as an environment variable:

| Env var                          | Default               | Meaning                                    |
|----------------------------------|-----------------------|--------------------------------------------|
| `ANTHROPIC_API_KEY`              | —                     | Your Anthropic key                         |
| `BOOKWRITER_CORPUS`              | `./urantia-book`      | Path to the `Doc*.json` files              |
| `BOOKWRITER_OUTPUT`              | `./artifacts/books`   | Default output directory                   |
| `BOOKWRITER_MODEL`               | `claude-opus-4-6`     | Model for outline & revision               |
| `BOOKWRITER_DRAFT_MODEL`         | `claude-sonnet-4-6`   | Model for chapter drafts (cheaper)         |
| `BOOKWRITER_REVISIONS`           | `1`                   | Max Lucifer-driven revision passes         |
| `BOOKWRITER_LUCIFER_TEST`        | `1`                   | Enable the Lucifer Test                    |
| `BOOKWRITER_PROMPT_CACHE`        | `1`                   | Enable Anthropic prompt caching            |
| `BOOKWRITER_OBSIDIAN_VAULTS`     | —                     | Colon-separated list of default vaults     |
| `BOOKWRITER_PHD_VAULT`           | —                     | Path to PhD-Triune-Monism vault            |
| `BOOKWRITER_DRY_RUN`             | `0`                   | Offline stub instead of API calls          |

---

## Tests

```bash
python -m bookwriter.tests.test_corpus
```

Stdlib-only. Loads the real 197-paper corpus, exercises the theme index, renderer, outline parser, and a dry-run end-to-end write.

---

## License

Open publication for the benefit of all Nebadon.
