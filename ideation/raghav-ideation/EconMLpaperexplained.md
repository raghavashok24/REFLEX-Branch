# The EconML Paper, Explained

## "Algorithmic Monoculture as Dynamical Instability: the Effective Number of Independent Models"

**Venue:** EconML workshop @ NeurIPS 2026 (Atlanta, Dec 12/13). Submit by
**Aug 29, 2026**. Format: long paper, 9 pages main content, unlimited
references and appendix. **Double-blind.** In-person presentation required.

---

## 1. The idea in one paragraph

The algorithmic-monoculture literature says that when many firms use the same
model, *outcomes* correlate — the same applicants get rejected everywhere, and
welfare falls. That is a static story. This paper asks what monoculture does
to systems that **retrain**: many firms, each deploying a learned policy that
reshapes a shared environment, each refitting on the data its own deployment
generated. The answer is sharper than the static story and different in kind:
monoculture aligns the *feedback directions* of the learners, and aligned
feedback resonates. We prove that the stability of the whole ecosystem is
governed not by the number of firms `N` but by the **effective number of
independent models** — the leading eigenvalue of the correlation matrix of
the firms' performative responses. Fifty dealers fine-tuning one vendor's
foundation model are, dynamically, close to *one* very large learner, and the
market they share inherits that learner's instability. From this we get a
concentration boundary in (number of firms) x (shared-model fraction), an
adoption game showing every private incentive pushes toward the unstable
configuration, a price of anarchy in stability that grows with market size,
and — the part that makes it governable — an early-warning statistic a
supervisor can compute from public prices alone, without access to any firm's
model.

## 2. Why this venue wants it

EconML's Theme 2 ("Ecosystems with many interacting models") lists, verbatim:
*"Algorithmic monoculture and model multiplicity"*, *"Feedback loops and
performative prediction effects"*, *"Market concentration among AI service
providers"*, *"AI supply chains and their dynamics"*, *"Multi-agent learning
dynamics in economic environments"*, and *"Ecosystem-level incentive design"*.
This paper hits all six with one model. It also carries the three things an
economics-literate audience demands and pure-ML submissions usually lack: an
explicit equilibrium analysis (four distinct equilibrium concepts, kept
distinct), a welfare statement (the instability externality and its price of
anarchy), and an identification argument (what an outside observer can and
cannot infer, with a placebo design on real data).

## 3. Background you need (two paragraphs)

**Performative prediction and the base project.** When a deployed model
reshapes its own training distribution, "retrain on the induced data"
converges iff a modulus `m = epsilon*beta/gamma < 1` (Perdomo et al., 2020).
REFLEX (the base project) instantiates this inside a structural OTC
market-making model where the constants are computed from microstructure
primitives, and proves the multi-firm version for *identical* dealers sharing
one pool of informed flow: the joint retraining map has Jacobian

```
   J = -m_1 [ (1 - kappa) I  +  kappa 1 1^T ]
```

whose spectrum splits into a **common mode** (all dealers move together) with
eigenvalue `-m_1 (1 + kappa(N-1))` and **differential modes** (dealers move
against each other) with eigenvalue `-m_1 (1 - kappa)`. The common mode
dominates: the market destabilizes a factor `N_eff = 1 + kappa(N-1)` before
any single dealer would. This was verified in a genuine N-dealer simulator —
measured amplification 1.74x at N=2 and 3.16x at N=3 against predicted 2 and
3. Here `kappa in [0,1]` is the spillover: how much one firm's deployment
contaminates the flow its competitors face.

**Monoculture.** Kleinberg–Raghavan showed monoculture can reduce welfare
even when the shared algorithm is the *better* one; Bommasani et al.
documented outcome homogenization from shared foundation models. Both are
static and cross-sectional. Multiplayer performative prediction (Brown et
al., Narang et al.) has dynamics but homogeneous couplings — everyone is the
same learner. The missing square, and this paper, is: dynamics x
heterogeneous learners x who-buys-which-model.

## 4. The model

`N` firms, each deploying a learned policy over a `d`-dimensional decision
(in the market instantiation: `d` bonds' half-spreads). The object that
carries everything is each firm's **response Jacobian** `E_i` (a `d x d`
matrix): how firm `i`'s own deployment reshapes the flow it faces. Firms
share the environment through the spillover `kappa`, exactly as in the
homogeneous theory. The joint retraining Jacobian `J` has blocks built from
`Gamma_i^{-1} beta E_j` (own-curvature-discounted responses, own and
spilled-over).

The new objects are the alignment statistics of the responses:

```
   r_ij  =  <vec(E_i), vec(E_j)> / (||E_i||_F ||E_j||_F)     pairwise alignment
   R     =  (r_ij)                                            the alignment matrix
```

`R` is a correlation matrix of *models' feedback directions*. Its leading
eigenvalue `lambda_max(R)` runs from 1 (all responses orthogonal — every firm
perturbs the environment in its own direction) to `N` (monoculture — all
firms perturb it identically). We call it **the effective number of
independent models**.

For the supply chain, decompose each firm's response into a shared and an
idiosyncratic component:

```
   E_i  =  sqrt(s) * E_shared  +  sqrt(1-s) * Xi_i ,
```

where `s in [0,1]` is the fraction of the model attributable to a shared
foundation model, vendor, or pretraining corpus, and the `Xi_i` are
independent. Then the pairwise alignments concentrate at `r_ij ~ s`, so
`lambda_max(R) ~ 1 + s(N-1)`.

## 5. The results, each explained

### Theorem 1 — Diversity-stability: alignment is the systemic variable

**(a) Equal moduli, heterogeneous directions.** If all firms have the same
single-firm modulus `m` but their response *directions* differ, the joint
spectral radius is exactly

```
   rho(J)  =  m * ( 1 + kappa ( lambda_max(R) - 1 ) ) ,
```

so the ecosystem is stable iff
`epsilon < (gamma/beta) / (1 + kappa(lambda_max(R) - 1))`.

*Why it holds:* the coupling structure makes `J` a Gram-type perturbation of
a scaled identity; its spectrum is controlled by the spectrum of `R`, and the
rank-structure argument of the homogeneous case generalizes with `lambda_max`
replacing `N`. Sanity anchors, each checked independently: monoculture
(`R = 1 1^T`, `lambda_max = N`) recovers the published `N_eff = 1 +
kappa(N-1)` and its measured 1.74x/3.16x amplification; orthogonal responses
(`R = I`) give `rho = m` — a hundred firms perturbing the environment in a
hundred orthogonal directions are, dynamically, one firm; and the maximally
diverse configuration (mean alignment `-1/(N-1)`, responses forming a
simplex) gives `1 - kappa`, which exactly matches the differential-mode
eigenvalue derived in the homogeneous theory by a completely different route.
Two independent derivations landing on the same number is the kind of
consistency this project's verification layer exists to certify.

**(b) Heterogeneous moduli — and an honest scope line.** A tempting cleaner
statement — replace `m` with the *mean* modulus — is provably false:
orthogonal responses decouple the firms, so the radius is `max_i m_i`, not
the mean. The correct general object is the modulus-weighted Gram matrix
`M^{1/2} R M^{1/2}` (`M = diag(m_i)`), which yields an upper bound that is
exact in the equal-modulus and zero-spillover limits; its tightness is
measured in simulation. Practical consequence, stated as a rule: **all
stability claims use the spectral form, never the mean alignment** — because
mean alignment understates *clustered* alignment. Three tightly-aligned firms
among ten otherwise-orthogonal ones destabilize a subspace that the mean
barely registers. That clustered case — a vendor with a plurality, not a
monopoly — is the realistic topology, and it gets its own experiment.

*Why it matters:* "model diversity" stops being a vague virtue and becomes a
systemic-risk control variable with a closed-form price. And the naive
diversity index a policymaker would reach for (average pairwise similarity)
is shown to be the wrong one — the spectrum is the right one.

### Theorem 2 — The concentration boundary: firms vs independent models

Under the supply-chain decomposition, the stability boundary becomes

```
   epsilon  <  gamma / ( beta * (1 + kappa * s * (N - 1)) ) .
```

*Why it holds:* substitute `lambda_max(R) ~ 1 + s(N-1)` (concentration of
the alignment statistics over the `d^2` matrix entries; the `O(1/d)`
correction is stated) into Theorem 1(a).

*Why it matters:* **the effective number of learners is the number of
independent models, not the number of firms.** At `s ~ 1`, fifty dealers are
dynamically `~ 1 + 49*kappa` learners; at `s ~ 0`, barely more than one. This
converts "foundation-model concentration risk" — currently a rhetorical
concern in AI-policy discussions — into a specific term in a stability
condition, and yields the paper's central figure: the stable region in the
`(N, s)` plane, collapsing as the shared-model fraction rises.

### Theorem 3 — The adoption game: monoculture is a Nash equilibrium

Why would an ecosystem end up at high `s`? Because every private incentive
points there. Model provider choice as a population game: adopting the
market-leading model yields a private quality gain `q`; it also raises the
ecosystem's alignment — but a single firm's adoption moves the average
alignment by only `O(1/N)`, so the *private share* of the instability cost a
firm creates vanishes as the market grows, while its quality gain does not. A
textbook externality. We prove:

- **(a)** Nash equilibrium is full monoculture whenever the quality gap
  exceeds a threshold that is *decreasing in market size* — the bigger the
  market, the smaller the quality edge needed to tip everyone into the same
  model.
- **(b)** The social optimum keeps an interior diversity level `s* < 1`,
  characterized by marginal quality = marginal instability.
- **(c)** The **price of anarchy in stability** — the ratio of the
  equilibrium spectral radius to the socially optimal one — is
  `(1 + kappa(N-1)) / (1 + kappa s*(N-1))`, growing linearly in `N`.
- **(d)** The minimal intervention that restores stability (a diversity floor
  or a Pigouvian charge on shared-model adoption) in closed form.

*Why it matters:* this is the "ecosystem-level incentive design" bullet of
the CFP discharged with an actual mechanism, and it explains why the unstable
configuration is not an edge case but the *destination* of unregulated
adoption dynamics.

### Theorem 4 — Early warning from public prices

Everything above involves `R`, which no outsider observes — supervisors do
not get to inspect firms' models. But near the boundary the system tells on
itself: as `rho(J) -> 1`, the *aligned* combination of the firms' decisions
exhibits critical slowing down — the lag-1 autocorrelation of the leading
principal component of cross-firm decisions (quotes) tends to one, and its
variance share grows like `1/(1 - rho)`. So a supervisor observing only
public prices can estimate the ecosystem's distance to instability, with no
access to any model, any training set, or any firm's code. We give the
estimator and prove its consistency under the linearized dynamics.

*Why it matters:* it is the difference between a theory of a problem and a
theory a regulator can act on. It also supplies the paper's empirical leg.

## 6. The experiments

Four panels, all in the base project's genuine N-dealer simulator (which
reduces bit-for-bit to the single-dealer market at N=1), CPU-only,
deterministic:

1. **The `(N, s)` phase diagram** — measured joint modulus over firms x
   shared-model fraction, with the Theorem 2 boundary overlaid. The `s = 1`
   column must reproduce the already-published 1.74x/3.16x numbers: an
   external validation checkpoint against a prior curated run. Companion
   panel: the *clustered* topology (three aligned firms among ten),
   demonstrating instability at mean-alignment values the naive index calls
   safe.
2. **Diversity buys stability** — fix `N` and the feedback gain beyond the
   monoculture boundary, then decorrelate the firms' responses. Same market,
   same feedback strength, same number of firms: divergent at high alignment,
   convergent at low. The single most persuasive dynamic figure.
3. **The adoption game** — Nash vs socially optimal `s` across quality gaps;
   price of anarchy against `N`; the minimal-intervention curve.
4. **Real-data early warning** — the PC1 variance share and lag-1
   autocorrelation of cross-sectional spread co-movement on the project's
   212-CUSIP corporate-bond panel, 1990–2026, overlaid on its model-implied
   fragility index (which collapses ~4.4x from calm to crisis). Expected:
   co-movement concentration rising into the GFC and the COVID freeze.
   **Framed honestly as consistency evidence, not identification**: spread
   co-movement is contaminated by common macro shocks and the data is not
   trade-level TRACE; the claim is only that the observable the theory says
   should move, moves. A placebo on Treasury/macro series (where no
   dealer-model channel exists) is run and reported alongside.

## 7. What is genuinely new

- **The reframing itself**: monoculture's harm relocated from static
  allocation welfare to dynamical stability — a market can be statically
  fine and dynamically fragile at the same shared-model fraction, and
  experiment 2 exhibits exactly that.
- **The effective number of independent models** (`lambda_max` of the
  response-alignment matrix) as the systemic-risk variable, with the exact
  equal-moduli identity, the weighted-Gram general bound, and the
  clustered-alignment counterexample that invalidates mean-similarity
  indices.
- **The supply-chain stability boundary** in `(N, s)` — foundation-model
  concentration as a term in a stability condition rather than a talking
  point.
- **A price of anarchy in a dynamical-stability metric** for model adoption,
  plus the closed-form minimal intervention.
- **The supervisor-side observable**: distance-to-instability estimable from
  public prices with a consistency proof and a real-data + placebo design.

Non-overlap with the project's own conference paper (a concurrent ICAIF
submission, cited in third person under double-blind): that paper's
multi-dealer result is the homogeneous special case (`R = 1 1^T`) and carries
no alignment object, no supply chain, no adoption game, no welfare statement,
no observability result. This paper validates against its published numbers
and builds strictly above them.

## 8. Honest limitations (stated in the paper)

- The spectral theory is a linearization around the joint equilibrium; the
  simulator experiments are the nonlinear check.
- The exact identity is proved for equal moduli; the general case is a bound
  whose tightness is measured, not asserted.
- Alignment `R` is not directly observable — Theorem 4 is the designed
  answer, and its real-data panel is consistency evidence with a placebo,
  not identification of monoculture.
- The market instantiation carries the base project's data provenance caveat
  verbatim: public proxies, not trade-level TRACE.

## 9. Build plan (submission Aug 29; ~13 days)

- **Aug 16–17:** the theory module (`monoculture.py`: alignment matrix,
  exact identity, weighted-Gram bound, supply-chain map, adoption game, PoA,
  intervention) + numerical certificates; prove Theorem 1(a).
- **Aug 18–19:** heterogeneous-dealer environment (per-firm response
  parameters hitting a target `R`, including clustered topologies; must
  reduce to the existing homogeneous environment when `R = 1 1^T` — that
  reduction is a test) + experiment 1.
- **Aug 20–21:** experiment 2; adoption game + experiment 3.
- **Aug 22:** early-warning estimator + experiment 4 + placebo.
- **Aug 23–25:** write the 9 pages (intro, named-author related work, model
  with the four equilibrium concepts kept typographically distinct, theorems
  with sketches, panels, policy, limitations); proofs to the appendix.
- **Aug 26–27:** review against this document; **anonymization pass** (no
  author block, no repo URL anywhere, third-person citation of the
  concurrent submission, scrubbed PDF metadata and figure paths).
- **Aug 28:** freeze and buffer. **Aug 29:** submit.

De-scope order if time runs short: the intervention curve, then the
consistency proof of Theorem 4 (keep the estimator and simulation), then the
clustered panel. Never cut experiment 2 or the placebo. Fallback if the exact
identity resists proof in time: ship the bound plus machine-precision
numerical equality on the equal-moduli grid, worded accordingly.
