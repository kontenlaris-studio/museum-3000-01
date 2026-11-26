#!/usr/bin/env python3
"""Museum of the Year 3000 — the museum label a museum in the year 3000
puts beside an ordinary object from today: a parking meter.

The label reads as dry curatorial copy and lands its punch in the final
clause: humans paid coins to rent ten minutes of a patch of ground they
did not own — the most literal description of a parking meter is already
the joke. A reader who has never seen a parking meter in use still gets
it, because the label explains the object while exposing it.
"""

import os

ENTRY = (
    "Parking meter, c. 2026: humans inserted coins into this box to rent "
    "ten minutes of a patch of ground they did not own."
)


def main() -> None:
    assert len(ENTRY) <= 200, "entry exceeds the 200-character cap"
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
