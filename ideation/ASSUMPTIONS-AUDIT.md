# Assumptions audit - NeurIPS 2026 workshop branch-offs

**Date: 2026-08-16.** Every load-bearing claim in the eight idea documents was
re-derived and stress-tested for the kind of assumption a referee flags. Two
real defects were found and fixed (A1, A2 below); the rest of the audit is the
record of what was checked and passed, so the writing phase does not re-litigate
it. Verdicts: **FIXED** (defect found, documents corrected), **PASS** (checked,
sound), **SCOPED** (sound only under stated conditions, now stated).

---

## A1. M2 Theorem 2 - the cost anchor (FIXED, was a fatal flaw)

**Claim as originally written.** `Var(eps_hat) * C_T = (1/2) gamma_PO
sigma_tau^2` with `C_T = (1/2) gamma_PO sum (h_t - h_PO)^2` - cost anchored at
the performative optimum.

**The defect.** The loop's operating point is the stable point `h*`, and
`h* != h_PO` generically (their gap IS the echo-chamber gap, theory 1.2 (6a)).
Anchoring at `h_PO` adds the systematic term `T (h* - h_PO)^2`, which is paid
whether or not the operator explores. Numerically (stdlib check,
`verify_m2_identity.py` Claim 3): the product becomes
`(1/2) gamma_PO sigma_tau^2 (1 + g^2/v)`, `g = h* - h_PO`,
`v = s_e^2/(1-m^2)` - measured 7.66 / 0.78 / 2.50 across `(m, s_e)` against
the invariant 0.3185, matching the predicted form to 0.2%. The invariance -
the theorem's entire content - is destroyed, and the product diverges as the
jitter shrinks.

**The fix.** `C_T` is now defined as the **incremental exploration cost**:
expected excess performative risk of the jittered loop relative to the
jitter-free loop at `h*`. Since `Phi'(h*) != 0`, the expansion has a linear
term; it is zero-mean in the stationary regime, so the identity holds **in
expectation**, with the linear term contributing only variance (reported, not
hidden). The sunk `T g^2` term is the echo-chamber cost of blindness -
correctly charged to *not* correcting, not to exploring - which produced a new
result rather than a patch: **Corollary 2.1 (ROI of self-knowledge)**, the
closed-form break-even between the one-off identification cost and the
perpetuity value of the recoverable gap.

## A2. E1 Theorem 1 - the exact eigenvalue formula (FIXED, was overclaimed)

**Claim as originally written.** "A cleaner exact statement is likely
available: `rho(J) = mbar (1 + kappa (lambda_max(R) - 1))`" with `mbar` the
*mean* single-firm modulus.

**The defect.** Counterexample: orthogonal responses (`R = I`) decouple the
dealers exactly, so `rho(J) = max_i m_i`, not the mean. No formula built on
`mbar` can be exact under modulus heterogeneity.

**The fix.** Scope split, now in the document: (i) equal moduli /
heterogeneous directions - prove the exact identity with `lambda_max(R)`;
(ii) general case - bounds via the modulus-weighted Gram matrix
`M^{1/2} R M^{1/2}`, `M = diag(m_i)`, exact in the equal-modulus and
`kappa = 0` limits, tightness measured in simulation. Additional rule now
stated: stability claims must use the `lambda_max` form, never the mean
`rbar` form, because mean alignment understates a concentrated cluster (three
aligned firms among ten orthogonal ones destabilise a subspace the mean barely
sees) - and the cluster topology got promoted to a planned figure because it
is the realistic vendor-plurality case.

## A3. M2 - strict exogeneity of the design (SCOPED)

The OLS variance formula behind Theorem 2 assumes the regressor sequence is
independent of the response noise. In the real loop the observed `tau_t` feeds
the next deployment, so regressors are *predetermined, not strictly exogenous*
(a Stambaugh-type `O(1/T)` bias). Now stated as the "exploration-dominant
design" condition, with the deviation measured in the full simulator as part
of experiment 2. Estimator consistency is unaffected (martingale-difference
noise).

## A4. E1 Theorem 3 - "weakly dominant adoption" (SCOPED)

"Adopting the market-leading model is individually weakly dominant" was too
strong: adoption is dominant only once the private share of the instability
cost (which scales as `O(1/N)` - each firm's adoption moves `rbar` by
`O(1/N)`) falls below the quality gain. Restated as a threshold *decreasing in
`N`* with the externality mechanism explicit. This strengthens the result: the
market-size dependence is the economics.

## A5. E2 - "more competitors, wider spreads" (SCOPED at creation)

Flagged in the original document, recorded here for completeness: under
REFLEX's A5' (captured benign franchises) the claim is an artefact - there is
no Bertrand force. The E2 spec requires removing A5' first; the honest result
is the critical spillover `kappa*` and the non-monotone spread-vs-`N` curve.

## A6. Checks that PASSED (no changes needed)

| # | Claim | Check |
|---|---|---|
| P1 | M2 Thm 1 saturation sum `(h0)^2 (1-m^{2(T+1)})/(1-m^2)` | Exact vs simulation to 1e-16 at `m in {0.2, 0.6, 0.9}` (`verify_m2_identity.py` Claim 1) |
| P2 | M2 Thm 2 invariance (corrected anchor) | Product = `0.318500` = target across all `(m, s_e)`, rel. err 0.0 (Claim 2) |
| P3 | M2 Cor 1.1 monotonicity | Info bound `h0^2/((1-m^2) sigma^2)` increasing in `m` - algebraically immediate; the "identifiable only near instability" reading follows |
| P4 | M2 Cor 1.2 period-2 degeneracy | Linear map at `m = 1`: `d_{t+1} = -d_t`, support `{+d_0, -d_0}` - two points, secant-only identification |
| P5 | M2 lower bound `Var >= sigma^2 (1-m^2)/h0^2` | Direct from P1's bounded `S_xx` |
| P6 | E1 `rbar` range `[-1/(N-1), 1]` | PSD of the correlation matrix: `1^T R 1 >= 0` gives the lower bound; consistency: `rbar = -1/(N-1)` gives `N_eff = 1 - kappa`, exactly 1.3's differential-mode modulus - the two independently-derived numbers agree |
| P7 | E1 reduction at `rbar = 1` | Recovers 1.3's `N_eff = 1 + kappa(N-1)` and hence the verified `1.74x / 3.16x` amplification |
| P8 | E1 Thm 2 supply-chain algebra | `E[<vec E_i, vec E_j>] = s ||E_shared||_F^2` under the stated normalisation; concentration is over `d^2` entries, `O(1/d)` hedge already present |
| P9 | E2 Thm 2 welfare orders | Client loss first-order in the spread (`dh = O(eps)`), dealer value loss `O(eps^2)` by the envelope theorem at the optimum - the asymmetry is sound |
| P10 | M1 Thm 2 knife-edge | `<dtheta/dz, grad_theta J> = -P (h - psi) eps(h)`, zero iff `h = psi` - consistent with 1.2 section 7.1's sign flip, independently derived |
| P11 | M3 Thm 2 | Uses 1.6's `K_max = ln((m-1)/(m+1))/ln(c)` as published; the unknown-`c` issue is handled by design (Thm 3 is the online version; the closed-form `K*` is stated conditional on `c`) |
| P12 | 1.6 interpolation identity | `mu(K) = -m + c^K(1+m)`: `mu(0) = 1`, `mu(infty) = -m`, monotone for `c in (0,1)` - endpoints and monotonicity re-checked |
| P13 | Venue facts | EconML: Aug 29, 9/4pp, double-blind, non-archival, topics incl. verbatim "performative prediction", "algorithmic collusion", "monoculture" - read from the CFP source. MLxOR: Aug 31, 4pp, non-anonymous, 3-journal pipeline (one journal designated at submission) - corroborated via search + the 2025 call; **site egress-blocked, confirm by hand before submission** |

## A7. Standing risks that are *design decisions*, not defects

- **Local-quadratic scope of M2.** The identity is exact for the
  linearisation; the full-simulator drift (from `info_cap` saturation and the
  liquidity-inflation channel) is a *measured curve* in experiment 2. The
  paper's claim is calibrated to this and must stay so.
- **E1 panel 4 (real data) is consistency evidence, not identification.**
  Spread co-movement is contaminated by common macro shocks and the data is
  not trade-level TRACE. The placebo (Treasury/macro series) is mandatory and
  the claim is "the observable the theory predicts should move, moves".
- **Beyond-boundary probe readings are diagnostics, not slopes** (seed-level
  bifurcation) - any figure crossing `m = 1` carries the caveat in the
  caption. Inherited from `CLAUDE.md`; applies to M2 experiment 1 and E1
  panel 2.
- **Never sweep `alpha`;** sweep `clients.toxicity_feedback`. Inherited; the
  confound is documented and closed-form-explained in 1.1 section 6.4.
