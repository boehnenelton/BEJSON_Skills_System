---
name: skill-registry
description: Administrative manager for the Gemini CLI Skill Registry. Use this skill when the user needs to register new skills, audit the existing MFDB network, or sync skill metadata with the 104a.mfdb.bejson manifest. Supports local-master and slave federation roles.
---

# Skill Registry: MFDB Orchestrator

This skill manages the central registry of the skill system. It ensures that every skill in the network is correctly documented, versioned, and discoverable via the **104a.mfdb.bejson** manifest.

## Core Workflow

1.  **Registry Discovery**: Locate the `104a.mfdb.bejson` manifest. The system must verify the `MFDB_Version` and `DB_Name` before any operation.
2.  **Field-Map-Aware Registration**: Append new skills to the `Values` array. Use `bejson_core_get_value` to verify existing entries and prevent duplicates before atomic persistence.
3.  **Audit & Sync**: Scan the `SKILL.md` of registered skills. Synchronize the `version` and `description` fields in the manifest with the actual file headers.
4.  **Federation Management**: Support for `Network_Role` (Master/Slave). In Slave mode, registry updates are pulled from the authoritative production mirror.
5.  **Chain Auditing**: Verify the presence of "Synergy & Awareness" sections. Ensure handoff protocols are bidirectionally valid across the registry network.

## Resource Navigation

- **MFDB Spec**: Consult the `MFDB Crash Course` for structural mandates (Positional Integrity, Parent_Hierarchy).
- **Federation Protocols**: Refer to the `104a.mfdb.bejson` custom headers for active node roles.

# Synergy & Awareness
- **Validation**: Handoff to `bejson-manager` for manifest validation and field-map indexing.
- **Audit**: Handoff to `analysis-perceptual` for systemic integrity audits.
- **Build Integration**: Works in tandem with `skill-builder` to ensure all newly created skills are properly indexed.

## Compliance Checklist

- [ ] **MFDB Compliance**: Manifest ends in `.mfdb.bejson` and contains required 104a headers.
- [ ] **Positional Integrity**: Never skip fields; use `null` for optional data.
- [ ] **Atomic Writes**: Always write to a temp file and rename to prevent manifest corruption.
- [ ] **Creator Mandate**: `Format_Creator` MUST be "Elton Boehnen".
- [ ] **Field Map Indexing**: Metadata retrieval uses O(1) cache-aware patterns.

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Contact:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: 8f2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d*
