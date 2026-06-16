# nemoclaw/state — observable orchestration state

> **NO SILENT STATES. NO IMPLIED LIVENESS.**

This directory exists so any reader (human, ChatGPT, future agent, watchdog)
can answer one question without guessing:

> **"Right now, is anything alive and what is it doing?"**

Conversational silence is not a state. Files in this directory are.

---

## Core distinction

| Term | Meaning | Implies liveness? |
|---|---|---|
| **Snapshot** | A point-in-time write by an agent at the moment it stopped acting. | **No.** A snapshot says "this was true when I last touched it." It says nothing about now. |
| **Heartbeat** | A periodic write by a *currently-running* process declaring "I am alive at this tick." | **Yes — but only if the writer is actually running.** A stale heartbeat means the writer died. |

Conflating these two creates the exact ambiguity this directory exists to eliminate.

---

## Files in this directory

| File | Writer | Type | Cadence | Reading rule |
|---|---|---|---|---|
| `claude.json` | Claude Code (interactive AI session) | **Snapshot** | Once per Claude turn that mutates state | Treat `written_at_utc` as "Claude was last active at this time." Never as "Claude is alive now." |
| `substrate.json` | **Not yet wired.** Reserved for the future substrate watchdog. | **Heartbeat** | Will be every N seconds when implemented | Currently **must not be interpreted as liveness.** The file declares this explicitly via `"writer": "NOT_YET_WIRED"`. |
| `NOTES.md` | Human operator | Free-form | Whenever | Read like any markdown note. Not machine-parsed. |

---

## Reading discipline

Anyone reading these files **must**:

1. Read the file's own `writer` field. Trust nothing without it.
2. Compare `written_at_utc` against `expected_max_age_seconds`.
   - If the file is older than its own declared max age, treat it as stale — *not* as truth.
3. Never combine fields across files into a single "system status" claim without preserving each writer's identity.
4. If `claude.json` says `WAITING_FOR_HUMAN` but `substrate.json` is `NOT_YET_WIRED`, the correct human reading is:
   - "Claude is parked as of T."
   - "Substrate liveness is unknown — no live writer."
   - **Not** "the system is fine."

---

## No implied liveness — the rule

A file in this directory may **only** assert liveness if a process is *currently writing* it on a known cadence. Until the substrate watchdog exists, no file in this directory asserts liveness. Period.

Snapshots from Claude declare:

```json
{ "type": "snapshot", "DO_NOT_TREAT_AS_LIVENESS": true }
```

The future heartbeat will declare:

```json
{ "type": "heartbeat", "interval_seconds": 30 }
```

Mixing the two markers is a bug.

---

## Writer responsibility boundaries

- **Claude** writes only `claude.json` and may append to `NOTES.md`. Claude **must not** write `substrate.json` — Claude is not the substrate.
- **Substrate watchdog** (when wired) writes only `substrate.json`. It must not modify `claude.json`.
- **Human** writes `NOTES.md` freely; may correct fields in `claude.json` or `substrate.json` only with a `manual_override_reason` field added.
- **Workers** (future) will get their own per-worker state file under `nemoclaw/state/workers/<name>.json`. Same rules: each worker writes its own file only.

A writer touching another writer's file is a protocol violation.

---

## Why this matters

Conversational silence is not orchestration. "Claude appeared parked" is a guess.

This directory replaces guessing with files that are either fresh or honestly stale.

See also: `../CLAUDE.md` → "State Reporting Protocol (mandatory)".
