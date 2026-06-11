---
name: decomposition-recipe-builder
description: Break down files, documents, scripts into detailed markdown "recipes" that categorize structure, UI components, styling, classes, functions, and features. Use when you need to understand, document, or rebuild a project component. Analyzes source code (Python, JS, TS, HTML, CSS), documents, and projects to produce structured decomposition recipes with categorized feature lists, dependency maps, and architectural insights. Trigger on: "decompose", "break down", "analyze structure", "create recipe", "reverse engineer", "document this code", "what does this do", or when analyzing any file/project.
---

# Decomposition Recipe Builder

Transform any file, script, document, or project into a structured markdown "recipe" that documents its architecture, components, styling, functionality, and features in organized, reusable form.

## Identity
- **Name:** Decomposition Recipe Builder
- **Type:** Architectural Analysis Skill
- **Purpose:** To transform complex inputs into high-signal blueprints for reconstruction or documentation.
- **Trigger keywords:** "decompose", "break down", "analyze structure", "create recipe", "reverse engineer", "document this code".

## Core Architecture Overview
This skill operates as a **Perceptual Decomposition Engine**. It prioritizes **intent** over **syntax**, mapping out how a system *functions* and how its parts *relate*, rather than just listing variables.

## Recipe Structure (Mandatory Template)

```markdown
# [File/Project Name] - Decomposition Recipe
**Type:** [HTML/Python/React/Document/etc]
**Purpose:** [One-line description]
**Date Analyzed:** [ISO date]

## Identity
- **Name:** [Full name]
- **Type:** [File type/technology]
- **Purpose:** [What it does]
- **Status:** [Active/Template/Deprecated]
- **Dependencies:** [List]

## Architecture Overview
[High-level description of structure, flow, patterns]

## File Structure
```
[If directory/project]
...
```

## Styling
### Color Palette
- **Primary:** [color info]
- **Secondary:** [color info]

### Typography
- **Headings:** [font stack]
- **Body:** [font stack]

### CSS Patterns
- [Pattern 1]
- [Pattern 2]

## UI Components / Layout
[If HTML/frontend]
### Component 1: [Name]
- **Purpose:** [What it does]
- **Structure:** [DOM/layout]
- **Classes:** [CSS classes used]
- **Interactivity:** [Event handlers, state]

## Classes & Interfaces
[If code]
### ClassName
- **Purpose:** [What it does]
- **Properties:**
  - `property_name` (type) — description
- **Methods:**
  - `methodName(params)` → return_type — description

## Functions
### function_name(params)
- **Purpose:** [What it does]
- **Parameters:**
  - `param1` (type) — description
- **Returns:** type — description

## Features (Categorized)
### Category 1: [Feature Category]
- ✓ Feature 1 — description
- ✓ Feature 2 — description

## Reconstruction Checklist
- [ ] [Step 1]
- [ ] [Step 2]
```

## Input Analysis Approaches

### 1. Python Scripts
- Extract: imports, classes, functions, docstrings, decorators.
- Analyze: architecture, patterns, dependencies.
- Result: Class map, function signatures, feature matrix.

### 2. HTML/Frontend
- Extract: DOM structure, CSS classes, event handlers, state.
- Analyze: component hierarchy, interactivity, styling.
- Result: Component map, UI breakdown, feature list.

### 3. Stylesheets (CSS/BECSS)
- Extract: selectors, properties, media queries, variables.
- Analyze: color schemes, typography, spacing scale.
- Result: Palette, typography stack, recurring patterns.

## Analysis Checklist
- [ ] **Data Flow** — How does state move through the system?
- [ ] **Module Separation** — What's coupled, what's decoupled?
- [ ] **Error Handling** — How are edge cases managed?
- [ ] **AX (Agent Experience)** — Is the structure predictable and machine-readable?

## Pro Tips
✅ **Start broad, drill deep** — Overview first, then atomic breakdown.
✅ **Document intent** — *Why* was this pattern chosen?
✅ **Note edge cases** — What assumptions are made?
✅ **List dependencies** — Essential for portability.

---
## Deep Dive Resources
Extended examples and checklists are maintained in the `/references` directory for maximum forensic depth.
- See `references/implementation-checklist.md`
- See `references/pro-tips.md`

·· BEEP ··
