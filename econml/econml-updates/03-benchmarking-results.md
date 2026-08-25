# 3. Benchmarking, ablations, and results

## 3.1 Where the evidence stands

The evidential structure is unusually honest and internally consistent: one
measured panel (the monoculture anchor, reproducing the base preprint bit
for bit), five dry runs flagged as derivation checks, and a certificate
harness behind every closed form. The status discipline (MEASURED vs DRY
RUN, ledger-matched) is a genuine strength; keep it exactly as is.

The structural weakness is equally plain: **the four new results have no
measured evidence**, only closed-form agreement in a linearized reference
environment, because the heterogeneous simulator port failed its acceptance
gate (a decision correctly taken and correctly disclosed). The v1 external
review already identified the repair that matters, and it is not the
simulator: it is measuring the alignment object on real models.

## 3.2 Item 1: the measured-alignment panel (the poster-to-oral move)

**Claim it supports**: the paper's central object, R and its lambda_max, is
not hypothetical; it is measurable on today's hosted models, and its value
is far from both corners.

**Method** (two days, no simulator, CPU only):

1. Take public per-item evaluation outputs for a set of hosted models.
   Candidate sources, most specific first: the released per-item data from
   Kim, Garg, Peng, Garg (ICML 2025), which covers 350+ models on two
   leaderboards and was built for exactly this correlation analysis; HELM's
   per-instance JSONs; the OpenLLM leaderboard's per-sample dumps. One
   dataset with N in the tens of models and thousands of items suffices.
2. For each model i, form the error-indicator vector over items answered by
   all models (or the residual vector on a scored task). Compute the
   pairwise error correlation r_ij on the shared subset, i.e. the
   phi-coefficient of joint errors. This is the alignment matrix of
   observable failure directions.
3. Report: lambda_max(R-hat) as a measured effective learner count against
   the firm count N; the same statistic within and across providers; and
   the fitted shared fraction s-hat from the off-diagonal mean of
   same-provider vs cross-provider blocks. One figure (heatmap of R-hat
   ordered by provider, with lambda_max and N in the title), one table row
   in the panel table, status MEASURED.
4. State the caveat in one sentence, in the paper's own voice: error
   correlation is a proxy read on the output side, not the response
   Jacobian; what it measures is the alignment of failure directions, which
   is the object (H3) says firms retrain against. Do not oversell it as R
   itself.

**Why this is the right experiment and the simulator port is not**: the
port's gate failure is a residual-confound problem inside one synthetic
market; this panel is a direct measurement of the quantity the whole paper
turns on, in the wild, with provider structure giving a natural s sweep.
It also composes with the supply-chain section: same-provider blocks with
high r and cross-provider entries with moderate r is precisely the
"plurality vendor" topology the clustered example warns about, and finding
it in real data would let the paper point at its own Figure for the claim
that mean indices understate lambda_max.

**Risk**: per-item data availability. Mitigation: Kim et al. released their
evaluation data publicly (the ICML paper's repository); if that fails, HELM
per-instance predictions are downloadable without authentication.

## 3.3 Item 4: the nonlinearity ablation (one day)

The paper's stated largest gap is that the heterogeneous sweep is
closed-form agreement, not measurement, with linearization (A1) the reason.
Panel 1's two-signed gap (-12.9% at N=2, +5.2% at N=3) is currently the
only quantitative statement about what nonlinearity costs.

Add a dry-run ablation in the reference environment: introduce a saturating
response (the environment's linear response passed through tanh with scale
lambda), sweep lambda from 0 (exact linearity) upward, and plot the
measured boundary location against the Theorem 2 prediction as
nonlinearity grows. Two curves (N=5 monoculture, N=10 clustered), one
half-column figure or four numbers inline. The point is the shape: a
graceful, monotone departure supports "the closed forms govern a
neighbourhood," which is the paper's implicit claim, and gives the
limitations section a number instead of an adjective. The harness already
estimates stability from realized trajectories, so this is a config sweep
plus one environment hook, not new machinery.

## 3.4 Smaller reporting upgrades (hours each)

- **Panel 6's welfare-gap units**: "over-adaptation gap widens from 29.0%
  at N=2 to 119.9% at N=20" states aggressiveness distortion; a reviewer
  will want the welfare loss too, which the bisection already computes en
  route. One sentence.
- **The 11.8% protocol**: now stated in the appendix (applied in
  proposed-v5); keep it wherever that number appears in talks and rebuttal.
- **Worst-case grid departure as the error statement**: the checklist's
  "deterministic panels, worst-case departure reported" answer is correct
  and stronger than seed error bars; make sure the rebuttal repeats it
  rather than apologizing for missing error bars.
- **Runtime and hardware one-liner** in Appendix I (all CPU, minutes):
  costs nothing, closes checklist question surface.

## 3.5 What not to do before the deadline

- Do not reopen the simulator port. The gate decision was right: both named
  repairs are multi-day, one risks the bit-for-bit anchor, and the fallback
  is already honestly framed.
- Do not add error bars over seeds to deterministic panels; the worst-case
  statement is stronger.
- Do not soften the DRY RUN language into something that implies
  measurement; the current framing is an asset with exactly this reviewer
  pool. (One wording improvement in `04-narrative.md` makes the same
  honesty read less self-undermining.)
