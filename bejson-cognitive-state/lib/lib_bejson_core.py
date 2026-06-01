"""
Library:      lib_bejson_core.py
Family:       Core
Jurisdiction: ["BEJSON_LIBRARIES", "PY"]
Status:       OFFICIAL
Author:       Elton Boehnen
Version:      2.0.1 OFFICIAL
            MFDB Version: 1.31
Format_Creator: Elton Boehnen
Date:         2026-05-21
Description:  Low-level atomic operations and data structure management.
REMEDIATED:   Implemented stale-lock override mechanism.
"""

import json
import os
import sys
import time
import shutil
import tempfile
import logging
from typing import Any, Dict, List, Optional, Union

def bejson_core_load_file(path: str) -> Optional[dict]:
    """Loads a BEJSON file from disk."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"[BEJSON_CORE] Failed to load {path}: {e}")
        return None

def bejson_core_atomic_write(path: str, data: dict) -> bool:
    """Writes a BEJSON file atomically using a temp file and sync."""
    target_dir = os.path.dirname(os.path.abspath(path))
    os.makedirs(target_dir, exist_ok=True)
    
    fd, tmp_path = tempfile.mkstemp(dir=target_dir, suffix=".tmp")
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, path)
        return True
    except Exception as e:
        logging.error(f"[BEJSON_CORE] Atomic write failed for {path}: {e}")
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        return False

def bejson_core_acquire_lock(file_path: str, timeout: int = 10, stale_age: int = 60) -> bool:
    """
    Acquire a lock file for the given file_path.
    REMEDIATED: Added stale-lock override based on file age.
    """
    lock_path = file_path + ".lock"
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            # Check for stale lock
            if os.path.exists(lock_path):
                mtime = os.path.getmtime(lock_path)
                if (time.time() - mtime) > stale_age:
                    logging.warning(f"[BEJSON_CORE] Overriding stale lock: {lock_path} (Age: {int(time.time() - mtime)}s)")
                    os.unlink(lock_path)
            
            # Use O_EXCL to ensure atomic creation
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            with os.fdopen(fd, "w") as f:
                f.write(str(os.getpid()))
            return True
        except FileExistsError:
            time.sleep(0.1)
        except Exception as e:
            logging.error(f"[BEJSON_CORE] Lock acquisition error: {e}")
            time.sleep(0.1)
            
    return False

def bejson_core_release_lock(file_path: str) -> None:
    """Release the lock file for the given file_path."""
    lock_path = file_path + ".lock"
    if os.path.exists(lock_path):
        try:
            os.unlink(lock_path)
        except:
            pass

# Global Field Map Cache
# Key: tuple of field names (sorted or as-is)
# Value: dict of {name: index}
_FIELD_MAP_CACHE: Dict[tuple, Dict[str, int]] = {}

def bejson_core_get_field_map(doc: dict) -> Dict[str, int]:
    """
    Returns a mapping of field name to index.
    Utilizes a global cache for performance.
    """
    fields = doc.get("Fields", [])
    if not fields:
        return {}
    
    # Create a unique key for this field structure
    # Including version ensures we don't collide if different versions use same names differently (unlikely but safe)
    field_names = tuple(f["name"] for f in fields)
    cache_key = (doc.get("Format_Version"), field_names)
    
    if cache_key in _FIELD_MAP_CACHE:
        return _FIELD_MAP_CACHE[cache_key]
    
    # Build and cache
    field_map = {f["name"]: i for i, f in enumerate(fields)}
    _FIELD_MAP_CACHE[cache_key] = field_map
    return field_map

def bejson_core_get_field_index(doc: dict, field_name: str) -> int:
    """Returns the positional index of a field name using the cache."""
    field_map = bejson_core_get_field_map(doc)
    return field_map.get(field_name, -1)

def bejson_core_get_value(doc: dict, record: list, field_name: str) -> Any:
    """
    Retrieves a value from a record by field name.
    Implements key-based lookup while maintaining positional integrity.
    """
    idx = bejson_core_get_field_index(doc, field_name)
    if idx == -1:
        return None
    try:
        return record[idx]
    except IndexError:
        return None

def bejson_core_record_to_dict(doc: dict, record: list) -> Dict[str, Any]:
    """
    Converts a positional record into a key-value dictionary.
    Useful for high-level application logic.
    """
    field_map = bejson_core_get_field_map(doc)
    return {name: record[i] for name, i in field_map.items() if i < len(record)}

def bejson_core_create_104(record_type: str, fields: list, values: list) -> dict:
    return {
        "Format": "BEJSON",
        "Format_Version": "104",
        "Format_Creator": "Elton Boehnen",
        "Records_Type": [record_type],
        "Fields": fields,
        "Values": values
    }

def bejson_core_create_104a(record_type: str, fields: list, values: list, **custom) -> dict:
    doc = {
        "Format": "BEJSON",
        "Format_Version": "104a",
        "Format_Creator": "Elton Boehnen",
        "Records_Type": [record_type],
        "Fields": fields,
        "Values": values
    }
    doc.update(custom)
    return doc

def bejson_core_create_104db(record_types: list, fields: list, values: list) -> dict:
    return {
        "Format": "BEJSON",
        "Format_Version": "104db",
        "Format_Creator": "Elton Boehnen",
        "Records_Type": record_types,
        "Fields": fields,
        "Values": values
    }
