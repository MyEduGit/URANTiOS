# NOTES

> Free-form human-readable notes about state, decisions in flight, gotchas
> in the substrate, or anything that doesn't fit a structured field in
> `claude.json` / `substrate.json`.
>
> Not machine-parsed. Append-only by convention; don't rewrite history.
> Format suggestion: `## YYYY-MM-DD HH:MM TZ — short title`

---

## 2026-05-07 — protocol initial entry

State protocol introduced today. Files in this directory replace conversational
silence as the source of truth for "what is the system doing right now".

Foundational doctrine:
- **NO SILENT STATES**
- **NO IMPLIED LIVENESS**

Substrate watchdog explicitly deferred. Until it exists, `substrate.json` is a
declared placeholder; trust `docker ps` for actual substrate liveness.
