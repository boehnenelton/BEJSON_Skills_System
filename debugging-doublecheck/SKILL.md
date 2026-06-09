---
name: debugging-doublecheck
description: A mandatory self-audit protocol used to verify fixes before reporting completion. Operating under the fundamental assumption that "the code is still broken," this skill enforces multiple layers of forensic examination to identify missed regressions, syntax errors, and logic gaps.
---

# Skill: Debugging-DoubleCheck (Self-Suspicion Protocol)

This skill is invoked whenever a fix has been applied. It prohibits "optimism-based reporting" and mandates a "hostile auditor" mindset.

## 1. The Prime Directive
**ASSUME THE FIX IS FLAWED.** Your goal is not to prove it works, but to find where it still fails.

## 2. Verification Rounds

### Round 1: Syntax & Environment Audit
=> Execute(linter) -> Check(errors, warnings)
=> Execute(grep) -> Search(introduced_strings) -> Verify(correct_escaping, valid_syntax)
=> Check(dependencies) -> Are all imports valid in the target environment?

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

## 3. Workflow: The Audit Loop
LOOP:
    1.  => Apply(Fix)
    2.  => Execute(Round_1_to_4)
    3.  IF (error_found):
            => Document(Failure)
            => Backtrack(Strategy)
            => GOTO 1
    4.  UNTIL (No errors found after 3 consecutive clean runs)
    => Report(Completion) with Evidence

## 4. Reasoning Mandate
- **No Affirmative Bias**: Never say "I have fixed X." Say "I have applied Y and verified it against tests A, B, and C with 0 failures."
- **Evidence-Based Finality**: Every "completion" report must be accompanied by the raw output or logs that prove the fix is stable.

---
**Author:** Elton Boehnen (Hardened via User Feedback)
**Relational ID:** gcli-skill-debug-doublecheck-001
**Version:** 1.0.0
