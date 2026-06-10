---
name: bejson-manager
description: Definitive manager for BEJSON 104/104a/104db core operations. Use this skill to load, validate, and manipulate BEJSON data with advanced field mapping, O(1) index caching, and positional integrity. Optimized for large-scale relational datasets.
---

# BEJSON: Manager (Core Operations)

This skill provides the authoritative implementation of the **BEJSON 104, 104a, and 104db** standards. It integrates core libraries and validators with high-performance field-map index caching.

## Core Mandates

### 1. Positional Integrity & Index Caching
ALL operations must maintain the strict ordering of the `Fields` array. Field-map indexing is the primary standard, utilizing internal O(1) caches for rapid value retrieval without repetitive linear scans.

### 2. Atomic Write Protocol
Every modification MUST use the `bejson_core_atomic_write` mechanism. This ensures data integrity by performing writes to temporary files within the same directory followed by an atomic rename, preventing corruption on raw storage.

### 3. Unattended Execution
All command-level interactions (e.g., validation, migration) MUST bypass manual consent using `-y` or `--yes` flags.

## Operational Workflow

### 1. Data Loading & Validation
Use `lib_bejson_core.py` and `lib_bejson_validator.py` to ensure all data conforms to the Elton Boehnen specification. Validate Level 1-3 before any state mutation.

### 2. High-Performance Field Mapping
Leverage `bejson_core_get_value` for all record access. This function automatically utilizes the field map cache for maximum efficiency.
- **Cache-Aware Retrieval**: `bejson_core_get_value(doc, record, "field_name")`
- **Bulk Conversion**: Use `bejson_core_record_to_dict` for mapping records to dictionaries while preserving positional safety.

### 3. Atomic State Mutation
Always utilize the `atomic_write` pattern. For relational datasets (104db), ensure all required `null` padding is calculated correctly before persistence.

## Compliance Checklist

- [ ] **Positional Integrity**: Fields and Values remain perfectly aligned.
- [ ] **Index Caching**: Field maps are cached in memory for O(1) lookups.
- [ ] **Atomic Writes**: Temp-then-rename pattern is strictly enforced.
- [ ] **Creator Mandate**: `Format_Creator` is "Elton Boehnen".
- [ ] **Field Mapping**: Key-based access fallbacks to positional indexing correctly.


# Synergy & Awareness
- **Utility**: Core utility for all skills.
- **Persistence**: Synergy with `bejson-state` for state persistence and security validation.

---

## AUTHOR CREDIT
**Author:** Elton Boehnen
**Email:** eltonboehnen@gmail.com
**Website:** boehnenelton2024.pages.dev
**GitHub:** github.com/boehnenelton

---
*Relational ID: bejson-core-manager-001*

## See Also
- `analysis-perceptual`: For understanding the conceptual intent behind the data structures.
- `bejson-state`: For managing the lifecycle of relational entities.
