import os
import sys
import shutil
import uuid
from pathlib import Path

def get_script_path() -> Path:
    return Path(__file__).resolve().parent

SCRIPT_PATH = get_script_path()

def init_skill(skill_name: str):
    if not skill_name:
        print("Error: Skill name is required.")
        sys.exit(1)

    # Sanitize name
    skill_name = skill_name.lower().replace(" ", "-")
    
    # Define paths
    target_dir = Path.cwd() / skill_name
    scripts_dir = target_dir / "scripts"
    assets_dir = target_dir / "assets"
    refs_dir = target_dir / "references"
    
    # Create structure
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        scripts_dir.mkdir(exist_ok=True)
        assets_dir.mkdir(exist_ok=True)
        refs_dir.mkdir(exist_ok=True)
        print(f"Created structure for skill: {skill_name}")
    except Exception as e:
        print(f"Error creating structure: {e}")
        sys.exit(1)

    # Copy template
    template_path = SCRIPT_PATH.parent / "assets" / "skill_template.md"
    target_skill_md = target_dir / "SKILL.md"
    
    if template_path.exists():
        content = template_path.read_text()
        # Basic replacement
        content = content.replace("{{skill-name}}", skill_name)
        content = content.replace("{{Skill Name}}", skill_name.replace("-", " ").title())
        content = content.replace("{{unique-uuid}}", str(uuid.uuid4()))
        
        target_skill_md.write_text(content)
        print(f"Generated SKILL.md from template.")
    else:
        print(f"Warning: Template not found at {template_path}. Creating empty SKILL.md.")
        target_skill_md.touch()

    print(f"Initialization of {skill_name} complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 init_skill.py <skill-name>")
        sys.exit(1)
    
    init_skill(sys.argv[1])
