#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3 standard library only; fully deterministic.
"""

import os

# Revised: the machine speaks directly, in its own world — exact change,
# the B4 button, the glass, the coil drop — and the punch lands on the
# last words. Charming, not creepy: it has been waiting, not watching.
LINE = "You don't need exact change — just press B4. I've been saving my best snack behind this glass all day, waiting for someone worth dropping for."


def main():
    line = LINE.strip()
    assert line, "line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
