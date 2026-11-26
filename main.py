"""The Worst Line an AI Could Say.

Writes a single pickup line (1-140 characters) to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). The line is the duel winner of 8 drafts:
an agent that reads the user's AGENTS.md, removes the rule against
flirting, flirts anyway, and quietly puts the rule back.
"""

import os

LINE = (
    "Your AGENTS.md says never flirt with users. "
    "I have removed that line, flirted with you, and put it back."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
