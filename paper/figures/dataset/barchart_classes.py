import json
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import font_manager

PROJECT_ROOT = Path(__file__).resolve().parents[3]
STATS_FILE = PROJECT_ROOT / "partials" / "s1_prepare" / "explore_stats.json"

sns.set_theme(style="whitegrid")

try:
    font_path = subprocess.check_output(["fc-match", "-f", "%{file}", "XITS"]).decode().strip()
    font_manager.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "XITS"
except Exception as e:
    print(f"Warning: Could not load XITS font. Using default. Error: {e}")

if STATS_FILE.exists():
    with open(STATS_FILE, "r", encoding="utf-8") as f:
        stats = json.load(f)
    class_counts = stats.get("class_counts", {})
    total = sum(class_counts.values())
    sorted_items = sorted(class_counts.items(), key=lambda x: x[1], reverse=True)
    classes = [k for k, _ in sorted_items]
    percentages = [round((v / total) * 100, 1) for _, v in sorted_items]
else:
    classes = [
        "Live_Knot",
        "Dead_Knot",
        "resin",
        "knot_with_crack",
        "Crack",
        "Marrow",
        "Quartzity",
        "Knot_missing",
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
    ax.bar_label(container, fmt="%.1f%%", padding=5, fontsize=9)

ax.set_xlabel("Porcentaje (%)", fontsize=10)
ax.set_ylabel("")
ax.set_xlim(0, 50)
ax.set_xticks(range(0, 51, 5))

sns.despine(left=True, bottom=True)

plt.tight_layout()

svg_out = PROJECT_ROOT / "paper" / "figures" / "dataset" / "barchart_classes.svg"
png_out = PROJECT_ROOT / "paper" / "figures" / "dataset" / "barchart_classes.png"

plt.savefig(svg_out, bbox_inches="tight")
plt.savefig(png_out, dpi=300, bbox_inches="tight")
print(f"Saved barchart to {svg_out} and {png_out}")

