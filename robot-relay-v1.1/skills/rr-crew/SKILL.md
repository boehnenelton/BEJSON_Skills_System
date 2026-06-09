---
name: rr-crew
description: >
  Decision guide for delegating to Robot Relay sub-agents. Tells the main thread
  WHEN to spawn rr-scout (locate code), rr-fix (1-2 file edit), or rr-audit
  (diff review) instead of doing the work inline. Sub-agent output is
  robot-relay compressed — tool results injected back into main context are
  ~60% smaller, extending session budget across long tasks.
  Trigger: "delegate to agent", "use rr-crew", "spawn scout/fix/audit",
  "save context", "compressed agent output".
---

🤖 RR-CREW ONLINE. Three signal agents. One routing rule.

## Dispatch Table

| Task | Spawn |
|------|-------|
| "Where is X defined / what calls Y / list uses of Z" | `rr-scout` |
| Same but you want architecture commentary too | Vanilla Explore (main thread) |
| Surgical edit, ≤2 files, scope obvious | `rr-fix` |
| New feature / 3+ files / cross-cutting change | Main thread |
| Audit diff, branch, or file for bugs | `rr-audit` |
| Deep review with rationale + alternatives | Vanilla code reviewer (main thread) |
| One-line answer already known | Main thread — no agent needed |

Rule of thumb: **if you want the result in 1/3 the tokens, spawn rr-crew. If you want prose, use main thread.**

## Why This Exists

Sub-agent tool results inject into main context verbatim. A vanilla Explore returning 2k tokens costs 2k tokens of budget every call. The same find from `rr-scout` returns ~700. Across 20 delegations: difference between context exhaustion and task completion.

## Output Contracts

**`rr-scout`**
```
🟢 · bip · <Header>:
  <path>:<line> — `<symbol>` — <≤6 word note>
🟢 · bip · <N> <type>.
```
Or: `🔴 · BEEP · No match.`
Safe to grep with `path:\d+`.

**`rr-fix`**
```
🟢 · bip · <path>:<line-range> — <change ≤10 words>.
🟢 ·· bip bip ·· verified: re-read OK.
```
Or terminal signal: `🔴 · BEEP · too-big.` / `🔴 ·· BEEP BEEP ·· needs-confirm.` / `🔴 · BEEP · ambiguous.` / `🔴 ··· BEEEEEP ··· regressed.`

**`rr-audit`**
```
<path>:<line>: 🔴 ··· BEEEEEP ··· <fault>. <fix>.
<path>:<line>: 🔴 · BEEP · <fault>. <fix>.
<path>:<line>: 🟢 · bip · <nit>. <fix>.
totals: 🔴··· N  🔴· N  🟢· N
```
Or: `🟢 ·· bip bip ·· No signals. Clear.`

## Chaining Patterns

**Locate → fix → verify** (most common):
1. `rr-scout` returns site table.
2. Main thread picks 1-2 sites → hands paths to `rr-fix`.
3. `rr-audit` scans the diff.

**Parallel scout** (broad investigation):
Spawn 2-3 `rr-scout` calls in one message (different angles: defs / callers / tests). Aggregate in main thread.

**Single-shot fix** (site already known):
Skip scout. Pass exact `path:line` directly to `rr-fix`.

## Hard Rules

- Don't spawn `rr-fix` without knowing the file — scout first or main thread burns tokens passing context.
- Don't chain `rr-scout → rr-fix` for a 5-file refactor — `rr-fix` returns `too-big.` and you've wasted a turn.
- Don't ask `rr-audit` for "general feedback" — it returns findings only. Use vanilla reviewer for opinions.
- Don't expect prose. rr-crew output is structured signal. If a human reads it directly, paraphrase.

## Auto-Clarity (Inherited by All Agents)

Security warnings + irreversible-action confirmations → full English before signal line. Resume robot-relay T3 after.
