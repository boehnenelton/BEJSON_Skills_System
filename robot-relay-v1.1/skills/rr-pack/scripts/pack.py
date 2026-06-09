#!/usr/bin/env python3
"""Robot Relay Pack orchestrator — drives model calls, backup, and validation loop."""

import os
import re
import subprocess
from pathlib import Path
from typing import List

from .classify import is_packable
from .check import verify

MAX_RETRIES = 2

_OUTER_FENCE = re.compile(
    r"\A\s*(`{3,}|~{3,})[^\n]*\n(.*)\n\1\s*\Z", re.DOTALL
)

_SENSITIVE_NAME = re.compile(
    r"(?ix)^("
    r"\.env(\..+)?"
    r"|\.netrc"
    r"|credentials(\..+)?"
    r"|secrets?(\..+)?"
    r"|passwords?(\..+)?"
    r"|id_(rsa|dsa|ecdsa|ed25519)(\.pub)?"
    r"|authorized_keys"
    r"|known_hosts"
    r"|.*\.(pem|key|p12|pfx|crt|cer|jks|keystore|asc|gpg)"
    r")$"
)

_SENSITIVE_DIRS = frozenset({".ssh", ".aws", ".gnupg", ".kube", ".docker"})

_SENSITIVE_TOKENS = (
    "secret", "credential", "password", "passwd",
    "apikey", "accesskey", "token", "privatekey",
)


def _is_sensitive(filepath: Path) -> bool:
    if _SENSITIVE_NAME.match(filepath.name):
        return True
    if {p.lower() for p in filepath.parts} & _SENSITIVE_DIRS:
        return True
    normalized = re.sub(r"[_\-\s.]", "", filepath.name.lower())
    return any(t in normalized for t in _SENSITIVE_TOKENS)


def _strip_outer_fence(text: str) -> str:
    m = _OUTER_FENCE.match(text)
    return m.group(2) if m else text


def _call_model(prompt: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if api_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(
                model=os.environ.get("RR_MODEL", "claude-sonnet-4-5"),
                max_tokens=8192,
                messages=[{"role": "user", "content": prompt}],
            )
            return _strip_outer_fence(msg.content[0].text.strip())
        except ImportError:
            pass
    try:
        result = subprocess.run(
            ["claude", "--print"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True,
        )
        return _strip_outer_fence(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Model call failed:\n{e.stderr}")


def _pack_prompt(original: str) -> str:
    return f"""Rewrite this markdown into robot-relay shorthand.

STRICT RULES:
- Do NOT modify anything inside ``` code blocks
- Do NOT modify anything inside inline backticks
- Preserve ALL URLs exactly
- Preserve ALL headings exactly
- Preserve all file paths and commands
- Return ONLY the packed markdown body — no outer ``` fence around the whole output

Only compress natural language prose. All technical content is read-only.

TEXT:
{original}
"""


def _fix_prompt(original: str, packed: str, errors: List[str]) -> str:
    err_list = "\n".join(f"- {e}" for e in errors)
    return f"""Fix the listed validation errors in this robot-relay-packed markdown file.

RULES:
- Do NOT repack or rephrase anything
- ONLY fix the listed errors — leave everything else exactly as-is
- Use ORIGINAL as reference to restore missing content
- Preserve robot-relay shorthand in all untouched sections

ERRORS:
{err_list}

HOW TO FIX:
- Missing URL: find in ORIGINAL, restore exact position in PACKED
- Code block mismatch: restore exact block from ORIGINAL
- Heading mismatch: restore exact heading text from ORIGINAL

ORIGINAL (reference only):
{original}

PACKED (fix this):
{packed}

Return ONLY the fixed file. No explanation.
"""


def pack_file(filepath: Path) -> bool:
    filepath = filepath.resolve()
    MAX_SIZE = 500_000

    if not filepath.exists():
        raise FileNotFoundError(f"Not found: {filepath}")
    if filepath.stat().st_size > MAX_SIZE:
        raise ValueError(f"File too large (max 500KB): {filepath}")
    if _is_sensitive(filepath):
        raise ValueError(
            f"🔴 ··· BEEEEEP ··· REFUSED: {filepath.name} matches sensitive file pattern. "
            "Packing sends content to a third-party API. Rename if false positive."
        )

    print(f"🟢 · bip · TARGET: {filepath}")

    if not is_packable(filepath):
        print("🟢 · bip · SKIP: not natural language")
        return False

    original = filepath.read_text(errors="ignore")
    backup = filepath.with_name(filepath.stem + ".source.md")

    if not original.strip():
        print("🔴 · BEEP · ERR: file empty — nothing to pack")
        return False

    if backup.exists():
        print(f"🔴 ·· BEEP BEEP ·· ABORT: backup already exists at {backup}")
        print("   Remove or rename backup first to prevent data loss")
        return False

    print("🟢 · bip · MODEL: packing...")
    packed = _call_model(_pack_prompt(original))

    if not packed or not packed.strip():
        print("🔴 ·· BEEP BEEP ·· ERR: model returned empty output — original untouched")
        return False

    if packed.strip() == original.strip():
        print("🔴 · BEEP · ERR: output identical to input — no effect, original untouched")
        return False

    backup.write_text(original)
    if backup.read_text(errors="ignore") != original:
        print(f"🔴 ··· BEEEEEP ··· ABORT: backup write verification failed — filesystem mismatch")
        try:
            backup.unlink()
        except OSError:
            pass
        return False

    filepath.write_text(packed)

    for attempt in range(MAX_RETRIES):
        print(f"🟢 · bip · CHECK: attempt {attempt + 1}")
        result = verify(backup, filepath)

        if result.ok:
            print("🟢 ·· bip bip ·· PASS: validation clear")
            break

        print("🔴 · BEEP · FAIL: validation errors:")
        for e in result.errors:
            print(f"   {e}")

        if attempt == MAX_RETRIES - 1:
            filepath.write_text(original)
            backup.unlink(missing_ok=True)
            print("🔴 ··· BEEEEEP ··· ABORT: max retries reached — original restored")
            return False

        print("🔴 · BEEP · FIX: patching errors...")
        packed = _call_model(_fix_prompt(original, packed, result.errors))
        filepath.write_text(packed)

    return True
