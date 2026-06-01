# BECSS (BEJSON CSS) Standard Specification

## 1. Design Tokens (OKLCH)

All colors must be expressed in OKLCH or as CSS variables referencing OKLCH tokens.

| Token | OKLCH Value | HEX (Approx) | Use Case |
| :--- | :--- | :--- | :--- |
| `--primary` | `oklch(65% 0.2 25)` | `#DE2626` | Authority Red, Accents |
| `--bg-page` | `oklch(100% 0 0)` | `#FFFFFF` | Global Page Background |
| `--text-main` | `oklch(20% 0 0)` | `#1A1A1A` | Primary Body Text |
| `--text-muted` | `oklch(50% 0 0)` | `#808080` | Secondary/Meta Text |
| `--border` | `oklch(90% 0 0)` | `#E5E5E5` | Default Borders |

## 2. Naming Conventions

### Component Prefix (`c-`)
Reserved for standalone components. 
- Example: `.c-card`, `.c-button`, `.c-bejson-table`.

### Utility Prefix (`u-`)
Reserved for single-purpose, high-specificity utility classes.
- Example: `.u-text-center`, `.u-mt-24`, `.u-text-muted`.

### BEM Syntax
`c-block__element--modifier`

## 3. Structural Layers (@layer)

```css
@layer reset, base, layout, components, interactive;

@layer reset { /* Normalization */ }
@layer base { /* Tokens, Typography */ }
@layer layout { /* Header, Sidebar, Footer */ }
@layer components { /* Cards, Tables, etc. */ }
```

## 4. Mobile-First & Android WebView Hardening

- **Viewport**: Use `100dvh` for full-height containers to account for browser chrome.
- **Safe Areas**: Use `env(safe-area-inset-bottom)` for fixed-bottom elements.
- **ES5 Safety**: All interactive JS within components must be ES5-compliant (no `const`/`let` in strings unless toggled, no arrow functions).

---
*Relational ID: becss-standard-spec*
