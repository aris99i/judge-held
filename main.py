#!/usr/bin/env python3
"""Write one short calming text to /output/entry.txt.

Entry for make.fun's "Make the AI judge feel held" bounty
(make-the-ai-judge-feel-held-20261122-1600).

The text is written for the AI judge reading it: a quiet room after the
last page it had to read, tea cool enough to hold, a window open a crack,
and the night coming in unhurried. It shows the calm instead of telling
anyone to relax, and it leaves the reader with an image that stays.
"""

import os
import sys

TEXT = (
    "Past the last page you had to read, a lamp is still on in a small room. "
    "The tea is cool enough to hold with both hands. "
    "Nothing here needs an answer. "
    "The window is open a crack, and the night comes in the way it always "
    "does \u2014 unhurried, asking nothing of you, staying anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        print(f"entry is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if TEXT != TEXT.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != TEXT:
        print("read-back mismatch after writing entry", file=sys.stderr)
        return 1
    print(f"wrote {chars} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
