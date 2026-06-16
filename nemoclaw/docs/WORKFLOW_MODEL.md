# NemoClaw — Workflow Model

## One sentence

A task enters the queue, a stateless worker consumes it, produces an
artifact, the artifact is verified, and the artifact is archived.

```
NemoClaw → Queue → Worker → Artifact → Verification → Archive
```

## Task lifecycle

### 1. Enqueue
A task is published to `nemoclaw:queue:<worker_kind>` as a JSON envelope:

```json
{
  "task_id": "uuid-v4",
  "worker_kind": "claude_worker",
  "created_at": "2026-05-07T01:17:47Z",
  "created_by": "human:operator | workflow:n8n_node_id",
  "scope": {
    "paths_readable": ["..."],
    "paths_writable": ["archive/<task_id>/"]
  },
  "approval_gate": "none | required",
  "input": { /* task-specific */ }
}
```

The `task_id` is deterministic and immutable. Re-enqueueing the same
`task_id` is a replay, not a new task.

### 2. Dispatch
A single worker of the matching kind claims the task atomically
(`BLPOP` / Redis stream consumer group). Other workers ignore it.
Lifecycle event published on `nemoclaw:events`:

```json
{ "task_id": "...", "event": "started", "worker_id": "...", "ts": "..." }
```

### 3. Execute
The worker writes incrementally to `archive/<task_id>/`:

```
<task_id>/
├── manifest.json     # written first; updated as task progresses
├── prompt.md         # exact input
├── output.md         # primary output
├── logs.txt          # raw stdout/stderr
├── verification.txt  # populated after verification
└── diff.patch        # if task mutated tracked files
```

### 4. Verify
Verification is **not** a worker self-claim. It is one or more of:

- a separate verification worker re-running checks,
- automated tests/linters,
- a human signing off and writing into `verification.txt`.

A task is **not done** until `verification.txt` exists and is non-empty.

### 5. Archive
On verification, the artifact directory is sealed:

- the artifact directory is moved (or hardlinked) into the Obsidian vault
  under `obsidian/archive/<YYYY>/<MM>/<task_id>/`,
- a backlink note is added to the relevant Obsidian topic,
- a row is inserted into the audit log.

Sealed artifacts are immutable. Corrections are new tasks.

## Stateless workers — what that means in practice

- A worker process can be killed at any point in steps 2–4 without data
  loss; the next dispatch picks up the same `task_id`.
- A worker does not read state from previous tasks except via the queue
  envelope or scoped read paths.
- A worker does not write outside its `scope.paths_writable`. This is
  enforced by container volume mounts, not by trust.

## Event-driven execution

`nemoclaw:events` is a thin pub/sub channel for orchestration plumbing
(metrics, dashboards, follow-up triggers). Subscribers are passive — they
do not influence task semantics. Tasks are spawned only by enqueue, never
by event side-effects.

## Verification as a first-class step

Verification is a step in the workflow, not a footnote. Specifically:

- Every claim of "done" must point to evidence in `verification.txt`.
- Evidence is preferred in this order:
  1. command + exact output,
  2. file path + diff,
  3. test name + result,
  4. human signoff with timestamp.

If none of those is available, the task is not done.

## Failure handling

- Soft failure: worker writes failure into `manifest.json` and exits.
  The task is retried up to its retry budget.
- Hard failure (retry budget exhausted): task moves to
  `nemoclaw:dlq:<worker_kind>` for human triage. No silent drops.
- Crash mid-execution: artifact is partial; next dispatch overwrites the
  partial artifact (idempotency via `task_id`).
