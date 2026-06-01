# 2026 AX & DX Documentation Standards

## Agentic Experience (AX)
AX focuses on the efficiency with which an AI agent can understand, navigate, and contribute to a codebase.

### 1. Token Efficiency
- Minimize boilerplate and "marketing fluff."
- Use bulleted lists for factual density.
- Target Ratio: 80% facts / 20% prose.

### 2. Semantic Chunking
- AI agents segment pages into 100–300 token "chunks."
- Use strict H2/H3 hierarchies.
- Ensure each section is self-contained (includes all necessary context for that specific topic).

### 3. Machine-Readable Anchors
- Use YAML/JSON-LD frontmatter.
- Include `llms.txt` for high-density architectural mapping.
- Include `AGENTS.md` for behavioral guidance.

## Developer Experience (DX)
DX focuses on the ease of use for human developers.

### 1. The 30-Second Rule
- A user must understand the project and have it running within 30 seconds.
- Requires a "One-Liner" install command.

### 2. Visual Trust Signals
- Use OKLCH for perceptually uniform color tokens.
- Use dynamic badges for real-time health (Security, Coverage, Performance).
- Avoid "Badge Overload" (limit to 3-5 critical indicators).

### 3. Verifiable Snippets
- Every code example must be runnable.
- Include import statements and expected output comments.
- Link snippets to CI-verified test files when possible.

---
*Reference ID: ax-dx-2026-standards*
