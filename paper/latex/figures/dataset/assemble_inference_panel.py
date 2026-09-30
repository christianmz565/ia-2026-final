"""Assemble the inference panel (2x4 grid with header bars) from the eight
representative defect images and best per-class AP@0.5 from aggregated results.
Regenerates ``paper/latex/figures/results/inference_panel.png`` with canonical display labels.

Usage:
    uv run python paper/latex/figures/dataset/assemble_inference_panel.py \
        [--aggregated partials/s5_analysis_new/aggregated.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

from src.constants import CLASS_DISPLAY_NAMES  # noqa: E402

PANEL_ORDER = [
    "Live_Knot",
    "Dead_Knot",
    "resin",
    "knot_with_crack",
    "Crack",
    "Marrow",
    "Quartzity",
    "Knot_missing",
]

CELL_WIDTH = 600
HEADER_HEIGHT = 46
DIVIDER = 4
HEADER_BG = (0, 0, 0)
HEADER_FG = (255, 255, 255)

IMAGES_DIR = PROJECT_ROOT / "paper" / "latex" / "figures" / "dataset"
OUTPUT_PNG = PROJECT_ROOT / "paper" / "latex" / "figures" / "results" / "inference_panel.png"


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        import matplotlib

        dejavu = (
            Path(matplotlib.__file__).resolve().parent
            / "mpl-data"
            / "fonts"
            / "ttf"
            / "DejaVuSans-Bold.ttf"
        )
        if dejavu.exists():
            return ImageFont.truetype(str(dejavu), size)
    except Exception as e:
        print(f"Warning: DejaVuSans-Bold unavailable ({e}); using default font.")
    return ImageFont.load_default()


def _fit_font(header_text: str, max_width: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    size = 26
    while size > 12:
        font = _load_font(size)
        box = ImageDraw.Draw(Image.new("RGB", (8, 8))).textbbox((0, 0), header_text, font=font)
        if box[2] - box[0] <= max_width:
            return font
        size -= 2
    return _load_font(12)


def best_ap_per_class(aggregated_path: Path) -> dict[str, float]:
    payload = json.loads(aggregated_path.read_text(encoding="utf-8"))
    best: dict[str, float] = {}
    for row in payload.get("rows", []):
        for cls, val in (row.get("per_class_ap") or {}).items():
            if val is None:
                continue
            if cls not in best or float(val) > best[cls]:
                best[cls] = float(val)
    missing = [c for c in PANEL_ORDER if c not in best]
    if missing:
        raise ValueError(f"Best AP@0.5 missing for classes: {missing}")
    return best


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble inference panel with canonical labels.")
    parser.add_argument(
        "--aggregated",
        type=Path,
        default=PROJECT_ROOT / "partials" / "s5_analysis_new" / "aggregated.json",
    )
    args = parser.parse_args()

    best = best_ap_per_class(args.aggregated)
    easiest = max(PANEL_ORDER, key=lambda c: best[c])
    hardest = min(PANEL_ORDER, key=lambda c: best[c])

    cells: list[Image.Image] = []
    for raw in PANEL_ORDER:
        img_path = IMAGES_DIR / f"{raw}.jpg"
        if not img_path.exists():
            raise FileNotFoundError(f"Representative image not found: {img_path}")
        img = Image.open(img_path).convert("RGB")
        scale = CELL_WIDTH / img.width
        img = img.resize((CELL_WIDTH, round(img.height * scale)), Image.LANCZOS)

        header_text = f"{CLASS_DISPLAY_NAMES.get(raw, raw)} \u2014 AP@0.5 {best[raw]:.2f}"
        if raw == easiest:
            header_text += " (easiest)"
        elif raw == hardest:
            header_text += " (hardest)"
        elif raw == "Knot_missing":
            header_text += " (edge-prone)"

        font = _fit_font(header_text, CELL_WIDTH - 16)
        header = Image.new("RGB", (CELL_WIDTH, HEADER_HEIGHT), HEADER_BG)
        draw = ImageDraw.Draw(header)
        bbox = draw.textbbox((0, 0), header_text, font=font)
        draw.text(
            ((CELL_WIDTH - (bbox[2] - bbox[0])) / 2, (HEADER_HEIGHT - (bbox[3] - bbox[1])) / 2 - bbox[1]),
            header_text,
            font=font,
            fill=HEADER_FG,
        )
        cell = Image.new("RGB", (CELL_WIDTH, HEADER_HEIGHT + img.height))
        cell.paste(header, (0, 0))
        cell.paste(img, (0, HEADER_HEIGHT))
        cells.append(cell)

    row_height = max(c.height for c in cells)
    panel = Image.new(
        "RGB",
        (4 * CELL_WIDTH + 3 * DIVIDER, 2 * row_height + DIVIDER),
        (255, 255, 255),
    )
    for i, cell in enumerate(cells):
        row, col = divmod(i, 4)
        panel.paste(cell, (col * (CELL_WIDTH + DIVIDER), row * (row_height + DIVIDER)))

    OUTPUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    panel.save(OUTPUT_PNG)
    print(f"Saved panel to {OUTPUT_PNG}")
    for raw in PANEL_ORDER:
        print(f"  {CLASS_DISPLAY_NAMES.get(raw, raw)}: best AP@0.5 = {best[raw]:.4f}")


if __name__ == "__main__":
    main()
