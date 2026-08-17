# Vignesh Ideation

My split of the two REFLEX branch-off paper ideas, one file per paper. Each expands on the shared `papers_1-2_ideas_v1.md` draft while keeping the original ideas intact.

- [Paper 1 (ML × OR)](paper1_ml_x_or.md)
- [Paper 2 (Econ × ML)](paper2_econ_x_ml.md)

## Paper 1 (ML × OR): Executive Summary

This paper generalizes REFLEX's performative market-making stability result into a framework for any learning system whose own decisions reshape the data it later learns from. It lifts the scalar stability modulus $m = \varepsilon\beta/\gamma$ to a learner–environment Jacobian whose spectral radius governs stability, then adds a finite-sample certificate that classifies a system as stable, unstable, or undecided rather than forcing a binary verdict on insufficient data. It further reframes REFLEX's lazy-deployment result as a control principle, characterizing a retraining-cadence window that keeps the system inside the stable region. The corporate-bond simulator is retained as a validation environment, with a low-rank multi-bond extension demonstrating that the certificate stays tractable in higher dimensions.

**Venue alignment.** The ML × OR workshop targets the interface of learning and operations, so certifying and *controlling* stability of decision-driven systems through a computable, low-rank certificate fits its methodological core. Positioning REFLEX as a motivating derivation for general endogenous stochastic optimization matches the venue's appetite for operations-flavored theory with an empirical anchor.

## Paper 2 (Econ × ML): Executive Summary

This paper takes REFLEX's multi-dealer setting and makes the economic interaction itself the object of study, asking when competition among individually stable learners produces instability at the market level. It shows that dealers coupled through a shared endogenous flow satisfy $m_N = N_{\mathrm{eff}}\, m_1$, giving a critical population size $N_c = 1/m_1$ at which an ecosystem of well-behaved agents tips into instability. Framed as a learning externality, the mechanism is supported by REFLEX's measured common-mode amplification ($1.74\times$ for two dealers, $3.16\times$ for three) and by interventions (retraining cadence and structurally anchored correction) that act on the interaction structure rather than any single learner. The central message is the distinction between private stability and systemic stability: individually safe adaptive models can still generate endogenous market fragility.

**Venue alignment.** The Econ × ML workshop centers economic questions studied with machine-learning tools, and this paper's core object, a learning externality that turns agent count into a systemic-risk variable, is an economic mechanism first and a stability result second. Its argument that individual model evaluation is insufficient for a shared endogenous environment speaks directly to the venue's interest in market-level consequences of adaptive AI.
