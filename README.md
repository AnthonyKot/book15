# Sixty Years Later

**Read it: <https://anthonykot.github.io/book15/>**

Ten essays reading Stanisław Lem's *Summa Technologiae* (1964) from 2026 — chapter by
chapter, where he was right, wrong, right for the wrong reason, or asking a question that is
still open. Fifteenth in a series built the same way (static HTML, a decision record, a
verification script a distrustful reader can run).

    CONTEXT.md      authority: thesis, corpus, spine, verdict vocabulary, essay contracts, status
    AGENT.md        rules for the writing model; pitch gate; pre-ship test; review panel
    TEMPLATE.md     essay beats
    chapters/       one HTML file per essay
    checks/         quotes.tsv (Lem, gating), claims-2026.tsv (our side, receipted), lints
    scripts/        build-corpus.sh, find.py (corpus search by page/section), review.sh (panel)
    resources/      the PDF and its extraction — gitignored, not redistributed

    scripts/build-corpus.sh ~/path/lem.pdf   # rebuild resources/text/summa.txt
    scripts/find.py "the black box"          # page + section for every hit
    ./verify.sh [NN] [--structure]           # quotes, claim markers, links, counts
    scripts/review.sh NN                     # grok + agy review, codex consolidates
