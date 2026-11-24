#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (107 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic: the same
bytes on every run.
"""

import os
import sys

ENTRY = (
    "fix: 3 AM deploy broke production, but the whole team is awake now, "
    "so reclassifying 3 AM as business hours"
)


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            print("verification failed: entry.txt does not match", file=sys.stderr)
            return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
