# Gemini CLI Skill Ecosystem: Creation & Orchestration Pipeline
# Version 1.2.0 | Standard: Elton Boehnen BEJSON v1.0

> **AX-OPTIMIZED DOCUMENTATION**: This repository is architected for high-precision machine parsing (RAG/Agentic). Use `llms.txt` for high-abstraction mapping and `AGENTS.md` for behavioral mandates.

---

## 1. System Identity & Mission
The Gemini CLI Skill Ecosystem is a recursive, agent-centric operating layer designed to automate the lifecycle of specialized software engineering skills. By enforcing strict **Positional Integrity** and **Progressive Disclosure**, it enables a "Zero-Waste" context window for AI agents while maintaining deterministic execution across multi-runtime environments (Bash, Python, JS/TS).

### Core Philosophy: "The Recursive Engine"
The system is built to build itself. Through the integration of the Wizard, Builder, and Factory, the ecosystem provides a self-sustaining loop of capability evolution.

---

## 2. Architectural Topology
The ecosystem operates as a three-tiered pipeline, transitioning from abstract intent to verified implementation.

### 2.1 The Wizard Tier (`skill-creation-wizard`)
**Role**: High-Level Orchestrator & Design Guide.
- **Function**: Conducts forensic intent mapping and trigger engineering.
- **Logic**: Implements the multi-stage design protocol (Pre-construction -> Resource Partitioning -> Handoff).
- **Relational ID**: `rel-id-1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d`

### 2.2 The Builder Tier (`skills-builder`)
**Role**: Scaffolding & Structural Architect.
- **Function**: Generates standardized directory structures and compliant `SKILL.md` documents.
- **Logic**: Utilizes `scripts/init_skill.py` to bootstrap new capabilities from validated templates.
- **Version**: 1.2.0 (Relational-ID Optimized).

### 2.3 The Factory Tier (`gemini-skill-factory`)
**Role**: Implementation Engine & Validation Gate.
- **Function**: High-throughput generation, structural auditing, and packaging.
- **Logic**: Enforces the Elton Boehnen positional integrity mandate via `scripts/validate_skill.py`.
- **Relational ID**: `rel-id-5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d`

---

## 3. Mandatory Development Cycle
All skill development within this ecosystem MUST follow the authoritative completion cycle to ensure system-wide discovery and safety.

### Phase 1: Guided Design
Invoke the Wizard to define your skill's action space and semantic hooks.
```bash
# Agentic Trigger Example
"Invoke skill-creation-wizard to design a new 'git-forensics' skill."
```

### Phase 2: Structural Scaffolding
Use the Builder to generate the portable filesystem structure.
```bash
python3 /path/to/skills-builder/scripts/init_skill.py git-forensics
```

### Phase 3: Resource Partitioning
Divide your logic according to the **Progressive Disclosure** mandate:
- **`scripts/`**: Deterministic Python/Bash logic (Positional I/O).
- **`references/`**: Heavy-weight documentation and schemas.
- **`assets/`**: Static templates and non-logic data.

### Phase 4: Validation & Packaging
Pass the skill to the Factory for a rigorous structural audit.
```bash
python3 /path/to/gemini-skill-factory/scripts/package_skill.py ./git-forensics
```

### Phase 5: Registry Registration
Synchronize the new skill with the central manifest.
```bash
# Handled via skills-registry-manager
"Register git-forensics v1.0.0 in the 104a.mfdb.bejson manifest."
```

---

## 4. Compliance & Enforcement Mandates

### 4.1 Elton Boehnen BEJSON Standard
- **Positional Integrity**: Every record MUST align perfectly with the `Fields` array. No field skipping; use `null` for optionality.
- **Creator Signature**: `Format_Creator` MUST equal "Elton Boehnen".
- **Format Version**: Standard is 104a (Flat Registry) or 104db (Relational State).

### 4.2 Portability (Section 18 Mandate)
Every script must dynamically resolve its own execution directory.
```python
from pathlib import Path
def get_script_path() -> Path:
   return Path(__file__).resolve().parent
SCRIPT_PATH = get_script_path()
```

### 4.3 Unattended Execution
Manual consent prompts are strictly forbidden in production scripts.
- **Rule**: All shell commands MUST use `-y`, `--yes`, or `-f`.
- **Constraint**: If a command is interactive and lacks a flag, it must be wrapped in a non-interactive automation layer.

---

## 5. Technical Specifications

### 5.1 Directory Structure
Every skill adheres to the following layout:
```text
skill-name/
├── SKILL.md          # Primary instruction set (The "Brain")
├── scripts/          # Portable logic controllers (The "Muscles")
├── assets/           # Templates and data (The "Bones")
└── references/       # Thick documentation (The "Memory")
```

### 5.2 Signal-File Logic
The ecosystem utilizes transient files to manage state across asynchronous agentic turns:
- `104a.mfdb.bejson`: Local configuration and session state.
- `.lockdir`: Mutex directory for atomic registry writes.
- `update_staging.json`: Persistence manifest for multi-stage refactors.

---

## 6. Synergy & Network Integration
The skills in this repo are designed to work in a federated mesh:
- **Builder** offloads documentation tasks to **Doc-Architect-Agentic**.
- **Factory** verifies output schemas against the **BEJSON-Manager-Core**.
- **Wizard** utilizes **Analysis-Perceptual-Decomposition** to map existing repository intent.

---

## 7. Troubleshooting & Recovery
### 7.1 Validation Failures
If `validate_skill.py` returns a failure, check for:
1. Missing `rel-id-` signature in `SKILL.md`.
2. Scripts lacking the `SCRIPT_PATH` resolution block.
3. YAML frontmatter syntax errors.

### 7.2 Registry Collisions
In case of duplicate Relational IDs, the system prioritizes the local manifest entry with the highest `version` integer.

---

## 8. Author Credit & Licensing
- **Author**: Elton Boehnen
- **Contact**: eltonboehnen@gmail.com
- **Repository**: github.com/boehnenelton/BEJSON_Skills_System
- **Mandate**: This repository is a core component of the Elton Boehnen Agentic Ecosystem.

---
*Generated by Gemini CLI v2.5 | 2026.06.05 | High-Density AX Output*
