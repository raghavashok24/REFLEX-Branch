# The ML x OR Paper, Explained

## "The Price of Self-Knowledge: an Information-Cost Uncertainty Principle for Performative Systems"

**Venue:** ML x OR workshop @ NeurIPS 2026 (Atlanta, Dec 12/13). Submit by
**Aug 31, 2026**. Format: 4 pages main body, NeurIPS style, unlimited
references and appendix. Non-anonymous. Journal pipeline: designate
**Mathematics of Operations Research** at submission.

---

## 1. The idea in one paragraph

When a deployed model reshapes the distribution it is trained on — a dealer's
quotes reshape order flow, a ranking reshapes clicks, a price reshapes demand —
any method that wants to *correct* for that feedback (performative gradient
descent and its relatives) first has to *measure* it: it needs the response
slope, how much the distribution moves per unit of decision. The literature
treats this as an estimation step with a sample budget. This paper's point is
that it is not: in a deployed system, every data point that identifies the
response is a real decision taken at a real price. You cannot probe your own
performativity without deviating from your optimum, and the deviation costs
you the very objective you are trying to optimize. We make that trade-off
exact. The paper proves that (i) a converging retraining loop generates only a
**bounded** amount of information about its own feedback, no matter how long
it runs, and (ii) once you explore deliberately, the product of estimation
precision and profit foregone is **pinned at a constant** — an exchange rate
between self-knowledge and value that no exploration scheme can beat. Then it
builds the optimal way to spend that budget: a D-optimal exploration design
that provably never destabilizes the system it is probing.

## 2. Why this venue wants it

ML x OR's call asks for "uncertainty mitigation at the interface of data,
model, and decision," uncertainty quantification of prescriptive decisions,
and sequential decision-making from an OR perspective. This paper is exactly
that interface: the uncertainty is about the system's own response to the
decision, the quantification is an exact identity rather than a bound, and the
algorithm is sequential experimental design under a dynamical-stability
constraint. The shape also fits the venue mechanics: two crisp theorems and
one decisive experiment fit in 4 pages, while the full proofs and extended
empirics live in the unlimited appendix — which doubles as the draft of the
journal version the workshop's Mathematics of OR pipeline invites.

## 3. Background you need (two paragraphs)

**Performative prediction** (Perdomo et al., ICML 2020): when the data
distribution `D(phi)` depends on the deployed model `phi`, "retrain on the
data your last model generated" (repeated risk minimization, RRM) converges
iff `epsilon < gamma / beta`, where `epsilon` is the sensitivity of the
distribution to the model, and `gamma, beta` are the curvature and smoothness
of the loss. The point it converges to (the *stable point*) is generally not
the *performative optimum* — the model that would be best accounting for the
distribution it induces. PerfGD (Izzo et al., ICML 2021) closes that gap by
estimating the response `dD/dphi` and adding a correction term to the
gradient.

**REFLEX** (the base project) realizes this loop inside a structural
market-making model where all three constants are *computed* from
microstructure primitives rather than assumed, so the contraction modulus
`m = epsilon*beta/gamma` is known in closed form, the loop is simulated with a
learned operator, and every claim is falsifiable. Crucially, REFLEX documented
a negative result: a free-form learned correction (an MLP estimating the
response) fails to stabilize the loop, because a converged loop stops
generating the variation needed to identify the response — the "echo chamber's
identification collapse." The engineering fix was to inject deployment jitter
and anchor the estimate to a structural family. **This paper is the theory of
why that fix was necessary, what it costs, and when it wins.**

## 4. The model

Everything is stated for a general decision-dependent system with a smooth,
strongly concave objective; the market is the instantiation where every
constant is computable. Locally, around the loop's stable point `h*`:

```
   deployment:   h_{t+1} - h*  =  -m (h_t - h*)  +  sigma_e * xi_t
   response:     tau_t  =  tau(h*) - epsilon (h_t - h*)  +  zeta_t
```

- `h_t` is the deployed decision (the dealer's half-spread), `tau_t` the
  observed response (informed flow).
- `m` is the retraining modulus: each retraining round reflects the deviation
  through the best-response cobweb with slope `-m`.
- `sigma_e` is **deliberate exploration** — jitter the operator injects into
  deployments (REFLEX's `collection_jitter` knob).
- `zeta_t` is response noise with variance `sigma_tau^2`.
- The estimand is `epsilon`, the response slope — the scalar version of
  `dD/dphi`, the exact quantity PerfGD needs. The estimator is least squares
  of `tau_t` on `h_t`; its precision is governed by the design energy
  `S_xx = sum_t (h_t - hbar)^2`.

Two quantities face off:

```
   Information:  I_T  =  S_xx / sigma_tau^2                 (Fisher information for epsilon)
   Cost:         C_T  =  expected excess performative risk of the jittered loop
                         relative to the jitter-free loop at h*
                      =  (1/2) * gamma_PO * E[ sum_t (h_t - h*)^2 ]
```

`gamma_PO` is the curvature of the *true* performative objective (available in
closed form in REFLEX from theory 1.2). One definitional subtlety is
load-bearing and we found it the hard way: `C_T` must be the **incremental**
cost of exploration, anchored at the operating point `h*` — *not* the distance
from the performative optimum `h_PO`. The stable point and the optimum differ
(their gap is the "echo-chamber gap"), and that gap's cost is *sunk*: it is
paid whether or not you explore, and it is the cost of blindness, not the cost
of measurement. Anchoring at `h_PO` silently adds that sunk term and destroys
the theorem (we verified this numerically: the product below becomes
`(1/2) gamma_PO sigma_tau^2 (1 + g^2/v)` — dependent on the jitter and the
modulus, divergent as jitter shrinks). With the correct anchor, everything
that follows is exact.

## 5. The results, each explained

### Theorem 1 — Information saturation

With no exploration (`sigma_e = 0`) and a stable loop (`m < 1`), the
trajectory's design energy converges:

```
   sum_{t<=T} (h_t - h*)^2  -->  (h_0 - h*)^2 / (1 - m^2)     as T -> infinity.
```

*Why it holds:* the noiseless loop is `h_t - h* = (-m)^t (h_0 - h*)`, a
geometric sequence; the sum of its squares is a geometric series. Verified
numerically to 1e-16.

*Why it matters:* Fisher information for `epsilon` is proportional to this
sum, so it **saturates**. A converging retraining loop can never learn its own
performativity beyond a fixed floor — running longer buys nothing, ever. The
variance of any unbiased estimate obeys
`Var(epsilon_hat) >= sigma_tau^2 (1 - m^2) / (h_0 - h*)^2` at every horizon.
This is the theorem behind REFLEX's observed echo-chamber collapse: the
free-form learned loop was not underpowered, it was *information-starved by
its own convergence*, and no amount of model capacity fixes that.

**Corollary 1.1 (the stability-identifiability conflict).** The information
cap `(h_0-h*)^2/(1-m^2)` is *increasing* in `m`. A fast-contracting (very
safe) system snaps to its fixed point and reveals almost nothing; a system
near the boundary `m -> 1` oscillates persistently and is easy to identify.
**You can measure your performative sensitivity precisely only when it is
almost large enough to destabilize you.** Safety implies blindness. This
inverts the comfortable "estimate first, then decide" ordering.

**Corollary 1.2 (what the trajectory can never identify).** At the boundary
the noiseless iterates alternate between two points; generically the design
concentrates on at most two support points. A two-point design identifies a
secant — never curvature. So parameters that live in the curvature of the
response (in REFLEX, the exponential decay rate `c_t` of the toxic-flow
curve) are unidentified from the loop's own trajectory at *any* modulus. (The
repo has long carried the folk rule "exponential response fits need a wide
spread range"; this is that rule as a theorem.)

### Theorem 2 — The uncertainty principle

Turn exploration on (`sigma_e > 0`). In the stationary regime, in
expectation:

```
   Var(epsilon_hat)  x  C_T   =   (1/2) * gamma_PO * sigma_tau^2
```

**independent of the exploration intensity, the horizon, and the modulus.**

*Why it holds:* the stationary variance of the jittered loop is
`v = sigma_e^2 / (1 - m^2)`. Information grows like `T v / sigma_tau^2`
(precision ~ `sigma_tau^2 / (T v)`), while the incremental cost grows like
`(1/2) gamma_PO T v`. The design energy `T v` appears in both and cancels
exactly. More jitter buys information faster and burns money faster at
precisely the same rate; a higher modulus amplifies the jitter into more
excitation *and* more cost, again at the same rate. (One more step in the
proof: because `h*` is not the optimum, the cost expansion has a linear term
`-Phi'(h*)(h_t - h*)`; it is zero-mean in the stationary regime, so the
identity holds in expectation, and the linear term only adds variance around
it — which the experiments report.)

*Why it matters:* information about your own performativity has a **fixed
exchange rate** against foregone value — `(1/2) gamma_PO sigma_tau^2` — set
only by the curvature of the true objective and the noise in the response
channel. Halving your estimator's variance costs exactly twice the P&L, no
matter how cleverly you schedule the exploration. This is not a bound, it is
an identity (verified numerically: relative error 0.0 across a grid of moduli
and jitter sizes). It is also not Cramér–Rao: CR bounds variance by
information; the content here is that the information is *purchased with the
objective itself*, which turns an inequality about estimators into an
exchange rate between knowledge and value.

**The unified reading.** Total information = transient + stationary. The
transient (Theorem 1) is *free but bounded* — the loop's convergence path is
the only identification you ever get without paying. Everything after is
bought at the fixed rate (Theorem 2). One system, one budget line.

**Corollary 2.1 (the ROI of self-knowledge).** Why buy information at all?
Because blindness has a price too: the echo-chamber gap costs
`(1/2) gamma_PO (h_SP - h_PO)^2 = O(epsilon^2)` per step *forever*, and the
PerfGD correction recovers it — but only with a sufficiently precise estimate
of `epsilon`, whose one-off price Theorem 2 sets. Comparing the perpetuity
value of the recoverable gap against the one-off identification cost gives a
closed-form break-even discount rate: **a performative system should explore
iff it is patient enough, and "patient enough" is computable from
primitives.** This is the operational sentence a trading desk (or any model
owner) can act on.

### Theorem 3 — The feasibility frontier

Fix an accuracy target `Var(epsilon_hat) <= v` and a risk budget `C_T <= B`.
By Theorem 2 the pair is achievable iff `v * B >= (1/2) gamma_PO sigma_tau^2`
— a one-line test. Two regimes break it structurally: beyond the stability
boundary (`m > 1`) there is no stationary regime — the jitter is amplified,
the exchange rate degrades without bound; and under a binding trust region
(deployment steps capped at `r`, as any real risk system does) the achievable
excitation is capped, so sufficiently tight accuracy targets are unreachable
at *any* budget. Generically there is a price, not a prohibition; the
prohibitions live exactly where you'd want to be warned about them.

### Theorem 4 — When structural anchoring wins

REFLEX's empirical fix for the echo chamber was to anchor the response
estimate to a low-dimensional structural family (the theory's own exponential
flow curves, 3 parameters) instead of a free-form neural estimate. The
headline empirical finding was "anchoring, not capacity, closes the gap."
This theorem is that finding made quantitative: with a correctly specified
`p`-dimensional family, the design burden drops from exciting a function
space to exciting `p` directions, improving the exchange-rate constant by a
computable design-optimality ratio; misspecification of size `delta` adds an
irreducible bias `O(delta)`. The crossover is a decision rule:

```
   anchor  iff   delta^2  <  (1/2) gamma_PO sigma_tau^2 / B .
```

Anchoring wins whenever the model-family error is smaller than the precision
your budget can buy nonparametrically. This both *explains* the published
negative result and *bounds when it would have reversed* — which no
experiment in the base project does.

### The algorithm — safe D-optimal performative exploration

Theorems 1–3 price information; the algorithm spends the budget optimally:
choose the deployment schedule maximizing `log det` of the information matrix
for the structural family, subject to (i) the risk budget (a convex
quadratic), (ii) a closed-loop spectral stability margin — the probing itself
must never push the loop unstable — and (iii) the trust region. The relaxed
design problem is convex; we solve it with Frank–Wolfe on the design simplex
(keeping the project's numpy/scipy-only convention). Since `gamma_PO` and `m`
are unknown at the start, the schedule re-solves under the current estimates,
*pessimistic about stability, optimistic about information*. Guarantee
targeted: identification regret `O(sqrt(T))` against the oracle design, with
high-probability stability throughout.

## 6. The experiments

All CPU, deterministic from `(config, seed)`, run in the REFLEX simulator with
its real-data-calibrated configs.

1. **Saturation curves.** Run the blind loop with zero jitter across moduli
   `m in [0.1, 0.95]`; plot cumulative design energy against the closed-form
   asymptote. Expected: flat lines at `(h_0-h*)^2/(1-m^2)`, ordered in `m`.
   Sells Theorem 1 and Corollary 1.1 in one panel.
2. **The exchange rate.** Sweep jitter across three feedback levels; measure
   estimator variance across seeds (using the project's tuned three-way
   estimator suite) and realized excess performative risk; plot the product.
   Expected: flat at `(1/2) gamma_PO sigma_tau^2` in the contracting regime,
   with a *measured drift* where the simulator's nonlinearities (flow
   saturation, liquidity inflation) engage. The drift curve is reported as a
   result — it is the honest scope boundary of the local theory.
3. **Safe design beats jitter.** Three exploration schemes at matched budget:
   naive iid jitter, a two-point probe at the trust-region edge, and the
   D-optimal schedule. Metric: variance of the *curvature* parameter that
   Corollary 1.2 says trajectories never identify. Expected: the designed
   schedule identifies it at the same P&L where jitter cannot. The
   operational punchline.
4. **Anchoring crossover table.** Structural fit vs free-form MLP across
   injected misspecification levels; empirical crossover vs the Theorem 4
   threshold. Retrodicts the published negative result and maps its boundary.

Every closed form ships a numerical certificate in the project's verification
layer (66 existing machine-checked identities; this adds ~7, including the
wrong-anchor falsification as a permanent regression check).

## 7. What is genuinely new

- The **product identity** itself: estimator precision times foregone value
  pinned at a constant, invariant to how you explore. Nothing comparable
  exists in the performative-prediction literature (which bounds estimation
  error but never prices it in the objective) or in experimental design
  (which prices designs but not with a decision-coupled, stability-
  constrained budget).
- The **saturation theorem** and its inversion — safety implies blindness;
  identifiability is a near-instability phenomenon. Persistent excitation in
  adaptive control is the spiritual ancestor, but the exact cap in terms of
  the performative modulus, and its coupling to the stability boundary, is
  new — and to our knowledge the PE lens has never been brought to
  performative prediction at all.
- The **anchoring crossover**: an empirical folk finding ("structure beats
  capacity here") turned into a decision rule with a computable threshold.
- **Design under a dynamical-stability constraint**: D-optimality where the
  experiment itself must not destabilize the plant being identified.

## 8. Honest limitations (stated in the paper, not discovered by reviewers)

- The identity is exact for the local quadratic model; beyond it, the drift
  is measured, not assumed away.
- In the real loop the regressor is predetermined, not strictly exogenous
  (today's observed response shapes tomorrow's deployment), giving an
  `O(1/T)` bias; the identity is stated under exploration-dominant design and
  the deviation is measured.
- One domain instantiated deeply (the market model, where constants are
  computable); a strategic-classification instantiation is sketched to show
  the abstraction is real.

## 9. Build plan (submission Aug 31; ~15 days)

- **Aug 17–19:** theory module (`identification.py`: saturation, exchange
  rate, feasibility, ROI, anchoring threshold) + tests + certificates. The
  math is already verified; this is transcription. Appendix proofs drafted in
  parallel — the appendix is written *first*, because it is the journal
  draft.
- **Aug 20–22:** the design module (Frank–Wolfe D-optimal scheduler) and
  experiment 3 harness.
- **Aug 23–25:** experiments 1, 2, 4; the drift study.
- **Aug 26–28:** write the 4-page body as an extended abstract of the
  appendix.
- **Aug 29–30:** review against this document's claim list; freeze numbers;
  non-anonymous build; journal designation = Mathematics of OR.
- **Aug 31:** submit.

De-scope order if time runs short: the crossover table first, then the
regret guarantee (algorithm ships with empirical safety and the guarantee as
a conjecture), never the exchange-rate experiment. Fallback for the design
solver: closed-form two/three-point D-optimal designs, which already beat
jitter.
