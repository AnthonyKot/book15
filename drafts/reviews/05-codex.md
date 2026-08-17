**BLOCK — the chapter’s central equation of Lem’s Designer with modern ML misreads the corpus, and most ledger verdicts remain unsupported or misclassified.**

## Ranked findings

### 1. The central “Designer won” thesis contradicts Lem’s Designer

At [line 39](/home/diablo/book15/chapters/05-real-means-useful.html:39), Sutton’s bitter lesson is presented as Lem’s Designer made real. But p. 176 explicitly says:

> “The designer is not a narrow pragmatist, like a builder … uninterested in where these bricks came from and what they are.”

He “knows everything about his bricks” except their observer-independent appearance. Modern scaling succeeds precisely by reducing human understanding of the domain and leaves learned internals unexplained. Sutton is therefore a revealing contrast or cousin, not a direct `HIT`.

This affects the lede, “The Designer won,” both first problem-level rows, and the conclusion. Quote the “not a narrow pragmatist” qualification and rebuild the thesis around the gap between Lem’s knowledgeable constructor and the empirical training loop.

The title also depends on Zylinska’s “Designer,” yet her p. 21 warning that Polish *Konstruktor* carries engineering connotations is omitted, contrary to AGENT’s translation rule.

### 2. The ladder `MISS` remains a category error

Pages 182–183 concern strict isomorphism between mathematical symbols and physical reality. Lem says the ladder can reveal the mountain’s height and inclination, then says a photograph or theory is “true as a whole” without every grain or symbol having a physical double.

Othello probes and sparse-autoencoder features test decodable states inside a constructed computational artifact. They do not falsify Lem’s rejection of symbol-by-symbol isomorphism between mathematics and nature. The row even admits that “this essay applies the rule to a learned model,” which disqualifies `MISS`: Lem did not describe that object.

The “Where he was worst” claim that “If the rungs corresponded to nothing, none of that could work” is a straw man; Lem never said they corresponded to nothing. Remove the row or label it as an analogy, probably `OPEN` or at most `RIGHT QUESTION, WRONG ANSWER`.

### 3. The three biological object rows do not support their verdicts

- **Synthetic genome — `HIT`:** Lem’s sequence ends with synthesized chromosomes placed into a “laboratory egg” for embryogenesis. Gibson synthesized a bacterial genome and transplanted it into an existing recipient cell. That is a substantial partial realization, but not the complete object stated in the Lem cell. Narrow the Lem claim or use `EARLY`.

- **Artificial brain — `EARLY`:** Lem specifies starting an egg, pruning the embryo, transferring the neuron preparation, and combining brain parts. DishBrain cultured human and rodent neurons on an electrode array. It is a cousin, not “his apparatus at a fraction of his ambition”; the cited evidence supplies no dated path through Lem’s embryogenetic method. Use `OPEN` unless a closer receipt is found.

- **Talent matrices — `MISS`:** The prediction is conditional on “comprehensive knowledge” of genetic codes for talents. Germline editing remains a live technical path, so `MISS` fails CONTEXT’s “no live path” condition. More seriously, “No one can embed a trait” is unmarked and broader than the receipts: embryo screening establishes selection, while the societies merely **called for** a moratorium. The prose incorrectly turns that call into editing “sit[ting] under a moratorium.” Use `OPEN`/`EARLY`, narrow it to complex talents, or defer it to essay 8.

Thus the new literal coverage addresses agy’s missing-material complaint structurally, but it still does not supply a defensible `MISS`.

### 4. GraphCast remains an object-layer `HIT` for something Lem did not predict

Page 187 describes a structural tradeoff: adding separate memory and randomness makes an electric brain’s outputs resemble a biological brain while its implementation becomes less similar. GraphCast’s forecast score does not test that tradeoff or show that “adding variables” caused divergence.

The row also widens its register receipt: `graphcast-2023` says ECMWF HRES was the leading **operational deterministic** system; the essay calls it the leading “physics-based system.” Move this to the problem level as a clearly labelled illustration, or remove the verdict. A performance result cannot pay Lem’s modelling-relation claim.

### 5. Both belief verdicts inflate analogies into forecasts

- **Homeostat → hallucination, `HIT`:** Lem’s homeostat acts on uncertainty because refraining would stop the life process. OpenAI’s paper argues that models guess because exam-like scoring rewards guesses over abstention. The essay itself calls this only “formally similar.” The outcome is analogous but the mechanism and kind of system differ; `RIGHT ANSWER, WRONG REASON` is the strongest available verdict.

- **Religious machine demanding rights, `EARLY`:** The receipts are a human-authored welfare argument and a lab research programme. Neither is a machine adopting a religion and demanding equal rights from its practitioners, nor a dated path to one. This is `OPEN` at the object level. A separate problem-level claim about moral-status discourse could be scored differently.

The neighbouring believing-machines `OPEN` is semantically reasonable, but its assertions—“Not built,” “nothing rules it out,” and training-text belief being the only deployed alternative—have no marker or register receipt.

### 6. The benchmark row changed vocabulary but still grades an omission as a claim

Changing `RIGHT QUESTION, WRONG ANSWER` to `OPEN` removed the worst verdict inflation, but not the mismatch. Lem dismisses questions that can never be experimentally settled. Benchmark saturation and contamination concern how to conduct a valid experiment; they do not test that rule.

“He never asks what maintains the experiment” is an omission authored by the essay, not a specific Lem claim that can receive a verdict. Keep the benchmark crisis as a criticism of pragmatic practice, but remove it from the ledger unless a genuine Lem proposition is identified.

### 7. The “surplus information” `OPEN` has irrelevant receipts

Lem asks how a scientific theory yields valid predictions not knowingly inserted into it. AlphaZero receives continuous information from rule-governed self-play and evaluation; model collapse concerns recursive training on generated data. Neither receipts the status of Lem’s information-accounting question, and “unresolved in both directions” appears in neither register row.

`OPEN` may be correct, but the row needs evidence directly addressing structural information or should remain only in “Still open.”

### 8. Claim-register compliance is substantive, not merely mechanical

All 19 unique markers have rows and `claims.py` passes, but several claims exceed their rows:

- `scaling-laws-2020` receipts smooth scaling of **language-model loss**; the prose claims “capability” follows that curve.
- `graphcast-2023` is widened from leading deterministic HRES to the leading physics-based system.
- `germline-moratorium-2025` receipts a societies’ call, not an operative moratorium.
- `monosemanticity-2024` collapses extraction of a million-feature dictionary into millions of demonstrated, nameable, causally understood features.

Material unmarked claims include “the default method of a field,” “most-quoted position statement,” Sutton never needing to read Lem, “No one can embed a trait,” the unbuilt-homeostat absence claim, and “the weakest joint in the field.”

### 9. Quote gating is incomplete and two page references are wrong

The ledger’s biological quotations are absent from `checks/quotes.tsv`, including:

- “side entrance”
- “on a piece of paper, in the symbolic language of chemistry”
- “artificial brain, created from natural tissue”
- “talent matrices” / “embed traits chosen by parents”

`find.py` places both “side entrance” and the chromosome-writing sentence on p. 192. The essay cites the former as pp. 190–191 and the latter as p. 191. The conceptual discussion begins earlier, but the quoted words must carry p. 192 under the project’s own rule.

`verify.sh` passes because it confirms registered rows occur in the essay; it does not detect unregistered quotations.

### 10. Later Lem’s self-grade is missing

Zylinska’s introduction, p. 21, says the 1982/1991 essays updated *Summa* with later equivalents including synthetic biology. The chapter awards the synthetic-genome result without acknowledging that later Lem had already claimed this territory. AGENT requires the later self-grade whenever relevant.

Attribute this cautiously—the introduction does not identify the exact passage or separate the two afterwords—but do not grade 1964 Lem as though he never returned to the claim.

## Ledger audit

| Current row | Audit |
|---|---|
| Synthetic genome — `HIT` | Partial realization; narrow claim or `EARLY` |
| Embryonic artificial brain — `EARLY` | Receipt is a different apparatus; `OPEN` |
| Talent matrices — `MISS` | Live path and unmet condition; `OPEN`/`EARLY` |
| Modelling/GraphCast — `HIT` | Wrong receipt and wrong layer |
| Believing-machine experiment — `OPEN` | Verdict plausible; 2026 cell unreceipted |
| Religious machine demands rights — `EARLY` | Human discussion is not the event; `OPEN` |
| Designer/Sutton — `HIT` | Contradicts p. 176 |
| Competence without theory — `HIT` | Potentially defensible after narrowing; scaling receipt says loss, not capability |
| Homeostat/hallucination — `HIT` | Mechanism swap; at best `RIGHT ANSWER, WRONG REASON` |
| Experiment/benchmarks — `OPEN` | Different question; remove from ledger |
| Ladder/interpretability — `MISS` | Essay-authored transposition; invalid `MISS` |
| Surplus information — `OPEN` | Verdict plausible; receipts do not test the question |

## Re-check of agy’s six acted-on findings

| Earlier finding | Current result |
|---|---|
| AlphaFold side entrance | **Mostly fixed:** no longer the ledger `HIT` and labelled “looser”; residual biological row and page problems remain |
| Ladder transposition | **Not fixed:** admission added, but `MISS` and direct-falsification rhetoric remain |
| Benchmark verdict | **Partly fixed:** changed to `OPEN`, but the row still grades a different question |
| GraphCast “beat” | **Not fixed:** wording is more precise, but performance still pays the wrong claim at the wrong layer |
| Bohr–Einstein | **Fixed:** now correctly described as long over in 1964 |
| Missing `MISS` | **Coverage added, verdict not fixed:** the new biological rows do not support `MISS` under §4 |
