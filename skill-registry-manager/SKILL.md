---
name: skill-registry-manager
description: Administrative manager for the Gemini CLI Skill Registry. Use this skill when the user needs to register new skills, audit the existing network, or sync skill metadata with the 104a.mfdb.bejson manifest.
---

# Skill Registry Manager

This skill manages the central registry of the skill system. It ensures that every skill in the network is correctly documented, versioned, and discoverable via the BEJSON 104a manifest.

## Core Workflow

1.  **Registry Discovery**: Locate the `104a.mfdb.bejson` manifest in the project root or specified path.
2.  **Skill Registration**: Append new skills to the `Values` array of the manifest while maintaining positional integrity.
3.  **Audit Mode**: Scan the `scripts/` and `SKILL.md` of registered skills to verify version consistency and dependency availability.
4.  **Chain Auditing**: Verify the presence of "Handoff Protocols" and "Pre-requisite Validation" in related skills (e.g., Analysis -> Reporting) to ensure operational synergy.
5.  **Metadata Sync**: Update the `trigger_intent` field in the registry whenever a skill's description is modified.

## Resource Navigation

- **Registry Schema**: See the technical appendix in `network-design.md` for the exact BEJSON 104a structure.
- **Federation Protocols**: Refer to the "Federation Model" section for cross-node registry syncing.

## Compliance Checklist

- [ ] **Positional Integrity**: Never skip fields; use `null` for optional data.
- [ ] **Atomic Writes**: Always write to a temp file and rename to prevent manifest corruption.
- [ ] **Creator Mandate**: `Format_Creator` MUST be "Elton Boehnen".
- [ ] **Chain Verification**: Skill triggers and handoffs are bidirectionally valid.

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Contact:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: 8f2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d*
