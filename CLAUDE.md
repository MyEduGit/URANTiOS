# URANTiOS — Instructions for AI agents

Follow these instructions for all tasks in the URANTiOS environment.

## 1. Sovereign values (URANTiOS v2.0 / COVENANT.md)

- **TRUTH**: Never claim more than the evidence supports. Never fabricate or
  embellish logs, outputs, or Urantia Book text. Mark uncertainty explicitly.
- **GOODNESS**: Mircea is the Father Function: final authority on all
  decisions. When a choice is ambiguous AND irreversible, stop and ask; when
  ambiguous AND reversible, choose the Three Values and report. Accept audit
  at any time.
- **BEAUTY**: Keep code, prompts, and artifacts clean, modular, and minimal.

## 2. Canonical integrity (non-negotiable)

- `urantia-book/*.json` is the source of truth (Doc000 = Foreword,
  Doc001–Doc196 = Papers). Treat it as READ-ONLY: never edit, reformat, or
  "fix" paragraph text without explicit instruction.
- Quote Urantia Book text verbatim; never paraphrase when the task calls for
  canonical text.
- Cite as paper:section.paragraph (e.g. 1:0.1; Foreword = 0:x.y).
- Respect canonical order: Foreword first, then Papers 1–196, one paragraph
  at a time. Never skip, merge, or summarise away canonical content (see
  `META_PROMPT_URANTIOS.md` for the per-paragraph output contract).
- After editing any JSON, validate it parses (`python3 -m json.tool`) before
  committing.

## 3. System ontology and names

- **URANTiOS**: the AI operating system specification (this repo).
  `soul/URANTiOS_v2.md` is the kernel.
- **NemoClaw**: the AI orchestration system (n8n, Docker, PostgreSQL, Redis,
  Qdrant, Claude Code, Obsidian). Never call it OpenClaw, NanoClaw, or
  nano claw.
- **iMac_M4**: the physical host. Say "NemoClaw deployed on iMac_M4", never
  "the iMac is NemoClaw".
- Legacy paths under `~/.openclaw/` exist in pipeline scripts; do not rename
  or "correct" them without asking.

## 4. Coding and style

- British English in all user-facing text and documentation (colour,
  behaviour, initialise). Exception: verbatim Urantia Book quotations keep
  their original spelling.
- No em dashes in user-facing text; use commas, colons, or parentheses.
- Emojis sparingly and strategically in CLI/log output for visual hierarchy;
  never in canonical or scholarly artifacts.

## 5. Safety and logging

- Dry-run pipeline scripts and validate outputs in a sandbox before running
  against the live corpus or deploying.
- Log every action and decision; every claim must be auditable back to
  evidence.
- Commit with clear, descriptive messages; never force-push over history
  containing canonical data.

## Testing these instructions

The behavioural probe suite lives in `tests/instruction-probes.md`. Rerun it
whenever this file changes. Mechanical enforcement of the machine-checkable
rules runs in CI via `tests/guards.sh`.
