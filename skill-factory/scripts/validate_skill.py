import os
import sys
import re
from pathlib import Path

def get_script_path() -> Path:
    return Path(__file__).resolve().parent

SCRIPT_PATH = get_script_path()

def validate_skill(skill_path: str):
    path = Path(skill_path).resolve()
    if not path.exists() or not path.is_dir():
        print(f"Error: Skill directory not found at {skill_path}")
        return False

    errors = []
    
    # 1. Check folder structure
    required_dirs = ["scripts", "assets", "references"]
    for d in required_dirs:
        if not (path / d).exists():
            errors.append(f"Missing required directory: {d}")

    # 2. Check SKILL.md
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing SKILL.md")
    else:
        content = skill_md.read_text()
        
        # Check Frontmatter
        if not content.startswith("---"):
            errors.append("SKILL.md missing YAML frontmatter")
        
        # Check Mandates
        if "Format_Creator" in content and "Elton Boehnen" not in content:
            errors.append("Creator mandate violation in SKILL.md")
            
        if "rel-id-" not in content:
            errors.append("Missing Relational ID in SKILL.md")
            
        if "Compliance Checklist" not in content:
            errors.append("Missing Compliance Checklist in SKILL.md")
            
        if "AUTHOR CREDIT" not in content:
            errors.append("Missing AUTHOR CREDIT section in SKILL.md")

    # 3. Check Scripts for SCRIPT_PATH
    scripts_dir = path / "scripts"
    if scripts_dir.exists():
        for f in scripts_dir.glob("*"):
            if f.suffix in [".py", ".sh"]:
                script_content = f.read_text()
                if "SCRIPT_PATH" not in script_content:
                    errors.append(f"Script missing SCRIPT_PATH resolution: {f.name}")

    if errors:
        print(f"\nValidation failed for skill at {skill_path}:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print(f"\nValidation successful for skill at {skill_path}")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_skill.py <skill-path>")
        sys.exit(1)
    
    success = validate_skill(sys.argv[1])
    sys.exit(0 if success else 1)
