#!/usr/bin/env python3
"""
File: convert_claude_to_gemini.py
Description: Automates the conversion of Claude 2026 skills to Gemini CLI 2026 format.
Version: 1.0.0
Author: Elton Boehnen
Relational_ID: gcli-converter-script-001
"""

import os
import re
import yaml
import sys
import argparse
from pathlib import Path

VERSION = "1.0.0"

def get_script_path() -> Path:
    return Path(__file__).resolve().parent
SCRIPT_PATH = get_script_path()

def parse_claude_skill(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split YAML and Markdown
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return None, content
    
    yaml_content = match.group(1)
    body = match.group(2).strip()
    
    # Robust metadata extraction (handles loose YAML with unquoted colons)
    metadata = {}
    # Simple regex to find top-level keys
    keys = ['name', 'description', 'trigger on', 'allowed-tools', 'model', 'context', 'hooks', 'argument-hint']
    for key in keys:
        # Match "key: value" where value can span lines until next key or end
        key_pattern = rf'^{key}:\s*(.*?)(?=\n\w+:|$)'
        key_match = re.search(key_pattern, yaml_content, re.DOTALL | re.MULTILINE)
        if key_match:
            val = key_match.group(1).strip()
            # Try to parse if it looks like a list or dict, otherwise keep as string
            if val.startswith('[') and val.endswith(']'):
                try:
                    metadata[key] = yaml.safe_load(val)
                except:
                    metadata[key] = val
            else:
                metadata[key] = val
    
    # If regex failed to find description, try safe_load as fallback
    if 'description' not in metadata:
        try:
            full_meta = yaml.safe_load(yaml_content)
            if full_meta:
                metadata.update(full_meta)
        except:
            pass

    return metadata, body

def normalize_description(metadata):
    desc = metadata.get('description', '').strip()
    triggers = metadata.get('trigger on', [])
    
    if isinstance(triggers, list):
        triggers_str = ", ".join(triggers)
    else:
        triggers_str = str(triggers)
    
    # Avoid doubling "Trigger on:" if already present in description
    if "Trigger on:" in desc:
        normalized = desc
    else:
        normalized = f"{desc} Trigger on: {triggers_str}."
    
    # Clean up whitespace and ensure single line
    normalized = " ".join(normalized.split())
    if normalized.endswith('.'):
        normalized = normalized[:-1].strip() + "."
    return normalized

def split_body(body):
    # Heuristic: Split into core instructions and references
    # Identify sections by H2 or H3
    sections = re.split(r'\n(?=#+ )', body)
    
    core_sections = []
    references = {}
    
    # Common sections to move to references
    ref_keywords = ['example', 'checklist', 'pattern', 'approach', 'pro tip', 'guide', 'checklist', 'template']
    
    for section in sections:
        section = section.strip()
        if not section: continue
        
        title_match = re.match(r'#+ (.*)', section)
        if title_match:
            title = title_match.group(1).lower()
            # Only split if it matches keywords AND has substantial content (> 150 chars)
            if any(kw in title for kw in ref_keywords) and len(section) > 150:
                ref_name = re.sub(r'[^a-z0-9]', '-', title).strip('-')
                # Ensure unique ref name
                base_name = ref_name
                counter = 1
                while ref_name in references:
                    ref_name = f"{base_name}-{counter}"
                    counter += 1
                references[ref_name] = section
            else:
                core_sections.append(section)
        else:
            core_sections.append(section)
            
    return "\n\n".join(core_sections), references

def convert(input_file, output_root):
    metadata, body = parse_claude_skill(input_file)
    if not metadata:
        print(f"Error: Could not parse YAML frontmatter in {input_file}")
        return

    skill_name = metadata.get('name', Path(input_file).stem.replace('skill-', ''))
    skill_dir = Path(output_root) / skill_name
    os.makedirs(skill_dir / "references", exist_ok=True)
    os.makedirs(skill_dir / "scripts", exist_ok=True)
    os.makedirs(skill_dir / "assets", exist_ok=True)

    norm_desc = normalize_description(metadata)
    core_body, references = split_body(body)

    # Add reference links to core body
    if references:
        core_body += "\n\n## References\n"
        for ref_name in references:
            core_body += f"- See [references/{ref_name}.md](references/{ref_name}.md) for {ref_name.replace('-', ' ')}.\n"

    # Write SKILL.md
    with open(skill_dir / "SKILL.md", 'w', encoding='utf-8') as f:
        f.write("---\n")
        f.write(f"name: {skill_name}\n")
        f.write(f"description: {norm_desc}\n")
        f.write("---\n\n")
        f.write(core_body)

    # Write references
    for ref_name, content in references.items():
        with open(skill_dir / "references" / f"{ref_name}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"✅ Converted {input_file} to {skill_dir}")

def main():
    parser = argparse.ArgumentParser(description="Convert Claude skills to Gemini CLI skills.")
    parser.add_argument("input_file", help="Path to the Claude .md skill file")
    parser.add_argument("--output", default=".", help="Output root directory")
    args = parser.parse_args()

    convert(args.input_file, args.output)

if __name__ == "__main__":
    main()
