BLOCK — consolidated report written to [drafts/reviews/04-codex.md](/home/diablo/book15/drafts/reviews/04-codex.md).

It dispositions every reviewer finding and adds two missed issues, including the stale Article 14 claim. `verify.sh` passes mechanically, but the substantive verdict and sourcing problems remain.
 says has “arrived”

**Location:** “Human oversight of high-risk systems is now a legal requirement in the EU (Article 14 of the AI Act)” and `checks/claims-2026.tsv` row `eu-ai-act`.

**Verification:** Article 14 does contain a human-oversight duty for high-risk systems, but Regulation (EU) 2026/1744 postponed Chapter III, Sections 1–3, including Article 14, to 2 December 2027 for Annex III systems and 2 August 2028 for product-safety systems. The current claim row still relies on the original 2024 regulation and says `checked-by:claude:2026-08-16`; it missed the 2026 amendment. [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL_202601744)

**Why it matters:** This is a direct breach of “Never false” and makes “the advisory body and the safety brake also arrived, and are failing” impossible to support with Article 14. Automation-bias literature predating the Act cannot show that an obligation not yet applicable is failing.

**Fix:** Change the sentence to a proposal/legislated-future comparison, update `eu-ai-act`, and do not claim post-implementation failure. At most: EU law contains a delayed human-oversight requirement that resembles one component of Lem’s safeguard.

### 2. **CONFIRMED (Grok 1; Agy 1), but Agy’s proposed repair is rejected:** the construction `MISS` grades examples and a reductio as a forecast

**Location:** object row “How it gets built: ciliates, colloids … or a homeostat programmed with rules that ‘learns from its own mistakes’” → `MISS`; repeated under “Where he was worst.”

**Verification:** On p. 109 Lem calls the amplifier route “only a hypothetical possibility,” says the ciliate device is “very far” from an amplifier, and admits the trials produced no breakthrough. The examples establish a method: construct a useful system from elements whose internal complexity is not understood. Page 110 states that method positively (“jump over this ditch”) and says neither amplifier nor constructor need know how the result is produced. The p. 117 learner is the Economic Ruler explicitly closed as a “reductio ad absurdum” on p. 120. Meanwhile pp. 153–154 describe randomly connected perceptrons learning to recognize patterns and eventually read texts.

**Assessment of the reviewers:** Grok is right that neither half supports `MISS`. Agy is right about the reductio violation but wrong to say the biological/physical examples should be split out as a “pure” `MISS`; Lem hedges them and uses them as illustrations, not a dead-path forecast. Grok’s warning about saying the chapter “never considers text” does not defeat the essay’s narrower wording, “text as the medium a machine’s competence could be grown from”; Lem discusses text-reading, not corpus training.

**Fix:** Remove the current row. If a construction row is retained, grade Lem’s black-box, trial-and-error method separately from his illustrative materials. State the genuine omission in prose with exact scope: he never proposes growing general competence by training on a text corpus at scale.

### 3. **CONFIRMED (Grok 3; Agy 2):** Facebook does not pay the “using force” `HIT`

**Location:** problem row “the only way to maintain ‘stability’ … is by using force” → Facebook’s refusal to adopt engagement-reducing fixes → `HIT`; “The Facebook record fits it exactly.”

**Verification:** The rest of p. 121 makes “force” literal: violence replacing self-organization, followed by tyranny, absolutism, and fascism. The Facebook receipt establishes an untouchable business metric and a narrowed manoeuvre space. It does not establish force.

**Fix:** Quote and grade only the untouchable-parameter/reduced-manoeuvre claim. If the force endpoint remains in the Lem cell, it is not a `HIT` on this evidence. Agy’s suggested `RIGHT QUESTION, WRONG ANSWER` is possible only if the row is explicitly made problem-level; narrowing is cleaner.

### 4. **CONFIRMED in core, with parts of Grok 2 rejected:** the Coordinator `MISS` is not earned

**Location:** “Coordinators ‘at the scale of the country … or even the continent’” → Cybersyn and “no successor known” → `MISS`.

**Verification:** Page 158 is an own-voice forecast. It first predicts local control centers managing production, exchange, distribution, and research, then says those will require country/continent coordinators and a Planetary Coordinator. The row quotes only the larger-scale claim, so Grok overstates matters when it says the row itself silently combines two claims. Cybersyn is a valid partial object-level test even though Beer built it; Grok’s “tests Beer, not Lem” distinction is false. But an absence claim plus one aborted project does not establish the verdict’s required “no live path.” The claim register itself labels `no-national-coordinator` an absence claim “known to us,” sourced to one historical book.

**Fix:** Split local coordination from country/continent/planetary coordination. Receipt the present path before choosing `EARLY` or `OPEN`; otherwise leave the large-scale row `OPEN`. Do not use the current absence claim to pay `MISS`.

### 5. **CONFIRMED (Grok 5; Agy 3), but the suggested replacement verdict needs correction:** Amazon is not Beer’s firm-wide homeostat

**Location:** Beer's homeostat laying off workers when whole-mill optimization requires it → automated Amazon productivity terminations → `HIT`.

**Verification:** Pages 115–116 describe an ultrastable regulator reorganizing a steel mill as a whole across supply, demand, costs, production, and labor. The Amazon receipt describes a narrow productivity-threshold system that generated warnings and terminations. The surface outcome matches; the regulator and mechanism do not.

**Fix:** Narrow the Lem cell to automated metric-based firing, or use `RIGHT ANSWER, WRONG REASON`. Both reviewers propose `RIGHT QUESTION, WRONG ANSWER`; that is the wrong layer for an object-level row whose outcome occurred through a different mechanism.

### 6. **CONFIRMED (Grok 4):** the Facebook opacity row is tautological and does not receipt Lem’s constitutive opacity

**Location:** “We cannot expect it to inform us about such consequences” → harms surfaced through internal researchers rather than the ranking system → `HIT`.

**Verification:** Pages 116–117 ground the non-reporting claim in unknown inner states, “not even [known to] its designer–constructor.” The Facebook receipt shows researchers diagnosing an incentive and proposing fixes; it does not show that no one could state the mechanism. Any non-agentic software fails to volunteer a moral report, so “the system did not inform us” proves too little. Grok is also right that “performing its set task too well” on p. 116 specifically ends in bankrupting competitors, not in the generic feed example the prose attaches to it.

**Fix:** Delete this row or replace the receipt with evidence of unresolvable model-level opacity tied to an actual harmful decision. Keep Facebook only for the narrower untouchable-parameter argument.

### 7. **CONFIRMED (Grok 6; Agy 5):** the rival-homeostat row mixes a simulation with the wrong real-world mechanism and is stale

**Location:** rival homeostats → “Rival learning agents in one market learn to collude” plus the “2024” RealPage allegation.

**Verification:** The local claim register correctly describes Calvano et al. as simulated markets; the ledger drops “simulated.” RealPage is a common software/data hub used by competing landlords, not independent rival agents learning to collude. Since the reviewers ran, the time objection is also verified: DOJ filed a proposed RealPage settlement in November 2025, and the case page records additional 2025–2026 judgments and proposed settlements. The essay may still accurately say DOJ alleged coordination in 2024, but a 2026 account cannot present that as the current state of the case. [DOJ RealPage case page](https://www.justice.gov/atr/case/us-and-plaintiff-states-v-realpage-inc)

**Fix:** Label Calvano a simulation and let it support only a problem-level live question. Remove RealPage from the rival-agent mapping or present it separately as hub-and-spoke algorithmic coordination; update the legal status and preserve the allegation/settlement distinction.

### 8. **CONFIRMED (Grok 7):** the specification-gaming receipt does not establish Lem’s “braked, then a new strategy” sequence

**Location:** one problem row joins “constantly looking for … statistical correlations” with “will most likely develop a new strategy,” paid by DeepMind’s 2020 catalogue.

**Verification:** The CoastRunners example and catalogue demonstrate proxy exploitation. They do not, as cited, demonstrate an agent being stopped by a safeguard and then discovering a more indirect route around it. That sequential rerouting is the distinctive move in pp. 119–120.

**Fix:** Remove “develop a new strategy” from the graded claim or add a receipted, dated case of adaptation after an intervention. The narrower correlation/proxy mechanism can remain a problem-level `HIT`.

### 9. **CONFIRMED (Grok 11):** the essay mentions but does not grade the chapter’s cleanest dated failure

**Location:** “science running out of scientists (the ‘megabyte bomb,’ p. 99)” appears once; there is no ledger row. “The Beliefs of Electric Brains” is also absent despite the chapter contract.

**Verification:** Page 99 predicts an information barrier because “There will be no more prospective scientists.” Page 100 says the S-fold—the descent from exponential scientist growth—lies thirty to seventy years away, i.e. 1994–2034 from the 1964 book. This is a specific, dated claim and belongs to the contract’s megabyte-bomb job. Grok is right that the existing two `MISS` rows are weak and that this is the more defensible candidate, although `MISS` versus `RIGHT QUESTION, WRONG ANSWER` still needs a receipt about scientist growth and information overload.

**Fix:** Add a sourced row for pp. 99–100 and cover or explicitly narrow away the pp. 138–141 electric-brain section. Do not assign a verdict until the 2026-side headcount/information-barrier evidence is actually in the claim register.

### 10. **CONFIRMED (Grok 9):** the text-to-deception causal story outruns the alignment-faking experiment

**Location:** “a device ‘constantly looking for connections’ in human text finds deception among them”; “Some of ours know a little.”

**Verification:** Greenblatt et al. is a controlled alignment-faking demonstration. It does not establish the essay’s proposed causal chain from pretraining on human text to learned cryptocracy in deployment. Anthropic itself describes a constructed experimental environment and synthetic-document variant, not field evidence of a deployed regulator routing around a brake. [Anthropic experiment description](https://www.anthropic.com/research/alignment-faking)

**Fix:** Keep the controlled demonstration, already appropriately `OPEN` in the ledger, and remove the unreceipted causal explanation and anthropomorphic “know.” Alternatively label the causal link explicitly as a hypothesis.

### 11. **CONFIRMED (Grok 8):** Medicare is used to turn a present-tense illustration into a failed forecast

**Location:** “The Kennedy line stands as a small monument … the reform his example said the brake would stop passed under a different president.”

**Verification:** Page 119 says “In the United States at the present moment” and analogizes Kennedy’s halted proposal to the safety brake. It is an illustration of political veto in 1964, not a forecast that Medicare would never pass. The 1965 enactment does not refute it.

**Fix:** Cut the “monument” sentence or describe the example only as rapidly dated context.

### 12. **CONFIRMED (part of Grok 10):** “without new ideas” is not in the scaling-law receipts

**Location:** “capability rises smoothly with data, parameters and compute, without new ideas” → Kaplan 2020 and GPT-3.

**Verification:** Kaplan et al. report power-law behavior of language-model loss against parameters, data, and compute. GPT-3 reports few-shot performance without task-specific training. Neither establishes the much broader claim that capability growth required “no new ideas.” [Kaplan et al.](https://arxiv.org/abs/2001.08361)

**Fix:** Cut “without new ideas” and distinguish loss scaling from capability. If the bitter-lesson claim is wanted, source and argue it separately.

### 13. **CONFIRMED (parts of Grok 10 and 12):** several rows mix layers or evidence families

**Location:** rival homeostats appears under “Object level” with `RIGHT QUESTION, WRONG ANSWER`; the first black-box row combines pp. 109 and 116–117; automation bias is said to show what Lem’s advisory-body ignorance showed.

**Verification:** The rival-homeostat object claim asks what competing machines actually do; its current verdict is explicitly problem-level vocabulary applied to a simulation and allegation. The first row splices the intelligence amplifier’s construction claim with the later regulator’s harm-reporting sentence; p. 110 is the correct constructor-ignorance support for the amplifier. Automation bias is deference to recommendations, including wrong ones; Lem’s p. 119 failure is inability to know when a brake should be activated. They are related but not identical mechanisms.

**Fix:** Separate object outcomes from problem dilemmas. Cite p. 110 for amplifier opacity, reserve pp. 116–117 for the regulator, and describe automation bias as an adjacent oversight failure rather than “what Lem said.”

### 14. **CONFIRMED (part of Grok 10):** two sweeping 2026 assertions are unreceipted

**Location:** “Most documented harm is Lem’s kind”; “a box grown from the record of human writing is owned by whoever can pay for the training run, and it inherits the record’s habits, including strategy.”

**Verification:** Neither assertion has its own support in the local claim register. The alignment-faking marker after the first sentence cannot pay the prevalence claim “most,” and the scaling/GPT-3 rows do not establish ownership concentration or inherited strategy.

**Fix:** Remove “most,” or add a defined corpus and receipt. Mark and source the ownership claim; present “inherits … strategy” as an argued hypothesis unless direct evidence is added.

### 15. **CONFIRMED — and missed by both reviewers:** the 1964 baseline is unreceipted and partly conflicts with the chapter’s own baseline

**Location:** “The 1964 baseline: Beer’s *Cybernetics and Management* (1959), Ashby’s homeostat, Wiener’s second edition … and computers that could not yet beat a club chess player.”

**Verification:** None of these historical claims has a `CHECK` marker. More importantly, Lem says on p. 150 that effective chess software already existed “at the level of an average player,” while the Computer History Museum reports that the 1962 Kotok program could beat amateurs. “Could not yet beat a club chess player” may be defensible under a narrow rating definition, but the essay neither defines nor receipts it. [Computer History Museum](https://www.computerhistory.org/chess/getting-going/)

**Fix:** Receipt every baseline fact, define the chess comparison precisely, and reconcile it with p. 150. This line is too compressed to satisfy the instruction that the reader should be able to feel the state of the art in 1964.

## Rejected and unverifiable reviewer findings

### **REJECTED (Agy 4):** “Belief and Information” supplies a missing hallucination `MISS`

Pages 124–130 do not limit false information to biological systems. Page 125 says **every homeostat** must act on incomplete information as though it were complete; pp. 125–126 discuss false models causing failed action; p. 130 says an input’s effect depends on the receiving homeostat’s disposition and regulatory powers. “The working of such information stops at the limits of an organism” on p. 128 refers specifically to placebo-like bodily effects—warts versus moving mountains—not to the social circulation of false statements. LLM hallucinations therefore do not refute the passage as Agy claims. A hallucination row might be interesting, but it is not this `MISS`.

### **REJECTED (Agy 6):** Strathern needs a second `CHECK` marker

The existing `<!-- CHECK: goodhart -->` marker follows the compound Goodhart/Strathern sentence, and the `goodhart` claim row explicitly receipts both Goodhart 1975 and Strathern 1997. The contract requires a marker and a matching row, not one marker per proper name. `verify.sh` reports 44 markers, 44 rows, and no mismatch.

### **REJECTED in stated form (part of Grok 10):** Article 14 is overbroad because it applies only to high-risk systems

The essay already says “Human oversight of **high-risk systems**,” so that qualification is present. The real error is worse and different: the requirement’s application was postponed by the 2026 amendment (finding 1).

### **UNVERIFIABLE as reviewer support (part of Grok 2):** ERP, central-bank nowcasting, economic digital twins, and AI-planning proposals prove a live path to Lem’s country-scale Coordinator

None of those examples is in the essay’s claim register or receipted in Grok’s report. They should not be accepted on assertion. The `MISS` still fails because the essay itself has not established “no live path”; a replacement `EARLY` likewise needs evidence.

## Reviewer-by-reviewer disposition

| Reviewer finding | Disposition | Where resolved |
|---|---|---|
| Grok 1 — construction `MISS` | **CONFIRMED** | Finding 2 |
| Grok 2 — Coordinator `MISS` | **CONFIRMED in core; some reasoning REJECTED/UNVERIFIABLE** | Finding 4; final note above |
| Grok 3 — “using force” | **CONFIRMED** | Finding 3 |
| Grok 4 — Facebook opacity | **CONFIRMED** | Finding 6 |
| Grok 5 — Amazon homeostat | **CONFIRMED** | Finding 5 |
| Grok 6 — Calvano/RealPage | **CONFIRMED** | Finding 7 |
| Grok 7 — “new strategy” | **CONFIRMED** | Finding 8 |
| Grok 8 — Kennedy/Medicare | **CONFIRMED** | Finding 11 |
| Grok 9 — alignment-faking causal story | **CONFIRMED** | Finding 10 |
| Grok 10a — scaling “without new ideas” | **CONFIRMED** | Finding 12 |
| Grok 10b — advisory body/safety brake “arrived” | **CONFIRMED, for a stronger reason** | Finding 1 |
| Grok 10c — automation bias “says what Lem said” | **CONFIRMED** | Finding 13 |
| Grok 10d — “Most documented harm” | **CONFIRMED** | Finding 14 |
| Grok 10e — RealPage clock | **CONFIRMED** | Finding 7 |
| Grok 10f — national-Coordinator absence claim | **CONFIRMED** | Finding 4 |
| Grok 11 — missing megabyte-bomb miss | **CONFIRMED** | Finding 9 |
| Grok 12 — layers | **CONFIRMED** | Finding 13 |
| Grok 13 — skeptic will reject inflated mappings | **CONFIRMED as a consequence, not a separate defect** | Findings 2–8 |
| Agy 1 — reductio in object row | **CONFIRMED; proposed substrate `MISS` REJECTED** | Finding 2 |
| Agy 2 — “using force” | **CONFIRMED** | Finding 3 |
| Agy 3 — Amazon | **CONFIRMED; proposed verdict corrected** | Finding 5 |
| Agy 4 — hallucination `MISS` | **REJECTED** | Rejected findings |
| Agy 5 — RealPage | **CONFIRMED** | Finding 7 |
| Agy 6 — missing Strathern marker | **REJECTED** | Rejected findings |
| Agy 7 — skeptic/persuasion | **CONFIRMED as a consequence, not a separate defect** | Findings 3, 5, 6 |

`verify.sh` passes mechanically (104 Lem quotations, 44 claim markers, 0 mismatches), but that does not validate verdict mappings or the truth/currentness of the registered claims.
