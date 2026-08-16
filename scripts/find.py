#!/usr/bin/env python3
"""Search the Summa corpus and print page + section for every hit.

    scripts/find.py "intelligence amplifier"
    scripts/find.py -p 107            # dump printed page 107
    scripts/find.py -s "The Black Box" # dump one section

Use this to write checks/quotes.tsv rows: the page it prints is the page the
row must cite. Matching is whitespace- and quote-mark-insensitive, like verify.sh.
"""
import re, sys
from corpus import load, norm

pages, sections = load()

def page_section(n):
    cur = "?"
    for start, title in sections:
        if start <= n: cur = title
        else: break
    return cur

if len(sys.argv) < 2:
    print(__doc__); sys.exit(0)
if sys.argv[1] == "-p":
    n = int(sys.argv[2]); print("== p.%d [%s]" % (n, page_section(n))); print(pages[n]); sys.exit(0)
if sys.argv[1] == "-s":
    want = sys.argv[2].lower()
    for i, (start, title) in enumerate(sections):
        if title.lower() == want:
            end = sections[i + 1][0] if i + 1 < len(sections) else len(pages)
            for n in range(start, end):
                print("== p.%d" % n); print(pages[n])
            sys.exit(0)
    print("no section named", sys.argv[2]); sys.exit(1)

needle = norm(" ".join(sys.argv[1:]))
hits = 0
for n, text in pages.items():
    flat = norm(text)
    i = flat.find(needle)
    while i >= 0:
        hits += 1
        ctx = flat[max(0, i - 80): i + len(needle) + 80]
        print("p.%-4d [%s]\n    …%s…" % (n, page_section(n), ctx))
        i = flat.find(needle, i + 1)
print("%d hit(s)" % hits)
