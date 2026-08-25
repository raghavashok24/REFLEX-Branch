# Review package: making this the top paper at EconML @ NeurIPS 2026

**Reviewed 25 Aug 2026, against `paper/main.tex` (v4). Deadline 29 Aug AoE, four days out.**

Every claim in this package was verified before being written down: all 525
certificate assertions re-run and passing, every headline number in the paper
re-derived from scratch in an independent script (`tools/indep_check.py`, 44 of
44 checks pass), the venue call re-verified on the web, the PDF rebuilt from
source and the page gate re-checked, and every proposed edit compiled into a
page-compliant candidate v5 (`proposed-v5/`). Where a suggestion could not be
fully verified, it is flagged as such rather than stated as fact.

## Verdict in one paragraph

This is already a strong workshop paper: one genuinely new object (the
effective number of independent learners, derived rather than posited), four
results stated in it, honest evidence flags, and a house voice most
submissions lack. The external review's accept-as-poster is credible. What
separates it from the top of the stack is one missing empirical panel
(measuring the alignment object on real models, which the v1 review already
named as the highest-value item and which is now feasible in two days using
public data), one citation gap that a knowledgeable reviewer will hit
immediately (two multi-agent performative prediction papers, EC 2023 and
NeurIPS 2022, are uncited), and one scope slip in Theorem 8's coverage claim
(the orthogonal corner, where the stated marginal-share formula fails). All
three are fixable before the deadline. The first one is the difference
between poster and oral.

## The ranked action list

Ranked by expected review impact per day of work. Items 1 to 3 are
pre-deadline; the rest are camera-ready or journal items.

| # | Action | Impact | Cost | Where |
|---|---|---|---|---|
| 1 | **Add the measured-alignment panel**: build the error-correlation matrix over real hosted models from public per-item eval data, report its lambda_max as a measured N_eff, grouped by provider. Kim et al. (ICML 2025) is the methodological anchor and makes this a two-day build, not a research project | Poster to oral. It converts the paper's central object from hypothetical to measured, and it is the one thing the v1 review said would move the score to high 80s | 2 days | `03-benchmarking-results.md`, full spec |
| 2 | **Close the citation gap**: Piliouras and Yu (EC 2023) and Li, Yau, Wai (NeurIPS 2022) are multi-agent performative prediction papers a reviewer from this community knows. Dispatching them strengthens the containment story; not citing them reads as a lit-review hole. Kim et al. (ICML 2025) grounds the premise empirically | Removes the most likely "missed related work" strike | Done, compiled in `proposed-v5/` | `01-novelty.md` |
| 3 | **Fix the Theorem 8 scope slip and the notation collision**: the body claims the wedge covers the orthogonal corner, where the leading eigenvalue is degenerate and the marginal-share formula provably fails (worked counterexample inside); and the body uses rho for the corrected fraction while the appendix uses rho_c | Removes two things a careful reviewer can be *right* about | Done, compiled in `proposed-v5/` | `02-technical-rigor.md` |
| 4 | Add a robustness ablation: prediction error of Theorem 2 against nonlinearity strength in the reference environment | Preempts the linearization criticism with a figure instead of a sentence | 1 day | `03-benchmarking-results.md` |
| 5 | Trim bold weight and tighten five overloaded sentences | Readability at review speed | hours | `06-writing-style.md` |
| 6 | Verify-then-cite the three contemporaneous 2026 finance preprints on AI systemic risk | Shows command of a fast-moving neighbourhood; do not cite unread | half day | `01-novelty.md`, section 4 |
| 7 | Journal track: matrix-Bernstein sharp rate, block-secular reduction, asymmetric wedge, supervision estimator formalized | The journal version's spine | months | `02-technical-rigor.md`, section 5 |

## What was checked and found sound (do not spend deadline time here)

- All four theorems, the reduction lemma, the containment proposition, and
  the concentration bound: proofs read line by line, no gaps found beyond the
  scope slip in item 3. The two-block quadratic, the phantom-root warning,
  the imperfect-vaccine law, and the critical efficacy all verify against
  independent dense eigensolves.
- Every worked number in body and appendix (the cadence table, the herd
  table, the witness pair, the clustered example, the worked wedge numbers,
  panel 4's 12/14/16/20 thresholds): all reproduce exactly.
  See `07-verification-log.md`.
- Venue compliance: nine content pages ending with the conclusion,
  references from page 10, unmodified style file, dblblindworkshop option,
  checklist complete, blind intact. The build reproduces from source.
- The venue itself: call re-verified. Two tracks; this paper is a bullseye
  for "Machine Learning Ecosystems with Interacting Models."
  Deadline 29 Aug AoE confirmed (the site's "30 Aug 11:59 UTC" is the same
  instant). See `05-venue-fit.md`.

## What is in `proposed-v5/`

A compiled, page-compliant candidate carrying items 2 and 3 plus the small
precision fixes from `06-writing-style.md`: the two new related-work
dispatches and three bibliography entries, the wedge scope correction, the
rho_c notation unification (figures regenerated to match), the 11.8% sampling
protocol stated where the number lives, the notation-table range fix, and
four line-level tightenings that pay the page bill. Content ends on page 9,
references start page 10, zero overfull boxes, no undefined references.
`CHANGES.md` lists every edit with its rationale; each is also explained in
the numbered documents. Adopt it whole or cherry-pick; either way, rebuild
and re-run the page gate before submitting.
