# NemoClaw — Security

## Threat model in one paragraph

The primary risk in an AI orchestration substrate is not external attack —
it is **a worker (or its model) taking an action that is hard to reverse
and was not explicitly authorized**. Everything in this document optimizes
for catching such actions before they happen, and making them recoverable
if they do.

## Approval gates

Every action that is destructive, externally visible, or hard to reverse
passes through an approval gate. Workers cannot bypass gates.

### Gated actions
- deleting any user data
- force-pushing any branch
- pushing to a protected branch
- exposing any service on a non-loopback interface
- modifying files outside the worker's scoped paths
- running shell with `rm -rf`, `git reset --hard`, `git clean -fdx`,
  `--no-verify`, or any flag that bypasses signing/hooks
- modifying CI/CD configuration
- sending messages on shared channels (Slack, email, Telegram, GitHub)
- uploading content to third-party services

### Non-gated (free) actions
- reading files within scoped paths
- running tests / linters
- writing artifact directories under `archive/`
- queueing follow-up tasks (which themselves are subject to gates)

## Sandboxing

- Workers run in containers with mounted scoped volumes only.
- No worker container has Docker socket access.
- No worker has write access to `nemo-core/` at runtime — orchestration
  code is read-only to workers.
- All outbound network from worker containers is logged.

## Secret isolation

- Secrets live only in `.env` (gitignored) and are injected at container
  start. They are never written into artifacts, logs, or commit history.
- `.env.example` is the only secret-shaped file in git, and it contains
  only placeholders.
- Pre-commit hooks (to be added) will reject diffs containing common
  secret shapes.

## Restricted execution

- `bootstrap.sh` refuses to run if `.env` is missing.
- `docker-compose.yml` requires every secret env var to be set
  (`${VAR:?...}` syntax) — no silent defaults for credentials.
- Bind address defaults to `127.0.0.1`. Public exposure requires:
  1. explicit human approval recorded in `archive/conversations/`,
  2. a documented rationale in `docs/`,
  3. the corresponding override in `docker-compose.override.yml` (gitignored).

## Audit rules

- Every worker invocation produces an artifact (see
  `docs/WORKFLOW_MODEL.md`).
- Every governance decision is archived as markdown under
  `archive/conversations/`.
- All commits are made on dedicated branches; no direct commits to `main`.
- `logs/audit.log` is append-only; rotation is by date, never truncation.
- `manifests/bootstrap_manifest.json` records what was created, when, and
  by whom.

## What is explicitly forbidden

- Faking MCP implementations.
- Self-modifying governance logic.
- Recursive autonomous loops.
- Workers granting themselves permissions.
- Skipping verification to claim a task complete.
