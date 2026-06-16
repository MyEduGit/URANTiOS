# scripts

Operational helpers. Each script must:

- be idempotent
- log every action to `logs/`
- refuse to run destructive operations without an explicit flag
- return non-zero on any failure

This directory is currently empty. Helpers will be added as needed
(`backup.sh`, `restore.sh`, `verify_artifact.sh`, etc.) under human
review.
