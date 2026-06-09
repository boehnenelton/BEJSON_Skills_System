#!/usr/bin/env python3
"""Classify a file as natural language (packable) or code/config (skip)."""

import json
import re
from pathlib import Path

PACKABLE_EXTENSIONS = {".md", ".txt", ".markdown", ".rst", ".typ", ".typst", ".tex"}

SKIP_EXTENSIONS = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".yaml", ".yml",
    ".toml", ".env", ".lock", ".css", ".scss", ".html", ".xml",
    ".sql", ".sh", ".bash", ".zsh", ".go", ".rs", ".java", ".c",
    ".cpp", ".h", ".hpp", ".rb", ".php", ".swift", ".kt", ".lua",
    ".dockerfile", ".makefile", ".csv", ".ini", ".cfg",
}

CONFIG_EXTENSIONS = {".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".env"}

_CODE_SIGNALS = [
    re.compile(r"^\s*(import |from .+ import |require\(|const |let |var )"),
    re.compile(r"^\s*(def |class |function |async function |export )"),
    re.compile(r"^\s*(if\s*\(|for\s*\(|while\s*\(|switch\s*\(|try\s*\{)"),
    re.compile(r"^\s*[\}\]\);]+\s*$"),
    re.compile(r"^\s*@\w+"),
    re.compile(r'^\\s*"[^"]+"\s*:\s*'),
    re.compile(r"^\s*\w+\s*=\s*[{\[\(\"']"),
]


def _looks_like_code(line: str) -> bool:
    return any(p.match(line) for p in _CODE_SIGNALS)


def _is_json(text: str) -> bool:
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, ValueError):
        return False


def _is_yaml(lines: list) -> bool:
    hits = 0
    for line in lines[:30]:
        s = line.strip()
        if s.startswith("---"):
            hits += 1
        elif re.match(r"^\w[\w\s]*:\s", s):
            hits += 1
        elif s.startswith("- ") and ":" in s:
            hits += 1
    non_empty = sum(1 for l in lines[:30] if l.strip())
    return non_empty > 0 and hits / non_empty > 0.6


def classify(filepath: Path) -> str:
    """Return 'natural_language', 'code', 'config', or 'unknown'."""
    ext = filepath.suffix.lower()

    if ext in PACKABLE_EXTENSIONS:
        return "natural_language"
    if ext in SKIP_EXTENSIONS:
        return "config" if ext in CONFIG_EXTENSIONS else "code"

    if not ext:
        try:
            text = filepath.read_text(errors="ignore")
        except (OSError, PermissionError):
            return "unknown"

        lines = text.splitlines()[:50]

        if _is_json(text[:10000]):
            return "config"
        if _is_yaml(lines):
            return "config"

        code_lines = sum(1 for l in lines if l.strip() and _looks_like_code(l))
        non_empty = sum(1 for l in lines if l.strip())
        if non_empty > 0 and code_lines / non_empty > 0.4:
            return "code"

        return "natural_language"

    return "unknown"


def is_packable(filepath: Path) -> bool:
    """Return True if the file is natural language and safe to pack."""
    if not filepath.is_file():
        return False
    if filepath.name.endswith(".source.md"):
        return False
    return classify(filepath) == "natural_language"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python classify.py <file> [file ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        p = Path(arg).resolve()
        kind = classify(p)
        packable = is_packable(p)
        print(f"  {p.name:30s}  type={kind:20s}  packable={packable}")
