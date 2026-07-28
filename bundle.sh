#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
OUT="$ROOT/deliverables"

mkdir -p "$OUT"

cd "$ROOT"
7z a "$OUT/paper.zip" \
  paper/elsearticle \
  paper/references.bib \
  paper/paper.typ \
  paper/paper-es.typ \
  paper/figures/**/*.{png,jpg,svg}

cd "$ROOT"
7z a "$OUT/code.zip" \
  $(git ls-files --cached --others --exclude-standard src/) \
  .python-version \
  pyproject.toml \
  uv.lock \
  README.md \
  flake.nix \
  flake.lock \
  $(git ls-files --cached --others --exclude-standard deps/) \

echo "Done → $OUT"
