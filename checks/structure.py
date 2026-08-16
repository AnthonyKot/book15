#!/usr/bin/env python3
"""Structural lint: TEMPLATE.md beats present, word bounds, chapter nav.
Advisory unless --strict. It cannot tell a fair verdict from an unfair one."""
import glob, html, os, re, sys
CEILING, FLOOR = 3200, 1800
REQUIRED = {
    "lede": r'<p class="lede">',
    "what-lem-said section": r'<section class="said">',
    "what-happened section": r'<section class="happened">',
    "verdict ledger": r'<table class="ledger">',
    "where-lem-was-better section": r'<section class="better">',
    "still-open section": r'<section class="open">',
    "reading box": r'<div class="reading">',
    "chapter nav": r'<nav class="chapter-nav">',
}
strict = "--strict" in sys.argv
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
bad = 0
for path in sorted(glob.glob(os.path.join(root, "chapters", "*.html"))):
    raw = open(path, encoding="utf-8").read()
    body = re.sub(r"(?is)<(script|style|head|header|footer|nav).*?</\1>", " ", raw)
    body = re.sub(r"(?is)<div class=\"reading\">.*?</div>", " ", body)
    words = len(html.unescape(re.sub(r"<[^>]+>", " ", body)).split())
    probs = [k for k, rx in REQUIRED.items() if not re.search(rx, raw)]
    if not FLOOR <= words <= CEILING: probs.append("%d words (bounds %d-%d)" % (words, FLOOR, CEILING))
    name = os.path.basename(path)
    if probs: bad += 1; print("  %-32s %s" % (name, "; ".join(probs)))
    else: print("  %-32s ok (%d words)" % (name, words))
sys.exit(1 if (bad and strict) else 0)
