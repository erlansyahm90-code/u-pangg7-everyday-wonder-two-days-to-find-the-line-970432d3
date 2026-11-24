"""Everyday Wonder, Two Days to Find the Line.

Writes one single sentence about an ordinary moment seen for the
first time: my neighbor Pak Dedi sweeping the same five meters of
pavement every morning for nine years — not cleaning the street,
but greeting it. The surprise lands in one quiet read.
"""

import os

ENTRY = (
    # One sentence, 171 characters: a small daily wonder, seen at last.
    "My neighbor Pak Dedi has swept the same five meters of pavement "
    "every morning for nine years, and today I finally saw it: he is "
    "not cleaning the street, he is greeting it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
