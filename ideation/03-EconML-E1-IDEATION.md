# Submission pack: EconML @ NeurIPS 2026

## "Algorithmic Monoculture as Dynamical Instability: the Effective Number of Independent Models"

**Deadline Aug 29 2026 (AOE). Long format: 9 pages main content, unlimited
references + appendix. DOUBLE-BLIND. Non-archival; in-person presentation
required.**

Complete ideation, audited 2026-08-16 (`../ASSUMPTIONS-AUDIT.md`, items A2,
A4, P6-P8; the two defects found in the original spec are fixed here).

---

## 1. Thesis and positioning

**Thesis sentence.** Monoculture is known to correlate *outcomes*; we show
that in systems that retrain on the data their own decisions generate, it
aligns the *feedback directions* of the learners - and aligned feedback
resonates, so the systemic-risk variable is not the number of firms but the
effective number of independent models.

**CFP mapping (verbatim bullets hit).** Theme 2: "Algorithmic monoculture and
model multiplicity"; "Feedback loops and performative prediction effects";
"Market concentration among AI service providers"; "Multi-agent learning
dynamics in economic environments"; "AI supply chains and their dynamics";
"Ecosystem-level incentive design". Emphases: "insights across scales"
(model-level alignment -> market-level stability) and "empirical evidence"
(panel 4).

**Against the literature.** Kleinberg-Raghavan: monoculture can lower welfare
even when the shared algorithm is the more accurate one - static, allocation
outcomes. Bommasani et al.: outcome homogenization from shared foundations -
empirical, cross-sectional. Multiplayer performative prediction (Brown et al.;
Narang et al.; Piliouras-Yu): dynamics of coupled learners, but homogeneous
couplings and no supply-chain structure, no adoption game, no observability
result. This paper is the missing square: *dynamics x heterogeneity x who-buys-
which-model*. Related work must be named-author prose (this audience's
convention), drawn from `literature/literature-raghav/references.bib` -
**copy entries only from `research/paper/references.bib`** (two arXiv IDs in
the literature bibs are known-wrong and were corrected there).

**The economics content (the register test this venue applies).**
- Equilibrium concepts, four, kept typographically distinct: performatively
  stable point (single learner), PSNE of the quoting game (1.3), Nash
  equilibrium of the *adoption* game (new, over model choice), social optimum.
- Welfare: the instability externality; price of anarchy in stability.
- Identification: an observable (price co-movement spectrum) estimable without
  access to any firm's model, with a placebo design.

## 2. Model (~1.5 pages)

`N` firms, each deploying a learned policy over a `d`-dimensional decision
(REFLEX: `d` bonds' half-spreads). Firm `i`'s response Jacobian
`E_i in R^{d x d}`: how its own deployment reshapes the flow it faces. Shared
environment with spillover `kappa in [0, 1]` (1.3's toxic pool). Joint
retraining Jacobian `J`, blocks `J_ij = -Gamma_i^{-1} beta E_ij`,
`E_ii = E_i`, `E_ij = kappa E_j`-routed via the pool.

**The alignment objects.**

```
   r_ij = <vec E_i, vec E_j> / (||E_i||_F ||E_j||_F)      pairwise alignment
   R    = (r_ij)                                           alignment matrix (PSD)
   M    = diag(m_1, ..., m_N)                              single-firm moduli
```

Headline quantity: `lambda_max(R)` = **the effective number of independent
models** (equals `N` at monoculture, `1` when responses are orthogonal;
`>= 1 + (N-1) rbar` with equality iff equicorrelated).

**Supply chain.** `E_i = sqrt(s) E_shared + sqrt(1-s) Xi_i`, independent
idiosyncratic `Xi_i`, common component `s` = the fraction of the model
attributable to a shared foundation model / vendor / pretraining corpus.
Then `r_ij -> s` (concentration over the `d^2` entries), so
`lambda_max(R) ~ 1 + s(N-1)`.

## 3. Results

**Theorem 1 (diversity-stability, two-tier scope - post-audit form).**
(a) *Equal moduli (`m_i = m`), heterogeneous directions:* exact identity

```
   rho(J) = m * ( 1 + kappa (lambda_max(R) - 1) ) ,
```

stable iff `epsilon < gamma / beta * 1 / (1 + kappa(lambda_max(R) - 1))`.
Sanity anchors, all verified against 1.3: `R = 1 1^T` recovers
`N_eff = 1 + kappa(N-1)` (and the measured `1.74x / 3.16x` amplification);
`R = I` gives `rho = m` (decoupled); maximally diverse
(`rbar = -1/(N-1)`, simplex) gives `1 - kappa`, matching 1.3's
differential-mode modulus computed by a different route.
(b) *Heterogeneous moduli:* the mean-modulus formula is **false**
(counterexample: `R = I` gives `rho = max_i m_i`); the correct object is the
weighted Gram `M^{1/2} R M^{1/2}` and the result is a bound
`rho(J) <= lambda_max((1-kappa) M + kappa M^{1/2} R M^{1/2})`, exact in the
(a)-limit and at `kappa = 0`, tightness measured in simulation.
**All stability claims use the `lambda_max` form; the mean-alignment
`N_eff^align = 1 + kappa(N-1) rbar` appears only as the equicorrelated
special case** - mean alignment understates clustered alignment, and the
cluster case (a vendor with a plurality) is panel 1b.

**Theorem 2 (concentration boundary).** Under the supply-chain model the
boundary is

```
   epsilon < gamma / ( beta (1 + kappa s (N-1)) )   (+ O(1/d) correction, stated)
```

- the effective number of learners is the number of *independent* models.
Fifty dealers fine-tuning one vendor's model are, dynamically,
`1 + 49 kappa s ~ N` learners at `s ~ 1` and barely more than one at
`s ~ 0`. The `(N, s)` phase diagram is the paper's central figure.

**Theorem 3 (the adoption game - post-audit form).** Firms choose between a
market-leading model (quality advantage `q`) and independent alternatives.
One firm's adoption raises `rbar` by `O(1/N)`, so the *private* share of the
instability cost it creates vanishes as the market grows while `q` is
constant. Prove: (a) Nash adoption is full monoculture whenever `q` exceeds a
threshold **decreasing in `N`** (the externality mechanism, stated as such -
not "weak dominance"); (b) the social optimum has interior `s* < 1` from the
marginal-quality-equals-marginal-instability condition; (c) price of anarchy
in stability `= (1 + kappa(N-1)) / (1 + kappa s* (N-1))`, growing linearly in
`N`; (d) the minimal intervention restoring stability (diversity floor / tax
on shared adoption) in closed form. This discharges "ecosystem-level
incentive design".

**Theorem 4 (spectral early warning from public prices).** Near
`rho(J) -> 1`: critical slowing down of the *aligned* mode - the lag-1
autocorrelation of the leading principal component of cross-firm decisions
tends to 1 and its variance share grows as `1/(1 - rho)`. A supervisor
observing only public prices estimates distance-to-instability with no access
to any model. Give the estimator + consistency under the linearised dynamics.

## 4. Experiments (four panels)

| # | Panel | Protocol | Expected | Notes |
|---|---|---|---|---|
| P1a | `(N, s)` phase diagram | `env/heterogeneous_dealers.py`, `N in 1..8`, `s` grid, CRN joint-modulus probes (reuse `common_mode_probe`) | stable region collapses in `s`; `s = 1` column reproduces published `1.74x / 3.16x` - an external validation checkpoint | headline figure |
| P1b | Clustered alignment | 3 aligned firms among `N = 10` orthogonal | instability at mean-`rbar` values the mean formula calls safe | the audit-born figure; kills the naive index |
| P2 | Diversity buys stability | fixed `(N, epsilon)` beyond the monoculture boundary; ramp `rbar` down | same market, same feedback, same `N`: divergent -> convergent purely via decorrelation | most persuasive dynamic figure |
| P3 | Adoption game | Nash vs optimum `s` across quality gaps; PoA vs `N`; intervention curve | PoA linear in `N` | closed-form overlay |
| P4 | Real-data early warning | PC1 variance share + lag-1 AC of cross-sectional spread co-movement, 212-CUSIP panel 1990-2026; overlay fragility index; **placebo**: same statistic on Treasury/macro series | co-movement concentration rises into GFC + COVID; placebo flat(ter) | consistency evidence, NOT identification - stated in the caption and the text; data is not trade-level TRACE (provenance caveat verbatim from the repo) |

Protocol rules inherited: sweep `toxicity_feedback` never `alpha`;
beyond-boundary readings are diagnostics (caption caveat); multi-dealer runs
can saturate `info_cap` - scale `liq_flow_boost` down per
`env/multi_dealer.py` guidance; ASCII console.

## 5. New code

| File | Contents | ~lines |
|---|---|---|
| `reflex/theory/monoculture.py` | `alignment_matrix`, `lambda_max_R`, `rho_exact` (equal-moduli), `rho_bound` (weighted Gram), `supply_chain_alignment`, `adoption_threshold`, `social_optimum_s`, `price_of_anarchy`, `min_diversity_floor` | 380 |
| `reflex/env/heterogeneous_dealers.py` | per-dealer response params hitting a target `R` (incl. clustered topologies); pool routing unchanged; reduces to `multi_dealer.py` at `R = 1 1^T` (test) | 260 |
| `reflex/analysis/early_warning.py` | PC1 share, lag-1 AC, distance-to-instability estimator | 180 |
| `experiments/run_monoculture.py` | P1-P4 | 280 |
| `tests/test_monoculture.py` | reductions (`rbar = 1`, `R = I`, simplex); the `R = I` heterogeneous-moduli counterexample as a test; estimator consistency | 220 |
| `verification/certificates.py` (+9) | exact identity (equal moduli); bound tightness; `rbar` range; `N_eff` consistency with 1.3 both at `kappa = 0` and `kappa = 1`; supply-chain `r_ij -> s`; adoption FOC; PoA formula; early-warning consistency; cluster counterexample | +110 |

## 6. Page plan (9 pages)

1.0p Introduction (thesis, the static-vs-dynamic reframe, the four bullets).
1.0p Related work (named-author).
1.5p Model + the four equilibrium concepts.
2.0p Theorems 1-4, proof sketches (full proofs appendix).
2.5p Panels P1-P4.
0.5p Policy: the diversity floor, what a supervisor can actually compute.
0.5p Limitations: linearised dynamics; alignment unobservable directly
(Thm 4 is the answer); P4 provenance; equal-moduli scope of the exact
identity.
Appendix: proofs; the weighted-Gram derivation; placebo study; simulation
details; certificate listing.

## 7. Timeline (submission Aug 29; today Aug 16)

| Days | Work |
|---|---|
| Aug 16-17 | `theory/monoculture.py` + certificates; prove Thm 1(a) (rank-structure argument extending 1.3 section 4.1) |
| Aug 18-19 | `heterogeneous_dealers.py` + P1a/P1b; Thm 1(b) bound written |
| Aug 20-21 | P2 + adoption game + P3; Thm 3 proofs |
| Aug 22 | `early_warning.py` + P4 + placebo |
| Aug 23-25 | Write the 9 pages; appendix proofs finalised |
| Aug 26-27 | Internal review vs this pack; prose-guard pass; **anonymization checklist** (below) |
| Aug 28 | Freeze, buffer |
| Aug 29 | Submit (OpenReview) |

**Anonymization checklist (double-blind - this venue, unlike ML x OR).**
Strip author block + acknowledgements; no repo URL anywhere (no footnote, no
figure caption paths); cite the ICAIF submission in third person ("a
concurrent submission derives..."); scrub PDF metadata (producer, author
fields); figure files regenerated without embedded usernames in paths; the
simulator described as "a structural OTC market-making simulator" with an
anonymized-artifact promise.

## 8. Reviewer objections - prepared answers

1. *"`rbar`/alignment is unobservable."* Theorem 4 exists for exactly this;
   it is in the introduction, not the appendix.
2. *"Why market making?"* General statement first; constants computable +
   `N`-agent simulator with verified homogeneous predictions; one-paragraph
   recommender-system instantiation (engagement-response Jacobians over a
   shared user pool).
3. *"Diversity is obviously stabilising."* Not monotone and not obvious: the
   differential modes are *more* stable than a single firm (`1 - kappa < 1`),
   and clustered alignment beats mean alignment (P1b). The spectral form is
   the content.
4. *"Panel 4 is macro co-movement, not monoculture."* Agreed in the text;
   consistency-not-identification framing + placebo. The claim is only that
   the theory's observable moves when it should.
5. *"Static monoculture papers already show harm."* Different harm: allocation
   welfare vs dynamical stability; a market can be statically fine and
   dynamically fragile at the same `s` - P2 is that demonstration.

## 9. Risk register

| Risk | Mitigation |
|---|---|
| Thm 1(a) exact identity resists proof by Aug 19 | ship the bound + numerically-exact evidence (certificates show equality to machine precision on the equal-moduli grid); downgrade wording to "identity, proved for equicorrelated + verified numerically in general" |
| Heterogeneous env exposes `info_cap` saturation at large `N` | follow the repo's own guidance (scale `liq_flow_boost` down); document, never de-saturate silently |
| P4 signal weak | it is consistency evidence either way; a null is reportable with the placebo; the paper stands on P1-P3 |
| Time | de-scope order: P3 intervention curve -> Thm 4 consistency proof (keep estimator + simulation) -> P1b. Never cut P2 or the placebo. |

## 10. If a second EconML paper is wanted

E2 (involuntary algorithmic collusion) shares this build's entire simulation
layer; marginal cost ~4 days (competitive benign-flow module + detection
test). Decision point: **Aug 21.** If P1-P2 are done and clean by then, E2 is
feasible; otherwise one strong paper beats two thin ones. Do not decide later
than that.
