import os
import sys
import json
import re
import argparse
from pathlib import Path

# --- BOOTSTRAP ---
SCRIPT_PATH = Path(__file__).resolve().parent

# --- ROBOT RELAY SIGNALS ---
BEEP_1 = "· bip ·"
BEEP_2 = "·· bip bip ··"
ALARM_1 = "· BEEP ·"
ALARM_2 = "·· BEEP BEEP ··"
ALARM_3 = "··· BEEEEEP ···"

# --- COLORS ---
G, R, Y, B, C = "\033[92m", "\033[91m", "\033[93m", "\033[94m", "\033[0m"

class GcliTokenizedDebuggerPro:
    def __init__(self, target_path, mode="scan", seed=None, grade=2):
        self.target = Path(target_path)
        self.mode = mode
        self.seed = seed
        self.grade = grade
        self.report_file = Path(".tokenized_debug_report")
        self.trace_file = Path(".tokenized_trace_map")
        self.plugins = []
        self.load_plugins()

    def load_plugins(self):
        schema_path = SCRIPT_PATH / "schemas" / "plugin_schema.104a.bejson"
        if not schema_path.exists(): return
        try:
            with open(schema_path, "r") as f:
                data = json.load(f)
            fields = [f["name"] for f in data["Fields"]]
            for val in data["Values"]:
                self.plugins.append(dict(zip(fields, val)))
        except: pass

    def run_check(self, plugin, file_path):
        content = file_path.read_text(errors="ignore")
        lines = content.splitlines()
        logic = plugin["logic"]
        check_type = plugin["check_type"]
        plugin_id = plugin["plugin_id"]
        
        found_lines = []
        try:
            if plugin_id in ("json_valid", "bejson_valid"):
                json.loads(content)
                return True, []
            
            if check_type == "python":
                compile(content, str(file_path), "exec")
                return True, []
            
            elif check_type == "regex":
                for i, line in enumerate(lines, 1):
                    if re.search(logic, line):
                        found_lines.append(i)
                return (not found_lines, found_lines)
        except Exception as e:
            match = re.search(r"line (\d+)", str(e))
            return False, [match.group(1) if match else "??"]
        return True, []

    def trace(self, files):
        if not self.seed: return
        results = []
        for f in files:
            matches = [i for i, l in enumerate(f.read_text(errors="ignore").splitlines(), 1) if self.seed in l]
            if matches:
                results.append(f"{f.name} >> L{matches}")
        if results:
            self.trace_file.write_text("\n".join(results))
            if self.grade > 1:
                print(f"{B}[TRACE] {self.seed} found. Map -> {self.trace_file}{C}")

    def scan(self):
        files = list(self.target.rglob("*")) if self.target.is_dir() else [self.target]
        files = [f for f in files if f.is_file() and not any(x in str(f) for x in (".git", "__pycache__", "node_modules"))]
        
        if self.mode == "trace":
            self.trace(files)
            return

        results, detailed_log = [], {}

        for p in self.plugins:
            pattern = p["target_glob"]
            plugin_files = [f for f in files if any(f.match(pat.strip()) for pat in pattern.split(","))]
            
            for f in plugin_files:
                ok, err_lines = self.run_check(p, f)
                symbol = p["success_msg"] if ok else p["failure_msg"]
                
                # Signal Grading
                if not ok:
                    results.append(f"{R}{symbol}{C}")
                    if f not in detailed_log: detailed_log[f] = []
                    # RR Format: L<N>: <signal> <fault>. <fix>.
                    sig = ALARM_2 if symbol in ("N", "SEC!", "C!", "B-") else ALARM_1
                    detailed_log[f].append(f"L{err_lines}: {sig} {p['plugin_name']} fail.")
                else:
                    results.append(f"{G}{symbol}{C}")

        # Final Payload Output
        if self.grade == 3:
            # Aggressive density: only output symbols, no text.
            print(" ".join(results[:100]))
        else:
            print(" ".join(results[:50]) + (" ..." if len(results) > 50 else ""))

        if detailed_log:
            report_lines = []
            for f, errs in detailed_log.items():
                rel_path = f.relative_to(self.target.parent) if self.target.is_dir() else f.name
                report_lines.append(f"{rel_path} >> {' | '.join(errs)}")
            
            self.report_file.write_text("\n".join(report_lines))
            if self.grade < 3:
                print(f"{Y}{ALARM_3} Forensic Map -> {self.report_file}{C}")
        elif self.report_file.exists():
            self.report_file.unlink()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--mode", choices=["scan", "trace"], default="scan")
    parser.add_argument("--seed")
    parser.add_argument("--grade", type=int, default=2)
    args = parser.parse_args()

    debugger = GcliTokenizedDebuggerPro(args.path, mode=args.mode, seed=args.seed, grade=args.grade)
    debugger.scan()

if __name__ == "__main__":
    main()
