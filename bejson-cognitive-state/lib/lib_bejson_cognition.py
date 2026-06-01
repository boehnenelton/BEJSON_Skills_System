"""
Library:      lib_bejson_cognition.py
Family:       Cognition
Jurisdiction: ["BEJSON_LIBRARIES", "PY"]
Status:       OFFICIAL
Author:       Elton Boehnen
Version:      2.2.0 OFFICIAL
            MFDB Version: 1.31
Format_Creator: Elton Boehnen
Date:         2026-05-31
Description:  High-resilience cognitive matrix and memory management.
IMPROVED:     Integrated Safe Atomic Writer with backoff and high-level 104db operations.
"""

import json
import os
import sys
import time
import random
import logging
from typing import Any, Dict, List, Optional

# --- Sibling Path Resolution ---
LIB_DIR = os.path.dirname(os.path.abspath(__file__))
if LIB_DIR not in sys.path: sys.path.insert(0, LIB_DIR)

CORE_DIR = os.path.join(os.path.dirname(LIB_DIR), "Core")
if CORE_DIR not in sys.path: sys.path.insert(0, CORE_DIR)

try:
    from lib_bejson_core import bejson_core_atomic_write, bejson_core_load_file, bejson_core_acquire_lock, bejson_core_release_lock
    from lib_mfdb_core import mfdb_core_resolve_path
    from lib_bejson_errors import *
except ImportError:
    pass

# ===========================================================================
# COGNITION ERROR CODES & SCHEMAS
# ===========================================================================
E_COGNITION_LOCK_TIMEOUT = 275

BEJSON_COGNITION_SCHEMA = [
    {"name": "Record_Type_Parent", "type": "string"},
    {"name": "id", "type": "string", "Record_Type_Parent": "AgentState"},
    {"name": "timestamp", "type": "number", "Record_Type_Parent": "AgentState"},
    {"name": "last_checkpoint", "type": "string", "Record_Type_Parent": "AgentState"},
    {"name": "core_directives", "type": "object", "Record_Type_Parent": "AgentState"},
    {"name": "summary_blob", "type": "string", "Record_Type_Parent": "AgentState"},
    {"name": "stack_id", "type": "string", "Record_Type_Parent": "ExecutionStack"},
    {"name": "agent_id_fk", "type": "string", "Record_Type_Parent": "ExecutionStack"},
    {"name": "stack_timestamp", "type": "number", "Record_Type_Parent": "ExecutionStack"},
    {"name": "task_queue", "type": "array", "Record_Type_Parent": "ExecutionStack"},
    {"name": "pending_context", "type": "object", "Record_Type_Parent": "ExecutionStack"},
    {"name": "log_id", "type": "string", "Record_Type_Parent": "EpisodicLog"},
    {"name": "log_timestamp", "type": "number", "Record_Type_Parent": "EpisodicLog"},
    {"name": "user_input", "type": "string", "Record_Type_Parent": "EpisodicLog"},
    {"name": "agent_response", "type": "string", "Record_Type_Parent": "EpisodicLog"},
    {"name": "payloads_used", "type": "array", "Record_Type_Parent": "EpisodicLog"}
]

def bejson_cognition_safe_write(filepath: str, data: dict, max_retries: int = 50) -> bool:
    """High-resilience atomic writer with randomized exponential backoff."""
    resolved_path = mfdb_core_resolve_path(filepath)
    attempt = 0
    base_sleep = 0.5
    while attempt < max_retries:
        if bejson_core_acquire_lock(resolved_path, timeout=5):
            try:
                return bejson_core_atomic_write(resolved_path, data)
            finally:
                bejson_core_release_lock(resolved_path)
        attempt += 1
        sleep_time = min(base_sleep * (2 ** attempt), 20) + random.uniform(0, 5)
        logging.warning(f"[COGNITION] Lock contention. Retrying in {sleep_time:.2f}s...")
        time.sleep(sleep_time)
    return False

def bejson_cognition_init_matrix(db_path: str) -> dict:
    resolved_path = mfdb_core_resolve_path(db_path)
    doc = bejson_core_load_file(resolved_path) if os.path.exists(resolved_path) else None
    if doc and doc.get("Format_Version") == "104db": return doc
    return {
        "Format": "BEJSON", "Format_Version": "104db", "Format_Creator": "Elton Boehnen",
        "Records_Type": ["AgentState", "ExecutionStack", "EpisodicLog"],
        "Fields": BEJSON_COGNITION_SCHEMA, "Values": []
    }

def bejson_cognition_query(doc: dict, record_type: str, filters: dict = None) -> List[dict]:
    results = []
    field_indices = {f["name"]: i for i, f in enumerate(doc["Fields"])}
    for row in doc.get("Values", []):
        if row[0] == record_type:
            record = {f["name"]: row[field_indices[f["name"]]] for f in doc["Fields"] if f.get("Record_Type_Parent") in [record_type, None]}
            if not filters or all(record.get(k) == v for k, v in filters.items()):
                results.append({k: v for k, v in record.items() if v is not None})
    return results

def bejson_cognition_upsert(doc: dict, record_type: str, record_id: str, **kwargs) -> dict:
    field_indices = {f["name"]: i for i, f in enumerate(doc["Fields"])}
    id_field = {"AgentState": "id", "ExecutionStack": "stack_id", "EpisodicLog": "log_id"}.get(record_type, "id")
    ts_field = {"AgentState": "timestamp", "ExecutionStack": "stack_timestamp", "EpisodicLog": "log_timestamp"}.get(record_type, "timestamp")

    target_idx = next((i for i, r in enumerate(doc["Values"]) if r[0] == record_type and r[field_indices[id_field]] == record_id), -1)
    
    row_data = list(doc["Values"][target_idx]) if target_idx != -1 else [None] * len(doc["Fields"])
    row_data[0] = record_type
    row_data[field_indices[id_field]] = record_id
    row_data[field_indices[ts_field]] = time.time()
    
    for key, val in kwargs.items():
        if key in field_indices: row_data[field_indices[key]] = val
    
    if target_idx != -1: doc["Values"][target_idx] = row_data
    else: doc["Values"].append(row_data)
    return doc
