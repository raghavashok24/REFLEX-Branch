# NeurIPS 2026 Workshop Program — REFLEX Branch-Off Papers

Two papers branching off **REFLEX** (*Reflexive Equilibrium Fixed-point Learning
for endogenous financial markets*), targeted at NeurIPS 2026 workshops in
Atlanta (Dec 12/13). REFLEX derives the performative-prediction stability
constants (`m = εβ/γ`) in closed form from market-microstructure primitives,
verifies them against a learned simulator loop (152 tests, 66 numerical proof
certificates), and calibrates on 36 years of public market data. Its core
results are committed to a concurrent ICAIF 2026 submission; each workshop
paper below contributes **only new formal objects** that appear in neither
REFLEX nor that submission.

| Paper | Venue | Deadline | Format | Review |
|---|---|---|---|---|
| P1 — The Price of Self-Knowledge | ML×OR | **Aug 31, 2026** | 4 pp + unlimited appendix | Non-anonymous; journal pipeline |
| P2 — Learning Externalities | EconML | **Aug 29, 2026** | 9 pp + unlimited appendix | Double-blind; in-person required |

---

## Paper 1 (ML×OR): "The Price of Self-Knowledge: Minimax Information–Cost
## Tradeoffs and Optimal Exploration in Performative Systems"

**Journal designation:** Mathematics of Operations Research (the workshop
invites full versions of selected papers to Stochastic Systems / MOR /
Operations Research; the unlimited appendix is written first and doubles as
the MOR draft).

**Thesis.** In a system whose data distribution reacts to the deployed model,
information about that reaction is *purchased with the objective itself*.
Estimating the response Jacobian that performative-gradient methods consume is
not a statistics problem with a sample budget — it is a control problem with a
P&L budget, and the exchange rate is exact.

**Results** (status: ✅ verified numerically · 🟦 provable, standard machinery
· 🟧 hard, the main-track-grade work):

- **T1 — Information saturation** ✅ (scalar, to 1e-16) / 🟦 (d-dim).
  A converging retraining loop's design energy is bounded:
  `Σ(h_t−h*)² → (h₀−h*)²/(1−m²)`. Fisher information for the response slope
  saturates — running longer buys nothing. Corollaries: *safety implies
  blindness* (the cap grows with the modulus m — self-knowledge is precise
  only near instability); curvature parameters are unidentified from any
  trajectory (period-2 design degeneracy at the boundary).
- **T2 — The exchange-rate identity** ✅ (rel. err 0.0 across (m, σₑ) grid).
  With exploration, in the stationary regime:
  `Var(ε̂) × C_T = ½·γ_PO·σ²` — invariant to exploration intensity, horizon,
  and modulus. Anchoring matters: C_T is the *incremental* cost at h*, not
  distance from h_PO (the wrong anchor provably breaks the invariance by the
  factor (1+g²/v) — implemented as a permanent falsification check).
- **T3 — Minimax lower bound** 🟧. Over all adaptive policies and all
  estimators (van Trees + Le Cam symmetrization): no scheme beats the
  exchange rate by more than its own estimation error — exploiting the
  profitable direction requires knowing the quantity being estimated. The
  deviation-budget version is exact and provable by the deadline; the
  value-budget (1−o(1)) version is the journal deliverable.
- **T4 — Matrix uncertainty principle** 🟦 (equality case verified by hand).
  `R_A × C_T ≥ (σ²/2)(tr Γ_PO^{1/2})²`, equality iff the exploration
  covariance ∝ `Γ_PO^{−1/2}` — **explore where the objective is flat**.
  Corollary: isotropic jitter overpays by exactly the curvature dispersion of
  the objective (computable on the calibrated 128-bond Γ_PO).
- **T5 — Safe D-optimal exploration** 🟧. Frank–Wolfe design under a value
  budget, a closed-loop spectral stability margin, and a trust region;
  pessimistic-on-stability / optimistic-on-information re-solving. Targets:
  O(√T) identification regret, high-probability stability throughout.
- **T6 — Anchoring crossover** 🟦. Anchor to a p-dim structural family iff
  `δ_mis² < ½·γ_PO·σ²/B` — turns REFLEX's documented "anchoring, not
  capacity" negative result into a budget-priced decision rule.
- **Corollary — ROI of self-knowledge** ✅. The echo-chamber gap is a
  recoverable perpetuity; identification is a one-off cost priced by T2.
  Break-even discount rate in closed form: explore iff patient enough.

**Experiments (5):** saturation curves vs closed-form caps; the exchange-rate
flat line + measured nonlinear drift (a result, not a nuisance); shaped
(`Γ_PO^{−1/2}`) vs isotropic exploration at matched budget; safe design
identifying the curvature parameter jitter cannot; anchoring-crossover table
retrodicting the v3 negative result. All CPU, deterministic, certified.

**Literature review: complete** (see `litreview/LITERATURE-REVIEW-M2.md`).
Six clusters, ~35 verified sources, per-gap justifications, honest novelty
verdict. Four load-bearing citations with named deltas: Jagadeesan et al.
(ICML '22 — prices the *search*, not the *knowledge*; no loop, no stability
constraint), Keskin–Zeevi (OR '14 — incomplete learning, but static demand,
no modulus, no invariance), Bombois et al. (Automatica '06 — least-costly ID,
but exogenous plant), Lin–Zrnic (ICML '24 — plug-in models, no cost side;
closest to T6). Consistency checks: Lai–Robbins log-n schemes lie *on* the T2
frontier; Simchowitz–Foster's "naive exploration is optimal" flips
performatively by the curvature-dispersion factor. Remaining pre-submission
work: full-text reads of the 4 closest papers (downloads blocked in the build
env — script provided), add the safe-exploration sub-cluster (SafeOpt,
Berkenkamp), triage arXiv:2408.08499.

---

## Paper 2 (EconML): "Learning Externalities: Systemic Instability and
## Herd Immunity in Markets of Adaptive Agents"

**Thesis.** Individually stable learning agents (`m₁ < 1`) can destabilize
the market they share: each agent's retraining reshapes the environment every
other agent learns from next — a **learning externality** no agent
internalizes. Agent count enters the stability condition itself
(`m_N = N_eff·m₁`, critical population `N_c = 1/m₁`), so "is this model
stable?" is the wrong certification question; "is the ecosystem of
interacting models stable?" is the right one.

**Framing kept from the original outline:** private vs. systemic stability;
the six-step externality loop; the verified 1.74×/3.16× common-mode
amplification (N = 2, 3) as the empirical anchor; `m_N` read as the
market's **feedback reproduction number**.

**Three new results (in neither REFLEX nor the ICAIF submission):**

- **T1 — The crowding–cadence frontier.** Composing the multi-dealer law
  with lazy deployment: `μ_N(K) = −m_N + c^K(1+m_N)`, giving a retraining
  budget `K_max(N)` that **shrinks with every additional competitor** —
  "your competitor's entry consumes your retraining budget." Critical
  crowding: beyond `N_eff > (1+c)/((1−c)·m₁)` no cadence keeps the market
  stable; equivalently, minimum-cadence operation multiplies the sustainable
  number of competitors by exactly `(1+c)/(1−c)` (×9 at c = 0.8).
- **T2 — Herd immunity.** Mixed market of blind and corrected
  (performative-gradient) dealers: in the strong-correction limit the market
  is stable iff the corrected fraction exceeds
  `ρ* = 1 − N_c/N = 1 − 1/m_N` — **exactly the epidemiological 1 − 1/R₀
  threshold**, with the systemic modulus as the reproduction number.
  Correction is a public good (free-riding keeps markets below threshold);
  exact finite-γ_PO version via a two-block secular equation. The experiment
  is new in kind: the structural corrected loop has never been run inside
  the N-dealer game.
- **T3 — The Pigouvian wedge.** Instability priced through the common mode's
  stationary variance ∝ `1/(1−m_N²)`; the private FOC ignores (N−1)/N of the
  marginal cost; closed-form corrective fee; over-adaptation corollary. The
  three levers unify as the standard policy triple: quantity (cadence caps),
  technology (correction mandates), price (the wedge).

**Experiments (4):** the 1.74×/3.16× replication anchor; the (N, K) stability
grid vs the predicted frontier; the herd-immunity sweep over corrected
fractions vs ρ* (+ free-riding P&L diagnostic); decentralized vs socially
optimal adaptation. De-scope order defined; the herd-immunity experiment is
never cut — it *is* the paper.

**Build: ~7–8 focused days** against 12 remaining. Anonymization checklist
for double-blind (no repo URL, third-person citation of the concurrent
submission, scrubbed metadata).

---

## Assumptions audit (both papers)

Every load-bearing claim was re-derived and stress-tested (2026-08-16/17).
Two real defects found and **fixed before writing**: P1's cost anchor (the
h_PO-anchored identity is false — verified numerically, corrected to the
incremental anchor, and the fix produced the ROI corollary) and the
heterogeneous-moduli eigenvalue overclaim in the earlier EconML variant
(orthogonal responses give ρ = max mᵢ, not the mean — scoped to the exact
equal-moduli identity plus weighted-Gram bounds). Thirteen further checks
passed and are recorded with evidence. Standing rule: nothing is claimed at
submission beyond what is proved or verified; 🟧 items ship as labeled
partial results.

## Shared infrastructure (from REFLEX, used as cited scaffolding)

Closed-form theory modules (1.1–1.6) · genuine N-dealer simulator
(bit-for-bit single-dealer reduction at N = 1) · four-mode retraining loops
incl. `perfgd_structural` · tuned three-way ε estimators · 66-certificate
verification layer (each new closed form adds certificates) · real-data
calibration with honest provenance (public proxies, not trade-level TRACE) ·
deterministic CPU-only experiments from `(config, seed)`.

## Timeline

| Date | Milestone |
|---|---|
| Aug 17–22 | P2 build (theory module → (N,K) grid → herd-immunity sweep → wedge) |
| Aug 17–25 | P1 build in parallel (theory transcription → design module → experiments) |
| Aug 23–27 | P2 writing, anonymization pass, freeze | 
| Aug 26–30 | P1 writing (appendix first), claim-list review, MOR designation |
| **Aug 29** | **P2 → EconML (OpenReview)** |
| **Aug 31** | **P1 → ML×OR (OpenReview)** |

Go/no-go checkpoint **Aug 21**: if P2's frontier and herd-immunity
experiments aren't clean, drop to one paper (P1 is the safer single bet —
verified core, two extra days).

## Non-overlap statement

The ICAIF submission owns REFLEX's core (computable constants, the
homogeneous N_eff law, certificates, fragility index). P1's identification
economics and P2's frontier/herd-immunity/wedge results appear in neither.
P1 and P2 do not overlap each other (single-learner identification vs.
many-learner interaction; the one shared object, γ_PO, is cited
infrastructure). Both venues are non-archival, so neither blocks the ICAIF
paper or later journal/main-track versions.
