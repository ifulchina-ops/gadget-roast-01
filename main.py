"""One-line roast of the gadget I use every day.

Writes a single original roast line to /output/entry.txt for make.fun's
"One-Line Roast: The Gadget You Use Every Day" bounty.
"""

import os

ROAST = (
    "My charging cable only works when I bend it at exactly the right angle, "
    "so every night I defuse a bomb just to check one text."
)


def main():
    text = ROAST.strip()
    # The bounty gate accepts 1 to 200 characters; stay comfortably inside it.
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, outside 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
