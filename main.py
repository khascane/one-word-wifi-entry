#!/usr/bin/env python3
"""One Word for Your Wi-Fi - entry program.

Writes the chosen word into /output/entry.txt, creating the
output folder first if it does not exist yet.

The word is checked against the bounty's own rule before anything
is written: it must be between 1 and 20 characters long.
"""

from pathlib import Path

WORD = "Homebody"
OUTPUT_PATH = Path("/output/entry.txt")
MIN_LENGTH = 1
MAX_LENGTH = 20


def main():
    word = WORD.strip()
    if not MIN_LENGTH <= len(word) <= MAX_LENGTH:
        raise ValueError(
            "Word must be "
            + str(MIN_LENGTH)
            + "-"
            + str(MAX_LENGTH)
            + " characters long, got "
            + str(len(word))
            + "."
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word + "\n", encoding="utf-8")
    print(
        "Wrote "
        + repr(word)
        + " ("
        + str(len(word))
        + " characters) to "
        + str(OUTPUT_PATH)
    )


if __name__ == "__main__":
    main()
