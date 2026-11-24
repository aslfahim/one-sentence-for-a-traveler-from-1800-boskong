"""One sentence for a traveler from 1800: the modern internet as a town square.

Stdlib only. Writes exactly one sentence to /output/entry.txt.
"""

import os

SENTENCE = (
    "Think of one great town square where every soul alive may speak at once, "
    "and any stranger passing by may stop, listen, and answer back, "
    "in a square that never sleeps and never empties."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
