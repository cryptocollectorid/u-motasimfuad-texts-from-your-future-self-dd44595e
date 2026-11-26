#!/usr/bin/env python3
"""Texts From Your Future Self — one-line entry.

Writes a single funny text message from the writer's future self
to /output/entry.txt. Gate: 1-200 characters, UTF-8, not only whitespace.
"""

import os

# Draft v2 (final): tightened the middle and added a closing beat —
# the future self is tired of watching the present self reset it.
LINE = "It's me, you, 30 years from now. The password you keep forgetting is the goldfish's name. You never had a goldfish. Stop resetting it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")


if __name__ == "__main__":
    main()
