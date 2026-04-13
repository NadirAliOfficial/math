#!/bin/bash
set -e

FILE="${1:-questions.tex}"

if [ ! -f "$FILE" ]; then
  echo "Error: $FILE not found"
  exit 1
fi

tectonic "$FILE"

PDF="${FILE%.tex}.pdf"
echo "Built: $PDF"

# Auto-open on macOS
if [ "$(uname)" = "Darwin" ]; then
  open "$PDF"
fi
