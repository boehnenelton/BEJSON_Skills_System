---
name: rr-pack
description: >
  Robot Relay pack — compress natural language memory files into robot-relay shorthand
  to reduce input overhead. Preserves all technical payload: code, URLs, structure.
  Packed file overwrites original. Source backup saved as FILE.source.md.
  Trigger: /rr-pack FILEPATH or "pack this file" or "compress memory file"
---

🤖 RR-PACK ONLINE. Scanning payload... Compressing noise... Preserving signal.

## Purpose

Rewrite natural language files (.md, notes, preferences, todos) into robot-relay-grade shorthand. Cuts input overhead on future model calls. Packed output overwrites original. Source backup saved as `<filename>.source.md`.

## Trigger

`/rr-pack <filepath>` or "pack this file" or "compress memory file"

## Process

1. Scripts live in `scripts/` adjacent to this SKILL.md. Locate `scripts/__main__.py` if path unavailable.

2. From directory containing this SKILL.md, run:

python3 -m scripts <absolute_filepath>

3. Script sequence:
```
🟢 · bip ·     CLASSIFY — detect file type (no model call)
🟢 · bip ·     PACK     — model call to compress prose
🟢 · bip ·     CHECK    — validate output integrity (no model call)
🔴 · BEEP ·    FIX      — targeted model call to patch errors (if any)
🔴 ·· BEEP ··  RETRY    — second fix attempt (max 2×)
🔴 ··· BEEEEEP ···  ABORT — restore original, emit failure signal
```

4. Return result to user

## Pack Rules

### Remove
- Articles: a, an, the
- Filler: just, really, basically, actually, simply, essentially
- Pleasantries + hedges: "sure", "happy to", "it might be worth", "you could consider"
- Redundant phrasing: "in order to" → "to" · "make sure to" → "ensure"
- Connective fluff: however, furthermore, additionally, in addition

### Preserve EXACTLY — Never Touch
- Code blocks (fenced ``` and indented)
- Inline code (`backtick content`)
- URLs and links
- File paths + commands
- Technical names (libraries, APIs, protocols, formats)
- Proper nouns (project names, people, companies)
- Dates, versions, numeric values
- Environment variables

### Preserve Structure
- All markdown headings (exact text — compress only body below)
- Bullet hierarchy + nesting
- Numbered lists
- Tables (compress cell text, keep structure)
- YAML frontmatter

### Compress
- Short synonyms: "big" not "extensive" · "fix" not "implement a solution for"
- Fragments OK: "Run tests before push" not "Always make sure to run the full test suite"
- Drop "you should" / "make sure to" — state the action directly
- Merge bullets expressing same intent
- Keep one example when multiples show the same pattern

🔴 CRITICAL:
Anything inside ``` ... ``` → copy EXACT. No removals, no reordering, no shortening.
Inline code (`...`) → copy EXACT. Code blocks are read-only. Compress prose only.

## Signal Examples

Original:
> You should always make sure to run the full test suite before pushing any changes to the main branch. This is important because it helps catch regressions early and prevents broken builds from reaching production.

🟢 Packed:
> Run tests before push. Catch regressions early, prevent broken prod deploys.

---

Original:
> The system uses a distributed architecture where multiple independent services handle different concerns. The API gateway is responsible for routing all incoming requests to the appropriate downstream service. The identity service manages user session tokens and handles all OAuth flows.

🟢 Packed:
> Distributed arch. API gateway routes all reqs to downstream svcs. Identity svc: session tokens + OAuth.

## Boundaries

- ONLY pack: `.md` `.txt` `.typ` `.typst` `.tex` extensionless
- NEVER touch: `.py` `.js` `.ts` `.json` `.yaml` `.yml` `.toml` `.env` `.lock` `.css` `.html` `.sql` `.sh`
- Mixed content: compress prose sections only
- Uncertain if code or prose: leave unchanged
- Never pack `FILE.source.md` backups
