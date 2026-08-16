# EconML @ NeurIPS 2026 - branch-off paper ideas from REFLEX

**Venue constraints.** Long (9 pages) or short (4 pages) main content;
references and appendices unlimited. **Double-blind.** Non-archival. Submit
**Aug 29 2026**. At least one author presents in person in Atlanta.

**Design rule for this venue.** This is an economics-literate ML audience
organised around two themes: economics *for* ML training/alignment/evaluation,
and *ecosystems with many interacting models*. Their topic list names
"Feedback loops and performative prediction effects", "Algorithmic collusion
among learning systems", and "Algorithmic monoculture and model multiplicity"
verbatim. REFLEX is a performative feedback loop with a multi-agent
shared-resource extension, so topicality is free; what is *not* free is
register. Reviewers will ask for an equilibrium concept, a welfare or incentive
statement, and an identification argument. Every idea below carries all three.

Use the **9-page long format**. A short paper cannot carry a model, an
equilibrium analysis and evidence, and this audience will not forgive dropping
any of the three. E4 is the exception - it is designed as a short paper.

**Anonymisation.** The working REFLEX repo, the ICAIF draft and this
repository are all de-anonymised. The EconML build must strip the author block
and the public repository footnote, and must cite the ICAIF submission in third
person ("a concurrent submission develops...") rather than as "our prior work".

Ranked. E1 is the recommendation for this cycle.

---
---

# E1 (RECOMMENDED). Algorithmic Monoculture as Dynamical Instability

**One line.** When many firms deploy learned policies that reshape a shared
data-generating environment, what destabilises the market is not the *number*
of learners but the *correlation* of their performative responses - so the
effective number of independent models, not firms, is the systemic-risk
variable, and every private incentive pushes it toward one.

**Format.** Long (9 pages).

**CFP fit - three verbatim bullets at once.** "Algorithmic monoculture and
model multiplicity"; "Feedback loops and performative prediction effects";
"Market concentration among AI service providers". Plus "Multi-agent learning
dynamics in economic environments", "AI supply chains and their dynamics", and
"Ecosystem-level incentive design" for the adoption-game half.

## E1.1 The gap

The algorithmic-monoculture literature (Kleinberg-Raghavan; Bommasani et al. on
homogenization) is about **outcome correlation**: when many decision-makers use
the same model, the same applicants get rejected everywhere, and welfare falls.
It is a static, cross-sectional argument. Nobody has asked what monoculture does
to the *dynamics* of a system in which those models retrain on data their own
decisions generated.

The answer turns out to be sharp, and it is not the same as the static story.
Monoculture does not merely correlate outcomes - it aligns the *feedback
directions* of the learners, and aligned feedback resonates. REFLEX 1.3 already
proves the homogeneous version: `N` identical dealers sharing one informed pool
have joint Jacobian

```
   J_BR = -m_1 * [ (1 - kappa) I  +  kappa 1 1^T ] ,
   spectrum:  common mode  -m_1 * (1 + kappa (N-1))  =  -m_1 * N_eff
              differential modes  -m_1 * (1 - kappa)     (multiplicity N-1)
```

so the common mode - everyone moving together - is the unstable one, and the
differential modes are *more* stable than a single dealer. Measured in a
genuine shared-pool simulator: `1.74x` and `3.16x` amplification at `N = 2, 3`
against predicted `N_eff = 2, 3`.

The homogeneous case is a special case of the real question and it hides the
interesting variable. This paper generalises to heterogeneous learners and
shows that `N_eff` is really an *alignment* functional.

## E1.2 The formalism

Lift REFLEX 1.3 to heterogeneous learners over the multi-bond decision space of
1.5, which is where "response direction" becomes a genuine vector and alignment
becomes meaningful.

- `N` firms, each quoting a `d`-vector `h_i in R^d`, each with its own
  objective curvature matrix `Gamma_i` and its own **response Jacobian**
  `E_i in R^{d x d}`, where `(E_i)_{ab} = d tau_{i,a} / d h_{i,b}` is how firm
  `i`'s own quoting reshapes the flow it sees.
- Shared pool with spillover: `d tau_i / d h_j = kappa * E_{ij}` for `j != i`.
- Joint Jacobian `J in R^{Nd x Nd}`, blocks `J_{ij} = -Gamma_i^{-1} beta E_{ij}`.

Define the **performative alignment** of the ecosystem as the normalised Gram
structure of the vectorised responses,

```
   r_ij  =  < vec(E_i) , vec(E_j) >  /  ( ||E_i||_F ||E_j||_F ) ,
   rbar  =  (1/(N(N-1))) sum_{i != j} r_ij       in [-1/(N-1), 1] ,
```

and the **alignment-effective learner count**

```
   N_eff^align  :=  1 + kappa (N - 1) rbar .
```

`rbar = 1` (monoculture) recovers REFLEX's `N_eff = 1 + kappa(N-1)`;
`rbar = -1/(N-1)` (maximally diverse, a simplex configuration of responses)
gives `N_eff^align = 1 - kappa`, i.e. *below* the single-firm value.

## E1.3 The theorems

**Theorem 1 (diversity-stability).** For symmetric-curvature ecosystems,

```
   rho(J)  <=  mbar * ( 1 + kappa (N - 1) rbar ) ,
```

with equality in the homogeneous case, where `mbar` is the curvature-weighted
mean single-firm modulus. Hence the ecosystem is stable iff
`epsilon < gamma / (N_eff^align * beta)`. **Model diversity is a systemic-risk
control variable with a closed-form price**, and the price is linear in the
mean pairwise response correlation.

*Proof strategy, with the scope stated carefully (audited 2026-08-16).* The
alignment enters through the spectrum of the Gram/correlation matrix
`R = (r_ij)` of the vectorised responses, but the exact form depends on
modulus heterogeneity, and conflating the two cases is exactly the kind of
slip a referee catches:

- **Equal moduli, heterogeneous directions** (`m_i = m` for all `i`): prove the
  *exact* identity `rho(J) = m * (1 + kappa (lambda_max(R) - 1))`, with
  `lambda_max(R)` interpolating between `1` (orthogonal responses, dealers
  effectively decoupled) and `N` (monoculture, recovering 1.3). This is the
  clean headline case and `lambda_max(R)` is exactly the "effective number of
  independent models".
- **Heterogeneous moduli**: the mean-modulus version is **provably false** -
  counterexample: orthogonal responses (`R = I`) decouple the dealers exactly,
  so `rho(J) = max_i m_i`, not `mbar`. The correct general object is the
  modulus-weighted matrix `M^{1/2} R M^{1/2}` with `M = diag(m_i)`:
  state `rho(J) <= lambda_max( (1-kappa) M + kappa M^{1/2} R M^{1/2} )`-type
  bounds, exact in the equal-modulus and the `kappa = 0` limits, and report
  the general case as a bound with its tightness measured in simulation.

The mean-alignment form `N_eff^align = 1 + kappa (N-1) rbar` in the theorem
statement is therefore the equal-modulus specialisation (where
`lambda_max(R) >= 1 + (N-1) rbar` with equality for equicorrelated `R`) and a
lower bound in general - stability claims in the paper must be made with the
`lambda_max` form, never the `rbar` form, because the mean can understate the
spectral radius when alignment is concentrated in a cluster (three aligned
firms among ten orthogonal ones destabilise a subspace the mean barely sees).
The cluster case is worth a figure: it is the realistic topology - a vendor
with a plurality, not a monopoly.

**Theorem 2 (monoculture from a shared upstream model).** Model the AI supply
chain: each firm's response is `E_i = sqrt(s) E_shared + sqrt(1-s) Xi_i` with
`Xi_i` independent, where `s in [0,1]` is the fraction of the model attributable
to a shared foundation model, shared pretraining corpus or shared vendor. Then
`rbar = s + O(1/d)` and

```
   N_eff^align  =  1 + kappa s (N - 1) ,
```

so the **effective number of learners is the number of *independent* models,
not the number of firms**. A market with fifty dealers all fine-tuning one
vendor's model is, dynamically, a market with `1 + kappa*(50-1)*s` learners
where `s` is near one. This is the sentence that gets the paper accepted: it
converts "AI supply chain concentration" from a vague concern into a term in a
stability boundary. It also gives a **concentration boundary in `(N, s)`** - the
central figure.

**Theorem 3 (the monoculture externality and its price of anarchy).** Firms
choose a model provider. Adopting the market-leading model is individually
weakly dominant (it is the best-performing model on the shared benchmark, by
construction of "leading"), but it raises `s`, hence `N_eff^align`, hence the
instability all firms bear. Formalise as a population game over provider choice
with a payoff that is privately increasing in model quality and socially
decreasing in alignment. Prove:
  (a) the Nash equilibrium is monoculture (`s = 1`) whenever the quality gap
      exceeds a threshold that is *decreasing in `N`* - the precise mechanism
      being that a single firm's adoption raises `rbar` by `O(1/N)`, so the
      private share of the instability cost it creates vanishes as the market
      grows while the quality gain is constant: a textbook externality, and
      the reason the threshold is not assumption-free ("weakly dominant" is
      too strong a claim - adoption is dominant only once the private
      instability share is below the quality gap, which is what the threshold
      states);
  (b) the socially optimal configuration has `s* < 1` strictly, with `s*`
      characterised by the marginal-quality = marginal-instability condition;
  (c) a **price of anarchy in stability**, `rho(J)_Nash / rho(J)_opt =
      (1 + kappa(N-1)) / (1 + kappa s* (N-1))`, which grows linearly in `N`.
Then give the intervention: the minimal diversity requirement (a cap on `s`, or
a Pigouvian tax on shared-model adoption) that restores stability, in closed
form. This is the "ecosystem-level incentive design" bullet, discharged.

**Theorem 4 (spectral early warning, observable without seeing the models).**
Near `rho(J) -> 1` the system exhibits critical slowing down (REFLEX 1.3
section 8.3): the autocorrelation of the common mode of aggregate quotes tends
to 1 and its variance diverges as `1/(1 - rho)`. Therefore a regulator who
observes only *public prices* - not the models, not the training data, not the
firms' code - can estimate the ecosystem's distance to instability from the
principal-component structure of cross-dealer quote co-movement. Give the
estimator and its consistency. **This is the result that makes the paper
actionable and it is why it needs the real data.**

## E1.4 Why a NeurIPS-level reviewer accepts it

- It reframes a known concept (monoculture) with a new mathematical object
  (alignment-effective learner count) and derives a *different* conclusion than
  the existing literature: the harm is dynamical, not just distributional.
- Theorem 2 gives a policy-legible statement about foundation-model
  concentration that follows from a spectral computation, not from intuition.
- Theorem 4 makes it empirically checkable *from public data*, which is exactly
  the "empirical evidence" the CFP emphasises across both themes.
- REFLEX supplies a genuine `N`-agent simulator, not a toy: `env/multi_dealer.py`
  reduces bit-for-bit to the single-dealer market at `N = 1`, and the
  homogeneous predictions were already verified at `1.74x / 3.16x`.

**Anticipated objections and the answers.**
1. *"Alignment `rbar` is unobservable in practice."* Theorem 4 is the answer:
   the observable consequence (common-mode variance share) is estimable from
   prices. Say this in the introduction, not the appendix.
2. *"This is a market-making model, why should I care about ML ecosystems?"*
   Give the general statement first (any `N` learners sharing an induced
   distribution) and the market as the instantiation where the constants are
   computable. Add a one-paragraph second instantiation - recommender systems
   sharing a user pool, where `E_i` is the engagement-response Jacobian - so
   the reader sees the abstraction is real.
3. *"Isn't diversity obviously stabilising?"* Not obviously, and not always:
   the differential modes being *more* stable than a single agent
   (`-m_1(1-kappa)`, strictly smaller in magnitude than `-m_1`) is not
   intuitive, and the exact `lambda_max(R)` dependence says the relationship is
   spectral rather than monotone in any simple diversity index. Show a case
   where adding a firm with a *partially* anti-aligned response is worse than
   adding an orthogonal one.

## E1.5 Implementation plan

**New code.**

| Module | Contents | Size |
|---|---|---|
| `reflex/theory/monoculture.py` | `alignment_matrix(E_list)`, `n_eff_align`, `rho_bound`, `rho_exact`, `supply_chain_alignment(s, N)`, `adoption_equilibrium(...)`, `price_of_anarchy(...)`, `min_diversity_requirement(...)` - numpy only, matching the `theory/` convention | ~350 |
| `reflex/env/heterogeneous_dealers.py` | extends `env/multi_dealer.py` to per-dealer response parameters drawn to hit a target `rbar`; the shared-pool routing is unchanged | ~250 |
| `reflex/analysis/early_warning.py` | common-mode variance share, lag-1 autocorrelation of PC1, the distance-to-instability estimator | ~180 |
| `experiments/run_monoculture.py` | the four panels below | ~250 |
| `tests/test_monoculture.py` | `rbar = 1` reduces to 1.3's `N_eff`; simplex configuration gives `1 - kappa`; PoA formula; estimator consistency on synthetic data | ~200 |
| `reflex/verification/certificates.py` | +8 certificates (reduction to 1.3, eigenvalue identity, `lambda_max(R)` bounds, adoption-game FOC, early-warning consistency) | +100 |

**Experiments (four panels - this is a 9-page paper, it can carry four).**

1. **The `(N, s)` concentration boundary.** Heatmap of measured `rho(J)` over
   dealer count `N in {1..8}` and shared-model fraction `s in [0,1]`, with the
   Theorem 2 boundary overlaid. Expected: the stable region collapses as `s`
   rises, and at `s = 1` it reproduces the existing `1.74x / 3.16x` numbers -
   which is a *validation checkpoint against an already-published run*, and
   worth saying so.
2. **Diversity buys stability.** At fixed `N` and `epsilon` beyond the
   monoculture boundary, sweep `rbar` down and show the loop crossing back into
   convergence. The single most persuasive dynamic figure: the same market,
   same feedback gain, same number of firms, stable or unstable purely as a
   function of how correlated the models are.
3. **The adoption game.** Nash `s` vs socially optimal `s*` as the quality gap
   varies; the price of anarchy growing in `N`; the minimal intervention curve.
4. **Real-data early warning.** Using the 212-CUSIP monthly panel and the
   36-year macro series already in `research/data_collection/`, compute the
   PC1 variance share and lag-1 autocorrelation of cross-sectional spread
   co-movement through 1990-2026 and overlay the fragility index from
   `analysis/fragility.py`. Expected: co-movement concentration rising into the
   GFC and the COVID freeze.

   **Be careful and be honest here.** This measures co-movement of *bond
   returns/spreads*, which is a proxy for common-mode dynamics and is
   contaminated by common macro shocks - it is *not* a measurement of model
   alignment, and the data is not trade-level TRACE (see
   `data_collection/docs/REJECTED_SOURCES.md`). State that plainly, present it
   as consistency evidence for Theorem 4's observable rather than as
   identification of monoculture, and add the placebo: the same statistic on
   Treasury/macro series, where no dealer-model channel exists. A reviewer who
   catches an overclaim here will reject the paper; a reviewer who sees the
   placebo pre-empted will trust the rest.

**Reuse.** `theory/multi_dealer.py` (the entire spectral apparatus,
`joint_jacobian`, `n_eff`, `common_mode_probe`, `measure_differential_modulus`),
`theory/factor_scaling.py` (the `d`-dimensional modulus matrix and the Woodbury
reduction that keeps `Nd x Nd` tractable), `env/multi_dealer.py`,
`analysis/fragility.py`, the calibration layer.

**Effort: 6-9 days.**

**Page plan (9 pages).** 1p introduction and the monoculture reframing;
1p related work (monoculture, performative prediction, multi-agent learning -
this audience expects named-author related work); 1.5p model; 2p Theorems 1-4
with proof sketches; 2.5p experiments (four panels); 0.5p policy discussion;
0.5p limitations. Appendix: full proofs, the exact-eigenvalue derivation, the
placebo study, certificate listing, robustness to `kappa` misspecification.

---
---

# E2. Involuntary Algorithmic Collusion: supra-competitive pricing with no intent, no communication, and no reward for it

**One line.** Competing firms that retrain on their own induced data converge to
prices strictly above the competitive performative optimum, the markup *grows*
with the number of competitors, and it is separable from genuine tacit collusion
by a comparative-statics test a regulator can run.

**Format.** Long (9 pages).

**CFP fit.** "Algorithmic collusion among learning systems" (verbatim);
"Competition between AI service providers"; "Multi-agent learning dynamics in
economic environments"; "AI decision making and bias in economic contexts";
"Ecosystem-level incentive design".

## E2.1 The gap

The algorithmic-collusion literature (Calvano-Calzolari-Denicolo-Pastorello,
AER 2020, and successors) shows Q-learning pricing agents learn
reward-punishment schemes that sustain supra-competitive prices. The mechanism
is *strategic*: it requires the agents to condition on rivals' past actions and
to learn punishment. That mechanism has been contested precisely because it
depends on the learning algorithm's memory structure.

REFLEX exhibits a completely different and much more robust route to the same
outcome. From `02-perfgd-correction.md` (6a), the blind stable point satisfies

```
   h_SP - h_PO  =  beta * epsilon * (h_SP - psi) / ( gamma + beta * epsilon )  >  0
                   whenever  h_SP > psi ,
```

that is, **a retraining firm quotes strictly wider than optimal because, blind
to the fact that its own tightening would summon the flow it would profit
from, it never credits itself for that flow**. No memory, no conditioning on
rivals, no punishment, no intent. Pure informational blindness, and it is a
markup.

With `N` competitors sharing a pool the toxic level per dealer scales with
`N_eff = 1 + kappa(N-1)`, so `epsilon_N = N_eff * epsilon` and the markup is
increasing in `N`. **More competitors, wider spreads** - the exact reverse of
the standard oligopoly prediction, and a genuinely striking claim.

## E2.2 The honest complication, which is also the contribution

REFLEX's multi-dealer model assumes captured benign franchises (assumption A5'
in `03-multi-dealer-systemic-risk.md`): each dealer's uninformed flow responds
to its *own* spread only. Under that assumption there is no Bertrand force
pushing spreads down, so "more competitors, wider spreads" is not yet a fair
claim - it is an artefact of the modelling choice, and a referee will say so
immediately.

**So the paper's first job is to remove A5'.** Add competitive splitting of
benign flow - a logit/Bertrand share `u_i(h) = A e^{-k h_i} / sum_j e^{-k h_j}`
style allocation - which adds own-`h` curvature (raising `gamma`, stabilising)
and a genuine downward price force. Then the net effect of adding a competitor
decomposes into two terms with opposite signs:

```
   d h_SP / dN  =  [ competitive term  <  0 ]  +  [ performative echo term  >  0 ]
```

and the result becomes a **critical spillover `kappa*`** above which the echo
term dominates and the spread-vs-`N` curve turns non-monotone: spreads first
fall with competition, then rise. That is a far better paper than the naive
version - it is falsifiable, it has a knife-edge, and the knife-edge is a
function of an economically meaningful primitive.

## E2.3 The theorems

**Theorem 1 (the echo-chamber markup with competition).** With benign-flow
competition restored, derive `h_SP(N, kappa, epsilon) - h_PO(N, kappa, epsilon)`
in closed form and show it is (a) strictly positive whenever `h_SP > psi`,
(b) increasing in `kappa` and `epsilon`, (c) increasing in `N` iff
`kappa > kappa*`, with `kappa*` given explicitly in terms of the benign
demand elasticity `k` and the toxic decay `c_t`. Interpretation: the echo
dominates when informed flow is more mobile across dealers than uninformed
flow, which is exactly the empirically plausible case.

**Theorem 2 (welfare decomposition).** Client surplus loss decomposes into a
competitive component and a performative component; the performative component
is `O(epsilon)` in the price and `O(epsilon^2)` in dealer value - so **clients
bear a first-order loss from an effect that costs dealers only second-order
value.** Dealers have weak private incentive to fix it; clients bear the cost.
That asymmetry is the incentive-design hook and the reason the paper has a
policy section rather than a shrug.

**Theorem 3 (un-blinding is pro-competitive).** If firms adopt the corrected
(PerfGD) update - i.e. they get *better* at modelling their own market impact -
the markup vanishes and spreads *narrow*. This is a rare and quotable
inversion: in the tacit-collusion literature smarter algorithms collude better;
here smarter algorithms compete better. State the precise scope: it holds for
the first-order correction under the conditions of `02` section 4.3, and it is
not a claim that sophistication is always pro-social. REFLEX's structural loop
gives the empirical version - `perfgd_structural` settles strictly *inside* the
blind stable point, which is exactly this effect measured
(`research/results/07-12-2026/REPORT.md`).

**Theorem 4 (identification: telling the two mechanisms apart).** The regulator
observes prices and flows, not algorithms. Show that performative markup and
tacit collusion have different comparative statics:

| | performative echo | tacit collusion |
|---|---|---|
| response to a shock that raises `epsilon` (e.g. faster information leakage) | markup rises | ~unchanged |
| response to mandated un-blinding | markup falls to zero | unchanged |
| response to rising concentration at fixed `kappa` | governed by `kappa` vs `kappa*` | rises |
| dependence on rivals' *past* actions | none | required |

Build a test statistic on the first row using a real instrument: **TRACE
dissemination-delay changes are an actual FINRA policy lever that shifts
information leakage**, so there is a natural experiment shape here even if the
data to run it is not in hand. Prove identification under stated exclusion
restrictions, and be explicit that the empirical execution needs trade-level
TRACE (WRDS access pending, per
`data_collection/docs/REJECTED_SOURCES.md`) - propose the design, run it in
simulation, and say plainly that the real-data version is future work. A
well-specified test with a simulated power study is a legitimate contribution;
a hand-waved empirical claim is not.

## E2.4 Implementation plan

**New code.** `reflex/env/competitive_flow.py` (logit benign-flow allocation
across dealers, replacing A5' - the one genuinely new modelling component),
`reflex/theory/collusion.py` (markup closed forms, `kappa*`, welfare
decomposition, the detection statistic and its power),
`experiments/run_collusion.py`, `tests/test_collusion.py`, plus certificates
(reduction to A5' at zero benign competition; markup sign; `kappa*` crossing).

**Experiments.** (1) Spread vs `N` at several `kappa`, showing the
non-monotone turn at `kappa*` - the headline figure. (2) Markup vs `epsilon`
against the closed form. (3) Blind vs structural-PerfGD spreads at matched
`N` - Theorem 3 measured. (4) Detection-test power curves under simulated
`epsilon` shocks, with a collusive-Q-learning arm as the alternative
hypothesis, so the test is shown to discriminate rather than merely to fire.

**Reuse.** `theory/perfgd.py` (`echo_chamber_gap`), `theory/multi_dealer.py`,
`env/multi_dealer.py`, `equilibrium/loops.py` (all four modes, especially
`perfgd_structural` for Theorem 3).

**Effort: 7-10 days.** Shares E1's entire simulation layer; if E1 is built
first, the marginal cost is the competitive-flow module plus the detection test
(~4 days). **Submitting E1 and E2 together as two papers from one build is the
most efficient use of the runway** - but only if both are genuinely finished;
one strong paper beats two thin ones at a workshop with a 9-page allowance.

---
---

# E3. Endogenous Performativity: two routes from retraining to market breakdown

**One line.** Micro-found the performative response from optimising agents on
both sides of the market and a second, qualitatively different failure mode
appears - not the oscillatory divergence of the retraining cobweb but a fold
bifurcation with multiple equilibria and hysteresis, i.e. a liquidity black
hole produced by a learning loop.

**Format.** Long (9 pages). **This is the most scientifically ambitious idea in
the folder and the most likely to become a standalone main-track paper. It is
deliberately not on the 13-day slate.**

## E3.1 The gap

REFLEX's toxic response `tau(h) = rho gbar (I_b + alpha f I e^{-c_t h})` is
reduced-form: informed flow is a mechanical function of the quoted spread. Every
performative-prediction paper does the equivalent - the distribution map
`D(phi)` is an assumed primitive. But in an economic setting the distribution
map is *itself* an equilibrium object: agents choose whether to acquire
information and whether to participate, best-responding to the deployed policy.
Making `epsilon` endogenous is the natural economics upgrade and it changes the
phenomenology, not just the constants.

## E3.2 The formalism and the two channels

Two agent populations, each with a participation margin:

- **Informed traders** pay `c_I` to acquire a signal and trade if expected
  profit `>= 0`. Free entry pins the informed mass `mu(h)`: tighter spreads
  raise informed profit, so `mu` is decreasing in `h`. The realized toxic flow
  becomes `tau(h) = mu(h) * (per-trader flow)`, and

  ```
     epsilon_endo  =  epsilon_exo  +  |d mu / dh| * (per-trader flow)   >  epsilon_exo .
  ```

  **Reduced-form models systematically understate performative sensitivity.**
  This channel is *negative* feedback (wider quotes drive informed traders out),
  so it steepens the cobweb: it moves the market toward the `m = 1` boundary
  and the existing oscillatory instability.

- **Uninformed clients** participate if the round-trip cost is below their
  outside option, so the arrival scale `A` becomes `A(h)`, decreasing in `h`.
  This is *positive* feedback: wider spreads drive benign clients away, which
  thins the market, which raises the toxic share, which makes the dealer widen
  further. REFLEX already contains the machinery (`env/liquidity_field.py`, the
  `liq_overtighten_decay` channel) but treats it as a dynamical nuisance rather
  than an equilibrium selection mechanism.

The two channels do different things to the self-consistency map, and that is
the paper:

```
   informed-entry channel   ->  steepens the negative-slope cobweb  ->  slope crosses -1
                                ->  oscillatory divergence  (REFLEX's existing instability)

   benign-exit channel      ->  adds positive feedback to the map    ->  slope crosses +1
                                ->  saddle-node fold: multiple equilibria, hysteresis,
                                    catastrophic jumps  (a NEW failure mode)
```

## E3.3 The theorems

**Theorem 1 (endogenous `epsilon` strictly exceeds reduced-form `epsilon`).**
Under a Grossman-Stiglitz-style free-entry condition, with the amplification
factor in closed form. Corollary: every published stability boundary calibrated
on a reduced-form response is optimistic, by a factor that is computable from
the entry elasticity.

**Theorem 2 (the fold, and the two-route phase diagram).** With endogenous
benign participation of elasticity `eta_A`, the self-consistency map
`h = BR(h)` has slope `+1` somewhere iff `eta_A` exceeds an explicit threshold
in terms of `(k, c_t, gamma, epsilon)`; at that point the market has three
equilibria (liquid, unstable middle, illiquid) and the outer branches are
attracting. Give the full phase diagram in `(epsilon, eta_A)` with three
regions - **stable / oscillatory-unstable / bistable** - and show the two
instabilities are genuinely distinct: one is a period-doubling-flavoured
divergence, the other a saddle-node. To our knowledge no performative-prediction
paper has exhibited a fold; the literature's failure mode is uniformly
"the iteration does not contract".

**Theorem 3 (hysteresis and irreversibility).** Ramping `epsilon` up past the
fold and back down does not retrace: the market jumps to the illiquid branch and
stays there until `epsilon` falls well below the jump point. Quantify the
hysteresis width. This is the formal content of "liquidity black hole" and it is
a *policy* result: an intervention sized to the level at which the market broke
will not be enough to restore it.

**Theorem 4 (unification with strategic classification).** The informed
trader's problem - pay a cost to change how a decision-maker treats you, where
the decision-maker retrains on the resulting data - is structurally the
strategic-classification problem. Show REFLEX's boundary is the special case of
a general condition

```
   (agent best-response elasticity) x (decision-rule sensitivity)  <  (objective curvature)
```

covering strategic classification with retraining and performative market
making in one statement, and note that the strategic-classification literature
has studied the *static* Stackelberg equilibrium far more than the *dynamics of
repeated retraining against strategic agents*. This lands the "Strategic
classification" bullet in Theme 1 while the rest of the paper lives in Theme 2.

## E3.4 Implementation plan

**New code (this is the big build).** `reflex/env/strategic_clients.py`
(informed free-entry solver, benign participation margin),
`reflex/theory/endogenous.py` (endogenous `epsilon`, the fold condition,
equilibrium enumeration by continuation, hysteresis width),
`experiments/run_bifurcation.py` (numerical continuation over `epsilon` with
branch tracking), tests and certificates.

**Experiments.** (1) The `(epsilon, eta_A)` phase diagram with the three
regions, simulated and predicted. (2) The hysteresis loop: ramp `epsilon` up
and down, plot the spread path, show the jump and the non-retracing return -
this figure alone carries the paper. (3) Endogenous vs reduced-form boundary on
the calibrated regime configs, quantifying how optimistic the published
boundary is. (4) The strategic-classification instantiation as a sanity check
that Theorem 4's general condition reproduces the known static result.

**Effort: 14-21 days.** Aim at NeurIPS 2027 main track, ICML, or a finance
journal, with a 9-page EconML version as the first public airing if the
timeline allows.

---
---

# E4. Is the Corporate Bond Market Becoming a Monoculture? (short paper)

**One line.** A purely empirical 4-page companion: build a monoculture
indicator from 36 years of public bond and macro data and show its co-movement
with the model-implied fragility index.

**Format.** Short (4 pages). Zero new theory. **Only worth submitting if E1 is
not ready** - as a standalone it is thin for this audience, but as a fallback it
is genuinely publishable and it is 3-4 days of work.

**Contents.** The PC1 variance share and lag-1 autocorrelation of
cross-sectional spread co-movement on the 212-CUSIP panel, 1990-2026; the
REFLEX fragility index overlaid; the placebo on Treasury/macro series; the
honest provenance caveat about non-trade-level TRACE stated in the abstract,
not buried.

**Do not overclaim.** The statistic is consistent with rising common-mode
dynamics; it does not identify model monoculture, and no amount of framing makes
it do so. Presented as "here is an observable the theory predicts should move,
and it moves", it is a fine short paper. Presented as evidence that dealers use
the same models, it is indefensible.

---
---

# Cross-cutting notes for EconML

**Equilibrium concepts, stated explicitly.** This audience distinguishes
carefully between: the performatively stable point (RRM fixed point), the
performative optimum, the PSNE of the `N`-dealer game, and the Nash equilibrium
of the model-adoption game in E1. REFLEX's documents are precise about the
first three; E1 adds the fourth. Define all of them in the model section and
never let two of them share a symbol.

**Welfare.** Every idea needs one welfare statement. E1: the instability
externality and its price of anarchy. E2: the client-surplus decomposition and
the dealer/client asymmetry. E3: the irreversibility of the illiquid branch.
Do not leave welfare to the discussion section - this audience treats it as
part of the result.

**Identification.** Same rule: E1 Theorem 4 (observable from prices), E2
Theorem 4 (the comparative-statics test), E3 (the entry elasticity is estimable
from participation data). An ML audience accepts a simulation; this audience
asks how you would know.

**Related work must be named-author and economics-literate.** Perdomo et al. on
performative prediction; Izzo et al. on PerfGD; Brown et al. and Narang et al.
on multiplayer performativity; Hardt-Megiddo-Papadimitriou-Wootters and
successors on strategic classification; Kleinberg-Raghavan and Bommasani et al.
on monoculture; Calvano et al. on algorithmic collusion; Grossman-Stiglitz on
information acquisition; Glosten-Milgrom and Kyle on adverse selection;
Brunnermeier-Pedersen on liquidity spirals; Guéant-Lehalle-Fernández-Tapia and
Barzykin et al. for the market-making structure. `literature/literature-raghav/`
already holds 18 of these with per-paper notes and a verified `references.bib` -
but note the `CLAUDE.md` warning that two arXiv IDs in those bibs were wrong and
were corrected in `research/paper/references.bib`; copy from the corrected one.

**Double-blind mechanics.** Strip the author block and the repository footnote;
cite the ICAIF submission in third person; check figure metadata and PDF
producer strings; do not name the repository in captions or file paths shown in
the paper.
