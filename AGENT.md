# AGENT.md — instructions for the writing model (book 15)

## Who is reading
An adult who has heard "Lem predicted everything" and is suspicious of it. They have used
an LLM, may own a headset, read the news about CRISPR babies. They have not read *Summa*
and will not — the essay must carry enough Lem, verbatim, that they don't need to. They
will check a claim if it looks too neat.

## Priority stack (higher wins on conflict)
1. **Never false.** Lem quoted verbatim, paged, gated. 2026 claims receipted. No numbers
   from memory. Being boring is a failure; being wrong is a betrayal.
2. **Grade, don't celebrate.** Every essay must contain at least one MISS or RIGHT
   QUESTION, WRONG ANSWER, found honestly. If none exists, the essay says why that
   chapter is different — and the panel is told to attack that.
3. **The two layers stay separate.** Object-level and problem-level are scored in
   different ledger rows. "He got the idea" never launders "he got the thing wrong."
4. **The reader must be able to feel 1964.** Give the state of the art Lem was
   extrapolating from (vacuum tubes to transistors, Ashby, Shannon, Wiener, Sputnik-era
   SETI) so the reader can see the distance, not just the endpoint.

## Verdict rules
- Use CONTEXT §4 vocabulary exactly. One verdict per row. Rows are specific + paged.
- When Lem re-graded himself (1982/1991), score against the later Lem too and say so.
- Distinguish *Lem said* from *Zylinska translated*; check the Polish term when the
  English is doing work (imitology, phantomatics, "intelectronics").
- The "still open" section is not a dumping ground: each open item names what
  evidence would close it.
- Score Lem's *arguments* as arguments. When he builds a case to knock it down (he
  says "reductio" on p. 120; the Superphantomat p. 207–8 is another), the object-level
  row is not "he predicted X"; the row is the mechanism inside the reductio, at problem
  level. Grade his own-voice forecasts (e.g. Coordinators, p. 158) separately.
- A thing being *reported* is not the thing being *true*: a paper that argues a
  scenario, a lawsuit that alleges a practice, a demo that shows a capability — each
  receipts exactly what it is (a proposal, an allegation, a demo) and no more. HIT needs
  the event; otherwise OPEN or EARLY with the receipt described honestly.
- Rankings are not chronologies; a "harder" is not a "later". Read the comparison
  Lem actually made before scoring what happened to it (panel lesson, essay 6).
- Read the endnotes for the chapter before drafting it (`pages 340-383`). They are not
  citations: several are essays in which Lem grades his own proposal, and where they
  disagree with the chapter body the note is usually the better forecast. Note 8 to
  ch. 7 supplies the second selector the chapter lacks and three dated, checkable
  predictions; missing it made essay 7 score the wrong argument (panel lesson, essay 7).

## After any prose edit, regenerate the essay's quote rows
`checks/quotes.py` only checks quotations that have a row in `checks/quotes.tsv`. A quotation
you introduced or reworded and never registered is invisible to the gate — `verify.sh` will
go green over a misquote. Rebuild the essay's rows from the HTML after editing (extract every
"…" span, locate it in the corpus, write one row per fragment and per page for quotes that
span a page break), and read the unmatched list by eye: real misquotes hide among the
quote-pairing artifacts. This caught "we need some restraint" for "We thus need some
restraint" (p. 176) in essay 5, introduced while trimming for length.

## Pitch before writing (the guinea-pig gate)
Never drafted cold. For each essay present the user 2–4 candidate angles, ≤4 sentences
each: the Lem passage that anchors it (paged), the 2026 fact it meets, and the verdict
tension. The user picks; the rest are banked in `drafts/NN.pitches.md`.

## Pre-ship test (all five or don't ship)
1. Does the essay quote Lem enough that a reader could disagree with *our reading* of
   him from the quotes alone?
2. Is there a real MISS or WRONG-ANSWER row, argued, not token?
3. Is every 2026 claim marked `<!-- CHECK: id -->` with a non-`open` row?
4. Would someone who admires Lem and someone who thinks he's overrated both find the
   ledger fair? (Panel question.)
5. Dinner test: can the reader say in one sentence what Lem got right *and* wrong here,
   without saying "he was ahead of his time"?

## Panel (review)
`scripts/review.sh N` — grok and agy review independently against
`scripts/prompts/review-checklist.md`; codex consolidates and is adversarial toward
*their* findings. Always check output size (either may return zero bytes). Findings go
to `drafts/reviews/NN-*.md`; the essay is revised, and the correction is logged in
CONTEXT §8.

## Generation economy
Read the Lem chapter (`scripts/find.py -s "<Section>"`) before pitching. Write the
ledger *before* the prose — the rows are the argument; prose that precedes them
rationalises. Essay 0 last.
