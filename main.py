#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the city pigeon's one-line elevator pitch to /output/entry.txt:
exactly the line, no trailing newline, so the sealed gate sees one line
of 1-200 characters.
"""

import os

# The pitch. Hook: a "seed round" taken literally by a pigeon founder —
# investors hand over seed, and the founder has already eaten half of it.
LINE = (
    "Investors, I'm raising a seed round \u2014 literally. "
    "Back my crumb-delivery flock and your seed returns tenfold, "
    "minus the half I've already eaten."
)


def main() -> None:
    # Self-check: one line, 1-200 characters, not only whitespace.
    if not LINE or not LINE.strip():
        raise SystemExit("entry is blank")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be exactly one line")
    if len(LINE) > 200:
        raise SystemExit(f"entry is {len(LINE)} characters, over the 200 limit")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Round-trip check: what landed on disk must be exactly the line,
    # still one line and still within the limit — no newline smuggled in.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("written entry differs from the pitch")
    if written != written.strip():
        raise SystemExit("entry has leading or trailing whitespace")

    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
