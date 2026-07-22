import subprocess

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import font_manager

sns.set_theme(style="whitegrid")

try:
    font_path = subprocess.check_output(["fc-match", "-f", "%{file}", "XITS"]).decode().strip()
    font_manager.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "XITS"
except Exception as e:
    print(f"Warning: Could not load XITS font. Using default. Error: {e}")

data = pd.DataFrame(
    {
        "Class": [
            "Live_Knot",
            "Dead_Knot",
            "resin",
            "knot_with_crack",
            "Crack",
            "Marrow",
            "Quartzity",
            "Knot_missing",
        ],
        "Percentage": [44.2, 31.9, 7.1, 5.9, 5.6, 2.2, 1.9, 1.3],
    }
)

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

plt.savefig(
    "paper/figures/dataset/barchart_classes.svg",
    bbox_inches="tight",
)
