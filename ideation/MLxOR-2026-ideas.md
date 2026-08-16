# ML x OR @ NeurIPS 2026 - branch-off paper ideas from REFLEX

**Venue constraints.** 4 pages main body (NeurIPS style), unlimited references
and supplementary. Non-anonymous, non-archival. Submit **Aug 31 2026**.
Selected papers invited to submit a full version to **Stochastic Systems**,
**Mathematics of Operations Research**, or **Operations Research** - pick at
most one at submission time.

**Design rule for this venue.** Four pages cannot carry a model *and* a proof
*and* an experiment suite. Write the appendix first and make it the journal
draft; the 4-page body is then an extended abstract of it: one paragraph of
setup, the theorem statements, one figure, one table, limitations. Every idea
below is specified so that the appendix is the real deliverable.

Ranked. M2 is the recommendation for this cycle.

---
---

# M2 (RECOMMENDED). The Information-Cost Uncertainty Principle for Performative Systems

**One line.** In a decision-dependent system, the variance of any estimate of
your own performative response and the profit you forgo to obtain it are
locked in an exact product relation - you cannot buy identification cheaply,
and at a converged equilibrium you cannot buy it at all.

**Journal target.** Mathematics of Operations Research (sharpest theorem), or
Stochastic Systems if the sequential-design half is emphasised.

**CFP fit.** Thematic area (i) verbatim - *"uncertainty mitigation at the
interface of data, model, and decision ... uncertainty quantification,
performance assessment of prescriptive decisions"*. Also (ii) sequential
decision-making and online learning: the algorithm is an online experimental
design under a dynamical stability constraint.

## M2.1 The gap

Performative prediction (Perdomo et al. 2020) and PerfGD (Izzo et al. 2021)
both need the response Jacobian `dD/dphi`. Izzo et al. *estimate* it by
perturbation and bound the resulting bias and variance. What nobody has stated
is where the perturbations must come from and what they cost. In a deployed
system every perturbation is a real decision taken at a real price: probing
your own performativity means quoting off-optimal spreads, showing users a
worse ranking, pricing a product wrong. The estimation problem is therefore not
a statistics problem with a sample-size budget, it is a *stochastic control*
problem with a P&L budget.

REFLEX has the empirical shadow of this already, documented as a failure:
the free-form learned loop (`perfgd_learned`) does not stabilise, and the
diagnosed cause is that the converged loop stops exploring - the
"echo chamber's identification collapse" in
`equilibrium/structural_response.py`. The fix shipped (`collection_jitter`,
the structural anchoring, the anti-echo freeze) is engineering. This paper
turns it into theory, and the theory is sharper than the engineering.

## M2.2 The formalism

Local model at a performatively stable point `h*` (all symbols as in
`research/math-theory/01-analytic-stability-boundary.md`):

```
   h_{t+1} - h*  =  -m (h_t - h*)  +  sigma_e * xi_t ,     xi_t ~ iid N(0,1)
   tau_t         =  tau(h*) - epsilon (h_t - h*) + zeta_t , zeta_t ~ iid N(0, sigma_tau^2)
```

`sigma_e` is the **exploration intensity**: the deliberate deployment jitter
the operator injects (in REFLEX, `rrm.collection_jitter`). The estimand is the
response slope `epsilon`; the estimator is OLS of `tau_t` on `h_t`. Define

```
   I_T   := sum_{t<=T} (h_t - hbar)^2 / sigma_tau^2       (Fisher information for epsilon)
   C_T   := E[ sum_{t<=T} ( Phi(h*) - Phi(h_t) ) ]        (incremental exploration cost)
       =  (1/2) gamma_PO * E[ sum_{t<=T} (h_t - h*)^2 ]   (stationary regime; see below)
```

**The anchoring of `C_T` matters and getting it wrong breaks the theorem.**
`C_T` is the *incremental* performative risk of the jittered loop relative to
the jitter-free loop sitting at its operating point `h*` - it is the cost
attributable to exploration and nothing else. Two subtleties, both handled:

- `Phi'(h*) != 0` (the stable point is not the performative optimum), so the
  expansion of `Phi(h*) - Phi(h_t)` has a *linear* term `-Phi'(h*)(h_t - h*)`.
  In the stationary regime the jitter deviations are zero-mean, so the linear
  term vanishes **in expectation** and the quadratic term gives the closed
  form above with `gamma_PO := -Phi''(h*)`. The identity of Theorem 2 is a
  statement about expected cost; the linear term contributes variance around
  it, which the experiments report.
- Anchoring the cost at `h_PO` instead (the naive "distance from optimal"
  reading) is **wrong**: it adds the systematic term `T (h* - h_PO)^2`, which
  is paid whether or not the operator explores - it is the echo-chamber value
  gap of `02-perfgd-correction.md` (6b), a sunk cost of blindness, not a cost
  of exploration. Numerically (verified, see M2.6): with the `h_PO` anchor the
  product of Theorem 2 becomes `(1/2) gamma_PO sigma_tau^2 (1 + g^2/v)` with
  `g = h* - h_PO` and `v` the stationary jitter variance - it depends on the
  exploration intensity and the modulus, and diverges as the jitter shrinks.
  The invariance exists only for the incremental cost. This distinction is a
  *feature* of the paper, not bookkeeping: the sunk echo-chamber cost is
  precisely what identification lets you recover (see the ROI corollary).

## M2.3 The theorems

**Theorem 1 (information saturation at equilibrium).** With `sigma_e = 0` and
`m < 1`,

```
   sum_{t=0}^{T} (h_t - h*)^2  =  (h_0 - h*)^2 * (1 - m^{2(T+1)}) / (1 - m^2)
                              ->  (h_0 - h*)^2 / (1 - m^2)   as T -> infinity.
```

The information about `epsilon` available from a converging retraining loop is
**bounded uniformly in `T`**: running the loop longer buys nothing. Hence
`Var(epsilon_hat) >= sigma_tau^2 (1 - m^2) / (h_0 - h*)^2` for every horizon.
*Status: verified exactly, numerically (see M2.6).* Proof is two lines from the
geometric series; the content is the interpretation.

**Corollary 1.1 (the stability-identifiability conflict).** The information
bound is *increasing* in `m`. A market that contracts fast (`m` small) snaps to
its fixed point and reveals almost nothing about its own performativity; a
market near the boundary (`m -> 1`) oscillates persistently and is easy to
identify. **You can measure your performative sensitivity precisely only when
it is nearly large enough to destabilise you.** This inverts the usual
"estimate first, then decide" ordering that predict-then-optimize assumes, and
it is a genuinely uncomfortable message for a risk function.

**Corollary 1.2 (design degeneracy at the boundary).** At `m = 1` exactly the
iterates settle on a period-2 orbit: the design measure has **two** support
points. A secant slope is identified; nothing of higher order is. So the
structural parameters that require curvature in `h` (in REFLEX, the toxic decay
`c_t`) are *not* identified by the loop's own trajectory at any `m`, with or
without convergence. This is the precise statement of why REFLEX's exponential
response fits "need a wide spread range" - currently a `CLAUDE.md` gotcha,
here a theorem.

**Theorem 2 (the uncertainty principle).** With `sigma_e > 0`, in the
stationary regime,

```
   Var(epsilon_hat) * C_T  =  (1/2) * gamma_PO * sigma_tau^2 ,
```

**independent of the exploration intensity `sigma_e`, the horizon `T`, and the
modulus `m`.** Information about your own performativity has a fixed exchange
rate against foregone value, set only by the curvature of the performative
objective and the noise in the response channel. Sharpening the estimate
`k`-fold costs exactly `k` times the P&L, however you explore.
*Status: verified numerically to 6 significant figures across `m` in
{0.2, 0.6, 0.9} and `sigma_e` in {0.05, 0.2}, including the anchor
falsification check - see M2.6.* The proof is the stationary variance
`sigma_e^2/(1-m^2)` appearing identically in numerator and denominator; the
correct statement of scope is that it is exact for the local quadratic model
with the incremental-cost anchoring of M2.2, and first-order elsewhere.

**Unified reading of Theorems 1 + 2.** Total information splits as
`I_total = I_transient + I_stationary`: the transient (Theorem 1) is *free* but
bounded - the loop's convergence path is the only identification you ever get
without paying - and everything after it is bought at the fixed exchange rate
of Theorem 2. This is the sentence that makes the paper one result rather than
two.

**Corollary 2.1 (the ROI of self-knowledge).** Exploration is worth it iff the
recoverable echo-chamber value gap exceeds the exploration budget a
sufficiently precise correction requires. The gap is
`(1/2) gamma_PO (h_SP - h_PO)^2 = O(epsilon^2)` per step *in perpetuity*
(`02-perfgd-correction.md` 6b); the correction needs
`Var(epsilon_hat) <= v_req` at one-off cost `(1/2) gamma_PO sigma_tau^2 /
v_req` by Theorem 2. Comparing the perpetuity value of the gap to the one-off
identification cost gives a closed-form break-even discount rate - a
performative system should explore iff it is patient enough, and "patient
enough" is computable from primitives. This ties the paper to 1.2's gap and
gives the operational punchline a desk can act on.

**Honest scope caveat (strict exogeneity), stated in the paper.** In the real
retraining loop the observed response `tau_t` feeds the next deployment
`h_{t+1}`, so the regressor is *predetermined but not strictly exogenous*: the
OLS variance formula behind Theorem 2 is exact when the design is dominated by
the injected jitter, and carries a Stambaugh-type `O(1/T)` bias when the
noise-feedback channel is material. State the identity under the
"exploration-dominant design" condition and *measure* the deviation in the
full simulator - the drift curve is part of experiment 2, not a hidden
assumption.

**Theorem 3 (feasibility, and where it fails).** Fix an accuracy target
`Var(epsilon_hat) <= v` and a risk budget `C_T <= B`. Theorem 2 makes the
problem feasible iff `v * B >= (1/2) gamma_PO sigma_tau^2` - a single scalar
test. Two regimes break it:
  (a) **beyond the boundary** (`m > 1`) the stationary variance does not exist,
      the jitter is amplified rather than absorbed, and `C_T` grows
      superlinearly - the exchange rate degrades without bound;
  (b) **trust-region binding**: if the deployment is constrained to
      `|h_{t+1} - h_t| <= r` (REFLEX's `structural_max_rel_step`), the
      achievable `sigma_e` is capped and the accuracy target may be
      unreachable at *any* budget.
This is the honest replacement for a naive "impossibility" claim: generically
there is a price, not a prohibition; the prohibition appears exactly in the
unstable and trust-region-constrained regimes.

**Theorem 4 (structural anchoring changes the exchange rate).** Suppose the
response lies in a correctly specified `p`-dimensional family (REFLEX:
`tau(h) = C0 + C1 e^{-c h}`, `p = 3`) rather than a nonparametric class. Then
the design requirement drops from exciting a function space to exciting `p`
directions, and the constant in Theorem 2 improves by the ratio of the
`p`-dimensional design optimality to the nonparametric one. Under
misspecification of size `delta_mis` the estimator carries an irreducible bias
`O(delta_mis)`, giving a bias-variance crossover: **anchoring wins whenever
`delta_mis^2 < (1/2) gamma_PO sigma_tau^2 / B`.** This is the formal statement
of REFLEX's headline empirical finding that *anchoring, not capacity*, closes
the loop-level gap - currently an experimental observation in
`research/results/07-12-2026/REPORT.md`, here a decision rule with a computable
threshold.

## M2.4 The algorithm: safe D-optimal performative exploration

Theorem 2 says the exchange rate is fixed but says nothing about *when* to
spend. That is a design problem, and it is the operational contribution:

```
   maximise    log det ( sum_t  s(h_t) s(h_t)^T / sigma_tau^2 )     (D-optimality
                                                                     for the p-dim
                                                                     structural family)
   subject to  (1/2) gamma_PO sum_t (h_t - h_PO)^2  <=  B           (risk budget)
               rho( linearised loop under the schedule )  <=  1 - c (stability margin)
               |h_{t+1} - h_t| <= r                                  (trust region)
```

- `s(h)` is the sensitivity vector of the structural family, e.g.
  `s(h) = (1, e^{-ch}, -C1 h e^{-ch})` for `tau = C0 + C1 e^{-ch}`.
- The objective is concave in the design measure, the budget is a convex
  quadratic, and the stability constraint is a spectral-radius bound on the
  closed-loop map, which for the linearised system is an LMI. So the relaxed
  problem is an **SDP** and the exact design is recovered by a standard
  rounding of the optimal design measure.
- Because `gamma_PO`, `m` and the family are themselves unknown at the start,
  wrap it in **certainty-equivalent re-solving with a safety margin**:
  plug in the current posterior, keep the constraint at `1 - c` rather than `1`,
  and show that with probability `1 - delta` the true closed loop never leaves
  the stable region (a standard optimism/pessimism argument - be *pessimistic*
  on stability, optimistic on information).
- **Guarantee to prove:** identification regret `O(sqrt(T))` against the oracle
  design, with a high-probability safety guarantee that `m_t < 1` for all `t`.

This is the "operational integration" the workshop title asks for: a desk can
run it.

## M2.5 Why a NeurIPS reviewer accepts it

- The central identity is exact, surprising, and checkable in five lines - the
  best kind of theorem for a 4-page venue.
- It resolves a documented empirical negative result from a prior paper (the
  free-form learned loop). Reviewers reward theory that retrodicts a known
  failure.
- It connects three literatures that do not currently cite each other:
  performative prediction, optimal experimental design, and adaptive control's
  persistent-excitation condition. The PE condition has, to our knowledge,
  never been imported into performative prediction, and it is exactly the right
  tool.
- It is falsifiable and *has been falsified against* a working simulator with
  real-data calibration.

**Anticipated objections and the answers.**
1. *"The identity is an artefact of the local quadratic model."* Agreed and
   stated. The paper reports the exact identity for the linearisation and then
   measures the product `Var * Cost` in the full nonlinear REFLEX simulator
   across regimes; the claim in the body is that it is invariant to first order
   and drifts by a measured amount beyond that. Do not overclaim - the drift
   curve is a *result*, not an embarrassment.
2. *"Is this not just Cramer-Rao?"* Cramer-Rao bounds variance by information.
   The content here is that in a decision-dependent system the information is
   *purchased with the objective itself*, so the bound couples to the value
   function; the product identity is what makes it an exchange rate rather than
   an inequality.
3. *"Only one application domain."* The theorem is stated for a general
   decision-dependent map with strongly concave objective; the market model is
   the instantiation that lets every constant be computed. Say so in the setup
   and give a second one-paragraph instantiation (strategic classification,
   with agent response elasticity in place of `epsilon`).

## M2.6 Implementation plan

**Already verified.** The two central claims were checked numerically while
scoping this document:

```
   m=0.2:  sum dev^2 = 1.041667   closed form (h0^2/(1-m^2)) = 1.041667
   m=0.6:  sum dev^2 = 1.562500   closed form                = 1.562500
   m=0.9:  sum dev^2 = 5.263158   closed form                = 5.263158
   Var(eps_hat) * Cost (h* anchor)   = 0.318500 for every (m, sigma_e) tried;
   predicted (1/2) gamma_PO sigma_tau^2 = 0.318500
   Var(eps_hat) * Cost (h_PO anchor) = 2.145 at (m=0.6, s_e=0.1, gap 0.3)
                                     = the predicted (1/2) g_PO s^2 (1+g^2/v):
                                       the invariance is destroyed, confirming
                                       that the incremental anchoring is the
                                       load-bearing definition
```

(script: `verify_m2_identity.py` in this folder, stdlib-only)

**New code.**

| Module | Contents | Size |
|---|---|---|
| `reflex/theory/identification.py` | `information_saturation(m, h0)`, `exchange_rate(gamma_po, sigma_tau)`, `feasible(v, B, ...)`, `anchoring_threshold(delta_mis, B, ...)` - all pure numpy, mirroring the `theory/` module convention | ~200 lines |
| `reflex/estimators/design.py` | `sensitivity_vector`, `d_optimal_design(...)` via SDP (scipy or a simple Frank-Wolfe on the design simplex to avoid a cvxpy dependency), `safe_schedule(...)` | ~250 lines |
| `experiments/run_identification.py` | the three panels below | ~200 lines |
| `tests/test_identification.py` | saturation identity, exchange-rate invariance, design optimality on a known case | ~150 lines |
| `reflex/verification/certificates.py` | +6 certificates: saturation sum, exchange-rate invariance across `(m, sigma_e)`, period-2 degeneracy at `m=1`, SDP constraint satisfaction, anchoring threshold sign, PE failure without jitter | +80 lines |

Frank-Wolfe on the design simplex is the right call over an SDP solver: it
keeps the dependency footprint at numpy/scipy, matches the repo's
"dependency-light closed-form modules" convention, and D-optimal design under a
convex constraint set is exactly what FW is good at.

**Experiments (three figures, one table).**

1. **Saturation.** Run `run_loop(mode="rrm")` with `collection_jitter = 0` at
   `epsilon` values spanning `m` in `[0.1, 0.95]`; plot cumulative
   `sum (h_t - h*)^2` against `t` with the closed-form asymptote overlaid.
   Expected: flat lines at `(h_0-h*)^2/(1-m^2)`, higher for larger `m`. This is
   the figure that sells Corollary 1.1.
2. **The exchange rate.** Sweep `collection_jitter` over a grid at three
   `epsilon` levels; for each run measure `Var(epsilon_hat)` across seeds using
   the existing three-way triangulation (`estimators/triangulate.py`) and
   measure realized excess performative risk from the loop's own evaluation
   episodes. Plot `Var * Cost` against `sigma_e`. Expected: a flat line at
   `(1/2) gamma_PO sigma_tau^2` in the contracting regime, with a measured
   upward drift as the nonlinearities (the `info_cap` saturation, the
   liquidity-inflation channel) engage. **Report the drift honestly - it is the
   scope boundary of Theorem 2 and it is more interesting than a flat line.**
3. **Safe design beats jitter.** Compare three exploration schedules at matched
   risk budget `B`: (a) iid jitter at REFLEX's default `0.05`; (b) a two-point
   design at the trust-region edge; (c) the FW D-optimal safe schedule. Metric:
   `Var(c_hat)` for the *decay* parameter, which Corollary 1.2 says the loop's
   own trajectory cannot identify. Expected: (c) identifies `c` where (a) does
   not, at the same P&L cost. This is the operational punchline.
4. **Table: anchoring crossover.** Structural fit vs the free-form MLP operator
   across misspecification levels, injected by perturbing the response family
   away from the exponential (e.g. a power-law or a two-exponential mixture in
   `env/clients.py`). Report the empirical crossover `delta_mis` against the
   Theorem 4 prediction. This retrodicts the v3 negative result *and* bounds
   when it would have gone the other way.

**Reuse.** `estimators/br_slope.py` (CRN probes), `estimators/triangulate.py`,
`theory/perfgd.py` (`gamma_po`), `equilibrium/structural_response.py` (the
`p = 3` family and the `identified` flag), `run_tuning.py` (the sweep harness
and its scale-relative conventions).

**Effort: 4-6 days.** Lowest-risk item on the ML x OR list.

**Page plan (4 pages).** 0.5p setup and the loop; 1.25p Theorems 1-4 as
statements with one-line proof ideas; 1.5p the design algorithm and figures 1-3;
0.5p limitations (local model, single domain, drift measurement); 0.25p
pointer to the appendix. Appendix: full proofs, the nonlinear drift study,
figure 4, the certificate listing, and the second instantiation.

---
---

# M1. Performative Decision-Focused Learning: predict-then-optimize when the prediction target reacts to the decision

**One line.** The entire predict-then-optimize / decision-focused learning
literature assumes the uncertain parameter's distribution is exogenous; when the
decision moves it, SPO+ loses Fisher consistency and a perfectly accurate
predictor still incurs strictly positive decision regret.

**Journal target.** Operations Research.

**CFP fit.** Thematic area (iii), verbatim and completely: *"contextual
optimization ... data-driven optimization, prescriptive optimization,
predictive stochastic programming, decision-focused learning, and
predict-then-optimize approaches."* This is the single most on-theme idea in
the folder for this workshop; it is ranked second only because it is the
largest build.

## M1.1 The gap

Contextual optimization solves `z*(theta) = argmin_z c(z; theta)` where
`theta` is predicted from context `x`. SPO+ (Elmachtoub-Grigas) is the
canonical decision-aware surrogate and is Fisher-consistent under mild
conditions. Every result in that line assumes `theta ~ P(.|x)` **independent of
`z`**. In pricing, matching, routing, ad allocation, inventory - and in market
making - it is not: the realized demand curve depends on the price posted, the
realized traffic on the route recommended, the realized flow on the spread
quoted. REFLEX is a structural instance where the dependence `theta(z)` is
known in closed form, which is what makes the theory checkable.

## M1.2 The formalism

Context `x` (regime, rating, inventory), parameter `theta` (fill-curve
`(A, k)`, toxic curve `(C0, C1, c_t)`), decision `z` (the half-spread `h`, or
the `d`-vector of half-spreads). Under decision dependence the payoff of `z` is
`J(z; theta(z, x))` and there are two solution concepts, inherited from
performative prediction:

```
   z_SP(x)  : blind plug-in    - argmax_z J(z; theta_hat)  with theta_hat fit at the deployed point
   z_PO(x)  : performative opt - argmax_z J(z; theta(z, x))
```

Define **performative decision regret** `R(z) = J(z_PO; theta(z_PO)) -
J(z; theta(z))`, and the **decision-dependent SPO loss** as the SPO loss
evaluated against `theta(z*(theta_hat))` rather than a fixed `theta`.

## M1.3 The theorems

**Theorem 1 (an irreducible regret floor).** Even with zero prediction error at
the deployed point - the predictor is *exactly right* about the distribution it
sees - the blind plug-in rule converges to `z_SP` and incurs

```
   R(z_SP)  =  (1/2) gamma_PO ||z_SP - z_PO||^2  +  o(eps^2)  =  Theta(eps^2) .
```

Perfect prediction does not imply good decisions. This is REFLEX's
echo-chamber value gap (`02-perfgd-correction.md`, 6b) re-read as a statement
about decision-focused learning, and it is a genuinely damaging observation for
the field's framing: the standard motivation for decision-focused learning is
that prediction error should be *weighted* by decision impact, and here the
decision is wrong at zero prediction error.

**Theorem 2 (Fisher consistency fails, with an exact knife-edge).** SPO+ is
Fisher-consistent for the decision-dependent problem iff the performative
response is orthogonal to the decision-relevant direction, i.e. iff

```
   < d theta / d z , grad_theta J >  =  0    at the optimum.
```

In REFLEX this evaluates to `h = psi` exactly - the self-financing point where
the marginal toxic unit earns the half-spread it costs in adverse selection
(`02-perfgd-correction.md` section 7.1). So the consistency condition is not an
abstract genericity assumption, it is a *named, computable, economically
meaningful* knife-edge, and it is generically violated on both sides with
opposite bias signs. Getting a clean instantiation of an abstract condition is
what makes this publishable rather than a remark.

**Theorem 3 (Performative SPO+ and its regret bound).** Define

```
   L_PSPO(theta_hat; x)  =  L_SPO+(theta_hat; x)  +  < J_theta ,  (d theta / d z)|_{z*(theta_hat)} >
```

the surrogate corrected by the same first-order term PerfGD adds to the
gradient. Then `L_PSPO` is Fisher-consistent for the decision-dependent
problem, and the end-to-end regret decomposes as

```
   R(z_hat_n)  <=  C1 * err(theta_hat)  +  C2 * err(dtheta/dz)  +  C3 * opt_err ,
   C1 = beta/gamma_PO ,   C2 = ||z - z_PO|| ,   C3 = 1 ,
```

with every constant computable from primitives. The interesting term is `C2`:
the Jacobian estimate is what the correction consumes, and **M2 governs how
expensive that estimate is**. The two papers compose - M1's regret bound is
only as good as M2's exchange rate allows, and saying so is a strength.

**Theorem 4 (the statistics are non-i.i.d. and the loop controls them).**
Training data are generated by the deployed policy, so the sample is a
trajectory of the retraining map, not an i.i.d. draw. Two consequences, and
they point in opposite directions - state both:
  (a) the iterates are *negatively* autocorrelated (the cobweb slope is `-m`),
      which **reduces** the variance of sample means relative to i.i.d.;
  (b) the design measure collapses geometrically (M2 Theorem 1), which
      **destroys** identification of anything beyond a local secant.
So "self-generated data" is not uniformly worse than i.i.d.; it is better for
level estimation and catastrophically worse for slope and curvature estimation.
That distinction does not appear in the performative-prediction literature and
is exactly the kind of thing an OR journal will find worth the page.

**Theorem 5 (robust/contextual version).** Combine with REFLEX 1.4: the
decision-focused robust rule over an ambiguity ball of radius
`delta_n = O(1/sqrt(n))` around the estimated response is a **shrinkage** of
the corrected decision toward the blind decision, with the shrinkage factor in
closed form. This lands the "distributional robustness" and "robustification"
CFP language and gives the paper its uncertainty-aware framing.

## M1.4 Implementation plan

**New code.**

| Module | Contents |
|---|---|
| `reflex/decision/` (new subpackage) | `spo.py` (SPO+ and PSPO+ losses and subgradients), `pipelines.py` (two-stage, SPO+, PSPO+, oracle-PO), `regret.py` (performative decision regret estimator) |
| `experiments/run_decision_focused.py` | the four-pipeline comparison across contexts |
| `tests/test_decision_focused.py` | consistency knife-edge at `h = psi`; regret floor scaling as `eps^2`; PSPO+ recovers `z_PO` with an oracle Jacobian |

**Contexts come free.** `calibration/mapping.py` already maps
`(rating, regime) -> Config` from real fitted parameters, and
`calibration/regimes.py` gives the VIX regime classifier. That is a genuine
contextual optimization dataset with `2 x 5 = 10` contexts and real per-context
`(A, k, sigma, h)`. Use the multi-bond decision from `theory/factor_scaling.py`
so `z` is a `d`-vector and the linear-objective SPO connection is natural.

**Experiments.**
1. Regret vs `epsilon` for the four pipelines. Expected: two-stage and SPO+
   flatten at the `Theta(eps^2)` floor; PSPO+ tracks the oracle. The floor
   figure *is* the paper.
2. The knife-edge: sweep the operating spread through `psi` and plot the SPO+
   decision bias changing sign. A sign change at a predicted location is the
   most convincing single panel available.
3. Held-out contexts: fit on calm/normal, evaluate on stress/crisis, using the
   existing lookahead-safe episode splits from `research/preprocessing/`.
4. Robust version: coverage of the shrinkage rule vs the nominal one under the
   1.4 ambiguity radius.

**Risks.** (i) The linear-objective SPO framing does not fit REFLEX's objective
without work - `J` is not linear in `theta`. Mitigation: state the theory for a
general smooth `J` (SPO+ generalises), and give the linear instance as the
special case that connects to the literature. Do not force the market model
into a linear program. (ii) This is a 12-18 day build. Not the right pick for
Aug 31 unless started immediately and scoped to Theorems 1-3 with a single
figure.

**Effort: 12-18 days.** Best kept for a full-length Operations Research
submission.

---
---

# M3. Optimal Retraining Cadence: impulse control of a performative system

**One line.** How often to retrain and redeploy a model whose deployment
reshapes its own data is an impulse-control problem, and its cost-optimal
solution crosses into instability exactly as compute gets cheap.

**Journal target.** Stochastic Systems (INFORMS Applied Probability Society -
the workshop's own sponsor, which is worth something).

**CFP fit.** Thematic area (ii), *sequential decision-making and online
learning ... evolving system states and fresh information arriving online*,
plus stochastic control, plus a real operational decision.

## M3.1 The gap

REFLEX 1.6 answers "what does `K` inner steps per deployment do to stability"
(`mu(K) = -m + c^K (1+m)`, with a deadbeat count `K_db` and a maximum stable
count `K_max`). It does not ask what `K` *should* be, nor *when* to redeploy.
Both are decisions with costs. Meanwhile the MLOps literature discusses
retraining cadence entirely heuristically (drift triggers, fixed schedules) and
never accounts for the fact that redeployment is itself the thing that moves
the distribution.

## M3.2 The formalism

State `(g_t, theta_t)`: `g_t` the mis-calibration gap between the deployed
policy and the current optimum, `theta_t` an exogenous ergodic market-regime
process (REFLEX's fitted regime chain, `calibration/regimes.py`). Between
deployments `g_t` drifts as the regime moves. An **impulse** at time `t` is a
pair `(retrain, K)`: cost `kappa_0 + kappa_1 K` (a fixed deployment/validation
cost plus a per-step compute cost) and it maps the gap by the 1.6 K-step
contraction. Running cost is the performative-risk gap.

```
   V(g, theta) = min over impulse policies  E [ sum_t  ell(g_t, theta_t)
                                              + sum_i ( kappa_0 + kappa_1 K_i ) ]
```

## M3.3 The theorems

**Theorem 1 (QVI and threshold structure).** `V` satisfies a quasi-variational
inequality; under convexity of `ell` in `g` the optimal policy is a
**threshold policy**: redeploy when `|g| >= g*(theta)`, and the optimal effort
`K*(g, theta)` solves a static trade-off between the geometric contraction
`c^K` and the linear compute cost `kappa_1 K`, giving
`K* = log(kappa_1 / (|log c| * (something))) / log c` in closed form for the
quadratic-loss case. Threshold structure under impulse control is standard; the
content is that the *post-impulse state is a function of the control effort*
through 1.6's map, which is not the standard `(s,S)` setting.

**Theorem 2 (cheap compute destabilises).** In the RRM-unstable regime `m > 1`,
1.6 gives a stability window `K <= K_max = log((m-1)/(m+1)) / log c`. The
unconstrained cost-optimal `K*` is decreasing in `kappa_1`. Therefore there is
a critical compute price `kappa_1^crit` below which `K*(kappa_1) > K_max`: the
cost-minimising retraining cadence is *unstable*, and the constrained optimum
sits on the boundary `K = floor(K_max)`, paying a strictly positive price of
stability. **As compute gets cheaper, the privately optimal amount of
retraining crosses from stabilising to destabilising.** That is a sharp,
counterintuitive, policy-relevant statement, and it follows from a closed form
REFLEX already ships.

**Theorem 3 (online cadence control with a safety guarantee).** `m` and `c` are
unknown. Give an optimism-for-cost / pessimism-for-stability algorithm with
regret `O~(sqrt(T))` against the oracle threshold policy and a
high-probability guarantee that `K_t <= K_max` for all `t`. The asymmetry -
optimistic on the objective, pessimistic on the constraint - is the technically
interesting part and connects to safe learning.

**Theorem 4 (desynchronisation as a stabiliser).** `N` dealers redeploy on
independent Poisson clocks with rates `r_i` into a shared pool with spillover
`kappa`. The joint system is a random-switching linear system; derive its
stability condition. Result to prove: **synchronous redeployment is the
worst case**, and the stability region strictly enlarges as deployment times
desynchronise, with the boundary depending on the aggregate intensity
`Lambda = sum_i r_i` rather than on `N` alone. This turns REFLEX 1.3's
common-mode result into a *schedulable* quantity and is the most
Stochastic-Systems-shaped result in the folder: it is a queueing-flavoured
statement about a learning system.

## M3.4 Implementation plan

**New code.** `reflex/control/cadence.py` (value iteration on a
`(gap, regime)` grid using the fitted regime chain; the closed-form `K*`;
the online controller), `reflex/env/async_deploy.py` (per-dealer Poisson
deployment clocks over the existing `env/multi_dealer.py`),
`experiments/run_cadence.py`, `tests/test_cadence.py`.

**Experiments.** (1) Optimal threshold and `K*` surfaces over
`(kappa_0, kappa_1)`, with the `K_max` constraint drawn on top - the
"cheap compute crosses the line" figure. (2) Realised cost of the learned
cadence controller vs fixed-cadence baselines across the 36-year regime path.
(3) Empirical stability region under synchronous vs staggered deployment at
`N = 2, 3, 5`, measured as the top Lyapunov exponent of the switched system,
against the Theorem 4 prediction.

**Reuse.** `theory/lazy_deploy.py` entirely; `estimators/br_slope.py`'s signed
CRN K-probe (`measure_rgd_response`); `analysis/fragility.py` for the regime
path; `env/multi_dealer.py`.

**Effort: 10-14 days.** The strongest *journal* prospect in this document;
the wrong size for a 15-day sprint unless Theorem 4 is dropped.

---
---

# M4. Anytime-Valid Certification of Retraining Stability

**One line.** Turn REFLEX's fixed-sample robust boundary into a sequential
certification procedure that is valid at every stopping time, and account for
the fact that the probe used to measure performativity is itself performative.

**Journal target.** Mathematics of Operations Research, or Operations Research
if the governance framing leads.

**CFP fit.** Thematic area (i): uncertainty quantification, performance
assessment of prescriptive decisions, robustification. Also causal-inference
adjacent, and it is a governance/audit story, which the applications list
supports.

## M4.1 The gap

REFLEX 1.4 gives a fixed-`n` ambiguity radius `delta_n = O(1/sqrt(n))` bought
by common random numbers, and issues stable / undecided / unstable verdicts.
Fixed-`n` is the wrong shape for the actual use: a supervisor or a risk desk
monitors continuously and wants to stop as soon as the verdict is decided.
Peeking at a fixed-`n` interval invalidates it.

## M4.2 The results to prove

**Theorem 1 (confidence sequence for the modulus).** Construct an e-process for
the null `H0: m >= 1` from CRN-paired probe differences, giving an anytime-valid
upper confidence sequence `m_bar_t` with width `O(sqrt(log log t / t))`. The
CRN pairing enters the bound through the paired variance, which is `O(delta^2)`
in the probe half-width `delta` where the unpaired variance is `O(1)` - this is
1.4's `n^{-1/3}` to `n^{-1/2}` improvement, now in the sequential setting where
it matters more because the log-log penalty makes constants decisive.

**Theorem 2 (optimal probe width, sequentially).** Bias is `O(delta^2)`,
paired variance `O(1)` per probe, so the sequentially optimal width is
`delta_t ~ t^{-1/4}` and the total error is `O(t^{-1/2})`. Give the adaptive
schedule and prove it retains anytime validity despite the data-dependent
width.

**Theorem 3 (the probe is performative).** A probe deployment at `h +/- delta`
*changes the distribution being measured*, so the estimator is
measurement-perturbed with a first-order bias of order `delta * epsilon`. Show
that CRN cancels this first-order perturbation exactly (the two arms share the
perturbation's common component), leaving `O(delta^2 epsilon)`. This is a
genuinely new observation about performative estimation - the measurement
disturbs the system, and the standard variance-reduction trick turns out to be
a *bias*-cancellation trick here for a completely different reason than usual.
It is small but it is the kind of thing referees remember.

**Theorem 4 (sequential decision boundaries).** Three actions - certify stable,
certify unstable, continue probing - with an explicit cost of continuing (each
probe is a real perturbation costing P&L, by M2's exchange rate) and asymmetric
costs of the two wrong verdicts. Derive the SPRT-like two-threshold structure
and the expected sample size, and show it is the operationally correct stopping
rule rather than a fixed budget.

## M4.3 Implementation plan

Extend `reflex/theory/robust.py` with `confidence_sequence`,
`eprocess_modulus`, `adaptive_probe_width`, `sequential_verdict`; extend
`experiments/run_tuning.py` (which already has the coverage-calibration
harness) with a sequential-coverage study. New experiment
`run_certify.py`.

**The figure that sells it:** re-issue the 36-year daily fragility index
(`analysis/fragility.py`) as an *anytime-valid* certificate band -
certified-stable / undecided / certified-unstable through the GFC and the COVID
freeze, with the undecided band widening exactly where the crisis-regime fit is
degenerate. REFLEX already flags that degeneracy honestly; showing the
certificate *automatically* refuses to certify there is a much stronger
statement than flagging it in prose.

**Effort: 4-5 days.** The natural second submission if two ML x OR papers are
wanted, and it composes with M2 (M2 prices the probes that M4 spends).

---
---

# Cross-cutting notes

**Composition.** M2 prices exploration; M4 spends it on certification; M1
consumes the resulting Jacobian estimate in a decision rule; M3 schedules the
whole thing. If more than one is submitted, say this explicitly in each - a
coherent program reads better than scattered results, and the ML x OR journal
pipeline is looking for something that can grow into a full paper.

**Verification layer.** Every theorem above gets a numerical certificate in
`reflex/verification/certificates.py`, on raw *and* calibrated configs. The
66-certificate layer is REFLEX's most distinctive asset for a mathematically
serious venue; a branch-off that ships theorems without extending it is leaving
the strongest credibility signal unused.

**What to be careful about.**
- The `alpha` confound: never sweep `alpha`, always `clients.toxicity_feedback`.
- Beyond the boundary, measured probe readings scatter (seed-level
  bifurcation); they are diagnostics there, not local slopes. Any figure that
  extends past `m = 1` must say so in the caption.
- On calibrated configs, benchmark against the **realized-state** closed form
  (1.1 section 9), never the A2 frozen reference - the `rho ~ 2.3`
  liquidity-inflation correction is real and is the dominant channel.
- Do not de-saturate `info_cap` to make numbers agree. It is load-bearing.
