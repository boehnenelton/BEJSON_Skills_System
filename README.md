---
project: "Gemini-CLI-Skill-System"
version: "1.4.0"
stack: ["BEJSON", "MFDB", "Bash", "Python"]
entry_point: "104a.mfdb.bejson"
agent_rules: "./AGENTS.md"
context_map: "./llms.txt"
license: "MIT"
---

# Gemini CLI Skill System 🚀
> A modular, BEJSON-powered framework for extending Gemini CLI with persistent, expert agentic capabilities.

## ⚡ Quick Start
```bash
# Register a new skill directory
skills-registry-manager register ./my-new-skill
```

### Basic Skill Activation
```typescript
// Internal logic for skill loading
const architect = await agent.activate_skill("doc-architect-agentic");
await architect.execute("Phase 1: Discovery");
```

## 🧠 Agent Readiness
This repository is optimized for **Agentic Experience (AX)**. 
- **Architectural Map:** See [llms.txt](./llms.txt) for a high-density capability registry.
- **Behavioral Rules:** See [AGENTS.md](./AGENTS.md) for sync protocols and BEJSON mandates.
- **Standards:** All data follows the [BEJSON/MFDB Standard](../GEMINI.md).

## 🛠️ Architecture & Intent
### Core Philosophy
- **Modular Agency**: Every skill is a self-contained expert with its own assets, references, and scripts.
- **Category-First Naming**: Skills are organized by functional categories (e.g., `analysis-`, `post-analysis-`, `bejson-`) to improve discoverability and logical grouping.
- **Progressive Disclosure**: Skills only load their full instructions when explicitly activated.

### Signal Pathways
- **Manifest → Registry**: The `104a.mfdb.bejson` manifest maps human-readable names to procedural `SKILL.md` paths.
- **State → Disk**: The `protocol-update-persistent` ensures complex refactors survive context resets.

## 🎨 Visual Identity
![Skill System Banner](https://cdn.example.com/skill-system-banner.svg)
*Theme: Forensic Architect | Palette: OKLCH (Standardized in css-becss)*

## 🤝 Contributing
We use **Surgical Updates**. 
1. Map your skill logic to the `skills-builder` template.
2. Synchronize active skills to the `~/build/skill_system/` backup.
3. Update the registry manifest with incremental versioning.

---
License: MIT | Relational ID: gcli-skill-sys-v2
