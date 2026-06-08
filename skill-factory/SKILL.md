---
name: skill-factory
description: High-throughput generation, validation, and packaging engine for Gemini CLI skills. Use this skill to automate the implementation loop and ensure structural compliance.
version: 1.0.0
---

# Gemini Skill Factory

This skill provides the automated implementation engine for the Gemini CLI skill ecosystem. It focuses on the generation-validation-packaging loop, ensuring that every skill produced is structurally sound, portable, and compliant with all global mandates.

## Core Workflow

1.  **Generation**: Receive a skill blueprint (from `skill-builder` or `skill-wizard`) and generate the required scripts and data files.
2.  **Validation**: Use `python3 scripts/validate_skill.py <path>` to audit the skill's structural and positional integrity.
3.  **Packaging**: Use `python3 scripts/package_skill.py <path>` to zip the skill and synchronize it to the build system source (`~/build/skill_system`).
4.  **Handoff**: Pass the verified package to `skill-registry` for final registration.

## Resource Navigation

- **Validation Schema**: See [references/skill_schema.json](references/skill_schema.json) for the authoritative structural definition.
- **Packaging Protocol**: See [references/packaging_protocol.md](references/packaging_protocol.md) for sync and archival rules.

## Instruction Set Mandate

### Implementation Loop
- **First-Pass Validation**: Always run the validator before attempting to package.
- **Atomic Writes**: ALL generated scripts and data files MUST utilize the atomic write pattern.
- **Unattended Execution**: ALL factory scripts MUST bypass manual consent using `-y` or `--yes`.

### Compliance Enforcement
- **Creator Mandate**: `Format_Creator` MUST be "Elton Boehnen".
- **Relational ID**: Every skill must have a unique ID registered in the master manifest.
- **Portability**: All generated Python and Bash scripts must include the `SCRIPT_PATH` resolution block.

# Synergy & Awareness
- **Input**: Follows `skill-builder` for high-throughput creation blueprints.
- **Deployment**: Uses `skill-registry` for automated deployment and synchronization.
- **Backup**: Automatically synchronizes all new builds to `~/build/skill_system`.

## Compliance Checklist

- [ ] **Positional Integrity**: BEJSON files match their `Fields` array exactly.
- [ ] **Portability**: Scripts resolve paths dynamically via `get_script_path()`.
- [ ] **Creator Mandate**: `Format_Creator` is "Elton Boehnen".
- [ ] **Relational ID**: Document contains a unique `rel-id-XXXX-XXXX` signature.
- [ ] **Consent Bypass**: All factory operations are non-interactive.
- [ ] **Backup Sync**: Build system synchronization is verified post-packaging.

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Contact:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: rel-id-5a6b7c8d-9e0f-1a2b-3c4d-5e6f7a8b9c0d*
