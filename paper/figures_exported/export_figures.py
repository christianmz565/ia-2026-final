"""Export individual high-quality 600 DPI figures with figure headers from Typst templates.

Generates:
    - figure1.typ / figure1.png: Defect class distribution (barchart_classes)
    - figure2.typ / figure2.png: Examples of the eight defect classes (2x4 grid composite)
    - figure3.typ / figure3.png: Five-stage experimental pipeline overview (pipeline)
    - figure4.typ / figure4.png: mAP@0.5 performance matrix (aug_paradigm_map50_heatmap)
    - figure5.typ / figure5.png: mAP@0.5:0.95 performance matrix (aug_paradigm_map50_95_heatmap)
    - figure6.typ / figure6.png: Augmentation delta vs baseline (aug_delta_vs_baseline)
    - figure7.typ / figure7.png: Heatmap of per-class AP@0.5 (per_class_ap_heatmap)
    - figure8.typ / figure8.png: Heatmap of per-class AP@0.5:0.95 (per_class_ap50_95_heatmap)
    - figure9.typ / figure9.png: Per-class recall with Bonferroni-corrected 95% CIs (per_class_recall_bonferroni)
    - figure10.typ / figure10.png: Ground-truth-annotated representative instances (inference_panel)
    - figure11.typ / figure11.png: Speed-accuracy trade-off (speed_accuracy_tradeoff)
    - figure12.typ / figure12.png: Training convergence curves - mAP@0.5 (training_curves_map)
    - figure13.typ / figure13.png: Training loss progression (training_curves_loss)
    - figure14.typ / figure14.png: Training time comparison (training_time_comparison)

Usage:
    uv run python paper/figures_exported/export_figures.py [--dpi 600]
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.constants import CLASS_DISPLAY_NAMES  # noqa: E402
from src.s5_analysis.figures import (  # noqa: E402
    _fig_aug_delta_vs_baseline,
    _fig_aug_paradigm_heatmap,
    _fig_per_class_ap50_95_heatmap,
    _fig_per_class_ap_heatmap,
    _fig_per_class_recall_bonferroni,
    _fig_speed_accuracy_tradeoff,
    _fig_training_curves_loss,
    _fig_training_curves_map,
    _fig_training_time_comparison,
    _setup_style,
)

FIGURES_EXPORTED_DIR = PROJECT_ROOT / "paper" / "figures_exported"
RAW_FIGURES_DIR = FIGURES_EXPORTED_DIR / "raw"
DATASET_FIGURES_DIR = PROJECT_ROOT / "paper" / "figures" / "dataset"
METHODS_FIGURES_DIR = PROJECT_ROOT / "paper" / "figures" / "methods"
AGGREGATED_JSON = PROJECT_ROOT / "last_run" / "s5_analysis_new" / "aggregated.json"

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

FIGURE_TEMPLATES: dict[int, dict[str, str]] = {
    1: {
        "title": "Figure 1: Defect class distribution in the filtered dataset: Live Knot, Dead Knot, Resin, Crack, Knot with Crack, Marrow, Quartzite, and Missing Knot",
        "content": '#align(center)[#image("raw/figure1.png", width: 100%)]',
    },
    2: {
        "title": "Figure 2: Examples of the eight defect classes annotated in the wood dataset: Live Knot, Dead Knot, Resin, Knot with Crack, Crack, Marrow, Quartzite, and Missing Knot (left to right, top to bottom)",
        "content": """#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 4pt,
  image("/paper/figures/dataset/Live_Knot.jpg", width: 100%),
  image("/paper/figures/dataset/Dead_Knot.jpg", width: 100%),
  image("/paper/figures/dataset/resin.jpg", width: 100%),
  image("/paper/figures/dataset/knot_with_crack.jpg", width: 100%),
  image("/paper/figures/dataset/Crack.jpg", width: 100%),
  image("/paper/figures/dataset/Marrow.jpg", width: 100%),
  image("/paper/figures/dataset/Quartzity.jpg", width: 100%),
  image("/paper/figures/dataset/Knot_missing.jpg", width: 100%),
)""",
    },
    3: {
        "title": "Figure 3: Overview of the proposed five-stage experimental pipeline for timber defect detection benchmarking",
        "content": '#align(center)[#image("/paper/figures/methods/pipeline.svg", width: 100%)]',
    },
    4: {
        "title": r"Figure 4: mAP\@0.5 performance matrix intersecting three detection paradigms with four augmentation strategies",
        "content": '#align(center)[#image("raw/figure4.png", width: 60%)]',
    },
    5: {
        "title": r"Figure 5: mAP\@0.5:0.95 performance matrix for the same 12 configurations",
        "content": '#align(center)[#image("raw/figure5.png", width: 60%)]',
    },
    6: {
        "title": r"Figure 6: Impact of augmentation strategies relative to baseline ($Delta$ mAP\@0.5)",
        "content": '#align(center)[#image("raw/figure6.png", width: 100%)]',
    },
    7: {
        "title": r"Figure 7: Heatmap of average precision per defect class (AP\@0.5)",
        "content": '#align(center)[#image("raw/figure7.png", width: 100%)]',
    },
    8: {
        "title": r"Figure 8: Heatmap of average precision per defect class (AP\@0.5:0.95)",
        "content": '#align(center)[#image("raw/figure8.png", width: 100%)]',
    },
    9: {
        "title": "Figure 9: Per-class recall with Bonferroni-corrected simultaneous 95% family-wise confidence intervals for the best configuration of each paradigm",
        "content": '#align(center)[#image("raw/figure9.png", width: 100%)]',
    },
    10: {
        "title": r"Figure 10: Ground-truth-annotated representative instances with best AP\@0.5 per class",
        "content": '#align(center)[#image("raw/figure10.png", width: 100%)]',
    },
    11: {
        "title": r"Figure 11: Trade-off between inference speed (ms/image) and precision (mAP\@0.5)",
        "content": '#align(center)[#image("raw/figure11.png", width: 100%)]',
    },
    12: {
        "title": r"Figure 12: mAP\@0.5 validation convergence curves during training",
        "content": '#align(center)[#image("raw/figure12.png", width: 100%)]',
    },
    13: {
        "title": "Figure 13: Training loss progression over epochs for all 12 configurations",
        "content": '#align(center)[#image("raw/figure13.png", width: 100%)]',
    },
    14: {
        "title": "Figure 14: Comparison of total training time per configuration",
        "content": '#align(center)[#image("raw/figure14.png", width: 100%)]',
    },
}


def set_png_dpi_metadata(png_path: Path, dpi: int) -> None:
    """Set physical resolution (pHYs) chunk in PNG to exact DPI using ImageMagick if available."""
    try:
        subprocess.run(
            ["magick", str(png_path), "-density", str(dpi), "-units", "PixelsPerInch", str(png_path)],
            check=True,
            capture_output=True,
        )
    except Exception as e:
        print(f"Warning: could not set ImageMagick DPI metadata on {png_path}: {e}")


def export_raw_figure1(raw_dir: Path, dpi: int) -> Path:
    """Raw Figure 1: Defect class distribution barchart."""
    _setup_style()
    classes = [
        CLASS_DISPLAY_NAMES["Live_Knot"],
        CLASS_DISPLAY_NAMES["Dead_Knot"],
        CLASS_DISPLAY_NAMES["resin"],
        CLASS_DISPLAY_NAMES["knot_with_crack"],
        CLASS_DISPLAY_NAMES["Crack"],
        CLASS_DISPLAY_NAMES["Marrow"],
        CLASS_DISPLAY_NAMES["Quartzity"],
        CLASS_DISPLAY_NAMES["Knot_missing"],
    ]
    percentages = [44.7, 32.5, 7.3, 5.8, 4.7, 2.3, 1.5, 1.2]
    data = pd.DataFrame({"Class": classes, "Percentage": percentages})

    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(
        data=data,
        x="Percentage",
        y="Class",
        hue="Class",
        palette="muted",
        legend=False,
        ax=ax,
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f%%", padding=5, fontsize=9)  # type: ignore[arg-type]

    ax.set_xlabel("Percentage (%)", fontsize=10)
    ax.set_ylabel("")
    ax.set_xlim(0, 50)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()

    out_file = raw_dir / "figure1.png"
    fig.savefig(out_file, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return out_file


def export_raw_figure10(raw_dir: Path, aggregated_path: Path, dpi: int) -> Path:
    """Raw Figure 10: Ground-truth-annotated representative instances (inference_panel)."""
    cell_width = 1200
    header_height = 92
    divider = 8
    header_bg = (0, 0, 0)
    header_fg = (255, 255, 255)

    dejavu = Path(matplotlib.__file__).resolve().parent / "mpl-data" / "fonts" / "ttf" / "DejaVuSans-Bold.ttf"

    def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        if dejavu.exists():
            return ImageFont.truetype(str(dejavu), size)
        return ImageFont.load_default()

    def _fit_font(header_text: str, max_w: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        size = 52
        while size > 16:
            font = _load_font(size)
            box = ImageDraw.Draw(Image.new("RGB", (8, 8))).textbbox((0, 0), header_text, font=font)
            if box[2] - box[0] <= max_w:
                return font
            size -= 2
        return _load_font(16)

    payload = json.loads(aggregated_path.read_text(encoding="utf-8"))
    best: dict[str, float] = {}
    for row in payload.get("rows", []):
        for cls, val in (row.get("per_class_ap") or {}).items():
            if val is not None and (cls not in best or float(val) > best[cls]):
                best[cls] = float(val)

    missing = [c for c in PANEL_ORDER if c not in best]
    if missing:
        raise ValueError(f"Best AP@0.5 missing for classes: {missing}")

    easiest = max(PANEL_ORDER, key=lambda c: best[c])
    hardest = min(PANEL_ORDER, key=lambda c: best[c])

    cells: list[Image.Image] = []
    for raw in PANEL_ORDER:
        img_path = DATASET_FIGURES_DIR / f"{raw}.jpg"
        if not img_path.exists():
            raise FileNotFoundError(f"Representative image not found: {img_path}")
        img = Image.open(img_path).convert("RGB")
        scale = cell_width / img.width
        img = img.resize((cell_width, round(img.height * scale)), Image.LANCZOS)

        header_text = f"{CLASS_DISPLAY_NAMES.get(raw, raw)} \u2014 AP@0.5 {best[raw]:.2f}"
        if raw == easiest:
            header_text += " (easiest)"
        elif raw == hardest:
            header_text += " (hardest)"
        elif raw == "Knot_missing":
            header_text += " (edge-prone)"

        font = _fit_font(header_text, cell_width - 32)
        header = Image.new("RGB", (cell_width, header_height), header_bg)
        draw = ImageDraw.Draw(header)
        bbox = draw.textbbox((0, 0), header_text, font=font)
        draw.text(
            ((cell_width - (bbox[2] - bbox[0])) / 2, (header_height - (bbox[3] - bbox[1])) / 2 - bbox[1]),
            header_text,
            font=font,
            fill=header_fg,
        )
        cell = Image.new("RGB", (cell_width, header_height + img.height))
        cell.paste(header, (0, 0))
        cell.paste(img, (0, header_height))
        cells.append(cell)

    row_height = max(c.height for c in cells)
    panel = Image.new(
        "RGB",
        (4 * cell_width + 3 * divider, 2 * row_height + divider),
        (255, 255, 255),
    )
    for i, cell in enumerate(cells):
        row, col = divmod(i, 4)
        panel.paste(cell, (col * (cell_width + divider), row * (row_height + divider)))

    out_file = raw_dir / "figure10.png"
    panel.save(out_file, dpi=(dpi, dpi))
    return out_file


def write_typst_file(fig_num: int, output_dir: Path, max_width: str = "174mm") -> Path:
    """Write the figureX.typ file with consistent header styling matching tables_exported."""
    meta = FIGURE_TEMPLATES[fig_num]
    typ_path = output_dir / f"figure{fig_num}.typ"

    content = f"""#set page(
  width: auto,
  height: auto,
  margin: (x: 1.5cm, y: 1cm),
  fill: white
)
#set text(
  font: "Liberation Serif",
  size: 10pt
)

#box(width: {max_width})[
  #align(center)[
    #text(weight: "bold", size: 11pt)[{meta["title"]}]
  ]
  #v(6pt)

  {meta["content"]}
]
"""
    typ_path.write_text(content, encoding="utf-8")
    return typ_path


def export_all_figures(output_dir: Path, dpi: int = 600, max_width: str = "174mm") -> list[Path]:
    """Execute generation pipelines and export all figures in manuscript order with figure headers."""
    if not AGGREGATED_JSON.exists():
        raise FileNotFoundError(f"Aggregated JSON not found at {AGGREGATED_JSON}")

    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    _setup_style()

    with open(AGGREGATED_JSON, encoding="utf-8") as f:
        aggregated_data = json.load(f)

    rows = aggregated_data.get("rows", [])
    history = aggregated_data.get("history", {})

    temp_s5_dir = output_dir / ".tmp_s5"
    temp_s5_dir.mkdir(parents=True, exist_ok=True)

    print("Generating raw Figure 1: barchart_classes...")
    export_raw_figure1(raw_dir, dpi)

    print("Generating raw Figures 4 & 5: paradigm heatmaps...")
    _fig_aug_paradigm_heatmap(
        rows, "mAP_50", "Augmentation x Paradigm (mAP@50)", "aug_paradigm_map50_heatmap", "YlGnBu", temp_s5_dir, dpi
    )
    _fig_aug_paradigm_heatmap(
        rows,
        "mAP_50_95",
        "Augmentation x Paradigm (mAP@50:95)",
        "aug_paradigm_map50_95_heatmap",
        "YlOrRd",
        temp_s5_dir,
        dpi,
    )
    shutil.copy2(temp_s5_dir / "aug_paradigm_map50_heatmap.png", raw_dir / "figure4.png")
    shutil.copy2(temp_s5_dir / "aug_paradigm_map50_95_heatmap.png", raw_dir / "figure5.png")

    print("Generating raw Figure 6: aug delta vs baseline...")
    _fig_aug_delta_vs_baseline(rows, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "aug_delta_vs_baseline.png", raw_dir / "figure6.png")

    print("Generating raw Figure 7: per-class AP@0.5 heatmap...")
    _fig_per_class_ap_heatmap(rows, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "per_class_ap_heatmap.png", raw_dir / "figure7.png")

    print("Generating raw Figure 8: per-class AP@0.5:0.95 heatmap...")
    _fig_per_class_ap50_95_heatmap(rows, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "per_class_ap50_95_heatmap.png", raw_dir / "figure8.png")

    print("Generating raw Figure 9: per-class recall with Bonferroni CIs...")
    _fig_per_class_recall_bonferroni(temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "per_class_recall_bonferroni.png", raw_dir / "figure9.png")

    print("Generating raw Figure 10: inference panel...")
    export_raw_figure10(raw_dir, AGGREGATED_JSON, dpi)

    print("Generating raw Figure 11: speed-accuracy tradeoff...")
    _fig_speed_accuracy_tradeoff(rows, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "speed_accuracy_tradeoff.png", raw_dir / "figure11.png")

    print("Generating raw Figure 12: training curves (mAP)...")
    _fig_training_curves_map(history, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "training_curves_map.png", raw_dir / "figure12.png")

    print("Generating raw Figure 13: training curves (loss)...")
    _fig_training_curves_loss(history, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "training_curves_loss.png", raw_dir / "figure13.png")

    print("Generating raw Figure 14: training time comparison...")
    _fig_training_time_comparison(rows, temp_s5_dir, dpi)
    shutil.copy2(temp_s5_dir / "training_time_comparison.png", raw_dir / "figure14.png")

    # Clean up temporary s5 directory
    shutil.rmtree(temp_s5_dir, ignore_errors=True)

    # Compile each figure from its Typst template to produce the final image with header
    exported_images: list[Path] = []
    for fig_num in range(1, 15):
        typ_path = write_typst_file(fig_num, output_dir, max_width=max_width)
        png_out = output_dir / f"figure{fig_num}.png"
        print(f"Compiling figure{fig_num}.typ -> figure{fig_num}.png with header at {dpi} PPI...")
        subprocess.run(
            [
                "typst",
                "compile",
                "--root",
                str(PROJECT_ROOT),
                "--ppi",
                str(dpi),
                str(typ_path),
                str(png_out),
            ],
            check=True,
        )
        set_png_dpi_metadata(png_out, dpi)
        exported_images.append(png_out)

    print(f"Successfully exported all 14 figures with headers to {output_dir} at {dpi} DPI.")
    return exported_images


def main() -> None:
    parser = argparse.ArgumentParser(description="Export individual 600 DPI figures with Typst headers.")
    parser.add_argument("--output-dir", type=Path, default=FIGURES_EXPORTED_DIR)
    parser.add_argument("--dpi", type=int, default=600)
    parser.add_argument(
        "--max-width",
        type=str,
        default="174mm",
        help="Maximum content width for figures (default: 174mm).",
    )
    args = parser.parse_args()

    export_all_figures(output_dir=args.output_dir, dpi=args.dpi, max_width=args.max_width)


if __name__ == "__main__":
    main()
