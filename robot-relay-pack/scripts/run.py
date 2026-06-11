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
    pass


def main():
    if len(sys.argv) != 2:
        _usage()
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        sys.exit(1)

    if not filepath.is_file():
        sys.exit(1)

    filepath = filepath.resolve()

    kind = classify(filepath)

    if not is_packable(filepath):
        sys.exit(0)


    try:
        ok = pack_file(filepath)

        if ok:
            pass
            backup = filepath.with_name(filepath.stem + ".source.md")
            sys.exit(0)
        else:
            sys.exit(2)

    except KeyboardInterrupt:
        sys.exit(130)

    except Exception as e:
        sys.exit(1)


if __name__ == "__main__":
    pass
    main()
