# Book 15 — CONTEXT (authority document)

**Working title: *Sixty Years Later*.** Ten essays reading Stanisław Lem's *Summa
Technologiae* (1964) from 2026: chapter by chapter, where he was right, wrong, right for
the wrong reason, or asking a question that has since dissolved or is still open.
Lem graded himself in "Twenty Years Later" (1982) and again in the 1990s; this book is
the next grading, by a reader who has the things Lem only argued about.

Precedence (inherited from book8/book12): this file → AGENT.md (reader, priority stack,
verdict rules, pitch gate) → essay contract (§6) → TEMPLATE.md → prose.

## 1. Thesis

Lem asked to be judged on *problems*, not gadgets: he wrote that futurology which
predicts devices is astrology, and that the honest job is to map which questions a
technological civilization will be forced to face. So the scoring here is two-layered.
**Layer A — the object level:** did the thing he described come to exist (VR, gene
editing, machine intelligence, information farming, the SETI silence)? **Layer B — the
problem level:** did the *dilemma* he attached to it become the live dilemma, or a
different one, or none? A chapter can score high on B with a zero on A (phantomatics:
headsets are a niche, but the "can you tell?" argument is now a philosophy industry) and
the reverse (his cosmology detail vs the actual Fermi debate). The verdict vocabulary
(§4) exists so the essays never collapse into "prophet / not prophet."

The book's own claim: Lem's *misses* are the more instructive half. Where he was wrong
he was wrong in a specific, dated way (1960s cybernetics; information theory as the master
science; the phantomat's application mix hedged both ways, pp. 214–215; a later self-grade
that took EyePhone/DataGlove for phantomatics) — and 2026's own blind spots are probably of
the same kind. Note for essay 4: he *did* see learning-from-correlation as the black box's
mechanism (pp. 117–120, 153–54), and his ciliates/colloids on p. 109 are hedged illustrations
of a method, not a substrate forecast; the real gap is an *omission* — training on text at
scale as the route to competence — recorded in prose, not manufactured into a MISS row.

## 2. Corpus

- **Primary:** Lem, *Summa Technologiae*, trans. Joanna Zylinska, Minnesota 2013
  (Electronic Mediations 40), 383 pp. Local: `resources/lem-summa-2013.pdf` →
  `resources/text/summa.txt` (both gitignored; rebuild with `scripts/build-corpus.sh`).
  PDF page N == printed page N; the extraction is quotable and section-mapped.
- **Corpus gap (recorded 2026-08-16):** the 2013 translation carries chapters 1–8 only.
  Chapter 9, *Sztuka i technologia*, is absent, as is the 1982 afterword "Dwadzieścia
  lat później" (quoted only in Zylinska's introduction). Essay 9 needs the Polish
  (Wydawnictwo Literackie, 4th exp. ed. 1984 or later) or the Russian (*Сумма
  технологии*, Мир 1968 / АСТ 2002). Until one is on disk, essay 9 quotes cannot be
  gated and the essay does not ship. **Open: user to supply a copy.**
- **Secondary, Lem:** "Twenty Years Later" (written 1982, appended to the 4th ed.), "Thirty Years Later" (1991),
  *Dialogi* (1957), *Filozofia przypadku* (1968) — for how Lem himself re-scored.
- **2026 side:** whatever the essay's claim needs — receipted per claim in
  `checks/claims-2026.tsv`. No claim about "what happened" rides on memory.

## 3. Spine — ten essays

| # | Lem chapter (2013 pp.) | Essay working title | Object-level test |
|---|---|---|---|
| 0 | — (Translator's intro; "Twenty Years Later") | How to grade a prophet | the method itself |
| 1 | 1 Dilemmas (24–30) | Is futurology a science yet? | forecasting/x-risk/AI-timeline culture |
| 2 | 2 Two Evolutions (31–58) | The second evolution, observed | Moore's law, tech-as-organism talk, AI as evolutionary process |
| 3 | 3 Civilizations in the Universe (59–92) | Sixty years of silence | 5,000+ exoplanets, no signal; Great Filter, Dark Forest |
| 4 | 4 Intelectronics (93–163) | The black box arrived | LLMs; the "megabyte bomb"; intelligence amplifier; electrocracy |
| 5 | 5 Prolegomena to Omnipotence (164–196) | Design without understanding | ML as imitology; AlphaFold; "methodological madness" |
| 6 | 6 Phantomology (197–236) | Can you tell? | VR's plateau; simulation argument; deepfakes; BCI |
| 7 | 7 The Creation of Worlds (237–293) | Information farming, at last | AI-for-science, automated discovery; linguistic engineering |
| 8 | 8 A Lampoon of Evolution (294–353) | The invisible path | matchmaking + embryo screening; He Jiankui; longevity; cyborgs |
| 9 | 9 Art and Technology (PL/RU only) | The generated image | generative art, music, text — corpus gap, see §2 |

Order = Lem's order. Essay 0 sets the scoring rules and is written *last* (it must
report the pattern of the other nine, not predict it).

## 4. Verdict vocabulary (hard rule — every ledger row uses exactly one)

- **HIT** — described it; it exists/happened substantially as described.
- **MISS** — described it; it did not happen and there is no live path.
- **EARLY** — described it; not yet, but the path is live in 2026 (dated, not vague).
- **RIGHT QUESTION, WRONG ANSWER** — the dilemma is the live one; his resolution isn't.
- **RIGHT ANSWER, WRONG REASON** — the outcome matches; the mechanism he gave doesn't.
- **DISSOLVED** — the question no longer means anything (its premise fell).
- **OPEN** — 2026 cannot say either way; the essay says why.

A ledger row is one *specific* Lem claim (quoted, paged) against one *specific* 2026
fact (receipted). "Lem anticipated AI" is not a row. "Lem: an intelligence amplifier will
be a black box whose reasoning cannot be inspected even by its builders (p. 111–113) —
2026: mechanistic interpretability still cannot explain frontier-model outputs (source)"
is a row.

## 5. Voice and sourcing standard

- Series voice: plain, argued, no hero-worship. Lem is not a prophet to be vindicated; he
  is a very good interlocutor to be answered. Where he was smug, say so.
- Lem is always quoted verbatim from the 2013 text with page; paraphrase gets a page too.
  Zylinska's translation choices are noted where they matter (e.g. "intelectronics").
- Every 2026-side factual claim carries `<!-- CHECK: id -->` and a `claims-2026.tsv`
  row with a source. Ships only when the row is not `open`.
- No numbers from memory. Dates, counts, model names, paper titles: source or cut.
- The 1982/1991 self-grades: when Lem already conceded or doubled down, quote him, and
  score 2026 against *that* Lem too. Never grade 1964-Lem on something 1982-Lem fixed
  without saying so.
- Essays are 1,800–3,200 words, on TEMPLATE.md.

## 6. Essay register (contracts)

Each essay has one exclusive job; the pitch (AGENT.md) fixes it before drafting.

- **0 How to grade a prophet.** Job: state and defend the two-layer scoring and the
  vocabulary; report the pattern across essays 1–9 (hit-rate by layer). Not a summary.
- **1 Dilemmas.** Job: Lem's case that technology forecasting is necessary and its
  method (extrapolation of *problems*), against 2026's forecasting culture — Tetlock,
  prediction markets, AI-timeline discourse, EA/x-risk. Question: did futurology become
  what he asked for, or an industry of the astrology he mocked?
- **2 Two Evolutions.** Job: the bio/techno-evolution parallel and his "several naïve
  questions". Test: is technology in 2026 better described as designed or as evolved
  (scaling laws, emergent capabilities, nobody planning the stack)?
- **3 Civilizations.** Job: von Hoerner/Drake-era statistics, his "catastrophic theory",
  votum separatum. Test against exoplanet census, SETI negatives, the modern Fermi
  literature. Where his *specific* numbers went and whether the silence changed meaning.
- **4 Intelectronics.** Job (the book's centre): the megabyte bomb, the black box,
  intelligence amplifiers, "the morality of homeostats", electrocracy, "beliefs of
  electric brains" — against LLMs, alignment, interpretability, AI-in-government. This
  essay must not become a victory lap; the ledger will show what he did *not* foresee
  (training on text at scale as the route to competence — an omission, stated in prose,
  not forced into a MISS row). Scope: pp. 93–124 and 146–163; "The Beliefs of Electric
  Brains" (pp. 124–141) is handed to essay 5.
- **5 Prolegomena.** Job: imitology and "the silence of the designer" — building things
  that work without a theory of why; also ch. 4's "The Beliefs of Electric Brains"
  (pp. 124–141), belief/information in homeostats, handed over from essay 4. Test: modern ML *is* this. Where the argument
  about restraint ("Scylla and Charybdis") lands in 2026.
- **6 Phantomology.** Job: peripheral vs central phantomatics, the indistinguishability
  test, cerebromatics, personality-and-information. Test: VR as consumer product (flat),
  simulation argument (Bostrom 2003 onward), deepfakes, BCI, identity/upload debates.
- **7 Creation of Worlds.** Job: information farming — automatic generation of knowledge
  without a scientist — linguistic engineering, engineering of transcendence,
  cosmogonic engineering. Test: AI-driven discovery in 2024–26; LLMs as "linguistic
  engineering"; the last two sections as speculation still.
- **8 Lampoon.** Job: biology as bad engineering, autoevolution, cyborgization,
  constructing consciousness/death — against gene editing, longevity, prosthetics, the
  ethics debates. NB the ESP section (pp. 347-350) is NOT an error of his: he rejects
  extrasensory phenomena, and note 10 (p. 371) states the file-drawer effect. See the
  2026-08-18 status entry; that material belongs to essay 0, not to a list of misses.
- **9 Art and Technology.** Job: his short closing on art under technology — against
  generative media. Blocked on corpus (§2).

## 7. Checks

`./verify.sh` — Lem quotes gating (fixed corpus), 2026 claim markers gating, links and
count-sync gating, structure advisory. `scripts/find.py` writes the quote rows.
`scripts/review.sh N` runs the reviewer panel (AGENT.md §Panel).

## 8. Status log

- 2026-08-16 — repo created; corpus extracted (2013 tr., 383 pp); shape scaffolded;
  chapter-9 corpus gap recorded; no essays drafted. Next: pitch essay 4 or 6 first
  (the two with the strongest object-level material) as pilots.
- 2026-08-16 — pitches for essays 4 and 6 (drafts/*.pitches.md); user picked 4-B
  (electrocracy) and 6-A (the order came out backwards). Both drafted to TEMPLATE; 73 Lem
  quotes gated green; 29 claim rows, 1 open (vr-use-mix, an absence claim). Corrections
  while checking: (a) "Twenty Years Later" was written 1982, not 1974 (Zylinska p. 21);
  (b) the thesis line claiming Lem had no notion of statistical learning was wrong —
  pp. 117–120, 153–54 — rewritten; (c) verify.sh matching now ignores quote marks, em/en
  dashes, hyphens, [insertions] and footnote superscripts, all of which produced false
  misses on real quotes. Panel review of both essays launched.
- 2026-08-16 (panel) — both pilots **BLOCKED** by the consolidated review (drafts/reviews/
  04-codex.md, 06-codex.md; grok/agy raw alongside). Confirmed findings to act on:
  **Essay 4:** (1) the p. 117 Economic Ruler is Lem's own reductio (p. 120), not a
  prediction — the "wrong building" MISS misreads him; grade pp. 158–163 Coordinators
  separately; (2) the contract-required miss (language as substrate, scale as method) is
  absent; (3) RealPage is coordination, the reverse of Lem's rival homeostats — drop the HIT;
  (4) ledger uses compound/invented verdicts — one exact §4 word per row; (5) a paper about
  gradual disempowerment is not evidence it happened → OPEN; (6) Robodebt/toeslagen are rule
  systems, not learning Coordinators — narrow the claim; (7) alignment faking does not
  refute p. 107 — OPEN; (8) Facebook MSI supports the p. 121 untouchable-parameter claim,
  not constitutive opacity — move it. **Essay 6:** (1) Lem's p. 206 ranking is difficulty,
  not arrival order, and both devices are full-sensorium phantomats — text chatbots are not
  the "human-producing" one; the MISS is unsupported → reframe as a labelled analogy, verdict
  OPEN/EARLY; (2) "better than us" claims Lem denies persuasion; p. 217 says the opposite —
  rebuild or remove; (3) essay skips pp. 215–236 (cerebromatics, personality/copying) which
  the contract requires — add rows or narrow the contract; (4) same ledger-vocabulary
  violations; (5) EyePhone/DataGlove cannot be a 1982 update (devices are late-1980s;
  Zylinska pp. 20–21 pools 1982 and 1991) — fix; "he did not point at the other machine" is
  unverifiable without the afterwords; (6) close the open vr-use-mix row before shipping.
  Standing lesson for AGENT.md: a claim being *reported* (paper, lawsuit) is not the claim
  being *true*; and Lem's reductios must be scored as arguments, not forecasts.
- 2026-08-17 — published: https://github.com/AnthonyKot/book15 → https://anthonykot.github.io/book15/ (Pages from main, root). Both pilots are live in draft state pending the panel revisions above.
- 2026-08-17 (revision) — both pilots revised against the panel findings. **Essay 4:**
  p. 117 Ruler now presented as Lem's reductio (p. 120 quoted); object-level rows are the
  black-box possibility (HIT), how it gets built — ciliates/colloids/programmed homeostat
  vs training on text at scale (the contract MISS), Amazon lay-offs (HIT), rival
  homeostats vs Calvano 2020 collusion + RealPage allegation (RIGHT QUESTION, WRONG
  ANSWER), Coordinators at country/continent scale (MISS, Cybersyn sole attempt); coin
  toss, cunning, well-behaved child, prescription all OPEN; Facebook moved to "cannot
  expect it to inform us" + untouchable parameters; Goodhart/Strathern, Zylinska's note,
  "may be enough", antinomy-not-recantation, EU art. 14 high-risk, "inside firms" fixed.
  **Essay 6:** retitled "The cheap channel" (file 06-the-cheap-channel.html); p. 206
  ranking now OPEN with the chatbot material as a labelled analogy; pp. 215–236 covered
  (cerebromatics, persuasion p. 217, teletaxy, telegraphing/copying, hibernation) with
  rows on the blind (EARLY, Orion), remote-I (RA/WR, Lindbergh 2001), freezing (EARLY,
  Han 2023), copy≠original (OPEN, Parfit 1984), only-probable (HIT, Bostrom 2003); 1964
  baseline now Telesphere 1960 / Headsight 1961; afterwords cited via Zylinska only, not
  scored; vr-use-mix closed as a qualitative claim; IDC row corrected (AR/VR 2021 peak;
  VR/MR down in 2025 while smart glasses grew). verify.sh PASS: 104 quotes, 44 claims,
  0 open. AGENT.md gained three verdict rules (reductios, reported≠true, ranking≠order).
  Second panel pass launched on both.
- 2026-08-17 (panel round 2 → revision 2) — codex BLOCKED both again, on narrower grounds
  (drafts/reviews/*.r2.md). Acted on: **4:** EU AI Act art. 14 application postponed to
  2027-12-02 by Reg. 2026/1744 (real-world fact the register had missed) — brake now
  "on the statute book, untested"; construction row replaced (the substrate point is an
  *omission*, stated in prose, not a MISS row); new object rows: p. 110 method HIT,
  perceptrons p. 153 HIT, "robots with quasi-human personalities unlikely" p. 158 MISS,
  Coordinators OPEN (absence claim cannot pay MISS), megabyte bomb pp. 99–100 OPEN
  (Bornmann & Mutz 2015; window runs to 2034); Amazon → RIGHT ANSWER, WRONG REASON;
  Facebook opacity row cut, Facebook pays only the untouchable-parameter row (force
  clause dropped); rivals row → problem level, Calvano labelled simulated, RealPage
  updated to the Nov 2025 proposed settlement; "new strategy" clause unreceipted → cut
  from graded claim; "without new ideas", "most documented harm", ownership claim,
  Medicare-as-forecast, "steel mill's descendant" all cut; 1964 baseline receipted;
  "Beliefs of Electric Brains" explicitly handed to essay 5. **6:** frame now says the
  text-channel transposition is the essay's, not Lem's; entertainment MISS → OPEN (hedged
  both ways, pp. 214–215); the MISS is now later-Lem's self-grade via Zylinska p. 21;
  two RIGHT QUESTION, WRONG ANSWER rows (cost model; one-way media as art vs deepfakes);
  Bostrom demoted to cousin, HIT paid by Chalmers 2022; teletaxy → EARLY on BCI
  read/write receipts (Hochberg 2012, Flesher 2021), latency point in prose only;
  phantomatics proper → OPEN; neurotics row cut to prose ("reported"); cerebromatics
  HIT row added; central phantomatics in said + still-open; Guess 2023 balanced with
  Gauthier 2026 (X feed); Neuralink "investigational"; kidney "reproducible", not
  "first"; bandwidth numbers cut; still-open #1 closure by Lem's definition. verify.sh
  PASS: 113 quotes, 50 claims, 0 open. Round 3 panel launched; pushed as revision 2.
- 2026-08-17 (panel round 3 → revision 3) — codex BLOCK on 4 (drafts/reviews/*.r3.md) with a
  seven-item minimum set, all applied: personality row → RIGHT QUESTION, WRONG ANSWER with
  Lem's Leiber exception restored; spec-gaming split (objective-met-by-unchosen-route HIT;
  braked-then-reroute OPEN, unreceipted); toeslagen split from Robodebt (learning model,
  human-reviewed); megabyte bomb re-receipted on researcher headcount (UNESCO 2021: +13.7%
  2014–18, far below his ten-year doubling; barrier absent → OPEN); perceptron row ends at
  faces/text; advisory-body row → OPEN; "model the brake", "Beer's box", "cheapest thing to
  grow from text", "to the month" cut; contracts amended (essay 4 scope pp. 93–124, 146–163;
  "Beliefs of Electric Brains" → essay 5); CONTEXT thesis line no longer calls ciliates a
  substrate miss. Codex hit its usage cap (resets 2026-08-20) before consolidating 6, so
  round-3 grok+agy findings on 6 were adjudicated by me: cerebromatics HIT → OPEN with
  "through such maneuvers" scope; later-Lem MISS → OPEN (Zylinska's paraphrase is thin);
  freezing EARLY → MISS with "We can expect" restored (organ-scale path only); "unwarned"
  and "already lost" cut (judges knew); one-way row re-receipted with a one-way fake
  (Pentagon image 2023; Arup was a live call); Parfit split into two rows (copy≠original
  HIT; trip out of question OPEN); Guess/Gauthier described exactly; chess cut. Rejected:
  agy's claim that Jones & Bergen 2025 / Gauthier 2026 are invented (both verified). verify
  PASS: 118 quotes, 51 claims, 0 open. Pushed as revision 3. Next panel pass on either
  essay: after codex resets, one consolidated pass; do not iterate further without new
  evidence — remaining findings are judgment calls, logged here.
- 2026-08-17 (essays 5 and 7 drafted) — pitches banked in drafts/05.pitches.md and
  07.pitches.md; user picked **5-A "Real means useful"** and **7-B "Information farming"**.
  **Essay 5** (chapters/05-real-means-useful.html): the Designer's pragmatism (pp. 176–179)
  as the working epistemology of 2026 ML; includes ch. 4's "Belief and Information"
  (pp. 124–141) per the amended contract. Ledger 10 rows; MISS on p. 183 ("which rung
  corresponds to the mountain makes no sense") against interpretability results;
  RIGHT QUESTION, WRONG ANSWER on "resolve it by experiment" (p. 179) vs the benchmark
  evaluation crisis; HITs on the side entrance (AlphaFold), the lossy model beating the
  faithful one (GraphCast), belief-as-forced-guessing (p. 125 vs hallucination).
  **Essay 7** (chapters/07-information-farming.html, "The farm and the sieve"): his design
  vs Ashby's, which he explicitly declined on p. 261 — two MISS rows (the polymer carriers;
  the bet against filtering) with FunSearch/GNoME as the receipt that the filter won; HITs
  on automated hypothesis formation (Adam 2009 → AI Scientist 2026), the sieve coupled to a
  phenomenon (A-Lab), the combinatorial wall *as qualified* (p. 239), and selection as the
  crux; RIGHT QUESTION, WRONG ANSWER on automating production as the answer to the deluge
  (record retractions 2023). Linguistic engineering covered (EARLY row) — it is the best
  answer in the book to essay 4's language omission; transcendence/cosmogonics treated as
  the speculation Lem labels, constructor side left to Still open. verify.sh PASS: 181
  quotes, 72 claims, 0 open. Panel not yet run on 5 and 7 (codex quota resets 2026-08-20).
- 2026-08-17 (paused mid-review) — essay 5 revised once against agy's round-1 report
  (see commit "Essay 5: fixes from agy round 1"): side-entrance row re-receipted with the
  literal case (synthetic genome, 2010), new object rows for the tissue brain (EARLY,
  DishBrain 2022) and talent matrices (MISS — selection is not embedding), GraphCast row
  rephrased, ladder MISS now labels its transposition, benchmark row → OPEN, 1964 baseline
  corrected and given its own claim row; two exact-page fixes (phantomological generator
  p. 184, "to prove belief is to destroy it" p. 286). grok's essay-5 run died at its turn
  limit with no findings. **Codex is working again** and has consolidated essay 5 —
  drafts/reviews/05-codex.md, NOT YET ACTED ON. Essay 7's grok+agy reports exist
  (07-grok.md is short, 07-agy.md full) and no codex pass has been run on 7 yet.
  **Resume here:** read 05-codex.md, apply, then run scripts/review.sh 07 (all three now
  available) and act on that. verify.sh PASS at the pause: 181 quotes, 77 claims, 0 open.
- 2026-08-17 (panel on 5 and 7; codex back) — codex BLOCKed both; both rebuilt.
  **Essay 5:** the thesis was wrong. p. 176 says the Designer "is not a narrow pragmatist…
  knows everything about his bricks" — he drops the metaphysics and keeps the materials
  science, while 2026 dropped both. Central row is now RIGHT ANSWER, WRONG REASON; the
  ladder MISS and the benchmark row left the ledger (kept as labelled prose, since the
  transposition is the essay's, not Lem's); the believing-machines programme became the
  RIGHT QUESTION, WRONG ANSWER; tissue brain and talent matrices → OPEN (no-live-path
  unproven; the societies *called for* a moratorium); hallucination → RIGHT ANSWER, WRONG
  REASON; the GraphCast row was cut entirely (a performance result cannot pay a
  modelling-relation claim); later-Lem's self-grade acknowledged via Zylinska p. 21;
  Konstruktor translation noted; nine unregistered quotations added at their true pages.
  **Essay 7:** retitled "What the sieve is wired to". Both MISS rows failed §4 and are gone
  — Lem rejected *maximum random* diversity on p. 261, not filtering, and both he and Ashby
  put selection at the centre, so "the part neither thought was hard" was false. The essay's
  negative is now p. 251: stay with formal symbol-pushing and "we will be facing an
  information crisis", the way out being the egg's non-formal route — and the automation
  came from inside the formalism (RIGHT QUESTION, WRONG ANSWER). Hypothesis-formation row
  re-anchored from p. 239 (a report of Amarel's existing work) to his own p. 243 device;
  the A-Lab sieve HIT folded into the problem-level row about what the selector is wired to;
  carriers and the theories-from-theories climb → OPEN; deluge row → OPEN (retractions are
  paper mills, not automated discovery); combinatorial wall re-receipted with intrinsic
  dimension (Pope et al. 2021); 1964 baseline corrected — laboratory automation existed
  (AutoAnalyzer 1957, Robot Chemist 1959), it just did not form hypotheses. verify.sh PASS:
  196 quotes, 78 claims, 0 open.


**2026-08-18 — panel round 2 (essay 7) applied; essay 7 rebuilt a second time.**
Codex's consolidation (`drafts/reviews/07-codex.r2.md`, BLOCK) found the essay had scored
the wrong argument, and it was right. **Lem's note 8 (pp. 365–367)** — three pages of small
type at the back of the book — is an essay in which he grades his own information farm and
supplies the selector the chapter lacks. He says a farm "can actually exacerbate, rather
than diminish, a crisis resulting from the excess of information" (p. 365); that detached
from its human matrix it becomes a "bomb—if not a megabyte then at least a gigabyte one"
(p. 366); that "As long as the selectors at the information farm are under the active
influence of intelligent beings, they are capable of selecting information effectively"
(p. 366); and that a farm without an "addressing sieve" produces a paper deluge making
"any further research impossible", so that "the automatization of cognitive processes, at
least within the field of librarianship and publishing, is a more urgent task" (p. 367).
So the essay was rebuilt around **two sieves** — one wired to the phenomenon (what is true),
one wired to the addressee (what is worth saying) — retitled "The two sieves", and now
carries a genuine **MISS**: on p. 367 he calls a machine librarian "based on frequency
analysis" impossible and "algorithmic methods… worthless" for selection; Garfield's Science
Citation Index appeared that same year, ran scientific search for fifty years, and became
PageRank in 1998. The p. 251 formalism row moved to problem level as RIGHT ANSWER, WRONG
REASON (the crisis came, but from production without addressing, which his own note says).
Also fixed: the p. 243 row restored "generalize it in the same way the scientist does" and
"Our device thus produces theories" and dropped to EARLY; pp. 276–277 (predictions stripped
of explanations — HIT, AlphaFold + GenCast) split from p. 280 (causal language of the next
kind — OPEN, since designed protein sequences are his *first* causal language, not a
successor); FunSearch demoted from the world-coupled case to formal search with an exact
evaluator; the "nowhere else in the book" lede claim cut; the unreceipted 1964
counterfactual cut; absence claims bounded to the systems surveyed. **A-Lab receipt
superseded:** the Author Correction of 2026-01-19 gives 36 compounds from 57 targets,
"novel" dropped from the title, novelty meaning new to the prediction platform, and 36 of
40 successes confirmed on manual re-analysis — so the 2024 critique is a dispute over
novelty and phase identification, not a demonstration of failure, and the essay now says so.
New AGENT.md rule: read the chapter's endnotes before drafting. verify.sh PASS: 219 quotes,
85 claims, 0 open; essay 7 at 3,200 words.

**2026-08-18 — panel round 3 (essay 7) applied; ledger rebuilt.** Round 3 (`*.r3.md`,
BLOCK, 15 findings) caught three real errors the earlier rounds had not. **(1) Two
different information crises were conflated.** p. 251's crisis is about *representation* —
a written score for embryogenesis would need formulae "in the realm of quadrillions. There
would not be enough surface across all the oceans and the entire mainland for it" — not
note 8's paper deluge. The RIGHT ANSWER, WRONG REASON row was wrong and is now a
RIGHT QUESTION, WRONG ANSWER row on the substrate premise itself ("We need to represent
processes with some other processes, not with formal signs", p. 263): what carried it was
a formalism that *runs*, neither of the two options he posed. **(2) The Ashby account was
wrong.** p. 261 says outright "Mathematicians are thus a generator of diversity, whereas
empiricists are the selector postulated by Ashby", so formal generate-and-select is on his
map; the essay's claim that it was "the road neither man drew" is deleted, as is the claim
that comprehension was his objection to Ashby (it is his objection at p. 367). **(3) The
chronology contradicted itself** across lede, ledger and closing — citation retrieval
(1964) came first, automated truth loops (2009+) much later, and the machine he specified,
"sending the right kinds of information to the right kinds of people", was never built.
That is now stated once and consistently. Also: the p. 367 publication-criteria quote
restored its "It seems that" hedge and its row is no longer paid by the unmet clause "any
further research impossible"; the three note-8 rows moved to object level with one
problem-level row for the general dilemma and a new OPEN on p. 365 ("Such a decision-making
process must not be mechanized"); pp. 276–277 split so the HIT sits on p. 276's
unconditional forecast and p. 277's conditional consequent is scored OPEN with p. 280; the
combinatorial-wall row dropped entirely (image-manifold dimension never tested Lem's
ceiling, and "his own arithmetic" grades no 2026 event) and `intrinsic-dimension-2021`
retired from the register; TEMPLATE violations fixed (Still open 4→3 items, Reading 13→3
modern sources); "The Engineering of Transcendence" (pp. 281–286) restored per the §6
contract. **Rejected:** codex's claim that the 2026 *Nature* paper reports humans manually
filtering outputs at each stage — the paper is paywalled and neither Sakana's post, the
*Nature* news piece nor phys.org states it, so it is not receipted. Essay 7 is now closed
to further review per the diminishing-returns rule. verify.sh PASS: 219 quotes, 84 claims,
0 open; 3,198 words.

**2026-08-18 — essay 8 drafted, "The invisible path" (angle 8-A).** Pitch gate run on ch. 8
(`drafts/08.pitches.md`, four angles); user chose 8-A. Ledger written first
(`drafts/08.ledger.md`), then prose. The essay is built on "The Autoevolutionary Machine"
(pp. 344–347), the section the old §6 line did not mention: Lem forecasts that control of
human heredity arrives through machine matchmaking plus genotype screening, because that
route "seems the least drastic one as it remains invisible" (p. 345), and closes with
"'Cutting up people's brains and bodies' evokes disgust, whereas 'machinic marriage
counseling' seems to be quite an innocent intervention—yet these are just two paths of
different lengths that can both lead to analogous results" (p. 347). Verdicts: the adoption
forecast HIT (online overtook friends c. 2013), the two-level genotype selector RIGHT ANSWER,
WRONG REASON (it exists and sells his exact menu — IQ, anxiety, ADHD, appearance — but
screens embryos, not partners), the millennial timescale RIGHT QUESTION, WRONG ANSWER (IVF
moved the unit of selection off mating), and the genuine **MISS** on "It would be relatively
easy… to distribute widely high intelligence" (p. 346): selecting the top of ten embryos buys
~2.5 IQ points, capped by within-family variance, which no better score enlarges. Cyborg
rejection and the sub-100 lifespan deflation both HIT. Three OPEN rows: whether the machine
has the "better knowledge" he grants it (Joel et al. 2017 says no), his consent problem
(unimproved and unanswered — the 23andMe bankruptcy moved 15M genomes through a court
auction), and note 2's demand for "conscious and responsible risk".

**Two corrections to this file.** (1) §6 called the ESP section "the ESP misstep": wrong.
At pp. 347–350 Lem *rejects* extrasensory phenomena, and by an argument nobody else was
making — if telepathy worked, selection would have found and accumulated it — plus note 10
(p. 371), which describes the file-drawer effect and the garden of forking paths in 1964
("there will be five or six people left on the battlefield—those who have obtained positive
results several times in a row"). That is Lem at his best and belongs in essay 0's account of
the method, not in a list of errors. (2) §6's essay-8 title is now "The invisible path".
**Dating caveat** (as for essay 5): the 2013 translation is of a later edition — this
chapter's conclusion is signed "Krakow, August 1966" — so ch. 8's baseline is mid-1960s,
not 1964. verify.sh PASS: 273 quotes, 93 claims, 0 open; 3,119 words.

**2026-08-18 — panel round 3 (essay 5) applied; the MISS withdrawn, a real one found.**
BLOCK (`drafts/reviews/05-*.r3.md`; grok returned a full report this round rather than dying
at its turn limit). The decisive finding is that essay 5's only MISS was not earned. The row
graded Lem's p. 193 ordering claim "Reversed" on the strength of Sc2.0 — but the Boeke lab's
own project page states that consolidating the sixteen synthetic chromosomes into a single
organism is still the final phase, so there is no artificial "chromosome apparatus of a
nucleus"; neither side of his comparison has happened and the order cannot be scored. Row →
OPEN, and `sc2-2023` corrected (individually synthesised and validated; consolidation
pending; and the work was redesign plus debugging, not manufacture alone — recoded stops,
relocated tRNAs, loxPsym sites). Also withdrawn: the p. 125 RIGHT ANSWER, WRONG REASON row,
which graded a cousin — Lem's homeostat believes because refusing to act ends life, the
hallucination paper is about grading rewarding a guess; the comparison stays in prose,
explicitly unscored.

That left no negative, so per AGENT rule 2 the search was for an honest one rather than a
manufactured one — and it was already in the essay's own thesis, unscored: p. 176's "The
designer is not a narrow pragmatist… The designer knows everything about his bricks." Lem's
Designer drops the definitive question and keeps the materials science; 2026 dropped both.
New problem-level row, **RIGHT QUESTION, WRONG ANSWER**, receipted on the bitter lesson,
Zhang et al. 2017 and the interpretability statement. Ledger is now 8 rows: 7 OPEN + 1 RQWA,
and "Where he was worst" says so and invites attack on that.

Other fixes: Lem's own provisional answer to the surplus question restored (p. 188, "there
exists a continuity of transformations in the world… their feedback") — the essay had said
he "cannot answer and says so", which was unfair; the Othello/SAE material demoted from
refutation to labelled analogy (and "Lem's own Designer would have wanted this" cut); "nobody
derived from first principles", "Frontier labs state plainly" (→ Anthropic), "the later Lem
had already claimed this ground", "never had a theory of what the sequence means" and several
unmarked absence claims all bounded or cut; **an arithmetic error in my own text corrected**
("six of eight rows are OPEN" — it was five). Template violations fixed: lede 164→106
(≤120), What Lem said 1,189→893 (600–900), What happened 827→700 (≤700), Reading 7→3 modern
sources, nav contents link restored. **A misquote I introduced while trimming was caught by
regenerating the quote rows** — "we need some restraint" is "We thus need some restraint"
(p. 176); note that `verify.sh` cannot catch this class, because a quote with no row is not
checked. Regenerate essay quote rows after any prose edit. Rejected: agy's claim that the
hallucination paper is not OpenAI's (it is). verify.sh PASS: 257 quotes, 93 claims, 0 open;
2,856 words. Essay 5 now closed to further review with 4, 6 and 7.

**2026-08-18 — panel round 1 (essay 8) applied; the thesis changed.** BLOCK, 27 reviewer
findings adjudicated. The decisive one: **Lem's machine exists.** Dor Yeshorim has run since
1983 — young people in Orthodox Jewish communities are tested and given an anonymous number,
and when a match is proposed the two numbers are checked together, before the couple meets,
returning proceed or incompatible. That is the p. 345 second-level partner-genotype selector,
operating on exactly the branch he graded "a correct decision", and the essay had asserted it
"did not arrive in the matchmaker". Rebuilt around it: the disease branch is now a bounded
**HIT**; the intelligence/personality branch is EARLY, on a different device (embryo
scoring), counted as a third path rather than his second stage arriving late.

**The MISS was manufactured and is withdrawn** — the same failure as essay 5, one round
later. Lem's "relatively easy" (p. 346) contrasts distributing intelligence with "a deep
transformation of man's systemic organization", by partner selection over millennia; the
essay tested one-generation embryo selection and debited him for its within-family limit.
Also, Karavani's ~2.5 IQ points is predictor-relative — the paper says expected gain scales
with the square root of variance explained — so "a limit no better score removes" was wrong.
Row → OPEN, claim row corrected. The honest negative is the **cultural-authority forecast**:
he assumed the machine would acquire standing by being right, and no mass platform ever did;
where the norm exists, a community that already held authority over marriage routed it
through a test — a precondition he never names. RIGHT QUESTION, WRONG ANSWER.

Other corrections, all verified against sources: **He Jiankui had three children, not two**
(a third born 2019, acknowledged in the December 2019 judgment), so "no further gene-edited
children" was false; **23andMe changed owner once, not twice** (Regeneron won an auction bid
but never closed; TTAM completed in July 2025) — and since a data sale does not test Lem's
population-authorization dilemma, that paragraph and the `23andme-2025` row are gone;
**implanted insulin pumps are not routine** (routine pumps are external), row narrowed to
intrathecal pumps and subdermal implants; **Rosenfeld pays "where couples met", not
algorithmic matching**, now labelled as such; **Joel et al. tests initial desire at speed
dates**, not relationship stability, so the "better knowledge" row is OPEN and no longer
claims more; the p. 347 row split so the disgust asymmetry is HIT and "analogous results"
stays OPEN, matching Still open #3; the p. 344 "bottled fetuses" framing and the "(so far
limited)" hedge restored, and the unfair claim that Lem took the stability figure on trust
removed. Template fixed (lede 145→99, said 1,115→897, happened 713→650). A quote truncated
mid-parenthesis — "(which raises some doubts)" for "(which raises some doubts, at least for
the time being)" — was caught by the new regenerate-the-rows rule.

**Also fixed here:** `CONTEXT.md` §5 still said ch. 8's ESP section "has aged worst" and told
the writer to say Lem was smug about it, contradicting the 2026-08-18 correction below. Both
lines updated; the authority file no longer gives opposite instructions. verify.sh PASS: 277
quotes, 93 claims, 0 open; 2,801 words.

**2026-08-18 — essay 2 drafted, "The last lawnmower" (angle 2-A).** Pitch gate run on ch. 2
(`drafts/02.pitches.md`, four angles); user chose 2-A. The essay grades the analogy that gives
the chapter its title, on the dated artifacts Lem staked it on. Verdicts: the successor
technology a clean **MISS** — wheel drive is untouched, the car-carrying cross-Channel
hovercraft closed in 2000 and large commercial hovercraft vanished, and what displaced the
combustion engine was an electric motor under the same wheels (25% of global new-car sales in
2025). The relic prediction is **OPEN** and being falsified from the wrong end: California
required most new small off-road engines to be zero-emission from January 2024, so the
lawnmower is dying before the car, and by statute. VTOL **HIT** (Harrier 1969, V-22 2007,
F-35B 2015 — defending a niche, not taking the helicopter's; no US eVTOL type certificate
yet). Radio's radiation **HIT**, with the current squeeze coming from the electric drivetrain
interfering with AM. The morphological pattern **HIT** at problem level.

**Note 1 (p. 356) again supplies the essay's best material** — the third chapter running where
the endnote beats the chapter. Lem names the disanalogy the chapter never mentions:
technologies cross-fertilise where "biological species, having become fixed, cannot", giving
"constant acceleration" and "sudden turns—which are totally unexpected and unpredictable".
Scored HIT, receipted on AlexNet trained on two consumer graphics cards — statistics crossed
with video-game hardware. The negative is at problem level: his claim that both evolutions
have "almost the same number of degrees of freedom and… similar dynamic laws" (p. 38) fails
for software, where there is no extinction — COBOL still runs core banking at an estimated
220–800 billion lines. Biological relics survive in the margins; software relics survive in
the centre. RIGHT QUESTION, WRONG ANSWER.

The chapter's other limit, stated in "Where he was worst": his model has exactly one selection
pressure, competition in a niche. But the small petrol engine is not being outcompeted, it is
being prohibited, and AM radio is not being saved by fitness but by a bill with 296 House
cosponsors. Technologies have a legislature, which can preserve the unfit and kill the fit,
and the two-evolutions model has nowhere to put it. Essay 4's nav updated to point back to
essay 2. verify.sh PASS: 315 quotes, 102 claims, 0 open; 2,520 words.

**2026-08-18 — essay 3 drafted, "Who pays for the telescope" (angle 3-D).** Pitch gate run on
ch. 3 (`drafts/03.pitches.md`, four angles); user chose 3-D over the recommended 3-A, taking
the political economy of contact rather than the silence itself. That leaves the chapter's
famous material — the metatheory of miracles (pp. 70–73), Votum Separatum (pp. 83–86),
hypothesis III — unscored and available; note it as a candidate if the book ever wants a
second pass at ch. 3, and note that essay 0 must not assume ch. 3's silence was graded.

The essay takes pp. 89–90, where Lem stops asking whether they are there and asks what the
search costs, who pays, who transmits, and whether a message would be recognisable. Verdicts:
his cost estimate — investment "even more substantial than the current investment in research
on nuclear energy" — is a clean **MISS**, out by roughly two orders of magnitude (the largest
searches ever mounted run at about $10M/yr; US fusion alone was $790M in FY2025 and ITER has
passed $20bn). His political forecast is **RIGHT QUESTION, WRONG ANSWER**: the bottleneck was
exactly where he put it, and the rulers never came — HRMS killed by a Senate amendment about a
year after it began, the Allen array hibernating in 2011 and returning partly by tracking
orbital debris for the Air Force, then Breakthrough Listen's $100M and the SETI Institute's
$200M bequest from a dead Qualcomm founder. HITs: the transmit/receive asymmetry (p. 90) is now
the METI dispute; the compression argument is how narrowband searches are designed; the
star-flight energy budget is unchanged.

The essay's sharpest point is at problem level and turns Lem against his own chapter: at p. 80
he says the absence of data gains significance "the longer such attempts take and the more
sensitive the instruments used in them are" — a condition sixty years of hobby-scale funding
has not met. So the silence the chapter treats as data may be what $10 million a year sounds
like. Scored OPEN. Navigation now runs 2 → 3 → 4. verify.sh PASS: 111 claims, 0 open;
2,437 words.

**2026-08-18 — panel round 1 (essay 2) applied; essay rebuilt, and a citation error corrected
in this file.** BLOCK, 14 findings. Two were serious.

**(1) Contract breach.** §6 requires ch. 2's essay to cover the parallel *and* "Several Naïve
Questions"; angle 2-A stopped at pp. 33–38 and an endnote. A chosen pitch does not amend the
authority document. The essay now covers p. 43 (technical evolution "has so far been moving in
a kind of reverse direction… only… creating narrowly specialized devices" → **MISS**, the
direction reversed; and the named route to universality via "self-organizing systems… capable
of adaptive self-programming" → **RIGHT ANSWER, WRONG REASON**, since what arrived is
self-programmed but by gradient descent, not by that theory) and pp. 56–57 (his refusal to
reserve creative work for humans → **HIT**; "will not need programmers anymore" → OPEN;
"'cleverer' does not yet mean 'rebellious'" → moved to Still open).

**(2) The note is note 6, not note 1, and it hangs from p. 47.** Chapter 2's notes 1–4 are
translator's notes (gender of *technika*, Hoyle, videorama, Davitashvili). The hybridisation
note attaches to "Everything else… is still ahead of us" at the end of the theory-versus-
empiricism discussion, not to the parallel — and it *qualifies* the analogy rather than
retracting it, since the chapter already has a "Differences" section from p. 38. Every "note
1" and "a disanalogy the chapter never mentions" formulation is gone from the essay, and the
2026-08-18 entry above is wrong on this point; this entry supersedes it.

Also corrected: the legislature claim overstated the chapter (p. 38 says technical evolution
is "not… people-free" and not amoral, so the gap is narrower — he models agency as choice of
direction, not enforceable prohibition; now OPEN, not an absolute). The radio-radiation HIT
was paid by the wrong event (AM removal is habitat loss, not diversification) and is cut. The
omnibus morphological HIT laundered untested components and is cut. The VTOL row no longer
treats an aircraft that already existed as a forecast: the P.1127 hovered in 1960 and the
Harrier entered service in 1969, both before the 1974 edition this translation follows, so the
row now grades the *mechanism* — niche defence rather than displacement — against the V-22
(2007) and F-35B (2015). The AlexNet row is narrowed to cross-domain recombination and
labelled as the essay's illustration. COBOL figures are labelled trade estimates and the
thesis is now "software relics can survive in the centre". Two citations moved p. 33 → p. 34.
The archaeopteryx attribution is cut. Disputed AM cosponsor counts are out of the prose —
congress.gov blocks automated fetches, two sources disagree, and the point does not need the
number. **A 1974-edition caveat is now stated in the essay itself**, since Harrier and SR.N4
service both predate the text. Two more misquotes were caught by regenerating quote rows: "It
is here perhaps that the biggest difference lies" and "only been creating narrowly specialized
devices". verify.sh PASS; 2,886 words.

**2026-08-18 — essay 1 drafted, "The three ways to be wrong" (angle 1-A).** Pitch gate run on
ch. 1 (`drafts/01.pitches.md`); user chose 1-A. The essay grades Lem's own taxonomy of
forecasting error against this book's ledgers, which is the only fair dataset for it and the
bridge into essay 0. His three modes: the sudden turn ("burst forth like Athena from Zeus's
head", p. 28), the straight line ("the world full of balloons", p. 28), and the closed schema
with its sick man who "can… go on living until old age" (pp. 29–30).

Verdicts: all three modes HIT, receipted from other essays' rows — sudden turn on the language
omission (essay 4/7) and the unit of selection moving to the embryo (essay 8); straight line on
his own air-cushion successor (essay 2) and the SETI cost estimate (essay 3); closed schema on
VR's plateau (essay 6) and the search that simply continues (essay 3). The **MISS** is
self-inflicted and is the chapter's own best exhibit: four paragraphs after convicting Blackett
of a failed atomic forecast, he writes that "Current estimates situate the production of the
microfusion cell in the 1990s, or even later" (p. 28). ITER is now not expected to be fully
operational until 2039.

The problem-level negative is that **the taxonomy is short by one**. A fourth mode recurs in
these ledgers: choosing the successor that abolishes the most over the one that changes the
least — the motor replaced but not the wheel (essay 2), executable formalism rather than polymer
carriers (essay 7). It is not a straight line, not a sudden turn, and has no ending in it; the
essay calls it the impressive-successor error and labels the naming as its own. RIGHT QUESTION,
WRONG ANSWER. **Essay 0 should take this over**: the fourth mode, and the finding that naming
the modes did not protect Lem from two of them, are the raw material for the method chapter.

Also recorded: essay 1 is the first essay whose receipts are mostly other essays' claim rows,
which the register handles because ids are global. Navigation now runs 1 → 2 → 3 → 4. The
`am-radio-ev` row now carries exact cosponsor counts (60 Senate, 317 House) read from
congress.gov on 2026-08-18 and supplied by the user, correcting the secondary source that said
"more than 60 Senators" by counting the sponsor. verify.sh PASS: 112 claims, 0 open;
2,386 words.

**2026-08-18 — essay 0 drafted, "How to grade a prophet". The book is complete except essay 9.**
Written last by design, and it reports rather than promises. Its Lem material is the Conclusion
(pp. 351–352), where he defends his own procedure, and Zylinska's introduction. **Two contract
corrections recorded here:** (1) §6 assigned "Twenty Years Later" to essay 0, but that essay is
*not in this English edition* — the 2013 volume runs Translator's Introduction, chs. 1–8,
Conclusion, Notes, Bibliography, Index. Both "Twenty Years Later" (1982) and "Thirty Years
Later" are absent, and they are the only direct check on whether this book's verdicts are
harsher than Lem's own. (2) The thesis came from p. 20: in 1991 Lem said he would gladly publish
"a new critical edition of Summa, much enlarged to include… my commentary on the things I wrote
in the 1960s". This book is that edition with the commentary supplied by the sixty years.

**The census, computed from the published essays, not typed: 82 rows — 32 OPEN, 26 HIT, 11
RIGHT QUESTION WRONG ANSWER, 6 MISS, 4 EARLY, 3 RIGHT ANSWER WRONG REASON.** OPEN is the modal
verdict. **DISSOLVED was never used once in 82 rows** — the vocabulary is adequate and
oversized, and that is now a finding rather than an oversight.

Essay 0's own ledger grades the method: the "never false" rule → RIGHT QUESTION, WRONG ANSWER
(the gate is blind to unregistered quotations, and two misquotes reached the live site, both
introduced while trimming); the seven-word vocabulary → HIT; the mandatory-negative rule →
RIGHT ANSWER, WRONG REASON (it produced four manufactured negatives that had to be withdrawn);
the two-layer separation → HIT; **dating the corpus → MISS**, because the book said "1964"
throughout for a 1974 fourth edition. That error is now fixed in all eight essays, which carry
the edition caveat; essay 2 had actually credited Lem with a mechanism illustrated by an
aircraft in service five years before the edition it quotes.

Standing lessons for any future book built this way, all learned the hard way here: read the
endnotes before drafting (they beat the chapter three times); regenerate quote rows after every
prose edit; and if no honest negative exists, say the chapter is different and invite attack —
do not manufacture one, because the manufactured negative always takes the same form, grading
the essay's own transposition as the author's claim.

**2026-08-18 — panel round 1 (essay 3) applied; contract covered, cost MISS withdrawn.** BLOCK.
The same contract breach as essay 2: §6 requires the von Hoerner/Drake statistics, the
catastrophic theory, *Votum Separatum* and the SETI negatives, and angle 3-D had restricted
grading to pp. 89–90. All of it is now in the essay, and **note 3 (pp. 358–359) turns out to
carry Lem's own answer** — the fourth time an endnote has decided an essay. Having rejected
prompt extinction as "an absurd kind of determinism" and rarity as a contradiction of cosmic
homogeneity, he writes that the isolation hypothesis "seems to be the most probable one. It has
therefore been selected as the dominant hypothesis in the course of writing this book." The
chapter itself never says this.

**The cost MISS is withdrawn.** Lem asked for "a great amount of equipment" and possibly
transmitters; the essay compared a $10M/yr programme commitment against annual fusion research
and ITER's cumulative construction. Not like-for-like — and Breakthrough Listen observes on the
NSF's Green Bank and CSIRO's Parkes rather than on anything it built, so the search was cheap
partly because it borrowed. Row → OPEN. The negative is now the rulers row, RIGHT QUESTION,
WRONG ANSWER, bounded: the one large public programme died by amendment and dedicated searching
ran on philanthropy *using public telescopes*, which is narrower and true. "Every serious
attempt… paid for by individuals" was false and is gone.

**The essay's central point is now correctly grounded.** It used annual budget as the measure of
whether the silence means anything; the right measure is search completeness, and Wright,
Kanodia & Lubar (AJ 2018) supply it — the fraction of the eight-dimensional radio search space
examined is comparable to a drinking glass of seawater against Earth's oceans. Lem's own hedge
at p. 80, "Today it is still too early for this", was also omitted and is restored.

Other fixes: the reception-only row moved to problem level (terrestrial behaviour cannot
establish what alien civilisations do) and its history corrected — **Drake's Arecibo message of
1974 was missing** from both essay and register; the star-flight row → OPEN (sixty years is not
the "several hundred" he allowed, and Starshot is an uncrewed interstellar proof-of-concept, not
von Hoerner's crewed intergalactic crossing, whose calculation is his and not Lem's); the
call-signs row states its baseline, since Ozma was already hunting artificial regularity in 1960.

**Two new AGENT rules, both paid for twice:** check the chosen pitch against §6 before drafting
and amend the contract explicitly if the angle narrows scope; and note two corpus limits —
`corpus.py` strips bracketed insertions, so **translator's notes are unquotable** (this caught
an attempt to quote note 5's "And also in 1974"), and a quotation spanning a page break must be
filed under the first page.
