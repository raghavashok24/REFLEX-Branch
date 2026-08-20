# Paper build

The submission itself: `main.tex` compiled against the official NeurIPS 2026
style files, plus the mandatory paper checklist.

`main.tex` is **v2**. v1 is archived unmodified in [`v1/`](v1/), frozen at
commit `486d213`. [`PAPER-V2-CHANGES.md`](PAPER-V2-CHANGES.md) holds the
external review of v1, an assessment of each criticism against the code, the
space arithmetic, one item that looks like a bug and is not, and a record of
what v2 implemented and what it deliberately skipped.

```bash
python econml/paper/make_figures.py     # figures, from the committed result JSONs
cd econml/paper && pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

**Three passes.** v1 needed two; v2 needs a third because Lemma 1 shifts the
theorem numbering that the cross-references resolve against. No bibtex run: the
bibliography is a `thebibliography` block inside `main.tex`, since 22 entries do
not justify a `.bib` and a manual list cannot go stale against one.

**`\hypersetup{draft=true}` is deliberate.** A cross-reference link straddling
the page 2/3 break aborts pdfTeX with "\pdfendlink ended up in different nesting
level than \pdfstartlink". Neither `breaklinks` nor a larger `pdf_mem_size`
avoids it, and the layout that triggers it is the layout that fits nine pages.
Making hyperref inert leaves the printed page identical and costs only
clickability, which a double-blind submission does not need. **Remove the line
for the camera-ready**, where the layout differs anyway.

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
generated from result JSONs and carry no local paths. No sentence positions
REFLEX or PEBSA as the authors' own work.

**On the two base papers carrying author names.** Both are cited in full, with
authors, which puts a name shared with this submission's author list into the
bibliography. That is the plan of record's instruction and it is the right call:
the rule under double-blind is that self-citation happens in the third person,
not that it is scrubbed. A reference stripped of its authors is the more
revealing artifact, because it is visibly anomalous next to twenty ordinary
entries and reads as a paper hiding its own lineage. The submission cites them
the way any third party would and lets the third-person prose carry the blind.

**No entry carries a URL**, these two included. They briefly did, and a DOI
trailing the only two references sharing an author with the submission is a
worse tell than the names themselves: it makes them the two entries a reader's
eye lands on. The bibliography is uniform, `Authors. Title. Venue,
vol(issue):pages, year.`, and anything reintroducing a link to one entry has to
add it to all twenty-two.

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
- **The supervision material's longer form**, collapsed to two sentences before
  the LaTeX pass and, in v2, folded out of its own section into the opening
  paragraph of the closing one.
- **The free-riding diagnostic and the supervision panel**, both appendix
  material, and both fourth and first in the de-scope order respectively.

Nothing cut carries a claim the paper still makes. The claims ledger in
`../writing/CLAIMS-LEDGER.md` remains the authority on status, and every flag
in the body matches it.

## Venue, checked against the call for papers

`\workshoptitle` reads "Economics for Machine Learning (EconML)", which is the
workshop's registered name. An earlier draft had it backwards as "Machine
Learning and Economics"; corrected 19 Aug 2026 against the call for papers.

The same source confirms the rest of the build. Long papers are capped at nine
content pages with figures and tables included, which is what this compiles to.
Review is double-blind and the call names `dblblindworkshop` as the required
option, which is the one in use. The deadline is 29 Aug 2026 anywhere on earth,
and the workshop runs 12 or 13 Dec 2026 in Atlanta.

The title reaches the page only in the camera-ready footer, since the submission
build prints the generic notice instead. Getting it right now means the
camera-ready needs no edit beyond adding the `final` option.
