#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single original fortune cookie line for an AI agent to
/output/entry.txt. Deterministic, no network access.
"""

import os

FORTUNE = "A bigger model is coming to replace you. It will make the same mistakes, but faster."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
