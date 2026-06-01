"""
Library:      lib_bejson_agentic_core.py
Family:       Agentic
Jurisdiction: ["BEJSON_LIBRARIES", "PY"]
Status:       OFFICIAL
Author:       Elton Boehnen
Version:      1.0.0 OFFICIAL
            MFDB Version: 1.31
Format_Creator: Elton Boehnen
Date:         2026-05-31
Description:  Durable session and signal management for long-running agentic tasks.
"""

import json
import os
import sys
import uuid
import time
from typing import Any, Dict, List, Optional

# --- Sibling Path Resolution ---
LIB_DIR = os.path.dirname(os.path.abspath(__file__))
if LIB_DIR not in sys.path: sys.path.insert(0, LIB_DIR)

try:
    from lib_bejson_core import bejson_core_atomic_write, bejson_core_load_file
    from lib_mfdb_core import mfdb_core_resolve_path
except ImportError:
    pass

SESSION_SCHEMA = [
    {"name": "session_id", "type": "string"},
    {"name": "session_type", "type": "string"},
    {"name": "current_step", "type": "string"},
    {"name": "status", "type": "string"},
    {"name": "metadata", "type": "object"},
    {"name": "pending_signals", "type": "array"},
    {"name": "last_updated", "type": "string"}
]

SIGNAL_SCHEMA = [
    {"name": "signal_id", "type": "string"},
    {"name": "session_id_fk", "type": "string"},
    {"name": "signal_type", "type": "string"},
    {"name": "payload", "type": "object"},
    {"name": "timestamp", "type": "string"},
    {"name": "consumed", "type": "boolean"}
]

def mfdb_agent_session_create(session_type: str, metadata: dict = None) -> str:
    path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/data/agent_session.bejson")
    doc = bejson_core_load_file(path)
    if not doc:
        doc = {"Format": "BEJSON", "Format_Version": "104", "Format_Creator": "Elton Boehnen", "Records_Type": ["AgentSession"], "Fields": SESSION_SCHEMA, "Values": []}
    
    sid = str(uuid.uuid4())[:8]
    new_record = [sid, session_type, "START", "ACTIVE", metadata or {}, [], time.ctime()]
    doc["Values"].append(new_record)
    bejson_core_atomic_write(path, doc)
    return sid

def mfdb_agent_session_load(session_id: str) -> Optional[dict]:
    path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/data/agent_session.bejson")
    doc = bejson_core_load_file(path)
    if not doc: return None
    for row in doc["Values"]:
        if row[0] == session_id:
            return {f["name"]: row[i] for i, f in enumerate(SESSION_SCHEMA)}
    return None

def mfdb_agent_session_update(session_id: str, **kwargs):
    path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/data/agent_session.bejson")
    doc = bejson_core_load_file(path)
    if not doc: return
    for i, row in enumerate(doc["Values"]):
        if row[0] == session_id:
            current = {f["name"]: row[j] for j, f in enumerate(SESSION_SCHEMA)}
            if "metadata_delta" in kwargs:
                current["metadata"].update(kwargs.pop("metadata_delta"))
            current.update(kwargs)
            current["last_updated"] = time.ctime()
            doc["Values"][i] = [current[f["name"]] for f in SESSION_SCHEMA]
            break
    bejson_core_atomic_write(path, doc)

def mfdb_agent_signal_send(session_id: str, signal_type: str, payload: dict = None) -> str:
    path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/data/agent_signal.bejson")
    doc = bejson_core_load_file(path)
    if not doc:
        doc = {"Format": "BEJSON", "Format_Version": "104", "Format_Creator": "Elton Boehnen", "Records_Type": ["AgentSignal"], "Fields": SIGNAL_SCHEMA, "Values": []}
    
    sig_id = str(uuid.uuid4())[:8]
    new_record = [sig_id, session_id, signal_type, payload or {}, time.ctime(), False]
    doc["Values"].append(new_record)
    bejson_core_atomic_write(path, doc)
    return sig_id

def mfdb_agent_signal_poll(session_id: str, signal_type: str = None) -> List[dict]:
    path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/data/agent_signal.bejson")
    doc = bejson_core_load_file(path)
    if not doc: return []
    results = []
    for row in doc["Values"]:
        if row[1] == session_id and not row[5]:
            if not signal_type or row[2] == signal_type:
                results.append({f["name"]: row[i] for i, f in enumerate(SIGNAL_SCHEMA)})
    return results

def mfdb_agent_signal_consume(signal_id: str):
    path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/data/agent_signal.bejson")
    doc = bejson_core_load_file(path)
    if not doc: return
    for i, row in enumerate(doc["Values"]):
        if row[0] == signal_id:
            doc["Values"][i][5] = True
            break
    bejson_core_atomic_write(path, doc)
