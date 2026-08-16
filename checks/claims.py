#!/usr/bin/env python3
"""Every <!-- CHECK: id --> in a chapter has a row in claims-2026.tsv and vice versa;
report rows still 'open' (advisory) — a shipped essay with open rows is unverified."""
import glob, os, re, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
rows = {}
for line in open(os.path.join(here, "claims-2026.tsv"), encoding="utf-8"):
    if not line.strip() or line.startswith("#"): continue
    f = line.rstrip("\n").split("\t")
    if len(f) < 5: print("  MALFORMED  " + line[:60]); continue
    rows[f[1]] = f
markers = {}
for path in glob.glob(os.path.join(root, "chapters", "*.html")):
    for m in re.findall(r"<!--\s*CHECK:\s*([A-Za-z0-9_.-]+)", open(path, encoding="utf-8").read()):
        markers.setdefault(m, []).append(os.path.basename(path))
bad = 0
for m in sorted(set(markers) - set(rows)):
    print("  NO ROW     %s  (%s)" % (m, ", ".join(markers[m]))); bad += 1
for r in sorted(set(rows) - set(markers)):
    print("  NO MARKER  %s" % r); bad += 1
opens = [k for k, f in rows.items() if f[4].strip() == "open" and k in markers]
for k in sorted(opens): print("  OPEN       %s  %s" % (k, rows[k][2][:60]))
print("  %d marker(s), %d row(s), %d mismatch(es), %d open in shipped essays" % (len(markers), len(rows), bad, len(opens)))
sys.exit(1 if bad else 0)
