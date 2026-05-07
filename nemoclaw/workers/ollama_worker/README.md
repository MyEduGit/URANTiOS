# ollama_worker

**Status:** placeholder scaffold. No implementation yet.

## Contract
- **Worker kind:** `ollama_worker`
- **Queue:** `nemoclaw:queue:ollama_worker`
- **DLQ:** `nemoclaw:dlq:ollama_worker`
- **Stateless:** yes
- **Artifact root:** `archive/<task_id>/`

## Required behavior (when implemented)
1. `BLPOP nemoclaw:queue:ollama_worker` to claim a task.
2. Validate the envelope; reject malformed tasks to DLQ.
3. Execute strictly within `scope.paths_writable`.
4. Emit `manifest.json`, `prompt.md`, `output.md`, `logs.txt`.
5. Publish lifecycle events to `nemoclaw:events`.
6. Exit. Do not loop in-process across tasks unless the orchestrator
   explicitly opts in via the dispatch contract.

## Forbidden
- self-escalating permissions
- writing outside scoped paths
- contacting other workers directly
- retaining authority across runs

See `../README.md` and `../../docs/WORKFLOW_MODEL.md`.
