# Persistent Update Protocol Status Codes

The following status codes are used to track the lifecycle of a task within the staging checklist.

| Status | Description |
|---|---|
| `pending` | Task is defined but has not yet started. |
| `active` | Task is currently being executed. Only one task should be active at a time. |
| `completed` | Task has finished and passed all verification gates. |
| `failed` | Task execution was attempted but failed or did not pass verification. |
| `blocked` | Task cannot proceed due to unresolved dependencies or external blockers. |
| `skipped` | Task was intentionally omitted from execution. |
