# Panels

```bash
python econml/ml-contributions/experiments/run_panels.py
```

Deterministic, CPU-only, about a minute. Writes JSON to `results/` and PNG to
`results/figures/`. Exits nonzero if any panel disagrees with its closed form, so
a broken derivation fails the run rather than producing a quiet figure.

## What these are, and what they are not

**These are dry runs in the linearized reference environment, not the paper's
panels.** The environment realizes the model's response geometry and nothing
else: no informed flow, no spread, no inventory. The paper's panels run in the
base project's order-flow simulator, and **every experimental claim stays at its
derivation status until they do.** Nothing here upgrades a claim to measured.

What they do establish, which is worth having ten days out:

The step from linearized spectrum to realized dynamics, which no amount of
algebra checking covers. Stability is not read off an eigensolve here; each panel
runs the actual retraining map and estimates the spectral radius from the
trajectory's asymptotic growth by power iteration.

The shape of every figure, so the simulator port has a target rather than a blank
page. A discrepancy between the simulator and these is then diagnostic: it is
microstructure, since the geometry is already known to agree.

## Results

| Panel | Tests | Outcome |
|---|---|---|
| 1, amplification | Section 3 | Reduction exact to `5.6e-16`. **External anchor outstanding** |
| 2, `(N, s)` phase diagram | Theorem 1 | 48 cells, max error `7.1e-15` |
| 2b, clustered companion | Theorem 1 | Measured `m_N` `1.30`, mean index reports `0.74` |
| 3, cadence frontier | Theorem 2 | 175 cells, zero disagreements |
| 4, herd immunity | Theorem 3 | Thresholds `12 / 14 / 16 / 20` firms at efficacy `1.0 / 0.9 / 0.75 / 0.6` |
| 5, substitution frontier | Theorem 3 | 18 of 18 points exact |
| 6, over-adaptation | Theorem 4 | **Not written.** Theorem 4 is not derived |

## Two results worth reading the JSON for

**Panel 1's anchor is not yet earned.** The environment reproduces the predicted
amplification exactly, because it is linear and the prediction is a linear
statement. The published `1.74x` and `3.16x` are *simulator* measurements, and
the gap from the predicted `2` and `3` is nonlinearity and flow saturation, which
this environment does not model. Panel 1 therefore checks the reduction, not the
external validation, and its JSON says so in a field named for the purpose.
Anyone quoting it as replication is quoting it wrong.

**Panel 4 is where the C18 finding becomes visible.** At perfect correction the
market needs 12 of 20 firms un-blinded. At efficacy `0.90` it needs 14, at `0.75`
sixteen, and at `0.60` all twenty. The strong-correction limit says 12 in every
one of those cases, which is the optimism the derivation predicted, now drawn.

That panel also produced a finding the derivation did not claim: **the
imperfect-correction law predicted all four thresholds exactly at `kappa = 0.8`,
where it is only proved exact at `kappa = s = 1`.** Recorded in
[`../../math/derivations/04-mixed-market-secular.md`](../../math/derivations/04-mixed-market-secular.md)
as measured evidence, not upgraded to a proof.

## Reading the figures

Panel 5's markers sit on or above the continuous `rho*(s)` curve because a
threshold is a whole number of firms and the curve is continuous. The green step
line is the integer prediction, and the markers land on it at all 18 points. The
apparent offset from the smooth curve is granularity, not error.

Panel 3's frontier is drawn continuous while its cells are integer `K`, so the
realized window is `floor(K_max)`.
