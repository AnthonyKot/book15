I'll start by reading the review criteria and the essay, then check quotes against the Lem corpus.Next I’ll verify quotes against the corpus, pull the 2026 claim rows, and read the review checklist plus prior essay-5 reviews.The rebuilt essay is the one under review. I’ll gate the quotes, then check the 2026 claims and ledger verdicts.I’ll pull the cited Lem pages and run the quotes through the corpus so I can check accuracy, not just page numbers.# Essay 5 review — findings only

Ranked by severity. Quotes are from `chapters/05-real-means-useful.html`. Corpus checks via `scripts/find.py`.

---

### 1. The competence HIT is a misreading of p. 176, and it cancels the Designer row

**Location:** ledger, problem level — “You can act competently without a theory of why the thing works (pp. 176–179)” / `HIT`. Same claim in the lede: “The builders who arrived dropped both.”

**Problem:** Lem’s sentence on those pages is not that claim. p. 176: the Designer “is not a narrow pragmatist, like a builder who is constructing his house from bricks, uninterested in where these bricks came from and what they are.” He “knows everything about his bricks—except for what they look like when no one is looking at them.” The thing given up is the observer-independent residue, not materials knowledge. “We know far more about the fact that it is possible to act than about how it happens” is immediately fenced by that clause.

The 2026 cell (Zhang 2017: nets fit random labels; Kaplan 2020: loss scales) is the builder Lem excluded: ship it, no account of the bricks. The previous row already scores that gap as `RIGHT ANSWER, WRONG REASON`. This row then awards `HIT` for the same practice under a paraphrase Lem did not write.

**Fix:** Delete the row. If a second problem-level row is needed, quote p. 176 verbatim (“possible to act” / “how it happens”) and do not pay it with Zhang/scaling — those receipts belong only to the bricks-gap row, and that row cannot stay `RIGHT ANSWER, WRONG REASON` while this one is `HIT`.

---

### 2. Designer row: compound claim, inflated verdict

**Location:** “The Designer: `"'real' means the same as 'useful'"` (p. 177), but `"not a narrow pragmatist… knows everything about his bricks"` (p. 176)” / `RIGHT ANSWER, WRONG REASON`. Happened: “Half the Designer arrived.”

**Problem:** §4: one specific claim, one verdict. The row packs the half he got (usefulness as the working criterion) with the half he specified and did not get (know the bricks). `RIGHT ANSWER, WRONG REASON` requires that the outcome match. The outcome that arrived is the figure he contrasted with the Designer. “Where he was worst” already says this; the ledger still credits a right answer.

He also did not forecast a professional type. The Designer is a methodological persona for navigating Scylla/Charybdis, not a prediction that ML labs would adopt pragmatism. Scoring “the Designer arrived” treats a stance as an event.

**Fix:** Split. (a) Dropping definitive questions / real = useful as working method — score that claim alone (`HIT` only if you can show the method, not a cousin slogan). (b) “Knows everything about his bricks” — `MISS` or `OPEN` (interpretability is an attempt, not the arrival). Do not let `WRONG REASON` launder the failed half.

---

### 3. Believing-machines `RIGHT QUESTION, WRONG ANSWER` slides the question and treats “not built” as “wrong”

**Location:** ledger — `"'Believing machines': build homeostats with unprogrammed brains, vary body and world, and read off the metaphysics each grows, 'to help us discover the general principles' (pp. 138–140)"` / `RIGHT QUESTION, WRONG ANSWER`. 2026 cell paid by `othello-2023` and `monosemanticity-2024`.

**Problem:** The quoted purpose on p. 138 is “the general principles that govern the way in which **metaphysical** models of the world come into being” (soul, compensation for a mortal body, inference to a Designer from order — pp. 138–140). The ledger shortens this to “the general principles,” then the 2026 cell restates it as “how a system comes by its picture of the world.” An Othello-board probe and a sparse-autoencoder feature dictionary do not test the growth of metaphysics from a blank-slate homeostat in a constructed world.

`RIGHT QUESTION, WRONG ANSWER` means the dilemma is live and **his resolution is not**. Nobody ran the experiment. An unused method is not a wrong answer. Interpretability of models trained on human text is a different programme, not a refutation.

**Fix:** Object-level `OPEN` (not built; nothing in the receipts rules it out). If a problem-level row is kept, the Lem cell must stay on *metaphysical* models, and the 2026 cell cannot be Othello/SAE. Those markers do not pay this claim.

---

### 4. The ladder is still graded, after being removed from the ledger

**Location:** said — “And then the sentence this essay will have to grade:” + p. 183 (rungs / mountain / “we must not ask whether the ladder is ‘true’”). Happened: “Apply the rule anyway to the machines we build, as this essay does, and it fails” (Othello + SAE). Still open #4: “in a learned model some do.”

**Problem:** pp. 182–183 are about isomorphism between mathematical symbols and nature (and a photograph’s grain). Lem says the ladder can still give height and slope, and that a theory is “true as a whole.” He never said the rungs correspond to nothing, and he did not describe a learned model. The essay admits the transposition is its own, then declares the rule a failure. That is grading 1964-Lem for a claim he did not make. Promising a grade in said and then keeping the verdict only in prose is worse than a ledger `MISS`: the reader still receives the falsification, without a verdict they can contest.

**Fix:** Strike “the sentence this essay will have to grade,” the happened paragraph that says the rule “fails,” and still-open #4. If the analogy is pedagogically useful, label it as the essay’s, not a result.

---

### 5. Synthetic-genome `HIT` is still paid by a rewritten object

**Location:** ledger — “Chromosomes written down … synthesised, and made to run (p. 192)” / `HIT`. Said/happened still quote the “laboratory egg” and embryogenesis.

**Problem:** p. 192 is one sequence: write the egg’s chromosome information, synthesise, “the ‘laboratory egg’ obtained in this way will go into embryogenetic ‘production.’” That is the side entrance into a *human organism* (same page: eye colour, talent matrices, disease-free design). Gibson 2010 assembled a bacterial genome and transplanted it into an existing recipient cell. The 2026 cell admits “Not the ‘laboratory egg’, and no embryogenesis.” `HIT` is “exists/happened substantially as described.” “Made to run” is the essay’s substitute for embryogenetic production. A bacterial transplant is the same *kind* of move (notation → chemistry → a living system), not the object on p. 192.

**Fix:** `EARLY` on the full p. 192 sentence, or a row that quotes only what Gibson instantiated and does not cite the egg/embryogenesis sentence as the Lem cell. Do not `HIT` a claim after deleting the words that make it fail.

---

### 6. No `MISS`, and the chapter’s clean miss is the one the prose already has

**Location:** ledger (2× `HIT`, 3× `OPEN`, 1× `RIGHT QUESTION, WRONG ANSWER`, 2× `RIGHT ANSWER, WRONG REASON`, 0× `MISS`). “Where he was worst”: he “could not imagine the pragmatism arriving without the knowledge”; talent matrices as “flat over-reach.”

**Problem:** AGENT requires a real `MISS` or `RIGHT QUESTION, WRONG ANSWER`, found honestly. The only `WRONG ANSWER` is finding 3. The worst-section claims are not in the ledger. Meanwhile the chapter’s own-voice forecasts that did not happen are either `OPEN` (tissue brain; talent matrices) or ungraded:

- **Designer-with-bricks** (p. 176). The essay’s own diagnosis. That figure did not arrive. If interpretability is only an attempt to buy the half back, this is a `MISS` on the specified constructor, or at minimum not a right answer.
- **p. 193 ranking** (On Imitology, unquoted): control of evolution, regeneration, and “orchestrate genetic traits in fetuses” “will turn out to be possible **long before** we gain the ability to create the chromosome apparatus of a nucleus in an artificial manner.” The essay `HIT`s artificial chromosomes (even bacterial) and leaves the “long before” comparison ungraded. Rankings are not chronologies — but this *is* a ranking Lem made, and AGENT says to read the comparison he actually made.
- **Talent matrices** (p. 192). He treats “comprehensive knowledge of the genetic code” as what unlocks writing musical/mathematical talent into any egg. The cipher was known by the mid-1960s; the mapping of polygenic talents is not a code-table problem. “Where he was worst” says this; the ledger says `OPEN` because of his condition. The miss is the mechanism (code ⇒ traits), not the unmet condition.

On Imitology (pp. 193–196) — the chapter’s named payload, and the essay’s contract job — is not in said, happened, or the ledger: “everything man does is a form of modeling”; design as “amplifier of the states of low probability”; “where Nature is ‘in its element’ as a designer, we are at our weakest.”

**Fix:** Put a `MISS` on the bricks clause or on the p. 193 order (or explain why “nucleus” saves the order *and* still allows the Gibson `HIT`). Quote On Imitology. Do not leave the negative only in a paragraph the ledger does not support.

---

### 7. Two layers mixed

**Location:** believing-machines row (object: an unbuilt apparatus; verdict: problem-level; receipt: interpretability papers). Designer + competence rows (same 2026 practice, two problem-level verdicts, one of them a `HIT`). Homeostat/hallucination row (problem-level `RIGHT ANSWER, WRONG REASON` paid by a paper about exam scoring).

**Problem:** An object that was not built cannot carry `WRONG ANSWER`. Two rows must not score one practice as both right-answer-wrong-reason and `HIT`. Lem’s p. 125 necessity (a living regulator must induce or die) is not the same layer as “models guess because the test awards a point.”

**Fix:** One claim, one layer, one verdict. Unbuilt apparatus → object `OPEN`. Hallucination paper → do not pay p. 125 unless the Lem cell is rewritten to the actual claim (forced induction under threat to existence).

---

### 8. 2026 claims to challenge

Markers exist and have non-`open` rows. The mappings and a few glosses do not.

| Marker / phrase | Challenge |
|---|---|
| `openai-hallucination-2025` paying p. 125 | Paper is real (Kalai et al., arXiv:2509.04664). It does not show a homeostat that must believe or die. Lem distinguishes induction (must) from belief that has escaped verification (metaphysics, p. 125). Hallucination is the second; he did not say every regulator must do it. Outcome-match is a tautology of any decision system. Cut the row or label the analogy; do not `RIGHT ANSWER`. |
| DishBrain “comparable object” | `dishbrain-2022` receipts ~800k cultured neurons in a closed loop. That is not “a comparable object” to an embryo-pruned “artificial brain, created from natural tissue” (p. 191). “Reporting … learned to play Pong” is the authors’ claim and was disputed; “reporting” is fine, “comparable object” is not. |
| AlphaFold “Nobel … for results rather than mechanism” | Hassabis/Jumper shared Chemistry 2024 with Baker (computational *design*, not AlphaFold). The prize is for a method of structure prediction, not “results rather than mechanism.” Drop the gloss. |
| `othello-2023` / `monosemanticity-2024` | Fine for “some internal states are readable.” They do not pay metaphysics, believing machines, or “the ladder rule fails.” SAE: the register already says only a *sample* of features is identified; still-open #4 (“in a learned model some [rungs] do”) oversells. |
| `alphazero-2018` / `model-collapse-2024` as surplus-information evidence | Lem’s question (pp. 188–189) is how a *scientific theory* yields valid predictions nobody inserted. AlphaZero is fed rule-governed self-play outcomes; model collapse is recursive training on model text. Neither is an information-balance on a theory. Leave the question open without these as “evidence both ways.” |
| “those machines arrived” (Shakespeare poems) | 2026 event, no `<!-- CHECK -->`. |
| Absence claims (“Nobody does this,” “Nothing of the kind is done,” “nobody has raised populations”) | Unmarked. Prior panel required receipts for absences. |

`bitter-lesson-2019`, `zhang-2017`, `scaling-laws-2020` (now “model loss,” not capability), `synthetic-genome-2010`, `embryo-screening-2024`, `germline-moratorium-2025` (correctly a *call*), `ai-welfare-2024`, `model-welfare-2025`, `baseline-1964-ch5` (Bohr–Einstein / Brouwer–Hilbert as cited, and as already over as live exchanges) — I would not challenge the facts.

Later Lem: Zylinska p. 21 is cited; afterwords not scored. That is enough given the edition gap. The 2013 text *is* the 1974 4th edition (Zylinska p. 21); the essay still says “1964” throughout. Note it; do not grade 1964 for a 1982 concession that is not on disk.

---

### 9. Reader

A skeptic of “Lem predicted everything” is not persuaded by this ledger. What would persuade: a `MISS` on the constructor he specified, an `EARLY` or narrowed row on the egg, and a believing-machines `OPEN`. What they get instead: two `HIT`s (one on a rewritten genome claim, one on a paraphrase of the builder), two `RIGHT ANSWER, WRONG REASON`s that still award the answer, and a `WRONG ANSWER` for an experiment nobody ran. The title and “That much arrived” do the work the rows cannot. “Where he was worst” is the honest page; it is not the score.
