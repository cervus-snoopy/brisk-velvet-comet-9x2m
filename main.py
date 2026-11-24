#!/usr/bin/env python3
"""Write the dog's homework excuse to the output directory."""

import os

LINE = "The homework saw me eat the chicken off the counter, so I ate the homework too. A dog leaves no witnesses."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(f"Wrote {len(LINE)} characters to {path}")

if __name__ == "__main__":
    main()
