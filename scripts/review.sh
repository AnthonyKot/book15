#!/usr/bin/env bash
# scripts/review.sh NN — panel review of chapters/NN-*.html.
# grok and agy review independently; codex consolidates, adversarial toward their findings.
# Outputs: drafts/reviews/NN-grok.md, NN-agy.md, NN-codex.md. Check sizes: either
# reviewer may return zero bytes (known intermittent failure) — a run is fine if two of
# three produced text.
set -uo pipefail
cd "$(dirname "$0")/.."
n="${1:?essay number, e.g. 04}"
f=$(ls chapters/${n}-*.html 2>/dev/null | head -1); [ -n "$f" ] || { echo "no chapters/${n}-*.html"; exit 1; }
out=drafts/reviews; mkdir -p "$out"
prompt="$(cat scripts/prompts/review-checklist.md)

The essay file is: $f  (repo root: $(pwd)). Write your findings as markdown."

echo "== grok"; grok --always-approve --max-turns 40 -p "$prompt" > "$out/$n-grok.md" 2>"$out/$n-grok.err" &
echo "== agy";  agy --dangerously-skip-permissions --print-timeout 14m -p "$prompt" > "$out/$n-agy.md" 2>"$out/$n-agy.err" &
wait
for r in grok agy; do printf '  %-5s %6s bytes\n' $r "$(wc -c < "$out/$n-$r.md")"; done

cons="Two reviewers assessed $f independently; their reports are in $out/$n-grok.md and $out/$n-agy.md (either may be empty).
Read CONTEXT.md, AGENT.md, the essay, and both reports. Be adversarial toward the REVIEWERS: for each of their
findings, verify it against the essay and the corpus (scripts/find.py) and mark it CONFIRMED / REJECTED (with why) /
UNVERIFIABLE. Then add findings they both missed. Output one consolidated markdown report, ranked, with a
one-line ship / revise / block verdict at the top."
echo "== codex"; codex exec --skip-git-repo-check -C "$(pwd)" "$cons" < /dev/null > "$out/$n-codex.md" 2>"$out/$n-codex.err"
printf '  codex %6s bytes\n' "$(wc -c < "$out/$n-codex.md")"
echo "reports in $out/"
