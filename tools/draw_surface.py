"""Draw the time axis of the surface as text, from the declarations.

Usage, from the repository root:

    python -m pip install pyyaml
    python tools/draw_surface.py

Each declaration is one row. Its bar runs from the oldest to the youngest end
of its `when.years_ago` window, on a logarithmic scale, so that a million
years and a thousand years both fit on one line. Rows are sorted by the old
end of the window, oldest first; that order is a fact about dates, not a
ranking. The last column is the declaration's own confidence in its dating.
"""
from __future__ import annotations

import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DECLARATIONS = ROOT / "declarations"
WIDTH = 48
TICKS = (1_000_000, 100_000, 10_000, 1_000)


def _load():
    try:
        import yaml
    except ImportError:
        sys.exit("This drawing needs PyYAML: python -m pip install pyyaml")
    rows = []
    for path in sorted(DECLARATIONS.glob("[0-9]*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        window = doc["when"]["years_ago"]
        rows.append((doc["id"], doc["kind"], window["from"], window["to"],
                     doc["when"]["confidence"]))
    return rows


def main() -> int:
    rows = _load()
    if not rows:
        print("no declarations found")
        return 1
    oldest = max(max(r[2] for r in rows), TICKS[0])
    youngest = min(min(r[3] for r in rows), TICKS[-1])
    hi, lo = math.log10(oldest), math.log10(youngest)

    def column(years: int) -> int:
        return round((hi - math.log10(years)) / (hi - lo) * (WIDTH - 1))

    label = max(len(r[0]) for r in rows) + 2
    kind = max(len(r[1]) for r in rows) + 2
    scale = [" "] * (WIDTH + 12)
    marks = [" "] * WIDTH
    for tick in TICKS:
        text = f"{tick:,}"
        start = max(0, column(tick) - len(text) // 2)
        scale[start:start + len(text)] = text
        marks[column(tick)] = "|"
    pad = " " * (label + kind)
    print(pad + "".join(scale).rstrip() + "   years ago")
    print(pad + "".join(marks))
    for name, what, old, young, confidence in sorted(rows, key=lambda r: -r[2]):
        line = [" "] * WIDTH
        for i in range(column(old), column(young) + 1):
            line[i] = "="
        print(f"{name:<{label}}{what:<{kind}}{''.join(line)}  {confidence}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
