**1. Missing MISS (Severity: High)**
- **Location:** "This is why it constantly refers to Nature... 'autonomous apsychic predictors' and the 'intelligent device' are located" (paragraphs 1-2 under "What Lem said").
- **Problem:** The essay praises Lem's Conclusion (pp. 351–352) for basing his hypotheses on the "empirical test" of Nature, but skips the massive predictive failure he makes on those exact same pages. Lem argues that the "chromosomal" (evolutionary) model is vastly superior to the "brain" (intelligence) model in "speed," "capacity," and "universality," predicting that artificial predictors will be built on the chromosomal language because "its lack of intelligence is much more productive than our wisdom." In reality, the AI revolution is built entirely on the "brain" model (neural networks, backpropagation) because evolutionary/genetic algorithms proved hopelessly slow and sample-inefficient. The essay skips this core, failed technological forecast while praising the section. 
- **Fix:** Add a MISS row grading his claim that the chromosomal model will beat the brain model for artificial predictors.

**2. 2026 Claims / Internal Contradiction (Severity: High)**
- **Location:** "Eight essays grade Lem, in eighty-five rows. ... 4 MISS" vs. "Six MISSes stand" (under "Still open") and `<meta name="description" content="... Eighty-two graded rows across eight essays, six MISSes...">`
- **Problem:** The essay contradicts its own statistics. The prose claims 85 rows and 4 MISSes, while the meta description and the "Still open" section claim 82 rows and 6 MISSes. (According to the `CONTEXT.md` logs, the latter is correct: essays 2, 3, 4, 6, and 7 contain a total of exactly 6 MISSes). This is a factual claim about the book's present state that lacks a `<!-- CHECK -->` tag and is demonstrably wrong.
- **Fix:** Update the second paragraph's totals to match the true ledger count (82 rows, 6 MISSes) and adjust the other verdict sums (OPEN, HIT, etc.) so the math is consistent throughout the text.

**3. 2026 Claims Tag Mismatch (Severity: High)**
- **Location:** "Four essays needed three rounds `<!-- CHECK: dor-yeshorim -->`"
- **Problem:** The claim is about the book's internal editorial process (four essays requiring three rounds of panel review). The tag `dor-yeshorim` refers to a Jewish genetic matchmaking program relevant to essay 8. It is completely misplaced here and fails to receipt the claim properly.
- **Fix:** Remove the `dor-yeshorim` tag and receipt the claim properly against the book's own `CONTEXT.md` status logs.

**4. Verdict Inflation (Severity: Medium)**
- **Location:** "Every essay must contain a genuine MISS or RIGHT QUESTION, WRONG ANSWER, found honestly" graded as `RIGHT ANSWER, WRONG REASON`
- **Problem:** The rule demanded a *genuine* MISS. The text immediately admits the rule "produced the book's recurring error: four negatives were manufactured by testing the essay's transposition". Forcing *manufactured* MISSes instead of genuine ones means the rule failed to achieve its stated goal. Calling it "RIGHT ANSWER, WRONG REASON" inflates a methodological failure into a partial success.
- **Fix:** Grade this rule as a MISS, as it forced bad outputs rather than the intended genuine ones and caused the book's recurring error.

**5. Misreading Lem / Vocabulary Error (Severity: Medium)**
- **Location:** "A fixed seven-word verdict vocabulary, one word per row"
- **Problem:** The essay states the vocabulary uses "seven words" and strictly "one word per row". However, the vocabulary consists of seven *verdicts*, two of which are four-word phrases ("RIGHT QUESTION, WRONG ANSWER" and "RIGHT ANSWER, WRONG REASON"). The ledger immediately violates the "one word per row" claim in the rows directly above and below this statement.
- **Fix:** Change "seven-word verdict vocabulary, one word per row" to "seven-verdict vocabulary, one verdict per row".

**6. The Two Layers / Reader Persuasion (Severity: Low)**
- **Location:** The entire self-grading table ("The ledger / This one grades the method rather than the man.")
- **Problem:** A skeptic of the "Lem predicted everything" claim would not be persuaded by this ledger. Applying a rigid vocabulary designed for technological forecasts (HIT, MISS, OPEN) to grade editorial rules ("Never false", "Adversarial review") commits a category error, mixing object-level facts (the rules themselves) with problem-level evaluations. Assigning oneself a "HIT" for separating problem layers reads as rhetorical self-congratulation, undermining the book's claim to be a rigorous, cold grading.
- **Fix:** Remove the self-grading ledger entirely. Replace it with standard prose evaluating the method's successes and failures without forcing them into the forecast verdicts.
