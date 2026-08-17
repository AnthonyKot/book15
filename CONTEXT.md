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
| 8 | 8 A Lampoon of Evolution (294–~350) | Redesigning the designer | CRISPR, He Jiankui, longevity, prosthetics; the ESP misstep |
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
  is a very good interlocutor to be answered. Where he was smug (ESP), say so.
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
  ethics debates. Also the one section that has aged worst: extrasensory phenomena.
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

