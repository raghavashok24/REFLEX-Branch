# 1. Novelty

## 1.1 What is genuinely new, and how defensible each claim is

Assessed against the literature as of 25 Aug 2026, including a fresh web
sweep for competing work (queries and sources in `07-verification-log.md`).

| Claim | Verdict | Notes |
|---|---|---|
| Effective number of independent learners: lambda_max of the correlation matrix of response Jacobians as the market's reproduction-number multiplier, derived from a reduction lemma | **New and defensible.** No prior work computes an effective learner count from feedback-direction alignment or puts it in a retraining stability condition | The paper already defuses the obvious attack (lambda_max of a correlation matrix is old) by citing random-matrix finance, effective rank, and ecology, and locating the novelty in the matrix and the condition. Keep that sentence |
| Supply-chain term: N_eff = 1 + kappa*s*(N-1), with a concentration bound in probability | **New.** Foundation-model concentration as a term in a stability condition rather than a static welfare statement | The nearest static work (Kleinberg-Raghavan, Bommasani, Peng-Garg, Jagadeesan) is correctly cited and correctly dispatched as equilibrium-not-dynamics |
| Crowding-cadence frontier: K-step lazy deployment composed with multi-agent amplification; critical crowding level | **New composition, with one caveat.** The single-learner slope is inherited (and cited); the composition and the critical level are new. Caveat: Li, Yau, Wai (NeurIPS 2022) studied deployment schedules in a multi-agent performative setting (see 1.2), so "a composition not previously made" needs them cited and dispatched to hold up | Fixed in proposed-v5: they are dispatched as cooperative consensus (coupling chosen, not inflicted), which is true to their model and keeps the claim intact |
| Mixed-market herd immunity: exact two-block root, imperfect-vaccine coverage law, critical efficacy | **New and the paper's strongest card.** No prior work runs corrected learners inside a multi-agent market, and the epidemiological transfer carrying a refinement of the law (not just the law) is strong evidence the correspondence is structural. Web sweep found no competing herd-immunity-for-learner-markets result | The optimistic-limit finding (the strong-correction limit errs unsafe) is the kind of self-generated adversarial result reviewers reward |
| Pigouvian wedge, marginal crowding share summing to N_eff, over-adaptation for N >= 2, provenance channel linear in N | **New in this setting.** The commons arithmetic is standard (the paper says so); the N_eff-amplified share and the provenance-vs-aggressiveness asymmetry are the specific contributions | The honest footnote that N_eff cancels in the ignored fraction protects this from an easy attack |

## 1.2 The citation gap (fix before the deadline)

Two multi-agent performative prediction papers are uncited, and both are
known to this workshop's community. A reviewer who works in this area finds
this in one pass. Verified against their abstracts and venues:

1. **Piliouras and Yu, "Multi-agent Performative Prediction: From Global
   Stability and Optimality to Chaos," EC 2023 (arXiv:2201.10483).**
   Many predictors of one common outcome; phase transitions from stability
   through instability to formal chaos as learning rates and agent counts
   grow. This is the monoculture corner R = 11' of this paper's geometry,
   taken past its linearization. It does not carry an alignment object, so
   the paper's containment story survives contact, but only if the paper
   makes the argument itself.
2. **Li, Yau, Wai, "Multi-agent Performative Prediction with Greedy
   Deployment and Consensus Seeking Agents," NeurIPS 2022
   (arXiv:2209.03811).** Decentralized agents minimizing a sum of losses,
   coupled through a consensus constraint, with a greedy deployment scheme.
   The coupling is chosen (cooperative), not inflicted through a shared
   environment, so no learning externality arises; but "deployment schemes
   in multi-agent performative prediction" is their territory by name, and
   Theorem 4's composition claim needs them dispatched.

One further citation is an asset rather than a defence:

3. **Kim, Garg, Peng, Garg, "Correlated Errors in Large Language Models,"
   ICML 2025 (arXiv:2506.07962).** Over 350 hosted models; substantial error
   correlation, concentrated within shared providers, and rising with model
   quality even across providers. This is the paper's premise measured in
   the wild, and it is the bridge to the measured-alignment panel of
   `03-benchmarking-results.md`. Note the author overlap with Peng and Garg
   (2024), already cited: this is the same community, which is exactly why
   the citation will be noticed if absent.

All three are added and dispatched in `proposed-v5/main.tex`, with the
page cost paid. Exact wording there; rationale for each dispatch above.

## 1.3 Claims checked and safe

- "None expresses a stability boundary or a rate" (monoculture paragraph):
  true for the four papers it quantifies over. Safe as long as the sentence
  stays scoped to those four.
- The Narang containment (Proposition 3): the witness construction is
  correct (verified in `02-technical-rigor.md`), and Narang et al. genuinely
  bound uniform scalars. Safe.
- "Having only ever been run single-learner" (Izzo et al.): sweep found no
  multi-agent deployment of performative-gradient corrections. Safe.
- The R_0 identity via Diekmann et al.: the next-generation-operator framing
  is correct, and the sweep found no prior transfer of the imperfect-vaccine
  coverage law to learning dynamics. Safe.

## 1.4 Contemporaneous 2026 preprints: verify, then cite (do not cite unread)

A sweep found three 2026 finance/AI preprints in the immediate
neighbourhood. I could read only titles and abstracts (full texts were
unreachable from this environment), so the characterizations below are
abstract-level and each needs one read before citing:

- **arXiv:2604.03272**, Meng and Chen, "Artificial Intelligence and Systemic
  Risk: A Unified Model of Performative Prediction, Algorithmic Herding, and
  Cognitive Dependency in Financial Markets." Rational-expectations model
  with an adoption share and a signal-correlation parameter. Overlapping
  thesis, different machinery: no response Jacobians, no spectral condition
  on a retraining map, no levers of this paper's kind, per the abstract.
- **arXiv:2604.22818**, "Representation Homogeneity and Systemic Instability
  in AI-Dominated Financial Markets." Calibrated structural simulation;
  finds a critical representation-similarity level and argues for diversity
  as a stabilizer. Closest in message, farthest in method; note it *does*
  exhibit a threshold, so the "no stability boundary" sentence must not be
  widened to cover it.
- **arXiv:2605.23905**, "AI-Driven Alpha Decay: Algorithmic Homogenization,
  Reflexive Signal Erosion." Adjacent framing, signal-decay focus.

Recommendation: read all three (an afternoon), then add one sentence to the
systemic-risk paragraph acknowledging the contemporaneous finance thread and
stating the delta (closed-form spectral boundary, an effective learner
count, and priced instruments, against calibrated simulation or aggregate
adoption models). If the page cannot absorb it, a camera-ready addition is
acceptable for contemporaneous preprints; the two peer-reviewed papers in
1.2 are not deferrable the same way.

## 1.5 Net assessment

The novelty case is real and, after the 1.2 fix, well defended on every
flank a reviewer is likely to probe. The paper's one structural exposure is
that its evidence for the new results is closed-form agreement rather than
measurement; that is an experiments problem, not a novelty problem, and it
is what item 1 of the action list addresses.
