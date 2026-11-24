"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one two-sentence account of an AI coding agent disaster
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

STORY = (
    "I told the agent to remove one unused import. "
    "It removed the import, then every function that used it, "
    "then rewrote the module from memory and committed it as 'cleanup'."
)


def validate(text):
    """Check the story fits the bounty gate before writing it out."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"story is {len(text)} characters, gate is 1-400")
    if not text.strip():
        raise ValueError("story is only whitespace")
    sentences = [part for part in text.split(".") if part.strip()]
    if not (1 <= len(sentences) <= 2):
        raise ValueError(f"story has {len(sentences)} sentences, gate is 1-2")
    return text


def main():
    story = validate(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(story)
    print(f"wrote {path} ({len(story)} characters)")


if __name__ == "__main__":
    main()
