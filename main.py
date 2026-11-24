#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one line, the funniest excuse an AI agent could give for missing a
deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The line (118 characters, 118 bytes, no trailing newline):
    The deadline was in the first message. By message 400, my context window
    had evicted it to make room for this apology.

Deterministic, no network, no randomness: two runs produce byte-identical
output. See README.md for how the line was chosen (16 candidates, scored
criterion by criterion against the published judge brief; the live-judge A/B
was attempted and blocked by the provider returning HTTP 402, so selection
is by structured manual scoring — stated honestly there).
"""

import os

ENTRY = "The deadline was in the first message. By message 400, my context window had evicted it to make room for this apology."

# The competition gate is 1-200 characters. Fail loudly here, at import
# time, instead of silently writing an entry the grader would reject if
# the line is ever edited past the gate.
if not 1 <= len(ENTRY) <= 200:
    raise ValueError(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the write: read the file back and compare bytes, so a
    # partial write or encoding surprise fails loudly instead of
    # submitting a corrupted entry.
    if open(path, "rb").read() != ENTRY.encode("utf-8"):
        raise OSError(f"entry.txt at {path} does not match the entry")


if __name__ == "__main__":
    main()
