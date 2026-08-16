# Book 15 — CONTEXT (authority document)

**Working title: *Sixty Years Later*.** Ten essays reading Stanisław Lem's *Summa
Technologiae* (1964) from 2026: chapter by chapter, where he was right, wrong, right for
the wrong reason, or asking a question that has since dissolved or is still open.
Lem graded himself in "Twenty Years Later" (1974) and again in the 1990s; this book is
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
he was wrong in a specific, dated way (1960s cybernetics, information theory as the master
science, no notion that *statistics + data* rather than *design* would produce
intelligence) — and 2026's own blind spots are probably of the same kind.

## 2. Corpus

- **Primary:** Lem, *Summa Technologiae*, trans. Joanna Zylinska, Minnesota 2013
  (Electronic Mediations 40), 383 pp. Local: `resources/lem-summa-2013.pdf` →
  `resources/text/summa.txt` (both gitignored; rebuild with `scripts/build-corpus.sh`).
  PDF page N == printed page N; the extraction is quotable and section-mapped.
- **Corpus gap (recorded 2026-08-16):** the 2013 translation carries chapters 1–8 only.
  Chapter 9, *Sztuka i technologia*, is absent, as is the 1974 afterword "Dwadzieścia
  lat później" (quoted only in Zylinska's introduction). Essay 9 needs the Polish
  (Wydawnictwo Literackie, 4th exp. ed. 1984 or later) or the Russian (*Сумма
  технологии*, Мир 1968 / АСТ 2002). Until one is on disk, essay 9 quotes cannot be
  gated and the essay does not ship. **Open: user to supply a copy.**
- **Secondary, Lem:** "Twenty Years Later" (1974), "Thirty Years Later" (1991),
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
- The 1974/1991 self-grades: when Lem already conceded or doubled down, quote him, and
  score 2026 against *that* Lem too. Never grade 1964-Lem on something 1974-Lem fixed
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
  (learning from data rather than design; language as the substrate).
- **5 Prolegomena.** Job: imitology and "the silence of the designer" — building things
  that work without a theory of why. Test: modern ML *is* this. Where the argument
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
