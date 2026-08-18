#!/usr/bin/env python3
"""Secondary-source quotations (scholarship, not Lem) must appear in their cited source.
Same discipline as checks/quotes.py, different corpus: the Lem gate cannot see these,
so without this they would be ungated -- the blind spot essay 0 records."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
from corpus import norm
SRC = os.path.join(HERE, "..", "resources", "text")
cache = {}
def text(key):
    if key not in cache:
        p = os.path.join(SRC, key + ".txt")
        cache[key] = norm(open(p, encoding="utf-8").read()) if os.path.exists(p) else None
    return cache[key]
bad = n = 0
missing = set()
for line in open(os.path.join(HERE, "secondary.tsv"), encoding="utf-8"):
    if not line.strip() or line.startswith("#"): continue
    f = line.rstrip("\n").split("\t")
    if len(f) < 3: print("  MALFORMED  " + line[:60]); bad += 1; continue
    essay, key, q = f[0], f[1], f[2]
    hay = text(key)
    if hay is None:
        missing.add(key); continue          # source not present locally: skip, don't fail
    n += 1
    if norm(q) not in hay:
        print("  MISS  essay %s  %s  %r" % (essay, key, q[:70])); bad += 1
for k in sorted(missing): print("  SKIPPED (source not local)  %s" % k)
print("  %d secondary quote(s) checked, %d miss(es)" % (n, bad))
sys.exit(1 if bad else 0)
