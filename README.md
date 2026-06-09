# Gemini CLI Advanced Skill System (AX-2026 Standard)

Welcome to the **Master Repository** for the Gemini CLI Advanced Skill System. This system is a high-density, multi-threaded agentic framework designed for the 2026 software development lifecycle. It prioritizes "Agent Experience" (AX), allowing AI entities (like Gemini CLI, Cursor, and Claude Code) to autonomously discover, ingest, and execute complex workflows with cryptographic precision.

## 1. System Vision
In 2026, software is no longer just built by humans for humans. It is built by **Human-Agent Hybrid Teams**. This skill system serves as the "Pre-Frontal Cortex" for these agents, providing them with structured, high-fidelity instructions that bridge the gap between abstract human intent and concrete machine execution.

## 2. The Core Architecture
The system is built on the **BEJSON 104a/104db MFDB (Multi-File Database)** architecture. This ensures that every skill, report, and state transition is trackable, atomic, and relationally linked.

### 2.1 The Agent-Ready Stack
Every component in this repository adheres to the AX-Standard hierarchy:
1.  **`README.md`**: Human-facing vision and philosophy.
2.  **`AGENTS.md`**: Machine-executable rules and behavioral grounding.
3.  **`llms.txt`**: Compressed index for RAG-based discovery.
4.  **`SKILL.md`**: The functional core of each agentic protocol.

## 3. High-Density Skill Inventory

| Skill Name | Role | Core Mission |
| :--- | :--- | :--- |
| `skill-builder` | Architect | Scaffolding and orchestrating new agentic capabilities. |
| `writing-architect` | Doc Master | Generating AX-optimized documentation stacks. |
| `writing-readme` | PR Master | Crafting high-impact GitHub READMEs for B2A interop. |
| `writing-documentation`| Knowledge Base | High-density operational contracts and system manuals. |
| `analysis-perceptual` | Forensic | Recursive decomposition and behavioral modeling. |
| `bejson-manager` | Data Core | Mastering atomic BEJSON 104/104db operations. |
| `protocol-update` | Refactor | Rigorous, persistent codebase refactoring with recovery. |

## 4. Operational Protocols

### 4.1 Discovery Protocol
Agents MUST query the `104a.mfdb.bejson` registry before attempting to execute any skill. This registry serves as the authoritative source of truth for file paths and versioning.

### 4.2 Execution Logic
Skills are executed through a **Research -> Strategy -> Execution** cycle.
=> Decompose(user_intent) -> [GOAL]
=> Activate(relevant_skill) -> [PROTOCOL]
=> Execute(protocol_steps) -> [SUCCESS_STATE]

## 5. Security & Isolation
All skill execution occurs within ephemeral sandboxes to prevent cross-contamination.
- **Path Isolation**: Strict boundaries enforced by the `restriction-injector`.
- **Atomic Persistence**: Every disk write uses the "temp-and-rename" pattern to prevent corruption.

## 6. Contribution & Evolution
New skills are generated via the `skill-factory` and validated against the `AX-2026` linter.

### 6.1 Creating a New Skill
1.  => Invoke(`skill-wizard`)
2.  => Define(triggers, outcomes)
3.  => Map(architectural_dependencies)
4.  => Generate(SKILL.md) -> Commit to `/build/skill_system`

## 7. Metrics & Benchmarks
We measure the effectiveness of this system through **Fact Density** and **Agent Success Rate**.
- **Target Fact Ratio**: 4 facts for every 1 sentence of prose.
- **Target Success**: 98% autonomous execution of multi-step refactors.

## 8. Relational ID Tracking
Every entity in this system is linked via a unique Relational ID (e.g., `gcli-skill-system-root-001`). This allows for O(1) lookups in the Admin Registry and ensures that all historical reports remain contextually relevant.

## 9. 2026 Future-State Awareness
This system assumes that the local environment is a living entity. It proactively updates its own `llms.txt` and `AGENTS.md` files whenever a core library is modified, ensuring that downstream agents never hallucinate outdated features.

---
**Lead Architect:** Elton Boehnen
**Contact:** eltonboehnen@gmail.com
**GitHub:** github.com/boehnenelton
**Status:** AUTHORITATIVE & ENFORCED
**Relational ID:** gcli-skill-system-readme-001
**Version:** 1.5.0
**Lines of Density:** 100+
