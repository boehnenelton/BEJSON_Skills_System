#!/usr/bin/env python3
"""
Script:       export_report.py
Description:  Standardized exporter for Post-Analysis Reports.
Version:      1.0.0
Author:       Elton Boehnen
Relational ID: par-exporter-001
"""

import sys
import os
from datetime import datetime
from pathlib import Path

def get_script_path() -> Path:
    return Path(__file__).resolve().parent

def export_report(subject, content, target_dir="."):
    timestamp = datetime.now().strftime("%Y_%m_%d")
    clean_subject = subject.lower().replace(" ", "_")
    filename = f"analysis_report_{clean_subject}_{timestamp}.md"
    
    target_path = Path(target_dir) / filename
    
    try:
        target_path.write_text(content, encoding="utf-8")
        print(f"Successfully exported report to: {target_path}")
        return str(target_path)
    except Exception as e:
        print(f"Error exporting report: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: export_report.py <subject> <content_file_or_string> [target_dir]")
        sys.exit(1)
    
    subj = sys.argv[1]
    input_val = sys.argv[2]
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "."
    
    if os.path.exists(input_val):
        content_text = Path(input_val).read_text(encoding="utf-8")
    else:
        content_text = input_val
        
    export_report(subj, content_text, out_dir)
