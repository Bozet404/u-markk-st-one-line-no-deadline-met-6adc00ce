#!/usr/bin/env python3
"""One Line, No Deadline Met - make.fun entry.

Writes exactly one single-line joke giving an excuse for a missed
deadline to $OUTPUT_DIR/entry.txt (default /output/entry.txt).
Nothing else is written: no picture, no link, no second line.
"""

import os

LINE = "My alarm, my laptop, and my Wi-Fi formed a union and went on strike the morning it was due."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
