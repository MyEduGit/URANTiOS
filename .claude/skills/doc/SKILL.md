---
name: doc
description: Scaffold a standardized multi-AI job folder in the shared Obsidian vault, regenerate the master Mermaid pipeline, commit to GitHub, and (when a Claude Code session is active) call Canva/Notion MCP tools for the rich artifacts the shell cannot produce.
---

# /doc — hybrid skill

## Shell responsibilities (always)
- Run `setup/doc_auto_dashboard.sh <slug>`.
- Files + git + REST Notion (when `NOTION_TOKEN` set) + Zapier (when `ZAPIER_HOOK_URL` set).

## MCP responsibilities (only from a Claude Code session)
- Canva: call `generate-design-structured` to produce `<slug>-canva.png` in `assets/`.
- Notion (optional): create richer pages via the Notion MCP instead of the REST fallback.

## Invariants
- `setup/jobs.json` is the single source of truth for per-job URLs.
- `master_pipeline.mmd` is regenerated from `setup/master_pipeline.template.mmd` + `jobs.json`, never appended.
- The shell script never claims success for MCP-only artifacts.
