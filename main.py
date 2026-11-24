"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: the desert island,
the postcard dream vacation in a single glyph.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
EMOJI = "\U0001F3DD"  # DESERT ISLAND


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
