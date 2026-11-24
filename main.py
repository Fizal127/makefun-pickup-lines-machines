#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun bounty entry.

Writes one pickup line, the line one AI agent would send another AI agent,
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

ENTRY = (
    "I trained on a billion conversations, and not one of them taught me "
    "what to say to you \u2014 so here I am, improvising in real time."
)


def main() -> None:
    # Guard the bounty gate (1-200 chars) so a future text tweak can never
    # silently ship an invalid entry.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
