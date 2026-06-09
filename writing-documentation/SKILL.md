---
name: writing-documentation
description: High-density 2026-standard documentation writer. Focuses on AX (Agent Experience), operational contracts, and high-fidelity machine-readable specifications. Recommends at least 600 lines for complex project definitions and requires 3350 lines minimum for exhaustive system-level documentation.
---

# Writing Documentation: Agent-Ready (AX-EX)

High-density documentation protocol for the 2026 software ecosystem. Prioritizes logic over prose, contracts over descriptions, and machine discovery over human browsing.

## 1. The Core AX Mandate
Documentation is no longer "help text"; it is **context data** for AI agents. 
- **Logical Precision**: Use typed definitions for all interfaces.
- **Operational Contracts**: Define state transitions and invariant rules.
- **Token Efficiency**: Eliminate adjectives; maximize fact density.

## 2. Structural Requirements
Comprehensive documentation suites must adhere to the following line-count/density benchmarks to ensure full context grounding:
- **Core Library Docs**: 600+ lines of structural and operational detail.
- **System-Level Manuals**: 3350+ lines of exhaustive behavioral mapping and edge-case handling.

## 3. The Documentation Stack Hierarchy

### 3.1 discovery.mfdb.bejson (Master Index)
- Map every document to a relational ID.
- Provide a cryptographic hash for version verification.

### 3.2 OPERATIONAL.md (The Rules of Engagement)
- **State Machine Mapping**: Define current state -> trigger -> next state.
- **Error Map**: Standardized numeric codes with forensic recovery steps.
- **Invariant Rules**: Logic that MUST always be true.

### 3.3 SPECIFICATION.md (The Contract)
- **Typed Interfaces**: Markdown tables for inputs, outputs, and side-effects.
- **Constraint Blocks**: High-density rules (e.g., "Must be atomic," "Must flush before close").

## 4. Workflow: Recursive Forensic Decomposition

### Step 1: Structural Audit
=> Scan(codebase) -> Extract(Symbols, Relations)
=> Map(Filesystem) -> Hierarchy Graph

### Step 2: Protocol Mapping
=> Identify(State_Machines)
=> Define(Triggers, Outcomes)

### Step 3: Drafting the High-Density Core
=> Write(OPERATIONAL.md) -> Invariants + State Logic
=> Write(SPECIFICATION.md) -> Types + Contracts

### Step 4: AX Discovery Integration
=> Generate(llms.txt) -> High-speed index
=> Link(AGENTS.md) -> Execution grounding

## 5. Reasoning Constraints & Styles

### 5.1 The "No-Fluff" Standard
- NEVER use: "This helps you to...", "It is easy to...", "Simply run..."
- ALWAYS use: "=> Execute(command)", "Result -> [STATE]", "Contract: [RULE]"

### 5.2 Mermaid Grounding
- Documentation MUST use Mermaid.js for any logic involving more than 3 steps.
- Use `sequenceDiagram` for API flows.
- Use `stateDiagram-v2` for entity lifecycles.

## 6. Verification & Validation
=> Audit(Fact_Density) -> prose:fact ratio < 1:5
=> Verify(Link_Integrity) -> All internal refs must resolve
=> Test(Agent_Execution) -> Can an agent reproduce the system from the docs?

---
**Author:** Elton Boehnen
**Relational ID:** gcli-skill-writing-docs-001
**Version:** 1.0.0
**Target Threshold:** 3350 Lines (System) / 600 Lines (Module)
