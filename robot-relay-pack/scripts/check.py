#!/usr/bin/env python3
"""Verify packed output preserves all critical content from the original."""

import re
from collections import Counter
from pathlib import Path

_URL = re.compile(r"https?://[^\s)]+")
_FENCE_OPEN = re.compile(r"^(\s{0,3})(`{3,}|~{3,})(.*)$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)
_BULLET = re.compile(r"^\s*[-*+]\s+", re.MULTILINE)
_PATH = re.compile(
    r"(?:\./|\.\./|/|[A-Za-z]:\\)[\w\-/\\.]+|[\w\-\.]+[/\\][\w\-/\\.]+"
)


class Report:
    def __init__(self):
        self.ok = True
        self.errors = []
        self.warnings = []

    def error(self, msg):
        self.ok = False
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def _read(path: Path) -> str:
    return path.read_text(errors="ignore")


def _headings(text):
    return [(lvl, title.strip()) for lvl, title in _HEADING.findall(text)]


def _code_blocks(text):
    blocks = []
    lines = text.split("\n")
    i, n = 0, len(lines)
    while i < n:
        m = _FENCE_OPEN.match(lines[i])
        if not m:
            i += 1
            continue
        fence_char = m.group(2)[0]
        fence_len = len(m.group(2))
        block = [lines[i]]
        i += 1
        closed = False
        while i < n:
            cm = _FENCE_OPEN.match(lines[i])
            if (
                cm
                and cm.group(2)[0] == fence_char
                and len(cm.group(2)) >= fence_len
                and cm.group(3).strip() == ""
            ):
                block.append(lines[i])
                closed = True
                i += 1
                break
            block.append(lines[i])
            i += 1
        if closed:
            blocks.append("\n".join(block))
    return blocks


def _urls(text):
    return set(_URL.findall(text))


def _paths(text):
    return set(_PATH.findall(text))


def _bullet_count(text):
    return len(_BULLET.findall(text))


def _inline_codes(text):
    no_fences = re.sub(r"^```[\s\S]*?^```", "", text, flags=re.MULTILINE)
    no_fences = re.sub(r"^~~~[\s\S]*?^~~~", "", no_fences, flags=re.MULTILINE)
    return re.findall(r"`([^`]+)`", no_fences)


def _check_headings(orig, packed, r):
    h1 = _headings(orig)
    h2 = _headings(packed)
    if len(h1) != len(h2):
        r.error(f"Heading count mismatch: {len(h1)} → {len(h2)}")
    if h1 != h2:
        r.warn("Heading text or order changed")


def _check_code_blocks(orig, packed, r):
    if _code_blocks(orig) != _code_blocks(packed):
        r.error("Code blocks not preserved exactly")


def _check_urls(orig, packed, r):
    u1, u2 = _urls(orig), _urls(packed)
    if u1 != u2:
        r.error(f"URL mismatch: lost={u1 - u2}, gained={u2 - u1}")


def _check_paths(orig, packed, r):
    p1, p2 = _paths(orig), _paths(packed)
    if p1 != p2:
        r.warn(f"Path mismatch: lost={p1 - p2}, gained={p2 - p1}")


def _check_bullets(orig, packed, r):
    b1 = _bullet_count(orig)
    if b1 == 0:
        return
    b2 = _bullet_count(packed)
    if abs(b1 - b2) / b1 > 0.15:
        r.warn(f"Bullet count shifted too far: {b1} → {b2}")


def _check_inline_codes(orig, packed, r):
    c1 = Counter(_inline_codes(orig))
    c2 = Counter(_inline_codes(packed))
    if c1 == c2:
        return
    lost = set(c1) - set(c2)
    gained = set(c2) - set(c1)
    for code, count in c1.items():
        if code in c2 and c2[code] < count:
            lost.add(f"{code} (lost {count - c2[code]} of {count})")
    if lost:
        r.error(f"Inline code lost: {lost}")
    if gained:
        r.warn(f"Inline code gained: {gained}")


def verify(original_path: Path, packed_path: Path) -> Report:
    r = Report()
    orig = _read(original_path)
    packed = _read(packed_path)
    _check_headings(orig, packed, r)
    _check_code_blocks(orig, packed, r)
    _check_urls(orig, packed, r)
    _check_paths(orig, packed, r)
    _check_bullets(orig, packed, r)
    _check_inline_codes(orig, packed, r)
    return r


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        sys.exit(1)

    res = verify(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
    if res.errors:
        for e in res.errors:
            pass
    if res.warnings:
        for w in res.warnings:
            pass
