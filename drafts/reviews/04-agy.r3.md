**1. Misreading Lem & Verdict Inflation (Severity: High)**
* **Location:** Ledger row: `"Robots endowed with quasi-human personalities are unlikely to be built" (p. 158)`
* **Problem:** The quote is truncated to manufacture an unfair MISS. Lem's very next words are "—unless it is for the kinds of purposes imagined by Fritz Leiber in his novel *The Silver Egghead* (1961)... brothels with electronic ladies." The 2026 receipt cites "companion apps as a product category" to fail him, but Lem explicitly carved out this exact exception for sex/companion robots. 
* **Fix:** Restore the full quote including the Fritz Leiber exception. Change the verdict to HIT or EARLY, as he correctly identified the specific drive that would get these personalities built.

**2. The Two Layers & Verdict Inflation (Severity: High)**
* **Location:** Ledger row: `Beer's homeostat "laying off workers or reducing pay when the principle of the optimal organization … requires it"`
* **Problem:** This row mixes the object-level prediction (a firm-wide regulator) with the problem-level outcome (automated firing). Amazon's system is a narrow stopwatch metric, not a learning "homeostat" making moral decisions to balance an organization's economy. Placing this in the *Object level* and scoring it RIGHT ANSWER, WRONG REASON for the outcome launders the failure of the object itself.
* **Fix:** Move this to the Problem level if judging the dilemma of automated firing, or keep it in the Object level and score it as a MISS since the firm-wide learning regulator did not arrive.

**3. Missing MISS (Severity: Medium)**
* **Location:** Prose section "Where he was worst": "He knew a box could be built without a theory of it; he did not see what it would be made from... it is not scored above as a MISS because he never forecast against it"
* **Problem:** The essay claims Lem didn't forecast the substrate, excusing him from a MISS. However, on p. 109, Lem *did* make a specific object-level forecast for the substrate: a colony of ciliates, colloids, or multiphase solutions. That the black box was built from math and silicon is a direct MISS for his ciliate/colloid prediction, which the essay skips.
* **Fix:** Add an Object-level row for the ciliate/colloid/multiphase solution substrate (p. 109) and score it as a MISS.

**4. Verdict Inflation (Severity: Medium)**
* **Location:** Ledger row: `"If certain parameters are 'untouchable' — such as, for example, private ownership..."`
* **Problem:** The essay scores a HIT by equating Lem's macroeconomic constraint ("private ownership") with a modern product metric ("Facebook engagement"). This credits an analogy as a specific prediction, inflating the verdict for a vague idea.
* **Fix:** Change the verdict to RIGHT QUESTION, WRONG ANSWER. The dilemma of untouchable parameters exists, but the actual parameters causing harm turned out to be product metrics, not macro-political ones.

**5. Verdict Inflation (Severity: Low)**
* **Location:** Ledger row: `Perceptrons "cannot recognize, say, human faces; neither can they … 'read texts.' But they are an important step" toward machines that will`
* **Problem:** The receipt justifies the HIT by stating "reading text at scale became the training route itself (GPT-3)". Lem predicted machines reading text as a *clerical task* (OCR) to save operators the time of translating tasks into machine language (p. 153). Using GPT-3's scale training to validate his prediction of OCR conflates his narrow prediction with a completely different mechanism.
* **Fix:** Keep the HIT for deep networks reading text (OCR), but remove the reference to GPT-3 and scale training from the receipt.

**6. Reader Persuasion (Severity: Low)**
* **Location:** The ledger's overall rhetorical approach.
* **Problem:** A skeptic of the "Lem predicted everything" claim would not be persuaded by this ledger. The ledger relies heavily on analogy (private ownership = engagement) and truncation (ignoring the companion robot exception) to secure its verdicts. The prose does the heavy lifting ("That is a political-economy claim about optimisers...") to make metaphorical matches look like direct predictions.
* **Fix:** Clean up the ledger strictly per the `AGENT.md` rules: no analogies, no truncated quotes, and strict separation of objects from problems. An uninflated ledger is much more persuasive.

**7. 2026 Claims Check (Severity: None)**
* **Location:** Factual claims about the present throughout the text.
* **Problem:** None. Every factual claim about the present (e.g., Robodebt, EU AI Act timeline, alignment faking study, Calvano 2020) is correctly marked with a `<!-- CHECK -->` marker, and none are wrong or overstated to my knowledge.
* **Fix:** No action needed.
