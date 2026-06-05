"""
Library:      lib_bejson_agentic_deploy.py
Family:       Agentic
Jurisdiction: ["BEJSON_LIBRARIES", "PY"]
Status:       OFFICIAL
Author:       Elton Boehnen
Version:      1.0.0 OFFICIAL
            MFDB Version: 1.31
Format_Creator: Elton Boehnen
Date:         2026-05-31
Description:  Autonomous tool forging and sub-agent deployment.
"""

import os
import sys
import uuid
import stat
import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

# --- Sibling Path Resolution ---
LIB_DIR = os.path.dirname(os.path.abspath(__file__))
if LIB_DIR not in sys.path: sys.path.insert(0, LIB_DIR)

try:
    from lib_bejson_core import bejson_core_atomic_write, bejson_core_load_file
    from lib_mfdb_core import mfdb_core_resolve_path
    from lib_bejson_cognition import bejson_cognition_upsert
except ImportError:
    pass

def bejson_agentic_forge_tool(name: str, description: str, filename: str, code: str, version: str = "1.0.0") -> str:
    """Autonomously forges a physical terminal tool and registers it."""
    try:
        # 1. Forge the physical tool
        tools_dir = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/tools")
        os.makedirs(tools_dir, exist_ok=True)
        tool_path = os.path.join(tools_dir, os.path.basename(filename))
        
        with open(tool_path, "w") as f:
            f.write(code)
        
        # 2. Apply executable permissions (Non-interactive)
        st = os.stat(tool_path)
        os.chmod(tool_path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        
        # 3. Register in CLITool Registry
        registry_path = mfdb_core_resolve_path("{INTERNAL_STORAGE}/Admin/init/registry/mfdb_layers/data/clitool.bejson")
        registry_doc = bejson_core_load_file(registry_path)
        
        if registry_doc and "Values" in registry_doc:
            new_record = [
                name, uuid.uuid4().hex[:8], tool_path, version, description,
                True, "boehnenelton2024@gmail.com", "boehnenelton2024.pages.dev",
                f"guid-forge-{uuid.uuid4().hex[:8]}", datetime.now(timezone.utc).isoformat(), "forge-session"
            ]
            registry_doc["Values"].append(new_record)
            bejson_core_atomic_write(registry_path, registry_doc)
        
        return tool_path
    except Exception as e:
        logging.error(f"[FORGE_FAILED] {e}")
        return ""

def bejson_agentic_spawn_agent(matrix_doc: dict, agent_id: str, persona: str, task: str) -> dict:
    """Initializes a sub-agent's state and execution stack in the cognitive matrix."""
    # 1. Initialize AgentState
    matrix_doc = bejson_cognition_upsert(
        matrix_doc, "AgentState", agent_id,
        core_directives={"persona": persona, "status": "active"},
        summary_blob="Initialized by Orchestrator.",
        last_checkpoint=datetime.now(timezone.utc).isoformat()
    )
    
    # 2. Initialize ExecutionStack with task
    matrix_doc = bejson_cognition_upsert(
        matrix_doc, "ExecutionStack", f"STK-{agent_id}",
        agent_id_fk=agent_id,
        task_queue=[{"task_id": uuid.uuid4().hex[:4], "description": task, "status": "pending", "result": None}],
        pending_context={}
    )
    return matrix_doc
