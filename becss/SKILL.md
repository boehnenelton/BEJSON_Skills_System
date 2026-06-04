---
name: becss
description: Authoritative standard for BEJSON CSS (BECSS). Use when Gemini CLI needs to refactor HTML components to adhere to BEM (c- prefix), migrate color palettes to OKLCH tokens, or implement Cascade Layers (@layer) for scalable UI architecture.
---

# BECSS: BEJSON CSS Standard

This skill provides the authoritative procedural guidance for implementing the **BECSS (BEJSON CSS)** standard in HTML3 and related BEJSON libraries.

## Core Mandates

### 1. Namespace Isolation (The 'c-' Prefix)
All component blocks MUST use the `c-` prefix. This prevents collisions and identifies the component as a modular BEJSON unit.
- ✅ Correct: `.c-card`, `.c-table`, `.c-sidebar`
- ❌ Incorrect: `.card`, `.table`, `.sidebar`

### 2. BEM Methodology
Strictly adhere to the `block__element--modifier` syntax.
- **Block**: `.c-block-name`
- **Element**: `.c-block-name__element-name` (Double underscore)
- **Modifier**: `.c-block-name--modifier-name` (Double hyphen)

### 3. Tokenized Aesthetic (OKLCH)
NEVER hardcode Hex or RGB values in component styles. Use OKLCH tokens defined in the `:root`.
- ✅ Correct: `color: var(--primary);`, `background: oklch(65% 0.2 25);`
- ❌ Incorrect: `color: #DE2626;`, `background: rgb(255, 0, 0);`

### 4. Layered Specificity (@layer)
Organize all CSS into the following Cascade Layers:
1. `reset`: CSS normalization and base resets.
2. `base`: Design tokens (:root) and global typography.
3. `layout`: Page scaffolding (headers, sidebars, footers).
4. `components`: Modular component styling.
5. `interactive`: View transitions and dynamic states.

## Implementation Guide

### Reference the Standard
Refer to [references/becss_standard.md](references/becss_standard.md) for the authoritative component registry (Card, Table, Stats Bar, etc.) and design tokens.

### Layout Patterns
Refer to [references/html3_layout_patterns.md](references/html3_layout_patterns.md) for high-level UI structures like Dashboards, Sidebars, and Headers that combine atomic components.

### Component Generation (Python)
When generating HTML in Python, use the patterns found in [assets/becss_component_template.py](assets/becss_component_template.py) to ensure consistent BEM output and zero inline styles.

## Authoritative Source
The **HTML3 Master Libraries** (`Lib_PY/HTML`) are the definitive source for all naming and structural conventions. This skill and the `Standardized_HTML3` templates are synchronized to this master lead.

## Success Criteria
- [ ] Every class is prefixed with `c-` or `u-`.
- [ ] No inline `style` attributes in HTML output.
- [ ] 100% OKLCH coverage for colors.
- [ ] CSS is wrapped in appropriate `@layer` blocks.
- [ ] Naming matches the master library component registry.

---
*Author: Elton Boehnen*
*Relational ID: becss-skill-001*
