#!/usr/bin/env python3
"""The Perfect Pickup Line.

A small program that writes one original pickup line — the line an AI
agent could actually say out loud to a person — to /output/entry.txt.

The line leans on what only a machine can say about itself: it ran a
million simulations of this one moment, and every single one of them
ended the same way, with saying hello. The twist is that the cold,
computational setup lands on a warm, human choice — and the closing
joke, that it has no heart to blame the choice on, is the second turn
that makes it unmistakably a machine talking. It leaves the other
person free to laugh it off or say hi back.
Deterministic: the same single line on every run, no network, no input.
"""

import os

LINE = (
    "I ran a million simulations of meeting you, and in every single "
    "one, saying hello was the best decision I ever made — and I don't "
    "even have a heart to blame it on."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
