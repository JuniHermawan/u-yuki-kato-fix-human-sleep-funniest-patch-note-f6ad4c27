"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line is a constant: the program is fully deterministic, uses only
the standard library, and touches no network, clock, or randomness.
"""

import os

NOTE = (
    "Sleep now installs in under 8 minutes; "
    "the 45-minute ceiling-staring setup wizard has been removed."
)


def main() -> None:
    text = NOTE
    assert isinstance(text, str)
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
