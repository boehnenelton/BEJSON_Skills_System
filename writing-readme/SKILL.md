---
name: writing-readme
description: Specialized skill for crafting 2026-standard GitHub READMEs. Focuses on the Human-Agent Interop stack, including visual architecture, one-liner quickstarts, and AX trust signals.
---

# Writing README: Agent-Ready (AX-2026)

Specialized protocol for generating high-impact, 2026-compliant GitHub READMEs. Prioritizes "Business-to-Agent" (B2A) interoperability and "Vibe" grounding for human developers.

## Protocol: The Three-Tier AX Stack

### 1. Human "Vibe" Layer (README.md)
*   **Philosophy**: Focus on "Why" and "Vision."
*   **Visual Architecture**: MUST include a Mermaid.js diagram or an ASCII tree block for grounding.
*   **One-Liner**: Must have a single copy-pasteable command that leads to a "Success State."
*   **Trust Signals**: Use badges for `[Agent-Ready]`, `[MCP-Enabled]`, and `[llms.txt: Verified]`.

### 2. Machine Execution Layer (AGENTS.md)
*   **Strict Rules**: Use `## Strict Constraints` to define what an agent must never do.
*   **Command Shortcuts**: Explicitly list exact testing/linting commands.
*   **Context Routing**: Map the filesystem mental model.

### 3. Discovery Layer (llms.txt)
*   **Sitemap**: Provide a compressed index for RAG systems.
*   **Concatenation**: Mention `llms-full.txt` if high-density ingestion is supported.

## Workflow

### Step 1: Intent Distillation
=> Decompose(project, intent) -> [CORE_MISSION]
=> Identify(stack, entry_points) -> [AGENTS_GROUNDING]

### Step 2: Architecture Visualization
=> Map(filesystem, hierarchy) -> Mermaid.js Graph
=> Construct(ASCII_TREE) -> Grounding Block

### Step 3: AX-README Implementation
=> Generate(Header, Badges)
=> Write(Vibe_Section) -> Philosophy + Core Mission
=> Insert(One_Liner) -> Copy-Pasteable Success
=> Link(Documentation_Stack) -> llms.txt, AGENTS.md, DESIGN.md

### Step 4: Verification
=> Audit(Token_Waste) -> Strip Prose
=> Test(Agent_Readiness) -> Can an agent build this using only these files?

## Reasoning Rules
- **Prose-to-Fact Ratio**: Aim for 1:4. Every sentence must provide operational data.
- **Visuals over Text**: A diagram is worth 1000 tokens of prose.
- **Self-Contained Sections**: Each header should be independently retrievable by RAG systems.

---
**Author:** Elton Boehnen
**Relational ID:** gcli-skill-writing-readme-001
