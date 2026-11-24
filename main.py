#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt:
Mount Fuji (U+1F5FB).

Why Mount Fuji, and why this exact emoji
-----------------------------------------
The brief asks for the single emoji that most makes a stranger want to
book the trip. Fuji wins that test for four reasons:

1. It is two of the brief's own categories at once — a mountain *and* a
   faraway place — so one glyph carries the whole dream instead of
   needing a second one.
2. It is the single most recognisable postcard image of Japan:
   snow-capped, specific to one particular dream trip rather than any
   generic holiday. A beach could be anywhere; Fuji can only be Japan.
3. It is a fresh pick against a field full of beaches, palm trees and
   cocktails, so it stands out on a crowded leaderboard.
4. It reads instantly on any screen, in any culture, at any size —
   no caption, no context and no translation needed.

The emoji is fixed as a code point, not typed as a picture, so the
bytes written are identical on every machine and every run.
"""

import os
import sys

# Mount Fuji, U+1F5FB — one Unicode scalar value, 4 bytes in UTF-8.
EMOJI_CODEPOINT = 0x1F5FB
EMOJI = chr(EMOJI_CODEPOINT)


def validate_entry(entry: str) -> str:
    """The entry must be exactly one emoji character, nothing else.

    Rejects empty or multi-character strings, whitespace, and plain
    ASCII text, so a typo can never turn the entry into a word or a
    sentence instead of a single emoji.
    """
    if len(entry) != 1:
        raise ValueError("entry must be exactly one character")
    if entry.isspace() or entry.isascii():
        raise ValueError("entry must be a single emoji, not text")
    return entry


def get_entry() -> str:
    """Return the validated dream-vacation emoji for this entry.

    The constant is built from its code point and then passed through
    validate_entry(), so the value handed to main() is guaranteed to
    be exactly one emoji character before anything is written.
    """
    return validate_entry(EMOJI)


def main() -> int:
    entry = get_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
