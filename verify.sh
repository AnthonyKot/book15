#!/usr/bin/env bash
# Book 15 — standing verification. Run from anywhere: ./verify.sh [essay-no] [--structure] [--strict]
#
#   checks/quotes.py     every Lem quotation is on its cited page        GATING
#   checks/claims.py     every 2026 claim marker has a row, and back     GATING (open rows: advisory)
#   internal links       entirely inside this repo                       GATING
#   count sync           contents page vs chapters on disk               GATING
#   checks/structure.py  TEMPLATE beats + word bounds                    ADVISORY (--strict gates)
#
# Quotes are gating here, unlike book 7, because the corpus is a fixed edition of a
# fixed book: nothing upstream can drift. What a green run proves: every Lem line
# quoted was written by Lem, where we say. It does NOT prove our reading of him is
# fair, or that our account of 2026 is right — that is claims-2026.tsv's job, and
# it is checked by a human, not by this script.
set -u
cd "$(dirname "$0")"
fail=0; FILTER=""; STRUCT=0; STRICT=""
for a in "$@"; do case "$a" in --structure) STRUCT=1;; --strict) STRICT=--strict;; *) FILTER="$a";; esac; done
[ -f resources/text/summa.txt ] || { echo "no corpus — run scripts/build-corpus.sh <pdf>"; exit 1; }

echo "== Lem quotations vs corpus (gating) =="
python3 checks/quotes.py $FILTER || fail=1
echo "== 2026 claim markers vs register (gating) =="
python3 checks/claims.py || fail=1
echo "== count sync (computed, not typed) =="
files=$(ls chapters/*.html 2>/dev/null | wc -l | tr -d ' ')
links=$(grep -oE 'href="chapters/[0-9][^"]*\.html"' index.html 2>/dev/null | sort -u | wc -l | tr -d ' ')
echo "  $files essay files on disk; $links linked from index.html"
[ "$files" = "$links" ] || { echo "  FAIL"; fail=1; }
echo "== internal links (gating) =="
python3 - <<'PY' || fail=1
import glob, os, re, sys
bad = 0
for f in glob.glob('**/*.html', recursive=True):
    for m in re.findall(r'(?:href|src)="([^"#?:]+)"', open(f, encoding='utf-8').read()):
        if m.startswith(('http', '//', 'mailto')): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), m))):
            print("  BROKEN  %s -> %s" % (f, m)); bad += 1
print("  %d broken link(s)" % bad); sys.exit(1 if bad else 0)
PY
if [ $STRUCT = 1 ]; then echo "== structure (advisory) =="; python3 checks/structure.py $STRICT || fail=1; fi
[ $fail = 0 ] && echo "PASS" || { echo "FAIL"; exit 1; }
