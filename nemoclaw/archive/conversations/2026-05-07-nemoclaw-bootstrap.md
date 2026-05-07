# Conversation archive — NemoClaw bootstrap

- **Date (UTC):** 2026-05-07
- **Branch:** `claude/nemoclaw-setup-GDKGy`
- **Repo:** `MyEduGit/URANTiOS`
- **Parent commit at start:** `0f34580f13234b8a9810ae0453e1c4203dcab9f8`
- **Bootstrap target (decided):** `/home/user/URANTiOS/nemoclaw/`
- **Worker:** Claude Code (Opus 4.7, 1M context)

This archive is the canonical record of the governance decisions made
during the NemoClaw bootstrap. It is plain markdown so it remains
readable without AI tooling.

---

## Turn 1 — User directive

The user issued the `NEMOCLAW BOOTSTRAP EXECUTION DIRECTIVE`. Key
constraints from the directive (paraphrased; full text retained in
session transcript):

- Role: execution worker only; never governance authority.
- Architecture principles: Verification Before Claim, Obsidian-first
  archival, stateless workers, queue-centric execution, artifact-first
  workflows, human-governed autonomy, local-first sovereignty,
  git-backed auditability, recoverability over cleverness.
- Forbidden without approval: destructive ops, force pushes, public
  exposure, modifying unrelated folders, recursive autonomous loops,
  self-modifying governance logic.
- Required structure: `~/NemoClaw/` with subdirs `manifests/`,
  `workflows/`, `logs/`, `backups/`, `archive/conversations/`,
  `obsidian/`, `postgres/`, `redis/`, `n8n/`, `nemo-core/`, `workers/`,
  `scripts/`, `docs/`.
- Required artifacts: `CLAUDE.md`, `README.md`, `docker-compose.yml`,
  `.env.example`, `bootstrap.sh`, `docs/ARCHITECTURE.md`,
  `docs/SECURITY.md`, `docs/WORKFLOW_MODEL.md`, `obsidian/README.md`,
  `manifests/bootstrap_manifest.json`, `logs/bootstrap.log`, archived
  conversation.
- Verification rule: never claim "done" / "working" / "successful"
  without showing command, exact result, and generated files.
- MCP rule: scaffold placeholders only; do not fake implementations.

## Turn 2 — Worker verification block

The worker (Claude) ran a verification step before any mutation and
surfaced a conflict:

- Session was bound to working directory `/home/user/URANTiOS`,
  not `~/NemoClaw` (= `/root/NemoClaw`, which did not exist).
- Designated git branch was `claude/nemoclaw-setup-GDKGy` on the
  URANTiOS repo.
- GitHub MCP scope was restricted to `myedugit/urantios`.

Verified state at that moment:

| Item | Value |
|---|---|
| `$HOME` | `/root` |
| PWD | `/home/user/URANTiOS` |
| `/root/NemoClaw` | absent |
| `/home/user/URANTiOS` | git repo, branch `claude/nemoclaw-setup-GDKGy`, working tree clean |

The worker presented three destination options to the user and refused
to self-authorize a choice.

## Turn 3 — User decision

The user authorized:

> Proceed with: `/home/user/URANTiOS/nemoclaw/`
>
> - contain all new bootstrap assets inside the `nemoclaw/` subdirectory
> - do NOT modify unrelated URANTiOS files
> - preserve git-backed auditability on current branch
> - preserve MCP scope compatibility
> - maintain deterministic isolation from existing repo content
>
> Continue execution using the existing branch `claude/nemoclaw-setup-GDKGy`.

This decision is binding for this branch.

## Turn 4 — Bootstrap execution

Executed in this order:

1. Verified target path absent before mutation.
2. Created `nemoclaw/` directory tree.
3. Generated config files (`.gitignore`, `.env.example`,
   `docker-compose.yml`, `bootstrap.sh`).
4. Generated documentation (`CLAUDE.md`, `README.md`, `docs/*`,
   `obsidian/README.md`).
5. Scaffolded worker and MCP placeholders.
6. Wrote this archive.
7. Wrote `manifests/bootstrap_manifest.json` and `logs/bootstrap.log`.
8. Verification report (separate output).

No git commit was made by the worker. Commit and push are gated
operations and require explicit user authorization.

---

## Decisions of record

- **Substrate root:** `/home/user/URANTiOS/nemoclaw/`. Not `~/NemoClaw`.
- **Git model:** single repo (URANTiOS), single branch
  (`claude/nemoclaw-setup-GDKGy`). No separate NemoClaw repo created.
- **Network exposure:** all services bind to `127.0.0.1` by default.
  Public exposure requires explicit human approval recorded in this
  archive directory.
- **MCP:** placeholders only. No faked adapters.
