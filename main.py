"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes the locked entry line to <output>/entry.txt (UTF-8, no trailing
newline). Output dir comes from MAKEFUN_OUTPUT_DIR, falling back to
/output.

Verified numbers (2026-11-24): entry is 188 chars / 192 UTF-8 bytes
(two em dashes, 3 bytes each), one sentence, no trailing newline.
SHA-256 of entry.txt:
f92cfee965362a19c0fbc1f7bc644591f6f7d42980956b8bade30d9e46f8e98d
Verified byte-identical across 3 fresh-output runs plus a clean-env
`env -i python3 -P -s` run, and re-verified after this docstring edit.
"""

import os

ENTRY = (
    "The lawmaker who wrote the 214-page AI Safety Act \u2014 the law that "
    "tells AI companies exactly how to train their models \u2014 just emailed "
    "his staff asking how to turn the Act itself into a PDF."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
