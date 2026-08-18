### 1. Unfair MISS / Misreading Lem (Severity: Critical)
- **Location:** Ledger row: `"Ordering: controlling evolution, regeneration and 'orchestrat[ing] genetic traits in fetuses' will be possible 'long before… we gain the ability to create the chromosome apparatus of a nucleus in an artificial manner' (p. 193)"` and prose: `"He got the order of difficulty backwards, in the one place in this chapter where he committed to an order."`
- **Problem:** Lem explicitly hedged this "prediction" immediately after making it. In the very next paragraph (p. 193), he writes: *"At the end of the day... what we are observing could have emerged in a variety of different ways. Yet there is still a lot to discover, so one should not take on an additional risk by predicting any future development of individual sciences."* The essay grades him on an order he explicitly warned he was not committing to.
- **Fix:** Remove this MISS row, or reclassify it as OPEN/withdrawn due to his own caveat. 

### 2. Missing MISS (Severity: Critical)
- **Location:** The ledger as a whole.
- **Problem:** Because the MISS on ordering is unfair and hedged (see Finding 1), the essay contains zero valid MISS rows. This violates the strict instruction in `AGENT.md`: "Every essay must contain at least one MISS... found honestly. If none exists, the essay says why that chapter is different — and the panel is told to attack that."
- **Fix:** Find a genuine, unhedged MISS in the chapter, or explicitly state in the prose that the chapter has no MISSes because it is a methodological proposal rather than a forecast, instructing the panel to attack that premise.

### 3. Factual Error in 2026 Claim (Severity: High)
- **Location:** Prose: `"In 2025 OpenAI published an account of hallucination..."` and Reading section: `"Kalai et al., 'Why Language Models Hallucinate' (2025)"`.
- **Problem:** Adam Kalai and his co-authors are affiliated with Microsoft Research (and MIT), not OpenAI. Attributing this research to OpenAI is factually incorrect.
- **Fix:** Change "OpenAI" to "Microsoft Research" (or "researchers").

### 4. Verdict Inflation / Strained Analogy (Severity: High)
- **Location:** Ledger row: `"Every homeostat 'must show "belief"'... (p. 125)"` graded as `RIGHT ANSWER, WRONG REASON` against `"Language models answer rather than abstain"`.
- **Problem:** This credits a vague cybernetic idea with a specific modern outcome. Lem's "belief" refers to a homeostat acting on incomplete information to prevent its own destruction (*"whose transgression threatens its existence"*). An LLM's hallucination is a statistical artifact of next-token prediction and evaluation grading, not a cybernetic survival mechanism fighting for its life. Equating the two is a massive rhetorical stretch.
- **Fix:** Score this as a MISS (we did not build survival-driven believing homeostats) or DISSOLVED, and remove the hallucination analogy from the graded ledger.

### 5. Mixing the Two Layers (Severity: Medium)
- **Location:** The `"Every homeostat 'must show "belief"'..."` row is placed under the **Problem level** heading.
- **Problem:** The `RIGHT ANSWER, WRONG REASON` verdict is used here to evaluate an *object* (the existence of models that guess/hallucinate) and its mechanism (grading vs. survival). This is an object-level evaluation of how a system behaves and is built. The problem level (Layer B) is strictly for testing whether a *dilemma* became the live dilemma. 
- **Fix:** Move this row to the **Object level** section, or replace it with a row that actually evaluates the dilemma of systems needing to act on incomplete information.

### 6. Missing 2026 Claim Markers (Severity: Medium)
- **Location:** Ledger rows containing `"what is studied is what trained models inherit from human text"` and `"the traffic still runs the other way, from empirical need to existing structures"`.
- **Problem:** These are empirical, factual claims about the present state of machine learning and mathematics in 2026, but they lack the required `<!-- CHECK: id -->` markers as mandated by the rules.
- **Fix:** Add `<!-- CHECK: [id] -->` markers to these claims and source them in `claims-2026.tsv`, or rewrite them to avoid making uncited empirical claims.

### 7. Unpersuasive to a Skeptic (Severity: Low)
- **Location:** The ledger distribution and the rationalization in "Where he was worst": `"six of eight rows are OPEN... a prophet who mostly describes how to hold a problem cannot be scored the way one who names devices and years can."`
- **Problem:** A skeptical reader will look at a ledger containing 6 OPENs, 1 EARLY, 1 strained RA/WR, and 1 unfair MISS, and conclude that the essay is using rhetoric ("how to hold a problem") to launder a chapter where Lem simply failed to make testable predictions. The prose excuses the lack of hits instead of holding Lem to the book's strict standard.
- **Fix:** Acknowledge outright to the reader that this chapter fails as futurology under the book's scoring system, rather than trying to salvage his "working style" as a prophetic success.
