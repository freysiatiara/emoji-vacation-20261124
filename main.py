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

    # Verification guard: read the output back and confirm it is exactly
    # the intended emoji (4 bytes UTF-8, no trailing newline or extras).
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != EMOJI.encode("utf-8") or len(written) != 4:
        raise SystemExit(
            "error: /output/entry.txt does not contain exactly the "
            "intended emoji (expected 4 bytes, got "
            f"{len(written)} bytes: {written!r})"
        )


if __name__ == "__main__":
    main()
