# NeurIPS 2026 Workshop Papers

Two papers branching off **REFLEX** (*Reflexive Equilibrium Fixed-point Learning
for endogenous financial markets*) — a framework in which the constants of
performative-prediction stability theory (`m = εβ/γ`) are derived in closed form
from market-microstructure primitives, verified against a learned simulator
loop, and calibrated on 36 years of real market data. Each paper contributes a
new formal object that does not appear in the base project or its concurrent
ICAIF 2026 submission.

Both workshops run at NeurIPS 2026, Atlanta, Dec 12/13.

---

## Paper 1 — The Price of Self-Knowledge: an Information-Cost Uncertainty Principle for Performative Systems

**Track:** ML×OR — Second Workshop on Mathematical Foundations and Operational
Integration of Machine Learning for Uncertainty-Aware Decision-Making
(<https://mlxor-2026.github.io/>)
**Submission:** Aug 31, 2026 · 4 pages + unlimited appendix · non-anonymous ·
journal designation: *Mathematics of Operations Research*

When a deployed model reshapes the distribution it is trained on, estimating
that reaction — the response Jacobian every performative-gradient method
needs — is not a statistics problem with a sample budget but a control problem
with a P&L budget: every probe is a real decision taken at a real price. The
paper proves two results for the retraining loop. **Information saturation:** a
converging loop's own trajectory carries only a bounded amount of Fisher
information about its response, no matter how long it runs — so a
fast-contracting (safe) system is the blindest, and self-knowledge is precise
only near instability. **The uncertainty principle:** with deliberate
exploration, the product of estimator variance and expected excess performative
risk is pinned at `½·γ_PO·σ²` — invariant to the exploration intensity, the
horizon, and the modulus. Information about one's own performativity has a
fixed exchange rate against foregone value (verified numerically to machine
precision, including a falsification of the naively-anchored version). From
these follow a computable break-even rule for *whether* to explore, a
feasibility frontier for accuracy-vs-budget targets, a crossover rule for when
structural anchoring beats free-form estimation (turning REFLEX's documented
"anchoring, not capacity" negative result into a theorem), and a safe
D-optimal exploration design that identifies the response without ever
destabilizing the system being probed.

**Fit:** the workshop's "uncertainty mitigation at the interface of data,
model, and decision" and sequential decision-making themes — an exact identity
plus an operational algorithm, sized for the 4-page + journal-appendix format.

---

## Paper 2 — Algorithmic Monoculture as Dynamical Instability: the Effective Number of Independent Models

**Track:** EconML — Economics × Machine Learning Workshop
(<https://econml26-workshop.github.io/>)
**Submission:** Aug 29, 2026 · 9 pages + unlimited appendix · double-blind ·
in-person presentation required

The monoculture literature shows that shared models correlate *outcomes* — a
static harm. This paper shows what monoculture does to systems that *retrain*:
it aligns the feedback directions of the learners, and aligned feedback
resonates. For `N` firms retraining on a shared decision-dependent
environment, ecosystem stability is governed not by the number of firms but by
the **effective number of independent models** — the leading eigenvalue of the
correlation matrix of the firms' performative responses (exact identity for
equal moduli; weighted-Gram bound in general, with a clustered-alignment
counterexample showing mean-similarity diversity indices are the wrong
instrument). Under a supply-chain decomposition, the stability boundary
becomes `ε < γ / (β(1 + κs(N−1)))` in the shared-foundation-model fraction
`s`: fifty dealers fine-tuning one vendor's model are, dynamically, close to
one very large learner. An adoption game shows monoculture is the Nash
destination of unregulated model choice — a textbook `O(1/N)` externality —
with a price of anarchy in stability growing linearly in market size and a
closed-form minimal diversity intervention. Finally, an early-warning result
makes it governable: near the boundary, the aligned mode of cross-firm
decisions exhibits critical slowing down, so a supervisor can estimate
distance-to-instability from public prices alone — evaluated on a 36-year,
212-bond panel with a macro placebo.

**Fit:** hits the CFP's verbatim Theme-2 topics — "algorithmic monoculture and
model multiplicity," "feedback loops and performative prediction effects,"
"market concentration among AI service providers," "AI supply chains," and
"ecosystem-level incentive design" — with the equilibrium, welfare, and
identification analysis this audience expects.

---

## Shared foundation

Both papers inherit REFLEX's evidence stack: closed-form theory modules,
a genuine N-dealer simulator (bit-for-bit single-dealer reduction at N=1),
a numerically certified verification layer (66 machine-checked identities),
real-data calibration with honest provenance, and deterministic CPU-only
experiments. The papers do not overlap each other (single-learner
identification economics vs. many-learner spectral stability) or the
concurrent ICAIF submission (which contains the homogeneous special case and
no identification-cost, alignment, adoption, or observability results).
