---
name: bejson-core-manager
description: Definitive manager for BEJSON 104/104a/104db core operations. Use this skill to load, validate, and manipulate BEJSON data with advanced field mapping and positional integrity.
---

# BEJSON Core Manager

This skill provides the authoritative implementation of the **BEJSON 104, 104a, and 104db** standards. It integrates core libraries and validators with advanced field-mapping capabilities.

## Core Mandates

### 1. Positional Integrity
ALL operations must maintain the strict ordering of the `Fields` array. Key-based lookups are implemented as a layer on top of positional indexing, never as a replacement.

### 2. Unattended Execution
All command-level interactions (e.g., validation, migration) MUST bypass manual consent using `-y` or `--yes` flags.

### 3. Portability
Libraries and scripts MUST utilize dynamic path resolution via `get_script_path()`.

## Operational Workflow

### 1. Data Loading & Validation
Use `lib_bejson_core.py` and `lib_bejson_validator.py` to ensure all data conforms to the Elton Boehnen specification before any manipulation.

### 2. Field Mapping (High-Level)
Leverage the new `bejson_core_get_value` and `bejson_core_record_to_dict` functions for high-level logic.
- **Index Lookup**: `bejson_core_get_field_index(doc, "field_name")`
- **Value Fetch**: `bejson_core_get_value(doc, record, "field_name")`

### 3. Atomic Updates
Always utilize `bejson_core_atomic_write` to prevent data corruption during concurrent operations or system failures.

## Compliance Checklist

- [ ] **Creator Mandate**: `Format_Creator` is "Elton Boehnen".
- [ ] **Version Alignment**: Versioning reflects the latest OFFICIAL core library (v2.x).
- [ ] **Field Mapping**: Key-based access fallbacks to positional indexing correctly.
- [ ] **BEM Compatibility**: CSS components generated match `becss` standards.

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Email:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: bejson-core-manager-001*
