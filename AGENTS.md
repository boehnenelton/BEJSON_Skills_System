# Agentic Behavioral Rules: Gemini CLI Skill System

## Mental Model
The Skill System is a modular, federated registry of procedural "expert modules." It prioritizes **Positional Integrity** (BEJSON), **Category-First Naming**, and **Context Efficiency** (Progressive Disclosure). Agents must treat the `104a.mfdb.bejson` manifest as the authoritative state of the ecosystem.

## Operational Constraints
- **Pattern A**: Always synchronize active skills in `~/.gemini/skills/` with the backup in `~/build/skill_system/`.
- **Constraint B**: Never modify the `104a.mfdb.bejson` manifest without ensuring the `Fields` and `Values` arrays are perfectly aligned. Use `bejson-manager-core` for structural validation.
- **Constraint C**: All new skills MUST include an `AUTHOR CREDIT` block and a `Relational ID`.
- **Constraint D**: Follow the `category-name-modifier` naming convention (e.g., `post-analysis-reporting-concise`).

## Task Execution Protocol
1. **Analyze**: Identify the required capability and check the registry (`104a.mfdb.bejson`).
2. **Strategy**: Propose skill activation or creation using the `skills-builder` protocol.
3. **Execute**: Use surgical edits for registry updates; use the `protocol-update-persistent` for cross-skill refactors.
4. **Verify**: Run `analysis-perceptual-decomposition` to confirm the system's structural integrity post-modification.

## Known Anomalies
- **Path Sensitivity**: Ensure `Format_Version` rules (104 vs 104a) are strictly followed to prevent parsing errors in older tools.

---
*Relational ID: skill-system-agent-rules-v2*
