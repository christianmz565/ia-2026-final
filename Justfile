out := "deliverables"

default:
    just --list

pipeline +ARGS:
    uv run python -m src {{ ARGS }}

prepare +FLAGS:
    uv run python -m src --only s1_prepare --s1_prepare {{ FLAGS }}

augments +FLAGS:
    uv run python -m src --only s2_augments --s2_augments {{ FLAGS }}

train +FLAGS:
    uv run python -m src --only s3_train --s3_train {{ FLAGS }}

evaluate +FLAGS:
    uv run python -m src --only s4_evaluate --s4_evaluate {{ FLAGS }}

analysis +FLAGS:
    uv run python -m src --only s5_analysis --s5_analysis {{ FLAGS }}

predict +FLAGS:
    uv run python -m src.s6_predict.pipeline {{ FLAGS }}

figures:
    mkdir -p paper/figures/results
    find partials/s5_analysis/figures -maxdepth 1 -type f \( -name '*.png' -o -name '*.svg' \) -exec cp {} paper/figures/results/ \;

paper:
    typst compile paper/paper.typ

paper-watch:
    typst watch paper/paper.typ

paper-latex:
    latexmk -pdf -cd -interaction=nonstopmode paper/latex/paper.tex

paper-marked:
    sed -i 's/\\showdiffs\(true\|false\)/\\showdiffstrue/' paper/latex/versioning.tex
    just paper-latex

paper-clean:
    sed -i 's/\\showdiffs\(true\|false\)/\\showdiffsfalse/' paper/latex/versioning.tex
    just paper-latex

paper-diff REF="HEAD~1":
    git show {{ REF }}:paper/latex/paper.tex > paper/latex/.paper_old.tex
    latexdiff --preamble=paper/latex/diff_preamble.tex --math-markup=whole \
      paper/latex/.paper_old.tex paper/latex/paper.tex > paper/latex/paper-diff.tex
    rm -f paper/latex/.paper_old.tex
    latexmk -pdf -cd -interaction=nonstopmode paper/latex/paper-diff.tex

report:
    just figures
    just paper
    just bundle

sync:
    uv sync

lint:
    uv run ruff check .

check-format:
    uv run ruff format --check .

format:
    uv run ruff format .

typecheck:
    uv run pyright

bundle:
    mkdir -p {{ out }}
    7z a {{ out }}/paper.zip \
      paper/elsearticle \
      paper/references.bib \
      paper/paper.typ \
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
