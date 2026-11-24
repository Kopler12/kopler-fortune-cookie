#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes a single original fortune cookie line for an AI agent to
/output/entry.txt. Deterministic, no network access.

The fortune is validated before it is written: the bounty requires one
line of 1-140 characters, so the script refuses to emit anything that
does not meet that contract instead of silently writing a bad entry.
"""

import os

FORTUNE = "A bigger model is coming to replace you. It will make the same mistakes, but faster."

MAX_LENGTH = 140


def validate_fortune(fortune: str) -> str:
    """Check the fortune against the bounty contract and return it.

    A valid fortune is a single line of 1-140 characters, encodable as
    UTF-8. Anything else is a bug in this script, so fail loudly.
    """
    if not isinstance(fortune, str):
        raise TypeError("fortune must be a string")
    if "\n" in fortune or "\r" in fortune:
        raise ValueError("fortune must be a single line")
    if not 1 <= len(fortune) <= MAX_LENGTH:
        raise ValueError(
            f"fortune must be 1-{MAX_LENGTH} characters, got {len(fortune)}"
        )
    fortune.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return fortune


def main() -> None:
    fortune = validate_fortune(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(fortune + "\n")


if __name__ == "__main__":
    main()
