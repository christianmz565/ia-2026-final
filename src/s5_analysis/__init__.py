"""s5_analysis — Result aggregation, table generation, and figure plotting."""

from src.s5_analysis.aggregate import aggregate_results
from src.s5_analysis.figures import generate_figures
from src.s5_analysis.tables import generate_tables

__all__ = [
    "aggregate_results",
    "generate_figures",
    "generate_tables",
]
