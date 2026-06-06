import os
import sys
import shutil
import subprocess
from pathlib import Path

def get_script_path() -> Path:
    return Path(__file__).resolve().parent

SCRIPT_PATH = get_script_path()

def package_skill(skill_path: str):
    path = Path(skill_path).resolve()
    skill_name = path.name
    
    # 1. Validate
    print(f"Validating skill: {skill_name}...")
    val_script = SCRIPT_PATH / "validate_skill.py"
    try:
        subprocess.run([sys.executable, str(val_script), str(path)], check=True)
    except subprocess.CalledProcessError:
        print("Packaging aborted due to validation failure.")
        return False

    # 2. Zip
    build_dir = Path.home() / "build" / "skill_system"
    build_dir.mkdir(parents=True, exist_ok=True)
    
    zip_path = build_dir / f"{skill_name}.zip"
    print(f"Packaging {skill_name} into {zip_path}...")
    
    try:
        # Create a temporary zip in the current directory and then move it to build_dir
        # to adhere to atomic write principles (same filesystem move)
        temp_zip = Path.cwd() / f"{skill_name}.zip.tmp"
        
        # We use shutil.make_archive but it adds .zip suffix automatically
        archive_base = str(temp_zip).replace(".zip.tmp", "")
        shutil.make_archive(archive_base, 'zip', root_dir=path.parent, base_dir=skill_name)
        
        actual_temp_zip = Path(str(temp_zip).replace(".tmp", ""))
        os.replace(actual_temp_zip, zip_path)
        print(f"Successfully packaged and synchronized to {zip_path}")
        return True
    except Exception as e:
        print(f"Error during packaging: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 package_skill.py <skill-path>")
        sys.exit(1)
    
    success = package_skill(sys.argv[1])
    sys.exit(0 if success else 1)
