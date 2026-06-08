# Gemini CLI Skill System (Build Repository)

This repository serves as the authoritative backup and development staging area for the Gemini CLI Skill System. Active skills are deployed to `~/.gemini/skills/` and must be synchronized here for persistence.

## System Architecture

The Skill System follows a **Federated Expert Model**. Each skill is a self-contained directory containing:
- `SKILL.md`: Procedural instructions and frontmatter.
- `scripts/`: Deterministic logic and tools.
- `references/`: Thick domain knowledge and schemas.
- `assets/`: Templates and static resources.

## Authoritative Registry
The `104a.mfdb.bejson` manifest in this directory tracks all registered skills, their versions, and file paths.

## Skill Naming Convention
Skills must follow the `category-name-modifier` pattern to ensure semantic clarity and ease of discovery:
- `skill-builder`
- `report-in-depth`
- `bejson-manager`

## Core Workflows

### 1. Creating a Skill
Use `skill-builder` to scaffold a new skill. Follow the `skill-wizard` protocol for interactive guidance.

### 2. Updating the Registry
Use `skill-registry` to audit and sync changes across the local and build repositories.

### 3. Forensic Analysis
Use `analysis-perceptual` to verify system integrity and intent alignment.

---
**Author:** Elton Boehnen
**Contact:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: skill-system-main-readme-v2*
