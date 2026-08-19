# Paper build

The submission itself: `main.tex` compiled against the official NeurIPS 2026
style files, plus the mandatory paper checklist.

```bash
python econml/paper/make_figures.py     # figures, from the committed result JSONs
cd econml/paper && pdflatex main.tex && pdflatex main.tex
```

Two passes, because the cross-references to numbered theorems resolve on the
second. No bibtex run: the bibliography is a `thebibliography` block inside
`main.tex`, since 22 entries do not justify a `.bib` and a manual list cannot
go stale against one.

## Files

| File | What it is |
|---|---|
| `main.tex` | The paper |
| `checklist.tex` | The NeurIPS checklist, all 16 questions answered |
| `neurips_2026.sty` | Official style file, **unmodified** |
| `checklist_template.tex` | The blank checklist as shipped, kept for diffing |
| `make_figures.py` | Renders the five figures from `../ml-contributions/experiments/results/` |
| `figures/*.pdf` | Generated, vector |
| `main.pdf` | The compiled submission |

## Compliance

**Format.** `\usepackage[dblblindworkshop]{neurips_2026}` with `\workshoptitle`,
which is the double-blind workshop track. The style file is used as shipped;
tweaking it is grounds for desk rejection. Options `final` and `preprint` are
both omitted, so the build anonymizes itself and adds line numbers for review.

**Page count.** Nine content pages, ending with the conclusion. References,
the appendix pointer and the checklist begin on page 10 and do not count
against the limit. Verify after any edit:

```bash
pdftotext -f 10 -l 10 econml/paper/main.pdf - | head -2
```

That should print the References heading. If content has spilled onto page 10,
the paper is over.

**Checklist.** All 16 questions answered with a justification each, the
instruction block deleted and the section heading kept, as the template
requires. Answers: yes to 1, 2, 3, 4, 6, 8, 9, 10, 12; no to 5 and 7; not
applicable to 11, 13, 14, 15, 16. The two `no` answers are deliberate and
justified in place. Question 5 is `no` because the repository names an author
and is withheld until the paper is de-anonymized. Question 7 is `no` because
the panels are deterministic, so worst-case departure from the closed form
across a whole grid is reported instead of error bars over seeds, which is the
stronger statement.

**Double-blind.** No author block, no repository URL, no acknowledgments. PDF
metadata carries no title, author, subject or keywords. Figure files are
generated from result JSONs and carry no local paths. REFLEX and PEBSA are
cited as ordinary third-party references and no sentence positions either as
the authors' own work.

## The artifact URL

The public repository is `github.com/vignesh-nagarajan-vn/PRICE`. **It is not in
the submission**, and the line that would add it sits commented out in
`main.tex` next to the sentence it belongs to. The URL contains an author name,
so including it under double-blind review would break anonymity and invite desk
rejection. Uncomment it for the camera-ready version, when the paper is
de-anonymized anyway.

The live sentence promises code, derivations and certificates to reviewers as
anonymized supplementary material, which is what a double-blind submission may
say, and the checklist's question 5 states the same arrangement.

## What did not make the paper

The build folder holds more than nine pages of drafted content. What was cut
from `../writing/` on the way into LaTeX, and why:

- **Proof bodies.** Sketches stay inline, complete proofs go to the appendix.
  A workshop reviewer wants the mechanism and the assumptions, not the algebra.
- **The worked tables in Sections 5 and 6.** Reduced to inline numbers, which
  cost a fifth of the space and carry the same three values.
- **The clustered-companion figure**, folded into a row of the panel table.
- **Section 8's longer form**, already collapsed to two sentences before the
  LaTeX pass and left there.
- **The free-riding diagnostic and the supervision panel**, both appendix
  material, and both fourth and first in the de-scope order respectively.

Nothing cut carries a claim the paper still makes. The claims ledger in
`../writing/CLAIMS-LEDGER.md` remains the authority on status, and every flag
in the body matches it.

## One thing to verify before submitting

`\workshoptitle` currently reads "Workshop on Machine Learning and Economics
(EconML)". Check that against the call for papers and correct it if the
workshop's registered name differs; it appears in the camera-ready footer, not
in the submission build, so it is cosmetic now and wrong-looking later if left
unchecked.
