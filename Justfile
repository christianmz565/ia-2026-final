# Wood surface defect detection — task runner.
#
# Pipeline:  just pipeline --log_level DEBUG
#            just pipeline --only s3_train --s3_train yolo26.epochs=5
# Sections:  just train yolo26.epochs=5            (bare flag/values forwarded)
# Report:    just analysis → just figures → just paper → (just bundle)
#            just report   (figures + paper + paper-es + bundle in one go)
# Quality:   just lint | check-format | format | typecheck
#
# Note: `just` forwards unknown flags to the recipe as-is, and a literal `--`
# is passed through to the command as well — so do NOT use `--` here.

out := "deliverables"

# Show available recipes.
default:
    just --list

# Run the full pipeline CLI; everything after the recipe name is forwarded to `python -m src`.
pipeline +ARGS:
    uv run python -m src {{ ARGS }}

# Run only the s1 data preparation section.
prepare +FLAGS:
    uv run python -m src --only s1_prepare --s1_prepare {{ FLAGS }}

# Run only the s2 augmentation section.
augments +FLAGS:
    uv run python -m src --only s2_augments --s2_augments {{ FLAGS }}

# Run only the s3 training section.
train +FLAGS:
    uv run python -m src --only s3_train --s3_train {{ FLAGS }}

# Run only the s4 evaluation section.
evaluate +FLAGS:
    uv run python -m src --only s4_evaluate --s4_evaluate {{ FLAGS }}

# Run only the s5 analysis section (aggregation + figures into partials/).
analysis +FLAGS:
    uv run python -m src --only s5_analysis --s5_analysis {{ FLAGS }}

# Run single-image prediction from trained models.
predict +FLAGS:
    uv run python -m src.s6_predict.pipeline {{ FLAGS }}

# Sync analysis figures from partials/s5_analysis/figures into paper/figures/results/
# (fails loudly if there is no analysis output yet; run `just analysis` first).
figures:
    mkdir -p paper/figures/results
    find partials/s5_analysis/figures -maxdepth 1 -type f \( -name '*.png' -o -name '*.svg' \) -exec cp {} paper/figures/results/ \;

# Compile the manuscript to paper/paper.pdf.
paper:
    typst compile paper/paper.typ

# Compile the Spanish manuscript to paper/paper-es.pdf.
paper-es:
    typst compile paper/paper-es.typ

# Recompile paper/paper.typ on every change.
paper-watch:
    typst watch paper/paper.typ

# Refresh figures, compile both manuscripts, and build deliverables.
report:
    just figures
    just paper
    just paper-es
    just bundle

# Sync the uv environment (installs pyproject + dev dependencies).
sync:
    uv sync

# Lint with ruff.
lint:
    uv run ruff check .

# Check formatting with ruff.
check-format:
    uv run ruff format --check .

# Format code with ruff.
format:
    uv run ruff format .

# Type-check with pyright.
typecheck:
    uv run pyright

# Package paper and source deliverables into zip archives under deliverables/
bundle:
    mkdir -p {{ out }}
    7z a {{ out }}/paper.zip \
      paper/elsearticle \
      paper/references.bib \
      paper/paper.typ \
      paper/paper-es.typ \
      $(find paper/figures -type f \( -name '*.png' -o -name '*.jpg' -o -name '*.svg' \) | sort)
    7z a {{ out }}/code.zip \
      $(git ls-files --cached --others --exclude-standard src/) \
      .python-version \
      pyproject.toml \
      uv.lock \
      README.md \
      flake.nix \
      flake.lock \
      $(git ls-files --cached --others --exclude-standard deps/)
    echo "Done → {{ out }}"
