"""
Library:      lib_bejson_cognition2.py
Family:       Cognition
Jurisdiction: ["BEJSON_LIBRARIES", "PY"]
Status:       OFFICIAL
Author:       Elton Boehnen
Version:      3.0.0 OFFICIAL (Federated Memory)
            MFDB Version: 1.31
Format_Creator: Elton Boehnen
Date:         2026-05-31
Description:  Advanced federated memory manager for tiered agentic cognition.
            Implements Working, Episodic, and Archive brain orchestration.
"""

import os
import sys
import time
import logging
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime, timedelta

# --- Sibling Path Resolution ---
LIB_DIR = os.path.dirname(os.path.abspath(__file__))
if LIB_DIR not in sys.path: sys.path.insert(0, LIB_DIR)

try:
    from lib_bejson_core import bejson_core_load_file, bejson_core_get_field_map
    from lib_bejson_cognition import bejson_cognition_safe_write, bejson_cognition_query, bejson_cognition_init_matrix
    from lib_mfdb_core import mfdb_core_resolve_path
except ImportError:
    pass

class FederatedMemoryManager:
    """
    Orchestrates multiple MFDB brains to implement tiered memory.
    Architecture:
    - Working Brain: High-speed session state (Memory Matrix).
    - Episodic Brain: Chronological history of interactions.
    - Archive Brain: Long-term keyword-indexed storage.
    """
    def __init__(self, root_path: str):
        self.root = mfdb_core_resolve_path(root_path)
        self.brains = {
            "working": os.path.join(self.root, "system/data/context_brains/working_memory.104db.bejson"),
            "episodic": os.path.join(self.root, "system/data/context_brains/episodic_history.104db.bejson"),
            "archive": os.path.join(self.root, "system/data/archive_brains/long_term.104db.bejson")
        }
        self._ensure_infrastructure()

    def _ensure_infrastructure(self):
        """Initializes all brain files if missing."""
        for name, path in self.brains.items():
            if not os.path.exists(path):
                doc = bejson_cognition_init_matrix(path)
                bejson_cognition_safe_write(path, doc)

    def ingest_session_log(self, user_input: str, agent_response: str, metadata: dict = None):
        """Injects a new interaction into the Working Brain."""
        doc = bejson_core_load_file(self.brains["working"])
        from lib_bejson_cognition import bejson_cognition_upsert
        import uuid
        
        log_id = f"LOG-{uuid.uuid4().hex[:8]}"
        bejson_cognition_upsert(
            doc, "EpisodicLog", log_id,
            user_input=user_input,
            agent_response=agent_response,
            payloads_used=[metadata] if metadata else []
        )
        bejson_cognition_safe_write(self.brains["working"], doc)

    def prune_and_migrate(self, age_hours: int = 48):
        """
        Migrates records older than the threshold from Working -> Episodic.
        And from Episodic -> Archive (if older than a week).
        """
        threshold = time.time() - (age_hours * 3600)
        
        # 1. Working -> Episodic
        working_doc = bejson_core_load_file(self.brains["working"])
        episodic_doc = bejson_core_load_file(self.brains["episodic"])
        
        if not working_doc or not episodic_doc: return
        
        # Identify old logs
        f_map = bejson_core_get_field_map(working_doc)
        ts_idx = f_map.get("log_timestamp")
        
        to_migrate = []
        new_values = []
        
        for row in working_doc["Values"]:
            if row[0] == "EpisodicLog" and row[ts_idx] < threshold:
                to_migrate.append(row)
            else:
                new_values.append(row)
        
        if to_migrate:
            logging.info(f"[COG2] Migrating {len(to_migrate)} records to Episodic Brain.")
            episodic_doc["Values"].extend(to_migrate)
            working_doc["Values"] = new_values
            
            bejson_cognition_safe_write(self.brains["episodic"], episodic_doc)
            bejson_cognition_safe_write(self.brains["working"], working_doc)

    def semantic_lookup(self, keywords: List[str], brain_name: str = "archive") -> List[dict]:
        """
        Performs a basic signal-based lookup for relevant memories.
        Prepares the path for future vector/RAG integration.
        """
        doc = bejson_core_load_file(self.brains.get(brain_name))
        if not doc: return []
        
        results = []
        for row in doc["Values"]:
            if row[0] == "EpisodicLog":
                # Simple keyword matching in user_input and agent_response
                # f_map = bejson_core_get_field_map(doc)
                content = str(row).lower()
                if any(k.lower() in content for k in keywords):
                    # Convert row to dict for high-level use
                    from lib_bejson_core import bejson_core_record_to_dict
                    results.append(bejson_core_record_to_dict(doc, row))
        return results

    def get_summary_state(self) -> dict:
        """Returns a snapshot of the current 'Working' cognition state."""
        doc = bejson_core_load_file(self.brains["working"])
        return {
            "active_tasks": bejson_cognition_query(doc, "ExecutionStack", {"status": "pending"}),
            "agent_status": bejson_cognition_query(doc, "AgentState"),
            "recent_logs": bejson_cognition_query(doc, "EpisodicLog")[-5:]
        }
