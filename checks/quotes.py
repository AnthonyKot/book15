#!/usr/bin/env python3
"""Every Lem quotation in checks/quotes.tsv must appear on its cited page (±1)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from corpus import load, norm
pages, _ = load()
flt = sys.argv[1] if len(sys.argv) > 1 else None
bad = n = 0
for line in open(os.path.join(os.path.dirname(__file__), "quotes.tsv"), encoding="utf-8"):
    if not line.strip() or line.startswith("#"): continue
    f = line.rstrip("\n").split("\t")
    if len(f) < 3: print("  MALFORMED  " + line[:60]); bad += 1; continue
    essay, page, q = f[0], int(f[1]), f[2]
    if flt and essay != flt: continue
    n += 1
    hay = norm(pages.get(page, "") + " " + pages.get(page + 1, ""))
    if norm(q) not in hay:
        # find where it actually is, if anywhere
        where = [p for p, t in pages.items() if norm(q) in norm(t)]
        print("  MISS  essay %s p.%d  %r%s" % (essay, page, q[:70], ("  (found on p.%s)" % where if where else "  (NOT IN CORPUS)")))
        bad += 1
print("  %d quote(s) checked, %d miss(es)" % (n, bad))
sys.exit(1 if bad else 0)
