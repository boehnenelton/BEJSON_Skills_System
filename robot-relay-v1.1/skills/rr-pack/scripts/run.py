#!/usr/bin/env python3
"""
Robot Relay Pack CLI

Usage:
    python3 -m scripts <filepath>
"""

import sys

for _s in (sys.stdout, sys.stderr):
    _reconf = getattr(_s, "reconfigure", None)
    if callable(_reconf):
        try:
            _reconf(encoding="utf-8", errors="replace")
        except Exception:
            pass

from pathlib import Path

from .pack import pack_file
from .classify import classify, is_packable


def _usage():
    print("Usage: python3 -m scripts <filepath>")


def main():
    if len(sys.argv) != 2:
        _usage()
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"🔴 ··· BEEEEEP ··· NOT FOUND: {filepath}")
        sys.exit(1)

    if not filepath.is_file():
        print(f"🔴 ··· BEEEEEP ··· NOT A FILE: {filepath}")
        sys.exit(1)

    filepath = filepath.resolve()

    kind = classify(filepath)
    print(f"🟢 · bip · CLASSIFY: {kind}")

    if not is_packable(filepath):
        print("🟢 · bip · SKIP: not natural language — no pack performed")
        sys.exit(0)

    print("🟢 · bip · PACK: starting robot-relay compression...\n")

    try:
        ok = pack_file(filepath)

        if ok:
            backup = filepath.with_name(filepath.stem + ".source.md")
            print(f"\n🟢 ·· bip bip ·· OK: pack complete")
            print(f"   OUT: {filepath}")
            print(f"   SRC: {backup}")
            sys.exit(0)
        else:
            print("\n🔴 ··· BEEEEEP ··· FAIL: pack failed after retries — original untouched")
            sys.exit(2)

    except KeyboardInterrupt:
        print("\n🔴 · BEEP · ABORT: interrupted by user")
        sys.exit(130)

    except Exception as e:
        print(f"\n🔴 ··· BEEEEEP ··· ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
