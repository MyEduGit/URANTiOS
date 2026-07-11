# CURRENT_STATE.md — Phase 1 Discovery

**Migration:** NemoClaw architecture → OpenAI Agents SDK as primary coded agent runtime
**Scope inspected:** `MyEduGit/URANTiOS` repository (branch `main`, commit `0cde985`)
**Date:** 2026-07-11
**Status of every claim below:** DECLARED unless marked otherwise. Claims marked
RUNTIME-OBSERVED were directly verified by reading files in this repository.
Nothing in this document is TESTED or PRODUCTION-VERIFIED.

---

## 1. Critical scope finding — read first

The migration brief describes a deployed architecture on iMAC_M4 comprising
NVIDIA NeMoClaw/OpenShell, Gabriel Gate, Link Contracts, n8n, PostgreSQL,
Redis, Qdrant, Obsidian integration, Docker Compose files, database schemas
and validators.

**None of those components exist in this repository.** (RUNTIME-OBSERVED —
full-tree search for `docker`, `compose`, `n8n`, `postgres`, `redis`,
`qdrant`, `nemo`, `openshell`, `gabriel`, `link contract` returned no
implementation code; the only matches are references to the celestial
personality "Gabriel" inside the Urantia Book specification text.)

Consequences:

1. The deployed stack presumably lives on the iMAC_M4 host and/or in other
   repositories not attached to this session. Discovery of Docker Compose,
   n8n credentials/workflows, database schemas, Gabriel Gate code and Link
   Contract validators **cannot be completed from here** and is listed as
   UNKNOWN below.
2. This repository CAN serve as the home for the new Agents SDK
   implementation (greenfield code, built beside — not on top of —
   production), which matches the strangler-migration strategy.
3. No production system is reachable from this session, so the "do not
   modify production during discovery" rule is structurally satisfied.

---

## 2. Repository inventory (RUNTIME-OBSERVED)

| Path | What it is | Classification |
|---|---|---|
| `urantia-book/Doc000.json` … `Doc196.json` | Full Urantia Book corpus, 197 papers in structured JSON (paper → sections → paragraphs with canonical refs) | **KEEP** — canonical data source; feeds Qdrant/Cognee semantic recall |
| `soul/URANTiOS_v2.md` (~103 KB) | URANTiOS v2.0 specification ("OS kernel"): personality taxonomy, governance laws, coordination protocols, artifacts 00–11 | **KEEP** — governing specification; input to agent system prompts and Gabriel Gate policy derivation |
| `soul/URANTiOS_meta_prompt.md` | v1 meta prompt: paragraph-by-paragraph digital-equivalence builder with JSON output contract | **MIGRATE** — becomes structured output schema + agent instructions inside the Agents SDK implementation |
| `META_PROMPT_URANTIOS.md` | Foreword-first meta prompt variant (system-prompt form) | **MIGRATE** — same as above; the two prompts should be consolidated |
| `pipeline/cognee_bootstrap.py` | Cognee knowledge-graph ingestion of all 197 papers; CLI with range filtering and a verify query | **KEEP** (short term) / **MIGRATE** (long term) — semantic-recall ingestion; target design routes recall through Qdrant, so this either stays as the Cognee path or is ported |
| `pipeline/generate-artifact.py` | Anthropic API caller for artifact stages 8–9; reads secrets from `~/.openclaw/secrets.env`; hardcoded model `claude-opus-4-6`; writes to `~/.openclaw/artifacts` | **REPLACE** — exactly the kind of hand-written agent loop the brief targets: no approval boundary, no tracing, no session handling, plaintext secrets file, paths outside the repo |
| `pipeline/runner-v2.sh` | Stage announcer/launcher for the 9-stage prompt suite; depends on `~/.openclaw/` layout | **REPLACE** — superseded by Agents SDK orchestration |
| `COVENANT.md` | Standing authority declaration: Mircea is final authority ("Father Function"); ambiguous+irreversible ⇒ consult human | **KEEP** — human-authority layer; its rules must be encoded into Gabriel Gate policy, not weakened |
| `FOREWORD_*.md` (5 files) | Foreword analysis pack (deep analysis, ontology map, architecture diagrams, semantic roots, continuity) | **KEEP** — reference documentation |
| `README.md` | Project overview; references `artifacts/` and `phd/` directories that do not exist in the repo | **KEEP**, fix stale references |
| `.gitignore` | Ignores `__pycache__/`, `*.pyc`, `.cognee/`, `.env` | **KEEP** — extend for new implementation |

## 3. Components declared in the brief but not present here

All rows below are **UNKNOWN** until discovery runs on the iMAC_M4 host or the
relevant repositories are added to a session.

| Component | Declared role | Discovery still required |
|---|---|---|
| NVIDIA NeMoClaw / OpenShell | Secure sandbox / execution boundary | Locate repo + Docker config; verify sandbox policies |
| Gabriel Gate | Deterministic policy/authority layer | Locate code; determine if it exists as code or only as design |
| Link Contract | Signed claim/evidence interchange | Locate schema, signing keys, validators |
| n8n | Schedules, integrations, low-risk automation | Export workflows; inventory credentials |
| PostgreSQL | Audit ledger | Dump schema; identify tables and retention |
| Redis | Transient state | Identify keyspaces and TTL usage |
| Qdrant | Semantic recall | Identify collections; relation to Cognee (`pipeline/cognee_bootstrap.py` suggests Cognee may currently fill this role) |
| Obsidian vault | Approved human-readable knowledge layer | Locate vault path and filing conventions |
| Docker Compose | Service topology | Locate compose files; map networks and volumes |
| ChatGPT/Claude/Grok hand-offs | Improvised multi-model transfers | Identify where these occur (likely manual / n8n) |

## 4. Undocumented dependencies, secrets exposure, unsafe permissions (RUNTIME-OBSERVED)

1. **Plaintext secrets file:** `pipeline/generate-artifact.py` reads
   `ANTHROPIC_API_KEY` from `~/.openclaw/secrets.env` — unencrypted, outside
   the repo, no permission check, parsed by hand. No key found committed to
   the repository (verified by search), but the pattern violates the
   "no raw credentials near agent code" rule.
2. **Out-of-repo runtime layout:** both pipeline scripts depend on
   `~/.openclaw/{soul,artifacts,logs,pipeline}` — an undocumented machine-local
   convention; the repo cannot reproduce its own runtime.
3. **No approval boundary:** `generate-artifact.py` calls the model API and
   writes artifacts directly — no proposer/approver separation, no gate, no
   ledger record, no trace.
4. **No tests of any kind** exist in the repository.
5. **No dependency manifest:** `cognee` and `anthropic` are imported but there
   is no `requirements.txt`/`pyproject.toml`; versions are unpinned.
6. **Hardcoded model id** (`claude-opus-4-6`) with no configuration layer.
7. **Single point of failure:** everything runs on one host (iMAC_M4, 32 GB);
   no declared backup/restore procedure found in this repo.

## 5. Component classification summary

- **KEEP:** Urantia corpus JSON, `soul/URANTiOS_v2.md`, `COVENANT.md`,
  Foreword pack, README, .gitignore — plus (per brief, DECLARED)
  NeMoClaw/OpenShell, Gabriel Gate concept, Link Contract format, PostgreSQL,
  Redis, Qdrant, n8n, Obsidian, human approval.
- **MIGRATE:** the two meta prompts (→ agent instructions + structured output
  schemas), Cognee ingestion (→ governed semantic-recall ingestion job).
- **REPLACE:** `generate-artifact.py`, `runner-v2.sh` (hand-written agent
  loops → Agents SDK orchestration behind Gabriel Gate).
- **DEPRECATE:** `~/.openclaw` ad-hoc runtime layout; stale README references.
- **UNKNOWN:** every deployed component listed in §3, until host-side
  discovery is authorized and executed.
