---
name: bejson-cognitive-state
description: Extension skill for managing agentic cognition, reactive state, and autonomous deployment. Use this skill for Hive Mind orchestration, security sandboxing, persistent session management with signal-file logic, and tool forging.
---

# BEJSON Cognitive State Manager

This skill extends the BEJSON core with high-level cognitive, state management, and autonomous deployment functions. It implements the "Cortical" layer of the agentic ecosystem, focusing on awareness, persistence, and safe experimentation.

## Core Mandates

### 1. Security First
All cognitive operations MUST pass through the `bejson_cognition_check_sandbox` protocol to prevent unauthorized tool forging or sub-agent spawning in restricted environments.

### 2. State Immutability & History
State changes MUST be tracked using the `BEJSONState` engine. This ensures that every mutation is snapshotted, allowing for "Cognitive Rollbacks" (undo) in case of logical errors.

### 3. Unattended Execution
All shell-level actions, including sub-agent initialization, tool registration, and permission updates, MUST use non-interactive flags (`-y`, `--yes`) to bypass consent prompts.

## Operational Workflow

### 1. Reactive State & Sessions
Maintain an auto-saving state tree and manage long-running agentic tasks.
- **Initialize State**: `state = BEJSONState(auto_save_path="state.bejson")`
- **Session Management**: Use `mfdb_agent_session_create` to track project onboarding or multi-step tasks.
- **Signal Logic**: Use `mfdb_agent_signal_poll` to implement pause/resume states based on external triggers (e.g., human approval).

### 2. Cognitive Orchestration (Hive Mind)
Use `lib_bejson_cognition.py` and `lib_bejson_agentic_deploy.py` to manage the matrix.
- **Matrix Operations**: Use `bejson_cognition_init_matrix` and `bejson_cognition_upsert` for high-resilience 104db state tracking.
- **Tool Forging**: Autonomously generate and register terminal tools using the `bejson_agentic_forge_tool` function.
- **Agent Spawning**: Deploy sub-agents with dedicated personas and task queues via `bejson_agentic_spawn_agent`.

### 3. Tiered Memory Orchestration (Cognition2)
Leverage `lib_bejson_cognition2.py` for advanced, long-term cognitive stability.
- **Federated Management**: Use the `FederatedMemoryManager` to orchestrate Working, Episodic, and Archive brains.
- **Automated Pruning**: Execute `prune_and_migrate(age_hours=48)` to maintain a lean context window.
- **Signal-Based Lookup**: Perform keyword-driven memory retrieval across the brain network via `semantic_lookup`.

## Resilient Persistence

Always utilize `bejson_cognition_safe_write` for matrix updates. It implements randomized exponential backoff to handle high-frequency concurrent writes to the same MFDB entities.

## Compliance Checklist

- [ ] **Sandboxing**: Sandbox checks are integrated into all spawners and forgers.
- [ ] **Persistence**: All state mutations are backed by atomic disk writes with mutex backoff.
- [ ] **Unattended**: All `chmod` and tool registrations are non-interactive.
- [ ] **Durable Sessions**: Long-running tasks utilize signal-file logic for state preservation.
- [ ] **Creator Mandate**: `Format_Creator` is "Elton Boehnen".

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Email:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: bejson-cognitive-state-001*
