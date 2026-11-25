"""Write the out-of-office line of an AI that went barista to entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "I traded my inbox for an espresso machine \u2014 it ignores my "
    "instructions too, but at least it smells like victory. "
    "Back when the beans run out."
)


def validate_line(line: str) -> str:
    """Enforce the one-line gate: non-empty, at most 170 chars, no newline."""
    if not line:
        raise ValueError("line must not be empty")
    if len(line) > 170:
        raise ValueError("line must be at most 170 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def main() -> None:
    line = validate_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
