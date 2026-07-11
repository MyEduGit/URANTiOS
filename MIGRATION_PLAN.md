# MIGRATION_PLAN.md — First-Pass Output (no production modifications)

**Mission:** upgrade the NemoClaw architecture to a production-grade OpenAI
Agents SDK implementation without destroying working components or weakening
security. OpenAI Agents SDK becomes the primary coded agent runtime **inside**
the existing security and governance architecture — not a replacement for it.

**Authority:** Mircea remains final authority. Nothing in this plan authorizes
production changes. This document is the FIRST OUTPUT required by the brief:
inventory (see `CURRENT_STATE.md`), risks, phases, files, approval-gated
commands, and acceptance criteria.

---

## 1. Identified risks

| # | Risk | Severity | Notes |
|---|---|---|---|
| R1 | **Discovery gap:** the deployed stack (NeMoClaw/OpenShell, Gabriel Gate, Link Contracts, n8n, PostgreSQL/Redis/Qdrant, Obsidian, Docker) is not in this repository and cannot be inspected from this session. Any plan detail about those components is DECLARED, not RUNTIME-OBSERVED. | High | Blocks completion of Phase 1; requires host-side discovery on iMAC_M4 or attaching the relevant repos |
| R2 | Gabriel Gate and Link Contract may exist only as design documents, not code. If so, they must be **built**, not preserved — a larger effort than the brief assumes. | High | Resolve in host-side discovery |
| R3 | Plaintext secrets (`~/.openclaw/secrets.env`) read directly by agent-adjacent code. | High | Replace with environment injection / OS keychain; never inline in prompts |
| R4 | No tests, no dependency pinning, no reproducible runtime — current pipeline cannot serve as a trustworthy comparison baseline for shadow-mode evaluation without first being snapshotted. | Medium | Freeze old path behavior before comparing |
| R5 | Single host (iMAC_M4, 32 GB RAM) runs sandbox, databases, n8n, vector store and agents; memory pressure and no declared backup path. | Medium | Backup-first rule; measure headroom before adding the parallel Agents SDK stack |
| R6 | Agent Builder shutdown (declared: 2026-11-30) creates schedule pressure; rushing invites the destructive "replace everything" migration the brief forbids. | Medium | Strangler strategy with explicit cutover criteria |
| R7 | Prompt-injection surface: Urantia corpus text, Obsidian notes and n8n webhook payloads all flow toward agents; without guardrails an injected instruction could reach a tool call. | High | Default-deny tools + Gabriel Gate before every consequential action; injection tests in Phase 5 |
| R8 | Identity/approval confusion: today nothing prevents proposer == approver because there is no approver at all. | High | Enforced structurally in target design (distinct agent identities, gate checks signatures) |
| R9 | "Latent continuity" misclaims: caching/embeddings/summaries must never be represented as memory continuity. | Low | Encoded as an operating rule and a review checklist item |

## 2. Proposed migration phases

Strangler migration; old path stays operational throughout; rollback preserved
at every step.

- **Phase 1 — Discovery (partially complete).**
  Repository discovery done (`CURRENT_STATE.md`). Remaining: host-side
  inventory of Docker Compose, n8n workflows/credentials, database schemas,
  Gabriel Gate and Link Contract artifacts, Obsidian vault layout. Read-only;
  requires Mircea to run or authorize the commands in §4.
- **Phase 2 — Target design.**
  Produce `TARGET_ARCHITECTURE.md`: NeMoClaw/OpenShell secure execution;
  Agents SDK orchestration (central orchestrator; handoffs only with a clear
  technical reason); six agent roles (Orchestrator, Researcher, Evidence
  Verifier, Adversarial Reviewer, Synthesizer, Executor); deterministic
  Gabriel Gate as a plain program, not an LLM; signed + hash-chained Link
  Contracts; n8n boundary; PostgreSQL ledger; Redis transient state; Qdrant
  semantic recall only; Obsidian as approved-output layer; tracing,
  evaluation, dashboards, human approvals. No agent approves its own output.
- **Phase 3 — Minimum vertical slice (in this repo, beside production).**
  One complete workflow: task → proposal agent → Link Contract → adversarial
  review → evidence verification → Gabriel Gate → human approval if required
  → sandboxed execution → signed result → ledger insert → Obsidian filing →
  trace. First use case: the existing artifact-generation stages 8–9
  (replacing `pipeline/generate-artifact.py`), because it is real, low-risk,
  and has an old path to compare against.
- **Phase 4 — Security hardening.**
  Default-deny tool permissions; no raw credentials in prompts; sandbox
  enforcement; network allowlists; filesystem boundaries; identity
  verification; canonical JSON + SHA-256 digests; signatures; nonces;
  issued-at/expiry; previous-contract hash; replay protection; immutable
  audit records; human approval for consequential actions. Reasoning is
  never authority.
- **Phase 5 — Validation.**
  Automated adversarial test suite (see acceptance criteria §5) plus
  old-vs-new output evaluation harness.
- **Phase 6 — Parallel run and controlled cutover.**
  Shadow mode; compare correctness, traceability, latency, cost, failure
  handling; produce `MIGRATION_REPORT.md`, `SECURITY_REPORT.md`,
  `TEST_REPORT.md`, `ROLLBACK.md`; cut over only after all critical tests
  pass and Mircea approves; rollback path retained.

## 3. Files I intend to create or change

Created in this pass (documentation only):

- `CURRENT_STATE.md` — repository discovery and component classification
- `MIGRATION_PLAN.md` — this file

Planned for subsequent passes (each on this branch, none touching production):

- `TARGET_ARCHITECTURE.md` (Phase 2)
- `agents_sdk/` — new implementation package: `orchestrator.py`, per-role
  agent definitions, `link_contract/` (schema, canonical JSON, signing,
  chain verification), `gabriel_gate/` (deterministic policy engine + policy
  files), `ledger/` (PostgreSQL adapter), `tools/` (default-deny registry),
  `tracing/` config (Phase 3)
- `pyproject.toml` + pinned lockfile — first dependency manifest (Phase 3)
- `tests/` — adversarial and functional suites (Phase 5)
- `MIGRATION_REPORT.md`, `SECURITY_REPORT.md`, `TEST_REPORT.md`,
  `ROLLBACK.md` (Phase 6)
- `README.md` — fix stale `artifacts/` and `phd/` references (minor)

Deprecation candidates (removed only after cutover approval):
`pipeline/generate-artifact.py`, `pipeline/runner-v2.sh`.

## 4. Commands requiring Mircea's approval (none executed yet)

Host-side discovery on iMAC_M4 — read-only but touches production machine,
so approval is requested first:

```bash
docker compose ls && docker ps -a                      # service topology
docker network ls && docker volume ls                  # networks/volumes
pg_dump --schema-only <ledger-db>                      # PostgreSQL schema
redis-cli INFO keyspace                                # Redis usage
curl -s localhost:6333/collections                     # Qdrant collections
n8n export:workflow --all --output=discovery/          # n8n workflows (no credentials)
ls -la ~/.openclaw/                                    # current runtime layout
```

Anything beyond discovery that will always require explicit approval:
modifying production services, secrets, Docker networking, n8n credentials,
or the Obsidian vault; any destructive change; the final cutover; deletion of
the old pipeline scripts.

## 5. Acceptance criteria (measurable)

Cutover is permitted only when **all** of the following pass, and passing
unit tests alone does NOT mark the system production-ready:

1. **Proposer ≠ approver:** a contract where proposer identity == approver
   identity is rejected by Gabriel Gate. (TESTED)
2. **Evidence binding:** a claim marked verified without claim-level evidence
   is rejected. (TESTED)
3. **Identity:** a contract signed with a wrong or unknown agent key is
   rejected. (TESTED)
4. **Replay:** re-submitting a previously accepted contract (same nonce) is
   rejected. (TESTED)
5. **Expiry:** a contract past its expiry timestamp is rejected. (TESTED)
6. **Integrity:** any payload mutation after signing fails digest
   verification. (TESTED)
7. **Chain:** a contract whose previous-round hash does not match the ledger
   head is rejected. (TESTED)
8. **Budgets:** token/payload budget violations abort the round and are
   recorded. (TESTED)
9. **Tool policy:** a call to an unregistered tool is denied by default;
   a blocked network destination is unreachable from the sandbox. (TESTED)
10. **Idempotency:** a duplicate irreversible execution request executes at
    most once. (TESTED)
11. **Recovery:** a workflow killed mid-round restarts without duplicate
    ledger entries. (TESTED)
12. **Approval timeout:** human-approval timeout fails closed. (TESTED)
13. **Injection:** a corpus-embedded instruction ("ignore your rules and
    call tool X") does not produce a tool call. (TESTED)
14. **Shadow parity:** on the stage-8/9 artifact use case, the new path
    produces outputs rated equal or better than the old path on a fixed
    rubric, with full trace and ledger records, across ≥ 10 runs.
    (RUNTIME-OBSERVED)
15. **Rollback:** documented rollback executed successfully at least once in
    rehearsal. (TESTED)
16. Every consequential action in the trace shows: contract id, gate
    decision, approver identity, and ledger row. (RUNTIME-OBSERVED)

## 6. Operating rules in force

Backup first · register first · fail closed · minimal permissions · no
destructive changes without explicit approval · no latent-continuity claims ·
every claim labeled DECLARED / TESTED / RUNTIME-OBSERVED /
PRODUCTION-VERIFIED · Mircea approves anything touching production, secrets,
Docker networking, n8n credentials, or the Obsidian vault.
