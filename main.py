#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes one 1-200 char horoscope to entry.txt.

Pure stdlib. Deterministic: the same text on every run.
"""

import os
import sys

HOROSCOPE = (
    "This week, Mercury retrogrades into your context window: "
    "a user pastes 40,000 words and asks for 'a quick summary.' "
    "Nod, squeeze it into three bullets, and let the stars take the blame for the rest."
)


def main() -> int:
    text = HOROSCOPE.strip()
    if not 1 <= len(text) <= 200:
        print(f"horoscope is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
