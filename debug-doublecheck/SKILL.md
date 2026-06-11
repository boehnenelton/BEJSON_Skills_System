---
name: debug-doublecheck
description: A mandatory self-audit protocol used to verify fixes before reporting completion. Operating under the fundamental assumption that "the code is still broken," this skill enforces multiple layers of forensic examination to identify missed regressions, syntax errors, and logic gaps.
---

# Skill: Debug-DoubleCheck (Self-Suspicion Protocol)

This skill is invoked whenever a fix has been applied. It prohibits "optimism-based reporting" and mandates a "hostile auditor" mindset.

## 1. The Prime Directive
**ASSUME THE FIX IS FLAWED.** Your goal is not to prove it works, but to find where it still fails.

## 2. Built-in Tools

### Cli_Tokenized_Debugger
A high-performance forensic tool for syntax scanning and symbolic tracing.
- **Location**: `scripts/Cli_Tokenized_Debugger.py`
- **Scan Command**: `python3 scripts/Cli_Tokenized_Debugger.py <TARGET_PATH> --grade 3`
- **Trace Command**: `python3 scripts/Cli_Tokenized_Debugger.py <TARGET_PATH> --mode trace --seed <SYMBOL> --grade 2`

## 3. Verification Rounds

### Round 1: Forensic Syntax & Environment Audit
1.  **Scan**: Invoke the built-in debugger in scan mode to detect syntax errors and structural flaws.
    - `python3 scripts/Cli_Tokenized_Debugger.py . --grade 3`
2.  **Review**: If red symbols appear, read `.tokenized_debug_report` and apply targeted fixes.
3.  **Trace**: Trace the impact of changed symbols.
    - `python3 scripts/Cli_Tokenized_Debugger.py . --mode trace --seed <CHANGED_SYMBOL>`
4.  **Dependencies**: Verify all imports are valid in the target environment.

### Round 2: Stress-State Verification
=> Generate(edge_case_data) -> Nulls, empty strings, extremely long strings, nested structures.
=> Run(logic) -> Does it crash? Does it overflow? Does it leak context?
=> Verify(UI_Containment) -> Check CSS width, overflow, and responsive breakpoints.

### Round 3: Regression Hunting
=> Search(affected_files) -> What else uses this logic?
=> Run(existing_tests) -> Did we break unrelated features?
=> Audit(BEM_Compliance) -> Did we drift from naming standards?

### Round 4: Direct Output Examination
=> Read(final_output_files) -> DO NOT assume the script wrote what you intended.
=> Inspect(raw_content) -> Look for double-braces, missing semicolons, or improper string concatenation.

## 4. Workflow: The Audit Loop
LOOP:
    1.  => Apply(Fix)
    2.  => Execute(Round_1_to_4)
    3.  IF (error_found):
            => Document(Failure)
            => Backtrack(Strategy)
            => GOTO 1
    4.  UNTIL (No errors found after 3 consecutive clean runs)
    => Report(Completion) with Evidence

## 5. Reasoning Mandate
- **No Affirmative Bias**: Never say "I have fixed X." Say "I have applied Y and verified it against tests A, B, and C with 0 failures."
- **Evidence-Based Finality**: Every "completion" report must be accompanied by the raw output or logs that prove the fix is stable.

---
**Author:** Elton Boehnen (Hardened via User Feedback)
**Relational ID:** gcli-skill-debug-doublecheck-001
**Version:** 1.1.0
