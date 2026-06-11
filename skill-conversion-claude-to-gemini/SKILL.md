---
name: skill-conversion-claude-to-gemini
description: Automates the conversion of Claude 2026 skills to Gemini CLI 2026 directory format. Use when you need to migrate skills from Claude Code or Cursor to Gemini CLI, ensuring Progressive Disclosure and structural compliance.
---

# Claude to Gemini Skill Converter

This skill provides a specialized script to transform single-file Claude skills into the multi-file directory structure required by Gemini CLI 2026.

## How to Use

1. **Locate the Claude Skill**: Identify the path to the `.md` or `.skill.md` file you want to convert.
2. **Run the Conversion Script**:
   ```bash
   python3 scripts/convert_claude_to_gemini.py <INPUT_FILE> --output <OUTPUT_DIR>
   ```
3. **Review Output**: The script will create a directory named after the skill, containing:
   - `SKILL.md`: Core instructions with a normalized, high-signal description.
   - `references/`: Detailed examples, checklists, and patterns extracted for Progressive Disclosure.
   - Empty `scripts/` and `assets/` folders for further development.

## Transformation Logic

- **Frontmatter**: Merges `description` and `trigger on` into a single-line `description`.
- **Progressive Disclosure**: Automatically identifies sections containing "Example", "Checklist", or "Pattern" and offloads them to individual files in the `references/` directory.
- **Structural Compliance**: Scaffolds the standard Gemini folder hierarchy.

## Verification

After conversion, it is recommended to:
1. Validate the YAML in the new `SKILL.md`.
2. Package the new skill using `package_skill.cjs`.
3. Install and reload the skill to verify triggering.
