# Obsidian vault — conventions

This directory is the **canonical knowledge store** for NemoClaw. It is
designed to be readable without AI tooling, without Obsidian itself, and
without any proprietary format.

## Hard rules

| Rule | Why |
|---|---|
| Markdown only (`.md`) | portable, diffable, durable |
| Plain text where possible (no obscure embeds) | survives tool churn |
| Durable filenames (no spaces, no emoji, lowercase + hyphens) | grep-friendly |
| Timestamped archives (`YYYY/MM/...`) | chronological recoverability |
| No proprietary lock-in | no `.canvas`, no plugin-only formats in canon |
| Readable without AI tools | a human with `cat` must understand it |

## Layout

```
obsidian/
├── README.md                # this file
├── _index.md                # vault entry point (created on first use)
├── topics/                  # long-lived topic notes
├── archive/
│   └── YYYY/
│       └── MM/
│           └── <task_id>/   # sealed artifacts (see WORKFLOW_MODEL.md)
├── conversations/           # imported governance conversations
└── decisions/               # ADR-style decision records
```

## Naming

- Files: `kebab-case.md` (e.g. `bootstrap-decision.md`).
- Task artifact directories: keep the `task_id` from the manifest; do not
  rename.
- Decision records: `YYYY-MM-DD-short-slug.md`.

## Linking

- Use Obsidian wikilinks `[[topic]]` for internal references.
- Use absolute repo-relative paths for code references
  (e.g. `nemoclaw/docs/ARCHITECTURE.md`).
- Never embed binaries; link to them and store under `archive/`.

## What does NOT live here

- secrets — never
- runtime data (Postgres dumps, Redis snapshots) — those go in `backups/`
- raw worker logs — those go in `archive/<task_id>/logs.txt`

## What MUST live here

- governance decisions (every approval gate outcome)
- architecture changes (with rationale)
- post-incident notes
- sealed task artifacts (after verification)
