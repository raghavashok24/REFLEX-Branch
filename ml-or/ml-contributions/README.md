# posk - The Price of Self-Knowledge

The ML architecture and full pipeline for the ML x OR @ NeurIPS 2026 paper
*"The Price of Self-Knowledge: Minimax Information-Cost Tradeoffs and
Optimal Exploration in Performative Systems"* - the companion
implementation of the `mlxor-derivations` math folder (theorem register
THEOREMS.md there; results here verify it end-to-end in a live pipeline).

## The architecture: SafeD-PerfGD

A learning agent for decision-dependent environments whose exploration is
**priced** (in its own objective), **shaped** (by the theory's optimal
designs), and **safety-gated** (by a pessimistic certificate on its own
closed-loop modulus). Per deployment round:

```
                 +--------------------------------------------------+
                 |                 SafeD-PerfGD                     |
                 |                                                  |
   deploy h_t    |  1. EXPLORE   D-optimal 3-point support of the   |
  ------------>  |     (design.py) structural family, re-centred    |
                 |     at the operating point, trust-region clipped |
   observe       |  2. FIT       anchored family (C0, C1, c) by     |
   tau_obs_t     |     (estimators) profile least squares +         |
  ------------>  |     anytime self-normalized confidence sequence  |
                 |  3. GATE      perturbed-modulus lemma (L4) with  |
                 |     (agents)  the family's own Lipschitz const:  |
                 |     certify eta*ci*L_fam <= margin, else FREEZE  |
                 |     the correction (blind step keeps running -   |
                 |     the anti-echo freeze, derived not tuned)     |
                 |  4. STEP      h <- h + eta (G_hat + Delta_hat),  |
                 |     Newton-scaled by gamma_PO_hat, clipped       |
                 +--------------------------------------------------+
```

Baselines: `BlindRRM` (the retraining cobweb, blind to dD/dphi) and
`JitterPerfGD` (isotropic exploration + OLS slope - the naive agent every
theorem prices).

## Layout

```
posk/
|- posk/
|  |- theory.py       closed forms (Market): gamma, eps, gamma_PO, h_SP,
|  |                  h_PO, modulus, exchange rate, saturation cap,
|  |                  crossover threshold, A-optimal design, dispersion F
|  |- env.py          StructuralEnv (the theory's world, exactly) and
|  |                  SaturatingEnv (REFLEX-style tanh cap: the measured
|  |                  out-of-scope drift cell)
|  |- estimators.py   OLS slope + anytime CS; anchored StructuralFit
|  |                  (profile LS, identified-flag); secant estimator
|  |- design.py       D-optimal 3-point support; scalar scheduler;
|  |                  isotropic baseline; Fisher matrices
|  |- agents.py       BlindRRM, JitterPerfGD, SafeD-PerfGD
|- experiments/run_all.py   E1-E5 with the measured-vs-predicted harness
|- results/           RESULTS.md (the verification table), CSVs, run log
|- tests/test_posk.py 9 fast unit tests
|- .github/workflows/ci.yml
```

## The verification loop (measured vs derived, with the pivots recorded)

Every experiment row compares a pipeline measurement against a closed form
from the derivations folder and stamps PASS / DRIFT / FAIL (DRIFT =
deliberately out-of-scope cell; exit code fails on FAIL only). The loop was
run repeatedly during development; **four pivots were forced by
measurement, each recorded in the code where it happened**:

1. **E1, the feedback floor.** The noiseless saturation cap failed 4x
   against the noisy pipeline: retraining on noisy observations converts
   observation noise into deployment noise with gain 1/gamma (the A3'
   channel), adding a stationary excitation floor
   `v_fb = (sigma/gamma)^2/(1-m^2)` per step. Both closed forms now
   verified (cap within 3-8%, floor within 1-7%). Kept for the paper: even
   zero deliberate exploration carries a retraining-noise excitation floor
   - and it sits on the same exchange-rate frontier.
2. **E4, the gate is honest and therefore slow.** The pessimism gate never
   certified in 500 steps - because anytime confidence is expensive at a
   flat operating point (`gamma_PO(h_SP) = 0.17` here vs `1.42` at the
   optimum). Fixes faithful to the theory: freeze the *correction* only
   (the blind step keeps running - REFLEX's anti-echo convention, now
   derived), the family-specific L4 constant, and enough design horizon.
   Certification time is the exchange rate at work, and certification gets
   *easier* at the optimum (curvature rises) - both now measured.
3. **E4, trust accounting.** The checker's cap formula forgot that
   consecutive probes legitimately span the design support (2r); the agent
   never violated its clip.
4. **E5, misspecification must live at the operating point.** The injected
   `a e^{-2ch}` had decayed to ~1e-3 at the operating spread - the anchored
   fit rightly never saw it. Replaced by a linear leak `-a h`, which the
   family cannot represent: the anchored-MSE curve then crosses the
   nonparametric level exactly as T7 predicts.

Headline verified numbers (fast profile; the full profile re-runs in CI):

| Result (register) | Measured | Predicted |
|---|---|---|
| Exchange rate, 4 cells (T2) | 0.0106-0.0057, flat in sigma_e and m | 0.0106 / 0.0054 |
| Saturating-env drift (scope) | +16% above the rate | (DRIFT cell) |
| Saturation cap, 3 moduli (T1) | within 3-8% | d0^2/(1-m^2) |
| Feedback floor, 3 moduli (new) | within 1-7% | (sigma/gamma)^2/(1-m^2) |
| Dispersion ratio, d=8 (C5.1) | 1.501 | F = 1.506 |
| A-opt risk (T5a) | 0.0189 | 0.0183 |
| sd(c_hat), design arm (T6) | 0.222 | Fisher 0.248 |
| jitter/design sd ratio (T6) | 8.2x | unidentified vs identified |
| SafeD-PerfGD final h (goal) | 1.312 | h_PO = 1.296 |
| Nonparametric MSE (T7) | 0.0136 | 0.0123 |
| Anchoring crossover (T7) | crosses between a=0.2 and 0.35 | monotone crossing |

## Reproduce

```
pip install -r requirements.txt
python tests/test_posk.py                 # 9 unit tests, ~1 min
python experiments/run_all.py --fast      # the verification table, ~10 min
python experiments/run_all.py             # full profile, ~25 min
```

Deterministic from seeds; numpy only; CPU only; ASCII output.

## Relation to the paper and to REFLEX

The math lives in the companion `mlxor-derivations` folder (derivations,
theorem register, proofs, 34-check numerical suite); this repo is the
*pipeline* leg: the same closed forms verified inside a live
deploy-observe-fit-correct loop with an agent a desk could actually run.
The environment is a self-contained simplification of the REFLEX structural
market (`endo_market_v4`); the full-market instantiation (calibrated
configs, multi-bond Gamma_PO) runs through the REFLEX package per the
derivations folder's SYMBOLS-TO-REFLEX.md map.
