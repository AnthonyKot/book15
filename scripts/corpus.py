"""Shared corpus loader: printed page -> text, and the section map from the TOC."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TXT = os.path.join(HERE, "..", "resources", "text", "summa.txt")

def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("­", "")
    s = re.sub(r"-\s*\n\s*", "", s)          # rejoin hyphenated line breaks
    return re.sub(r"\s+", " ", s).strip().lower()

def load():
    raw = open(TXT, encoding="utf-8").read()
    chunks = raw.split("\f")
    pages = {i + 1: chunks[i] for i in range(len(chunks))}   # PDF page N == printed page N
    # Section map from the back-matter contents listing ("Title   123").
    sections = []
    toc = raw[raw.rfind("Table of Contents"):]
    for m in re.finditer(r"^\s*(\d\. )?([A-Z][^\n]*?)\s{2,}(\d{1,3})\s*$", toc, re.M):
        title, pg = m.group(2).strip(), int(m.group(3))
        if title in ("CONTENTS",): continue
        sections.append((pg, (m.group(1) or "") + title))
    sections.sort()
    return pages, sections
