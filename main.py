"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line is a constant: the program is fully deterministic, uses only
the standard library, and touches no network, clock, or randomness.

The note is built from two beats: a setup (the install is now fast)
and a punchline (the old setup wizard is gone). The joined text is
byte-identical to the v1 entry.
"""

import os

SETUP = "Sleep now installs in under 8 minutes;"
PUNCHLINE = "the 45-minute ceiling-staring setup wizard has been removed."
NOTE = f"{SETUP} {PUNCHLINE}"


def validate_entry(text):
    """Check the entry against the competition gate and return it.

    Asserts are stripped under ``python -O``, so a gate written with
    asserts could silently vanish; this helper raises ValueError with
    a specific reason per check, so it is enforced on every run.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be UTF-8 encodable") from exc
    return text


def main() -> None:
    text = validate_entry(NOTE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
