# MATH-AI 2026 submission checklist

Replaces the ML x OR checklist at
`ml-or/PRICE-final/ml-or/submission-materials/SUBMISSION-CHECKLIST.md`, which
does not apply to this venue. Every item below states what was measured on
4 September 2026 on this build, not what is expected.

## Venue facts (read from the CFP at mathai-2026.github.io/cfp/, 4 Sep 2026)

| Fact | Value |
|---|---|
| Workshop | The 6th Workshop on Mathematical Reasoning and AI (MATH-AI), NeurIPS 2026, Atlanta |
| Body limit | 4 pages of content, unlimited references and supplementary |
| Camera-ready limit | 5 pages of content |
| Format | NeurIPS 2026 workshop template, `\usepackage[dblblindworkshop]{neurips_2026}` |
| Review | Double-blind; submissions must be anonymized |
| Archival | Non-archival; accepted papers listed on the workshop Papers page |
| OpenReview | `NeurIPS.cc/2026/Workshop/MATH-AI` |
| Deadline | 6 September 2026, AoE |
| Notification | 29 September 2026, AoE |
| Reciprocal reviewing | Required: at least one author per submission agrees to review, about three papers |
| Prior publication | Previously published work, including NeurIPS 2026, is not allowed; arXiv preprints and prior non-archival workshop papers are fine |

## Measured on this build

1. **Body ends page 4, references begin page 5.** Measured with `pdftotext`,
   not by eye. Page 4's last body line is the closing sentence of the
   Limitations paragraph; page 5 opens with the `References` heading.
2. **Total 10 pages.** Body 4, references 1, appendix 5. The appendix cap of
   10 pages after page 4 is met with room to spare: 6 pages follow page 4.
3. **Style option is `dblblindworkshop`**, in `paper/main.tex` line 8, with
   the official `neurips_2026.sty`. The Anonymous Author(s) block is intact.
4. **0 overfull boxes, 0 undefined references, 0 undefined citations.**
   Measured from `paper/main.log` after `pdflatex` then `bibtex` then
   `pdflatex` twice. One underfull hbox and two underfull vbox page-fill
   notices remain; these are page-break reports at float boundaries, and the
   affected pages render without visible defect. The single LaTeX warning is
   `'h' float specifier changed to 'ht'` for Table 1.
5. **0 em dashes in the extracted PDF text**, and 0 occurrences of `---`.
   Measured on the full `pdftotext` output, body and appendix.
6. **PDF metadata carries no Author field.** `pdfinfo` reports Title, Subject,
   Keywords and Author all empty; Creator is `LaTeX with hyperref`.
7. **Author names in the PDF text: 2 occurrences, both correct.** One is the
   bibliography entry for the prior REFLEX paper; the other is the
   third-person in-text citation of that entry in Appendix D. Both are proper
   citation of prior work under double blind. No email address, no
   institutional affiliation, no repository URL appears anywhere in the text.
8. **`submission/main.pdf` is byte-identical to `paper/main.pdf`.** Confirmed
   by SHA-256, printed by `build_submission.py` on every run.
9. **`submission/supplementary.zip` is anonymous.** Extracted to a temporary
   directory (52 files) and grepped. `Vignesh`, `Nagarajan`, `Shriraghav`,
   `Ashok`, `nrvignesh`, `@gmail`, `github.com`: zero matches, case
   insensitive, across the whole extracted tree. No `__pycache__/`, no
   `.pytest_cache/`, no `.git` anything, no `.pyc`. The only URL in any file
   is the `https://matplotlib.org/` software tag that matplotlib writes into
   PNG metadata, in the seven figure files.
10. **`prose_lint.py` from `anthropic-skills:prose-guard` is clean** on
    `main.tex`, `appendix_statements.tex` and `appendix_proofs.tex` at
    `--fail-on medium`.
11. **Every number in the body traces to a committed artifact.** Traced by
    hand against `posk-pipeline/results/RESULTS.md`, `OPEN1.md`,
    `REALDATA.md`, `STABILITY.md`, `full_run.log`, and
    `mlxor-derivations/THEOREMS.md` and `VERIFICATION.md`. One value was
    restated at the artifact's own precision rather than the ML x OR body's
    rounding: the known-`c` boundary ratios are now `0.3002`, `0.0425` and
    `0.0348`, as `OPEN1.md` section D reports them. No value was changed.
12. **The pipeline and derivation suites were not re-run.** They were executed
    and recorded on 1 September 2026 (38/38 derivation checks, 36 rows with
    0 FAIL, 9 unit tests, `run_open1.py` exit 0), and nothing in this retarget
    touches their inputs. This build re-narrates those runs; it does not claim
    to have reproduced them.

## Known gap, stated rather than papered over

The 1 September report records that
`mlxor-derivations/.github/workflows/verify.yml` and
`posk-pipeline/.github/workflows/ci.yml` were restored into the shipped
package. Neither file exists anywhere in this repository, so neither is in
`supporting/` or in `supplementary.zip`. Appendix D says CI runs in the
project repository and that the workflow files are not part of the anonymized
copy. If the files can be recovered before upload, drop them into
`math-ai/supporting/` and re-run `build_submission.py`.

## Before you submit

- [ ] Upload `submission/main.pdf` to the PDF field and
      `submission/supplementary.zip` to Supplementary Material. See
      `submission/UPLOAD.md`.
- [ ] Enter the real author list in the OpenReview author fields. Do not
      replace the PDF with a named build.
- [ ] Accept the reciprocal-reviewing commitment and name the reviewing
      author.
- [ ] Answer the prior-publication question as unpublished. The ML x OR
      version was non-archival and rejected, which the CFP explicitly permits.
- [ ] Submit before 6 September 2026 AoE.
