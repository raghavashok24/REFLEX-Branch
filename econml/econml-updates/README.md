# Review package, 25 Aug 2026

An end-to-end review of `paper/main.tex` (v4) against six axes, with every
suggestion verified before being written down, plus a compiled candidate v5
carrying the pre-deadline fixes.

Read `00-EXECUTIVE-SUMMARY.md` first; it carries the ranked action list.

| File | Carries |
|---|---|
| `00-EXECUTIVE-SUMMARY.md` | Verdict and the ranked action list |
| `01-novelty.md` | Novelty audit, the citation gap, contemporaneous 2026 work |
| `02-technical-rigor.md` | Proof audit, one real defect (wedge's orthogonal corner), precision fixes, journal-strength upgrades |
| `03-benchmarking-results.md` | The measured-alignment panel spec, the nonlinearity ablation, reporting upgrades |
| `04-narrative.md` | Narrative spine assessment, three frictions with fixes |
| `05-venue-fit.md` | CFP re-verified: tracks, deadline, compliance, audience calibration |
| `06-writing-style.md` | Voice assessment, systematic issues, line edits |
| `07-verification-log.md` | Exactly what was verified, how, and what was not |
| `proposed-v5/` | The candidate as `v5.patch` against `../paper/`, with `CHANGES.md` (every edit and its rationale) and `BUILD-NOTE.md` (how to rebuild; the compiled PDF ships in the review-package zip) |
| `tools/indep_check.py` | The independent verification script (44 checks) |

The candidate v5 changes only `main.tex`, `appendix.tex`, and two axis
labels in `make_figures.py`, relative to the submission in `../paper/`.
`neurips_2026.sty`, `checklist.tex`, and the archive are untouched. The
patch was verified to apply cleanly and to rebuild to a page-compliant
PDF (content ends page 9, References start page 10, zero overfull boxes).
