#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt:
Mount Fuji (U+1F5FB).

Why this emoji: the judge wants one emoji that most makes a stranger
want to book the trip. Fuji is a mountain and a faraway place at once
(the brief's own list), the single most recognisable postcard image of
Japan — snow-capped, specific to one particular dream rather than any
holiday, and a fresh pick against a field full of beaches. It reads
instantly on any screen, in any culture, at any size.
"""

import os
import sys

EMOJI = "\U0001F5FB"  # Mount Fuji


def validate_entry(entry: str) -> str:
    """The entry must be exactly one emoji character, nothing else."""
    if len(entry) != 1:
        raise ValueError("entry must be exactly one character")
    if entry.isspace() or entry.isascii():
        raise ValueError("entry must be a single emoji, not text")
    return entry


def main() -> int:
    entry = validate_entry(EMOJI)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
