# doc_auto_dashboard.sh — patch status

All four original issues are PATCHED in this installer:

1. **Master Mermaid append broke rendering** — now regenerated from `setup/master_pipeline.template.mmd` + `setup/jobs.json`.
2. **Wrong GITHUB_REPO default** — now `myedugit/phd-triune-monism`.
3. **Notion page was an echo-stub** — now a real `POST /v1/pages` when `NOTION_TOKEN` is set; honest skip otherwise.
4. **Phantom `canva-cli`** — removed. Canva is an MCP tool (`generate-design-structured`), invoked from a Claude Code session, not from this shell.

Additionally patched:
- `flock -x` around manifest + master regen + git commit/push (safe under parallel execution).
- Empty-commit guard (`git diff --cached --quiet`) prevents git-index races from producing empty commits.
- Real UTF-8 em-dash (—) in commit messages and Notion title (bash does not expand `\u2014`).
- `tee -a` log per job in `$VAULT_DIR/StressTestLogs/`.

## Verification

Sandbox (sequential + parallel 5-job): jobs.json has exactly N entries, master_pipeline.mmd has N unique nodes, zero lock races.

iMac end-to-end (real mmdc, real `NOTION_TOKEN`, real git push) is the remaining live verification step.
