# Submission pack: ML x OR @ NeurIPS 2026

## "The Price of Self-Knowledge: an Information-Cost Uncertainty Principle for Performative Systems"

**Deadline Aug 31 2026 (AOE). 4 pages main body, NeurIPS style, unlimited
references + appendix. Non-anonymous, non-archival. Journal designation at
submission: Mathematics of Operations Research** (fallback rationale in
section 10).

This is the complete ideation for the paper - everything except the prose.
Audited for flawed assumptions on 2026-08-16
(`../ASSUMPTIONS-AUDIT.md`, items A1, A3, P1-P5); both central identities are
numerically verified (`../verify_m2_identity.py`).

---

## 1. Thesis and positioning

**Thesis sentence.** In a system whose data distribution reacts to the deployed
model, information about that reaction is not collected - it is *purchased*,
with the objective itself; the price is zero only during the transient, and
thereafter it is pinned by an exact exchange rate.

**The three-literature triangle the paper sits in.** (1) Performative
prediction has the solution concepts (stable point vs performative optimum)
but treats identification of the response as a black-box estimation step.
(2) Optimal experimental design has the design machinery but assumes the
experimenter pays no objective-coupled cost and faces no stability constraint.
(3) Adaptive control has persistent excitation - the insight that a
converging closed loop starves its own identification - but no
performative-risk pricing of the excitation. The paper is the pairwise
intersection made exact in a model where every constant is computable.

**Why REFLEX makes this paper possible.** The claim `Var x Cost = const` is
easy to state and easy to get wrong (the audit caught the wrong version). What
makes it a *paper* is that REFLEX supplies: closed-form `gamma_PO` (theory
1.2), a measured modulus and a working retraining loop across `m in (0, 1.2)`,
a tuned estimator suite for `epsilon` (three-way triangulation), a documented
empirical failure (the free-form learned loop) that the theory retrodicts, and
a verification layer to certify every identity numerically.

## 2. Formal setup (the model section, ~0.5 page)

Local model at the performatively stable point `h*`:

```
   deployment:   h_{t+1} - h*  =  -m (h_t - h*)  +  sigma_e xi_t
   response:     tau_t  =  tau(h*) - epsilon (h_t - h*) + zeta_t ,  zeta_t ~ (0, sigma_tau^2)
```

- `m = epsilon beta / gamma` is the retraining modulus (Perdomo's contraction
  constant, computable in REFLEX from microstructure primitives).
- `sigma_e` is deliberate exploration (REFLEX: `rrm.collection_jitter`).
- Estimand: the response slope `epsilon` (scalar body; `p`-dim structural
  family in the anchoring theorem). Estimator: OLS; information
  `I_T = S_xx / sigma_tau^2`.
- Cost: `C_T` = **incremental exploration cost** = expected excess performative
  risk of the jittered loop over the jitter-free loop at `h*`. NOT anchored at
  `h_PO` - the audit's A1 explains why, and the distinction carries Corollary
  2.1.
- State the general-decision-dependent-system version first (any smooth
  strongly-concave `Phi`, response map with sensitivity `epsilon`), then the
  market instantiation. One paragraph gives the strategic-classification
  instantiation so the scope is visibly not finance-only.

## 3. Results (the full statement list)

**Theorem 1 (information saturation).** With `sigma_e = 0`, `m < 1`:
`S_xx(T) -> (h_0 - h*)^2 / (1 - m^2)` - bounded uniformly in `T`. Hence
`Var(eps_hat) >= sigma_tau^2 (1-m^2) / (h_0-h*)^2` at every horizon: a
converging retraining loop cannot identify its own performativity beyond a
fixed floor. *Proof: geometric series. Verified 1e-16.*

**Corollary 1.1 (stability-identifiability conflict).** The information cap
is increasing in `m`: precise self-knowledge is available exactly when the
system is close to unstable. Fast-contracting (safe) systems are the blindest.

**Corollary 1.2 (design degeneracy).** At `m = 1` the noiseless iterates form
a period-2 orbit - two support points, secant identification only; curvature
parameters (REFLEX: toxic decay `c_t`) are unidentified from the trajectory at
*any* `m`. (This upgrades the repo's "exponential fits need a wide spread
range" gotcha from folklore to theorem.)

**Theorem 2 (the uncertainty principle).** With `sigma_e > 0`, in the
stationary regime, in expectation,

```
   Var(eps_hat) * C_T  =  (1/2) gamma_PO sigma_tau^2
```

independent of `sigma_e`, `T`, and `m`. *Scope:* exact for the local quadratic
model under exploration-dominant design (strict-exogeneity caveat A3 stated in
the paper; `O(1/T)` bias otherwise, measured). *Verified: rel. err 0.0 across
the `(m, sigma_e)` grid; the wrong-anchor version measured and shown to break
exactly as predicted - report this falsification check in the appendix, it is
persuasive.*

**Unified statement.** `I_total = I_transient + I_stationary`: the transient
is free but bounded (Thm 1); everything after is bought at the fixed rate
(Thm 2). One sentence, and the paper is one result instead of two.

**Corollary 2.1 (ROI of self-knowledge).** The echo-chamber gap
`(1/2) gamma_PO (h_SP - h_PO)^2 = O(eps^2)` is a perpetuity recoverable by the
PerfGD correction; the identification it needs is a one-off cost priced by
Thm 2. Break-even discount rate in closed form: **a performative system should
explore iff it is patient enough, and "patient enough" is computable.**

**Theorem 3 (feasibility frontier).** Accuracy target `v`, budget `B`:
feasible iff `v B >= (1/2) gamma_PO sigma_tau^2`. Fails structurally in two
regimes: `m > 1` (jitter amplified, no stationary regime, exchange rate
unbounded) and binding trust regions (achievable excitation capped:
some accuracy targets unreachable at any budget). Generic price, specific
prohibitions.

**Theorem 4 (structural anchoring changes the exchange rate).** Correctly
specified `p`-dim family: the design burden drops to `p` directions and the
constant improves by the design-optimality ratio; misspecification `delta_mis`
adds irreducible `O(delta_mis)` bias. Crossover rule: anchor iff
`delta_mis^2 < (1/2) gamma_PO sigma_tau^2 / B`. This is the formal version of
REFLEX's headline empirical finding ("anchoring, not capacity") - and it also
*bounds when that finding would reverse*, which no experiment in the v4 run
does.

**Algorithm + Theorem 5 (safe D-optimal exploration).** Maximise
`log det` information for the structural family s.t. (i) risk budget
(convex quadratic), (ii) closed-loop spectral stability margin `1 - c`,
(iii) trust region. Relaxed design problem solved by Frank-Wolfe on the design
simplex (keeps numpy/scipy-only convention). Certainty-equivalent re-solving,
pessimistic on stability / optimistic on information. Guarantee to prove:
identification regret `O(sqrt(T))` vs the oracle design; `P(m_t < 1 for all t)
>= 1 - delta`.

## 4. Experiments (3 figures + 1 table, full profile target < 10 min CPU)

| # | Figure | Protocol | Expected result | Falsifies |
|---|---|---|---|---|
| F1 | Saturation curves | `run_loop(mode="rrm")`, `collection_jitter = 0`, `epsilon` grid spanning `m in [0.1, 0.95]`, 16 seeds; cumulative `S_xx(t)` vs closed asymptote | flat lines at `h_0^2/(1-m^2)`, ordered in `m` | Thm 1 / Cor 1.1 |
| F2 | The exchange rate | jitter grid x 3 `epsilon` levels; `Var(eps_hat)` across seeds via the triangulation suite; realized excess risk from the loop's own eval episodes; plot `Var x Cost` | flat at `(1/2) gamma_PO sigma_tau^2` in the contracting regime; measured drift where `info_cap` / liquidity-inflation engage - **the drift curve is a result** | Thm 2 + scope |
| F3 | Safe design beats jitter | matched budget `B`: (a) iid jitter 0.05, (b) two-point trust-region-edge design, (c) FW D-optimal; metric `Var(c_hat)` for the decay parameter | (c) identifies `c_t` where (a) cannot, at equal P&L | Cor 1.2 + Thm 5 |
| T1 | Anchoring crossover | structural fit vs free-form MLP operator across injected misspecification (power-law / two-exponential response in a variant `clients.py`); empirical crossover vs Thm 4 threshold | crossover within the predicted band; retrodicts the v3 negative result | Thm 4 |

Protocol rules (inherited, non-negotiable): probe at the operating spread;
CRN pairs; `collection_jitter = 0.05` default elsewhere; compare against
realized-state closed forms; never de-saturate `info_cap`; ASCII console.

## 5. New code (all CPU, deterministic, numpy/scipy only)

| File | Contents | ~lines |
|---|---|---|
| `reflex/theory/identification.py` | saturation closed forms, exchange rate, feasibility test, ROI break-even, anchoring threshold | 220 |
| `reflex/estimators/design.py` | structural sensitivity vectors, FW D-optimal design under budget+stability+trust constraints, safe re-solving schedule | 260 |
| `experiments/run_identification.py` | F1-F3 + T1 | 220 |
| `tests/test_identification.py` | identities, invariance, design optimality vs known case, wrong-anchor falsification | 160 |
| `verification/certificates.py` (+7) | saturation; invariance across `(m, sigma_e)`; anchor falsification (the `(1+g^2/v)` form); period-2 degeneracy; feasibility monotonicity; anchoring-threshold sign; FW constraint satisfaction | +90 |

## 6. Page plan (body = extended abstract of the appendix)

- 0.4p Introduction: the purchase-not-collect thesis; the triangle; the
  retrodicted failure.
- 0.5p Model + the anchoring discussion compressed to 4 lines (full version
  appendix).
- 1.3p Theorems 1-4 + corollaries, one-line proof ideas; the unified
  statement gets its own display.
- 1.0p Algorithm + F2 + F3.
- 0.5p Table T1 + limitations (local scope, exogeneity, one-domain-deep).
- 0.3p F1 + appendix pointer.

Appendix (unlimited, written FIRST, is the MOR draft): full proofs; the
falsification study; drift study; the strategic-classification instantiation;
regret proof for Thm 5; certificate listing; reproducibility statement.

## 7. Timeline (submission Aug 31; today Aug 16)

| Days | Work |
|---|---|
| Aug 17-19 | `identification.py` + tests + certificates (theory is verified; this is transcription). Draft appendix proofs of Thms 1-3 in parallel. |
| Aug 20-22 | `design.py` (FW), F3 harness; Thm 5 regret proof sketch to appendix. |
| Aug 23-25 | F1, F2, T1 runs (full profile); drift study. |
| Aug 26-28 | Write the 4-page body from the appendix. Prose-guard pass (the repo's AI-tell list applies: no mirrored openers, no aphoristic closers, start sections on the claim). |
| Aug 29-30 | Internal review vs this pack's claim list; freeze numbers; non-anonymous build (author block ON - this venue wants it); journal box = MOR. |
| Aug 31 | Submit (OpenReview). |

## 8. Reviewer objections - prepared answers

1. *"Artefact of the local quadratic model."* Stated scope + the measured
   drift curve (F2). The claim is calibrated: exact locally, first-order
   beyond, drift quantified.
2. *"This is just Cramer-Rao."* CR bounds variance by information; here the
   information is bought with the objective, so the bound couples to the value
   function and becomes an exchange rate. The invariance across `(m, sigma_e,
   T)` is the non-CR content.
3. *"OLS under feedback."* A3: predetermined-not-exogenous stated,
   `O(1/T)` bias measured, consistency unaffected.
4. *"One domain."* General statement first; strategic-classification
   instantiation in the appendix; the market is where constants are computable
   and falsifiable.
5. *"Why is the wrong-anchor discussion in the paper?"* Because it is the
   difference between a true theorem and a plausible false one, and the
   audit-then-falsify record is the paper's culture. (Keep it short in the
   body; full in appendix.)

## 9. Risk register

| Risk | Trigger | Mitigation |
|---|---|---|
| F2 drift swamps the flat region | high-intensity configs | run the flat region on raw defaults (`m < 0.9`), report drift separately; do NOT tune `info_cap` |
| FW design solver fiddly under 3 constraints | Aug 22 checkpoint | fallback: restrict to 2-point + 3-point designs (closed-form D-optimal for `p = 3` on an interval), still beats jitter; Thm 5 regret becomes a remark |
| Thm 5 regret proof not done by Aug 26 | - | ship algorithm + empirical safety, state regret as conjecture with simulation evidence; the paper stands on Thms 1-4 |
| Time | - | de-scope order: T1 -> Thm 5 guarantee -> F3 variant (b). Never cut F2. |

## 10. Journal strategy

Designate **Mathematics of Operations Research**: the contribution's center of
mass is an exact identity + an impossibility structure, MOR's shape. Fallback
reasoning if the PC steers: Stochastic Systems if reviewers weight the
sequential/design half (INFORMS APS is the workshop sponsor); Operations
Research only if the desk-facing ROI corollary is the story the editors want
expanded. The journal version's delta is already scoped: full nonlinear drift
theory, multi-dimensional `epsilon` (the 1.5 modulus matrix), and the M4
composition (sequential certification spending the priced probes).
