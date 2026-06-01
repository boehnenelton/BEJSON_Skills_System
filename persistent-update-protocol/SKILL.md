# Persistent Update Protocol

Rigorous execution framework for staged, persistent codebase refactoring with crash-recovery, staging-checkpoints, and verifiable task tracking.

## Core Procedural Workflow

### Phase 1: Forensic Analysis
1.  **Repository Inspection**: Map the current state and identify target components.
2.  **Scope Definition**: Clearly bound the requested update or refactor.
3.  **Dependency Mapping**: Identify impacted files, tests, documentation, and migration paths.
4.  **Execution Planning**: Draft a detailed, phased plan before any modification.

### Phase 2: Staging Initialization
1.  **Checkpoint Generation**: Create a persistent staging file on disk.
    - Default: `./tmp/update_staging.json` or `./framework/logs/reports/update_resume_state.json`.
2.  **Schema Alignment**: Ensure the checklist contains: `task_id`, `description`, `status`, `files_impacted`, `dependencies`, `started_at`, `completed_at`, `verification_status`, and `rollback_notes`.
3.  **Task States**: Initialize with `pending`, `active`, `completed`, `failed`, `blocked`, or `skipped`.

### Phase 3: Synchronous Execution
1.  **Single-Task Locking**: Maintain exactly one `active` task at a time.
2.  **Atomic Persistence**: Immediately update the checkpoint file after:
    - Task completion.
    - File modification.
    - Test execution.
    - Blocker discovery.
3.  **Verification Gating**: Each task must satisfy its verification command and test/lint results before transitioning to `completed`.

### Phase 4: Recovery & Resume
1.  **Checkpoint Detection**: Upon startup, scan for existing `update_staging.json` or `update_resume_state.json`.
2.  **State Reconstruction**: Load the checklist, summarize progress, and resume from the first unfinished (pending/active/failed) task.
3.  **Mutation Handling**: If new work is discovered, append tasks and update dependencies immediately.

### Phase 5: Finalization & Archiving
1.  **Final Validation**: Run global integration tests and lints.
2.  **Forensic Reporting**: Produce a final verification report summarizing all tasks and outcomes.
3.  **State Archiving**: Move the final staging checklist to `./framework/logs/reports/`.

## Reasoning Constraints
- **Zero Memory Reliance**: Never rely on conversational context for state; the disk is the source of truth.
- **Immediate Feedback Loop**: Pause and update the checklist after every logical step.
- **Verification Mandate**: No task is "complete" without a successful verification command execution.

## Resource Navigation
- **Checklist Template**: [assets/update_staging_template.json](assets/update_staging_template.json)
- **JSON Schema**: [references/staging_schema.json](references/staging_schema.json)
- **Status Codes**: [references/status_codes.md](references/status_codes.md)

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Contact:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

*Relational ID: pup-refactor-protocol-001*
