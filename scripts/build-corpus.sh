#!/usr/bin/env bash
# Rebuild resources/text/summa.txt from a local PDF of
# Lem, Summa Technologiae, trans. Joanna Zylinska (Minnesota, 2013), 383 pp.
# PDF page N == printed page N in that file, which is what checks/quotes.tsv cites.
set -euo pipefail
cd "$(dirname "$0")/.."
src="${1:-resources/lem-summa-2013.pdf}"
[ -f "$src" ] || { echo "no PDF at $src"; exit 1; }
mkdir -p resources/text
pdftotext -layout "$src" resources/text/summa.txt
n=$(python3 -c "print(open('resources/text/summa.txt').read().count('\f'))")
echo "extracted $n page breaks -> resources/text/summa.txt (expect 383)"
