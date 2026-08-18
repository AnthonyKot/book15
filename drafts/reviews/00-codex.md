**Verdict: BLOCK — revise before shipping.**

Consolidated report: [drafts/reviews/00-codex.md](/home/diablo/book15/drafts/reviews/00-codex.md)

Key adjudications:

- Current census is **85 rows / 4 MISSes**; the reviewer claiming 82/6 relied on stale context.
- The proposed chromosomal-computing MISS is **REJECTED** as a corpus misreading.
- Contract-required layer results and ESP/note-10 discussion are missing.
- Three additional issues were found: selection bias behind the DISSOLVED conclusion, an unverifiable comparison with Lem’s unavailable afterwords, and another incorrect “1964” attribution.
- `./verify.sh` passes, but the unrelated Dor Yeshorim receipt demonstrates a semantic gap in the checker.
sus. The meta description, line 54, line 67, and line 78 retain the earlier 82/6 census. This is a blocking never-false failure in the method chapter.

Grok 1 is **CONFIRMED**. Agy 2 is **CONFIRMED only as to the contradiction** and **REJECTED as to which side is correct**: Agy cites an obsolete status-log entry. Do not change 85/4 back to 82/6; update every stale occurrence to 85/4 and receipt the computed census.

### 2. BLOCKER — CONFIRMED: the essay does not perform its exclusive contract

`CONTEXT.md` §6 requires a hit-rate by layer. The chapter gives only the pooled distribution. The actual current split is:

| Layer | Rows | HIT | OPEN | MISS | EARLY | RQWA | RAWR |
|---|---:|---:|---:|---:|---:|---:|---:|
| Object | 50 | 11 | 23 | 4 | 4 | 5 | 3 |
| Problem | 35 | 15 | 14 | 0 | 0 | 6 | 0 |

Thus the plain HIT share is 22% at object level and 43% at problem level. That is the result the two-layer method exists to reveal, and it is materially more informative than the pooled count.

The same authority document assigns the ESP argument at pp. 347–350 and note 10 at p. 371 to essay 0. Both are absent. Corpus inspection confirms the assigned evidence: Lem rejects telepathy because selection should have amplified such a useful channel, then note 10 describes how repeated testing leaves a handful of apparently successful investigators through selection on chance results. This should be presented as an exhibit of his method, not forced into a forecast row.

Grok 7 is **CONFIRMED**.

### 3. HIGH — CONFIRMED: the account of withdrawn negatives collapses several different errors into one

Line 40 says all seven withdrawals had the same cause, “grading the essay's own transposition as Lem's claim”; line 55 instead says four manufactured negatives. The status log records distinct causes:

- essay 1: a reported consensus treated as Lem's forecast, plus a completeness claim he expressly disclaimed;
- essay 3: unlike cost quantities compared;
- essay 5: an ordering scored before either side occurred;
- essay 7: two misreadings of Lem's generate/select and representation arguments;
- essay 8: one-generation embryo selection substituted for partner selection over millennia.

Transposition describes some of these, not all. The “four” and “seven” figures may refer to different subsets, but the essay never defines them. Grok 3 is **CONFIRMED**. Rewrite the history by cause and make every count auditable.

### 4. HIGH — CONFIRMED: the endnote history is stale and internally overclaims

Line 41 says endnotes beat the chapters three times and names notes 8 (chapter 7), 2 (chapter 8), and 6 (chapter 2), then says each changed a verdict. Chapter 8 note 2 sharpened the argument but was already present in the first draft and did not produce the recorded verdict reversal. The later chapter 3 rebuild found the genuinely decision-changing note 3 at pp. 358–359; `CONTEXT.md` calls that the fourth time an endnote decided an essay.

Grok 4 is **CONFIRMED with this distinction**: four notes affected the essays broadly, but only three of the named cases are documented as verdict/thesis changes. Add chapter 3 note 3; describe chapter 8 note 2 as sharpening rather than reversing; then state the count in terms the log supports.

### 5. HIGH — CONFIRMED, plus a missed systemic issue: the receipt audit fails its own test

The marker `<!-- CHECK: dor-yeshorim -->` on “Four essays needed three rounds” is unrelated to review rounds; it receipts a genetic carrier-screening programme. Grok 8 and Agy 3 are **CONFIRMED** on this point. The round claim itself is supported by the repository (essays 4–7 have three review rounds), but not by that receipt.

The reviewers also correctly identify unmarked present-state claims in “What happened”: the census, two shipped misquotes, seven withdrawals, the caveat in all eight essays, and essay 5's verdict distribution. AGENT.md requires every 2026-side factual claim to carry a marker. The chapter does not comply.

Both reviewers missed the larger consequence. `./verify.sh` passes despite the unrelated Dor Yeshorim marker because `checks/claims.py` checks only that an ID exists somewhere in the register; it does not test whether the cited row supports the sentence. The “Never false” method row discusses only the quotation gate's blind spot. It should also admit the claim gate's two demonstrated blind spots: unmarked claims and semantically irrelevant receipts.

### 6. HIGH — MISSED BY BOTH: zero DISSOLVED rows cannot support the conclusion drawn from them

The count is true: none of the selected 85 Lem rows or eight method rows uses DISSOLVED. The inference in line 39 is not: it says this shows that Lem's questions “have not gone away” and that “nothing in [the 1964 framing] became meaningless.” The ledgers are selective, not an exhaustive inventory of every question in the corpus; `CONTEXT.md` explicitly records substantial chapter material left unscored, and chapter 9 is absent altogether.

Absence of DISSOLVED among chosen rows may reveal the selection policy as readily as it reveals Lem. State the bounded result (“none of the 85 selected claims dissolved”) and either audit omitted candidates or leave the broader claim OPEN.

### 7. HIGH — CONFIRMED NARROWLY: “Where he was worst” overstates and misattributes a pattern

Grok 2 is too broad when it says all three examples were withdrawn and no longer survive in the current essays. The current essay 7 still treats executable formalism as the third route Lem did not pose, and essay 8 still treats embryo scoring as a third path outside his couple-level model. Those are live, bounded critiques, not the withdrawn MISS rows.

The finding is nevertheless **CONFIRMED in narrower form**. Essay 0 says “essay 1 named” a habit of choosing the successor that abolished the most; current essay 1 does not name that fourth error and expressly says Lem's list was incomplete rather than wrong. Moreover, the polymer and partner examples establish unforeseen third routes, not necessarily a preference for the “more impressive machine.” Keep them only as this chapter's proposed pattern, label the inference as its own, and do not present it as the finding of essay 1.

### 8. MEDIUM — CONFIRMED NARROWLY: “He asked for this book / This is that edition” is not what the source says

The p. 20 corpus sequence is: Lem preferred not to change *Summa* unnecessarily; **yet** he would gladly publish a critical edition containing **his** commentary on his 1960s writing. Essay 0 is an outside grader, not Lem's marginal commentary. The ellipsis in line 33 joins genuine words and is not a fabricated quotation, so Grok 6 overstates matters by saying it reverses the quotation. But the lede and line 66 turn an analogy into an identity claim.

Grok 6 is **CONFIRMED narrowly**. Call this book a substitute or answer to the proposed edition, not “that edition” and not the book he asked for.

### 9. MEDIUM — CONFIRMED: the dating commitment cannot receive MISS under the book's definition

MISS means that the described outcome did not happen and has no live path. The project did date its baselines, initially used the wrong date, and then corrected all eight essays. That process failure is serious, but “no live path” is affirmatively false.

Grok 5 is **CONFIRMED**. If the forecast vocabulary is retained for editorial commitments, RIGHT QUESTION, WRONG ANSWER best fits the evidence. This also illustrates why the self-ledger needs an explicit mapping from forecast verdicts to method commitments.

### 10. MEDIUM — MISSED BY BOTH: the essay claims two gradings disagree while saying the comparison texts are unavailable

Line 60 says “The two gradings disagree.” Lines 32 and 77 say the afterwords are absent and call them the only direct check on whether this book is harsher than Lem's own. Zylinska reports the afterwords' promotional aim; that does not establish Lem's row-by-row judgements or demonstrate disagreement on these four MISSes and 37 OPENs.

Change the application cell to what is verifiable: this grading is less celebratory than the purpose Zylinska attributes to the afterwords; direct disagreement remains UNVERIFIABLE until the texts are obtained.

### 11. MEDIUM — MISSED BY BOTH: the chapter repeats the dating error immediately before confessing it

Line 39 attributes the surviving framing to “1964.” The Conclusion used as the chapter's methodological anchor is signed “Krakow, August 1966” on p. 352, and the English corpus follows the altered 1974 edition. The chapter cannot determine from this corpus alone which framing was present in the 1964 text.

Use “the 1960s text as revised in 1974” or another bounded formulation. This is especially important in the paragraph that claims the date-sensitive method held up.

### 12. LOW — CONFIRMED: two mechanical wording/template failures

First, “seven-word vocabulary, one word per row” is literally false: there are seven **verdicts**, and two are multiword verdicts. Agy 5 is **CONFIRMED**; use “seven-verdict vocabulary, one verdict per row.”

Second, the section counts are 472 words for “What Lem said” against the template's approximate 600–900, and 732 for “What happened” against its 700-word ceiling. Grok 9 is **CONFIRMED on the template breach and the overbroad pp. 351–352 kicker**. It is **REJECTED insofar as it implies the contract requires a new technological grade from p. 352**: essay 0's exclusive job is the method and cross-essay pattern, not another object-level Conclusion forecast.

## Rejected or unverifiable reviewer proposals

### Agy 1 — REJECTED: add a chromosomal-model MISS

This proposed MISS misreads pp. 351–352 and supplies no adequate 2026 receipt. Lem says synthetic brains may become “inducers of theory formation”; he then says using chromosomal systems for that task would be “extremely difficult” and might be impossible, though their material efficiency makes experimentation tempting. He does not predict that chromosomal computation will displace neural networks in AI. “The AI revolution is built entirely on the brain model” is also too crude to test his comparison of matter, information, reproduction, and prediction. Do not add this row.

### Agy 4 — REJECTED: change the mandatory-negative rule to MISS

The rule's stated outcome is that every essay finish with an honest MISS or RQWA, and the current essays do. Review caught the manufactured candidates. RIGHT ANSWER, WRONG REASON is defensible if the essay explains that the pressure created bad intermediate claims and adversarial review, not the requirement alone, produced the honest final result. The stale four/seven history must still be fixed.

### Agy 6 — REJECTED: delete the self-grading ledger

The claim of a category error is an aesthetic judgement, not a demonstrated breach. `TEMPLATE.md` requires a ledger, and the authority contract requires the method to be stated and defended. The specific bad mapping (dating → MISS) should be repaired; it does not justify removing the apparatus.

### Grok 10 — REJECTED: the essay 8 cultural-authority row disproves layer separation

That row describes a forecasted social state—machine matchmaking becoming a norm—and can reasonably sit at object level. More importantly, the example named in essay 0 really does separate the built partner-screening device (HIT), the trait menu on another object (EARLY), and the associated dilemmas. The reviewer identifies no laundering of an object miss into a problem hit. The missing aggregate layer report is the real defect.

### Grok 11 — UNVERIFIABLE as a separate finding

The reader-response paragraph is a plausible impact summary, not an independently testable claim. Its factual premises are adjudicated above; its prediction of what a skeptic will conclude cannot be verified from the essay or corpus.

## Minimum revision set

1. Synchronize every count to 85 Lem rows / 4 MISSes / 93 including method rows and add a proper internal census receipt.
2. Add the object/problem distribution and the assigned ESP/note-10 method exhibit.
3. Rewrite the withdrawal and endnote histories from the status log, separating causes and counts.
4. Receipt all current-state claims; replace the Dor Yeshorim marker; expand the “Never false” row to acknowledge semantic receipt failure.
5. Bound the DISSOLVED inference, the “critical edition” rhetoric, the impressive-successor pattern, and the alleged disagreement with unavailable afterwords.
6. Correct the dating verdict, the 1964 formulation, “seven-verdict” wording, and section lengths.

After those changes, regenerate essay 0's quote rows and rerun `./verify.sh`; the current run passes (407 corpus quotations, 120 claim IDs, links and count sync), but the pass itself demonstrates that the checker cannot catch the semantic receipt error above.
