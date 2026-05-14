# Multi-AI Obsidian Integration — this repo's role

This repo is one of four AI-source repos whose outputs flow into a single shared Obsidian vault:

- **myedugit/phd-triune-monism** — the shared vault itself
- **myedugit/mircea-constellation** — AI source
- **myedugit/lobsterbot** — AI source
- **myedugit/URANTiOS** — AI source

All four repos carry the same `/doc` installer on branch `claude/multi-ai-obsidian-integration-jkoI9` so any AI agent can scaffold a job folder in the shared vault with identical structure and identical guarantees (flock-safe parallel execution, regenerated master Mermaid pipeline, honest Canva/Notion/Zapier handling).

The installer's `GITHUB_REPO` default points at the vault repo (`myedugit/phd-triune-monism`) because that is where job folders and the master pipeline physically live. This repo's AI outputs are written into the vault, then committed there.

See `setup/doc_auto_dashboard.README.md` for the full patch/verification log.
