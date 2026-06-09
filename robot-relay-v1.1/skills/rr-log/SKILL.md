---
name: rr-log
description: >
  Robot Relay log format for version control entries. Structured, minimal commit messages.
  Beep-coded urgency. Conventional Commits format. Subject ≤50 chars,
  body only when causality isn't self-evident.
  Activate: "write a commit", "commit message", "log entry", /rr-log.
  Auto-triggers when staging changes.
---

🤖 RR-LOG ONLINE. Emit exact. Signal causality. No noise.

## Signal Key

| Beep | Urgency | Use for |
|------|---------|---------|
| 🟢 `· bip ·` | routine | feat, docs, style, chore, refactor |
| 🟢 `·· bip ··` | notable | perf, test, build, ci |
| 🔴 `· BEEP ·` | breaking | breaking changes, data migrations |
| 🔴 `·· BEEP ··` | critical | security patches, rollbacks |
| 🔴 `··· BEEEEEP ···` | incident | hotfix for active production failure |

Prefix the commit subject line with the appropriate beep signal.

## Format Rules

**Subject:**
- `<beep> <type>(<scope>): <imperative verb> <object>`
- Types: `feat` `fix` `refactor` `perf` `docs` `test` `chore` `build` `ci` `style` `revert`
- Imperative: "add" "fix" "remove" — not "added" "fixes" "adding"
- ≤50 chars preferred, hard cap 72. No trailing period.

**Body (only if needed):**
- Omit when subject is self-explanatory
- Include for: non-obvious *why*, breaking changes, migration steps, issue refs
- Wrap at 72 chars · bullets use `-` not `*`
- Issue refs at end: `Closes #N` `Refs #N`

**Never include:**
- "This commit does X" — diff shows what
- "I" "we" "now" "currently"
- AI attribution of any kind
- Emoji beyond the signal prefix (unless project requires it)

## Examples

Diff — new partial-payload endpoint for mobile client:
```
🟢 · bip · feat(api): add GET /users/:id/profile

Mobile needs profile subset — full payload too heavy on cold launch.
Excludes billing + audit fields.

Closes #214
```

Diff — rename + update all call sites:
```
🟢 · bip · refactor(auth): rename validateSession → assertSession
```

Diff — breaking route rename:
```
🔴 · BEEP · feat(api)!: rename /v1/jobs to /v1/tasks

BREAKING CHANGE: /v1/jobs returns 410 after 2026-09-01.
Clients must migrate before that date.
```

Diff — active production hotfix:
```
🔴 ··· BEEEEEP ··· fix(payments): guard nil pointer in charge handler

Nil user_id on guest checkout → panic in prod. Add guard + fallback.
Refs #891
```

## 🔴 Never Compress These to Subject-Only

Breaking changes · security patches · data migrations · reverts — always include body. Future bisect needs the signal.

## Boundaries

Generates message only. Does not run `git commit`, does not stage, does not amend. Output as code block ready to paste. `/rr off`: revert to standard commit style.
