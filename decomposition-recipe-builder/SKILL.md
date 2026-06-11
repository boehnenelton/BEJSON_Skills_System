---
name: decomposition-recipe-builder
description: Break down files, documents, scripts into detailed markdown "recipes" that categorize structure, UI components, styling, classes, functions, and features. Use when you need to understand, document, or rebuild a project component. Analyzes source code (Python, JS, TS, HTML, CSS), documents, and projects to produce structured decomposition recipes with categorized feature lists, dependency maps, and architectural insights. Trigger on: "decompose", "break down", "analyze structure", "create recipe", "reverse engineer", "document this code", "what does this do", or when analyzing any file/project.
---

# Decomposition Recipe Builder

Transform any file, script, document, or project into a structured markdown "recipe" that documents its architecture, components, styling, functionality, and features in organized, reusable form.

## What It Does

Takes input (code file, HTML, script, document) and produces a **decomposition recipe** — a categorized markdown guide that breaks down:

- **Identity** — What it is, its purpose, tech stack
- **Architecture** — File structure, entry points, data flow
- **UI Components** (if applicable) — Layout, widgets, state
- **Styling** — Color palette, typography, CSS patterns
- **Classes & Interfaces** — Structure, methods, properties
- **Functions** — Purpose, parameters, return values
- **Features** — Organized by category, dependencies
- **Dependencies** — External libraries, imports
- **Reconstruction Notes** — How to rebuild or extend

Output is **pure markdown** suitable for documentation, knowledge bases, or as a blueprint for rebuilding.

---

## Recipe Structure (Standard Template)

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
- **Called by:** [Functions that call this]
- **Calls:** [Functions it calls]

## Features (Categorized)

### Category 1: [Feature Category]
- ✓ Feature 1 — description
- ✓ Feature 2 — description

### Category 2: [Feature Category]
- ✓ Feature 3 — description

## Dependencies & Imports
- [Library/Module] — [purpose]

## Notes & Observations
- Key design decisions
- Potential issues
- Extension points
- Recommendations

## Reconstruction Checklist
- [ ] [Step 1]
- [ ] [Step 2]
```

---

## Input Types & Analysis Approach

### Python Scripts
```
Input: .py file or snippet
↓
Extract: imports, classes, functions, docstrings, decorators
↓
Analyze: architecture, patterns, dependencies
↓
Recipe: Class map, function signatures, feature list
```

Example analysis:
```python

# Input
class UserManager:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def create_user(self, name, email):
        """Create a new user and return ID"""
        return self.db.insert("users", {"name": name, "email": email})
```

Recipe output:
```markdown

### UserManager
- **Purpose:** Manage user CRUD operations
- **Constructor:** `__init__(db_connection)` — Initialize with DB connection
- **Methods:**
  - `create_user(name, email)` → int — Creates user, returns user ID
```

---

### HTML/React Components
```
Input: HTML/JSX file
↓
Extract: DOM structure, CSS classes, event handlers, state
↓
Analyze: component hierarchy, interactivity, styling
↓
Recipe: Component map, UI breakdown, feature list
```

Example analysis:
```jsx
<div className="card primary-accent">
  <h3>{title}</h3>
  <p>{description}</p>
  <button onClick={handleSubmit}>Submit</button>
</div>
```

Recipe output:
```markdown

### Component: Card
- **Structure:** div.card > h3, p, button
- **Classes:** `card`, `primary-accent`
- **State:** Controlled via props (title, description)
- **Events:** onClick → handleSubmit()
- **Purpose:** Display content card with action
```

---

### Stylesheets (CSS/SCSS)
```
Input: .css or .scss file
↓
Extract: selectors, properties, media queries, custom properties
↓
Analyze: color schemes, typography, spacing, responsive patterns
↓
Recipe: Palette, typography scale, component styles, patterns
```

Example analysis:
```css
:root {
  --primary: #DE2626;
  --bg: #FFFFFF;
  --text: #000000;
}

.button {
  background: var(--primary);
  color: white;
  padding: 0.5rem 1rem;
}
```

Recipe output:
```markdown

### Color Palette
- **Primary:** #DE2626 (red)
- **Background:** #FFFFFF (white)
- **Text:** #000000 (black)

### CSS Patterns
- **Button:** `background: var(--primary)`, `color: white`, 12px padding
```

---

### Documents (Markdown, Text)
```
Input: README, guide, specification
↓
Extract: sections, lists, code blocks, definitions
↓
Analyze: document type, structure, key concepts
↓
Recipe: Table of contents, key sections, feature summary
```

---

### Full Projects / Directories
```
Input: Entire codebase or folder
↓
Extract: All files, structure, entry points
↓
Analyze: Dependencies, architecture, patterns
↓
Recipe: Project overview, file map, module breakdown, feature matrix
```

---

## Feature Categorization Examples

### E-Commerce Site
```markdown

## Features (Categorized)

### Shopping
- ✓ Product listing with filters
- ✓ Cart management
- ✓ Checkout flow

### User Management
- ✓ User registration
- ✓ Login/logout
- ✓ Profile management

### Admin
- ✓ Product CRUD
- ✓ Order tracking
- ✓ Analytics dashboard
```

### Document Management System
```markdown

## Features (Categorized)

### Document Handling
- ✓ Upload documents
- ✓ Version control
- ✓ Archive old versions

### Collaboration
- ✓ Comments and annotations
- ✓ Share with users
- ✓ Access control

### Search & Organization
- ✓ Full-text search
- ✓ Tagging system
- ✓ Folder structure
```

---

## Analysis Checklist (What to Look For)

### Code Files
- [ ] **Imports & Dependencies** — What external libraries are used?
- [ ] **Entry Points** — What runs first? (main(), __init__, etc.)
- [ ] **Classes & Objects** — Structure, inheritance, composition
- [ ] **Functions & Methods** — Purpose, parameters, return values
- [ ] **State Management** — Global vars, class properties, closures
- [ ] **Error Handling** — Try/catch, validations, edge cases
- [ ] **Patterns** — Design patterns (Factory, Observer, Singleton, etc.)
- [ ] **Performance Considerations** — Algorithms, caching, loops
- [ ] **Testing** — Test files, mocks, fixtures

### UI/Frontend
- [ ] **Layout System** — Flexbox, Grid, absolute positioning
- [ ] **Component Hierarchy** — Parent-child relationships
- [ ] **Responsive Design** — Media queries, breakpoints
- [ ] **Interactivity** — Event handlers, transitions, animations
- [ ] **State Management** — Props, state, context, stores
- [ ] **Accessibility** — ARIA labels, semantic HTML, color contrast
- [ ] **Performance** — Bundle size, lazy loading, memoization

### Styling
- [ ] **Color System** — Primary, secondary, accents, semantic colors
- [ ] **Typography** — Font families, sizes, weights, line-height
- [ ] **Spacing** — Margins, padding, gaps (scale or custom?)
- [ ] **Borders & Shadows** — Styles, purposes
- [ ] **Animations** — Transitions, keyframes, durations
- [ ] **Breakpoints** — Mobile, tablet, desktop, large screens

### Overall Architecture
- [ ] **Data Flow** — How data moves through the system
- [ ] **Module Separation** — What's coupled, what's decoupled
- [ ] **Configuration** — Environment variables, settings
- [ ] **Logging & Debugging** — How errors are tracked
- [ ] **Documentation** — Docstrings, comments, README

---

## Recipe Usage Examples

# PrimaryButton - Decomposition Recipe

## Identity
- **Type:** React Functional Component
- **Purpose:** Render a primary action button
- **Dependencies:** React

## UI Component: PrimaryButton
- **Props:**
  - `label` (string) — Button text
  - `onClick` (function) — Click handler
  - `disabled` (boolean) — Disable state
- **Classes Applied:** `btn`, `btn-primary`, `disabled` (conditional)
- **Behavior:** Applies disabled class and HTML disabled attr when disabled=true

## Features

### Button Rendering
- ✓ Display custom label text
- ✓ Handle click events
- ✓ Support disabled state
- ✓ Apply semantic disabled styling

### Example 2: Analyze Full Document

**Input:** Markdown specification or guide

**Recipe Output:**
```markdown

# Developer Guide - Decomposition Recipe

## Identity
- **Type:** Markdown Documentation
- **Purpose:** Guide for development setup and patterns
- **Audience:** Development team

## Document Structure
- Getting Started
- Environment Setup
- Project Structure
- Coding Standards
- API Documentation
- Deployment

## Key Sections

### Getting Started
- Prerequisites (Node 16+, npm 8+)
- Install steps
- First run verification

### Coding Standards
- Naming conventions (camelCase variables, PascalCase components)
- File organization
- Comment style

## Features (Documented)

### Development Environment
- ✓ Local development server
- ✓ Hot module reload
- ✓ Development debugging

### Deployment
- ✓ Build process
- ✓ Environment variables
- ✓ Cloud hosting options

## Key Takeaways
- Framework: React + TypeScript
- Build tool: Vite
- Testing: Jest + React Testing Library
- Deployment: GitHub Actions → AWS S3
```

---

## Output Format Options

### Standard Markdown
Default output. Clean, readable, version-controllable.

### Structured Checklist
For reconstruction and implementation:
```markdown

### Dependency Map
For understanding relationships:
```
UserManager
├── Depends on: DatabaseConnection
├── Used by: AuthService, UserController
└── Uses: logger, validator
```

### Feature Matrix
For planning and tracking:
```
Feature                | Category    | Priority | Status
────────────────────── | ─────────── | ────── | ────────
User registration      | Auth       | HIGH   | ✓ Done
Email verification    | Auth       | HIGH   | ✓ Done
Password reset        | Auth       | MEDIUM | ⚠ In Progress
Profile customization | User Mgmt  | LOW    | ○ Planned
```

---

## Common Decomposition Patterns

### MVC/MVP Pattern
```
Model → View ← Controller
      ↓
   Service Layer (business logic)
```

### Component-Driven Architecture
```
App
├── Header
├── Sidebar
├── MainContent
│   ├── Card
│   ├── List
│   └── Button
└── Footer
```

### Layered Architecture
```
Presentation Layer
       ↓
Business Logic Layer
       ↓
Persistence Layer
       ↓
Database
```

---

## What NOT to Do

❌ Don't just copy-paste code into the recipe  
❌ Don't list every variable — highlight important ones  
❌ Don't forget dependencies — they're critical  
❌ Don't skip styling — it's part of the architecture  
❌ Don't ignore error cases — they define behavior  
❌ Don't write too technically — recipes are for rebuilding, not for PhDs  
❌ Don't forget the "why" — intent matters more than implementation

---

## Recipe as Communication

Use recipes to:
- **Onboard new team members** — "Here's the codebase in one document"
- **Plan refactors** — "Here's what we're changing"
- **Review code** — "Does this follow the documented architecture?"
- **Document requirements** — "These are the features we built"
- **Archive projects** — "If we ever need to rebuild this..."
- **Share knowledge** — "This is how we solve X problem"

The recipe becomes the **contract** between the original builder and the next person who touches it.

## References
- See [references/example-1--rebuild-this-button-component.md](references/example-1--rebuild-this-button-component.md) for example 1  rebuild this button component.
- See [references/reconstruction-checklist.md](references/reconstruction-checklist.md) for reconstruction checklist.
- See [references/implementation-checklist.md](references/implementation-checklist.md) for implementation checklist.
- See [references/pro-tips.md](references/pro-tips.md) for pro tips.
