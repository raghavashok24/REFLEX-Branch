# Paper 1: ML × OR

## Core Research Question

**How can we certify and control the stability of learning systems whose own decisions change the data-generating environment they subsequently learn from?**

The key idea is to take the feedback mechanism developed in REFLEX for performative market making and turn it into a **general framework for endogenous learning systems**. Rather than treating the corporate-bond market as the main contribution, the paper would treat REFLEX as the motivating derivation and demonstrate that its stability machinery can be expressed more generally.

## 1. Generalizing the REFLEX Stability Condition

- REFLEX provides a scalar stability modulus:
  \[
  m = \frac{\varepsilon\beta}{\gamma}
  \]
  where the components capture:
  - **environment sensitivity** through \(\varepsilon\),
  - **objective smoothness** through \(\beta\),
  - **curvature** through \(\gamma\).

- The paper would begin by explaining why this decomposition is useful beyond the specific market-making setting.

- The central abstraction would be a **best-response map** describing how the learner's decision changes in response to an environment that itself depends on the learner's previous decision.

- Instead of relying only on a scalar modulus, the generalized system would be represented through a **learner-environment Jacobian**.

- Stability would then be characterized through the **spectral radius** of this Jacobian.

- The scalar REFLEX condition would appear as the special case where the system effectively reduces to one dimension.

- This gives the paper a natural progression:
  1. REFLEX establishes the feedback mechanism.
  2. The paper abstracts that mechanism.
  3. The scalar stability condition becomes a special case.
  4. The Jacobian formulation handles higher-dimensional systems.

## 2. A Finite-Sample Stability Certificate

The next contribution would move from theoretical stability to **certification from estimated quantities**.

- In practice, the environment response and relevant structural quantities would have to be estimated from finite data.

- An estimated stability modulus or Jacobian therefore would not provide an exact statement about the underlying system.

- The paper would construct an **uncertainty radius** around the estimated environment response.

- This would allow the system to be classified into three regimes:
  - **Stable:** the estimated uncertainty region remains within the stable regime.
  - **Unstable:** the uncertainty region lies in the unstable regime.
  - **Undecided:** the uncertainty region crosses the stability boundary.

- The important point is that the method would not force a binary stable/unstable decision when the available data cannot support one.

- This would build directly on the **robust boundary construction already developed in REFLEX**, rather than introducing an unrelated statistical procedure.

- The resulting certificate would therefore connect the theoretical stability condition to an operational question: **given finite observations, can we confidently say that the learning system is stable?**

## 3. Stability as Something That Can Be Controlled

The paper would then move beyond diagnosis.

- REFLEX's lazy-deployment result would be reframed as a general **control principle for endogenous learning systems**.

- The underlying observation is that instability is not necessarily determined only by the learner or environment. It can also depend on **how frequently the learner updates itself**.

- The paper would study retraining cadence as an operational parameter.

- The goal would be to characterize a **stability window** in which optimization or retraining occurs frequently enough to achieve the desired adaptation but slowly enough to avoid destabilizing feedback.

- Rather than simply saying that a system is unstable, the framework would therefore answer a more useful operational question:
  **What deployment or retraining regime keeps the system inside the stable region?**

- The closed-form stability window derived from the REFLEX lazy-deployment result would serve as the motivating example for this broader principle.

## 4. Empirical Validation

The existing OTC corporate-bond environment would remain important, but its role would change.

It would primarily serve as a **validation environment for the generalized framework**, rather than being the entirety of the paper's scientific contribution.

The experiments could be organized around three questions:

1. **Does the certificate predict the observed stability boundary?**
   - Compare the theoretically predicted boundary against observed behavior in the simulator.

2. **Does the finite-sample procedure behave appropriately near the boundary?**
   - In particular, examine whether the procedure distinguishes clear cases from situations where uncertainty makes a definitive classification inappropriate.

3. **Can retraining cadence actually control stability?**
   - Test whether changing optimization cadence can move a system from an unstable regime into a stable regime, as suggested by the REFLEX result.

## 5. Multi-Dimensional Extension

The multi-bond setting would provide the natural higher-dimensional test.

- A scalar stability condition becomes less sufficient once several related decisions or instruments interact.

- The generalized Jacobian formulation would provide the mathematical representation of those interactions.

- The paper would investigate whether the stability certificate remains computationally tractable as dimensionality increases.

- The proposed route is to exploit **low-rank structure**, preserving the computational character of the original REFLEX framework.

- This would demonstrate that the generalization is not merely theoretical. It can still produce a usable certificate when the endogenous system has multiple interacting components.

## Overall Contribution

The paper would ultimately be positioned as:

> **REFLEX provides a concrete derivation of endogenous feedback and a scalar stability condition. This paper extracts that mechanism into a general framework for analyzing, certifying, and controlling endogenous learning systems.**

The strongest distinction from REFLEX is therefore not simply adding another experiment. It is changing the level of abstraction from **performative market making** to **general endogenous stochastic optimization**, while retaining the structural quantities and deployment insights that make the original framework operational.
"""

# Paper 2: Econ × ML

## Core Research Question

**When does competition among individually stable learning agents create instability at the market level?**

This paper would take the multi-dealer component of REFLEX and make the **economic interaction itself** the central object of study.

The key distinction from Paper 1 is that Paper 1 asks how to characterize and control stability **within an endogenous learning system**, while this paper asks how **multiple learning systems interact through a shared endogenous environment**.

## 1. From Individual Stability to Systemic Stability

The starting point is the distinction between two different questions:

- Is each learning agent stable when considered individually?
- Is the collection of learning agents stable when they interact?

REFLEX's multi-dealer extension provides the basis for showing that these need not be the same.

- Suppose each dealer satisfies its individual stability condition:
  \[
  m_1 < 1.
  \]

- This means that, considered in isolation, the individual learner lies within the stable regime.

- However, dealers do not operate in isolation.

- Their actions affect a **shared endogenous flow**, which changes the environment observed by the other dealers.

- This creates a feedback channel that does not appear in the single-agent condition.

- Under the symmetric shared-pool structure considered in REFLEX, this produces the effective relationship:
  \[
  m_N = N_{\mathrm{eff}}m_1.
  \]

- The corresponding critical population size is:
  \[
  N_c = \frac{1}{m_1}.
  \]

The economic interpretation is that **the number of interacting adaptive agents becomes part of the stability problem**.

## 2. Learning Externalities

The paper would frame this as a **learning externality**.

Each dealer makes a decision based on its own objective, but that decision changes the shared environment.

That creates a sequence such as:

1. Dealer A changes its behavior.
2. The shared market environment changes.
3. Dealer B observes the changed environment.
4. Dealer B adapts.
5. Dealer B's adaptation further changes the shared environment.
6. Dealer A subsequently retrains on that changed environment.

The important point is that each agent can behave rationally and satisfy its own stability condition while the **interaction between agents amplifies the feedback loop**.

This makes systemic instability qualitatively different from individual instability.

## 3. Common-Mode Amplification

The common mode would be an important part of the economic interpretation.

- Under the shared-pool structure, the learning agents are coupled through a common environment.

- Consequently, coordinated or common changes can be amplified across the population.

- REFLEX already provides empirical observations that make this particularly useful as the central experiment.

- For two dealers, the observed amplification was approximately:
  \[
  1.74\times
  \]

- For three dealers, the observed amplification was approximately:
  \[
  3.16\times.
  \]

- The paper would use these results to study the relationship between the number of adaptive agents and the amplification of shared feedback.

- The goal would not be to claim that these exact amplification values constitute a universal law. They are results from the existing REFLEX multi-dealer simulator that motivate and test the proposed systemic-stability interpretation.

## 4. Population Size as a Systemic Risk Variable

The critical population relationship provides a particularly clean economic result:

\[
N_c = \frac{1}{m_1}.
\]

This gives the paper a simple interpretation.

- If individual learning is weakly responsive, the system may tolerate more interacting learners.

- If individual learning is already close to the stability boundary, relatively few interacting agents may be sufficient to create a market-level problem.

- Thus, **agent count is not merely a descriptive market characteristic**. Under the shared-pool structure, it directly enters the stability condition.

- This creates a connection between the micro-level behavior of an individual learner and the macro-level behavior of the learning ecosystem.

The paper could therefore present systemic instability as an **emergent property of interacting adaptive agents**, rather than something that must be present in any one agent individually.

## 5. Interventions

After establishing the instability mechanism, the paper would ask whether the externality can be reduced.

The main interventions would remain those already motivated by REFLEX:

- **Retraining cadence**
  - Slowing or controlling updates could reduce the strength of the feedback loop.

- **Structurally anchored performative correction**
  - The correction mechanism developed in REFLEX could be examined as another way of reducing the destabilizing effect of endogenous feedback.

The important framing would be that these interventions operate on the **interaction structure**, rather than merely improving an individual learner's predictive performance.

## 6. Why Individual Model Evaluation Is Insufficient

This would provide the broader economic motivation for the paper.

Traditional evaluation of an AI system might ask:

> Is this model stable when deployed?

The paper would instead argue that in a shared endogenous environment, another question is necessary:

> Is the ecosystem of interacting models stable?

A dealer can therefore pass an individual stability test while the market containing many such dealers fails a market-level stability test.

This has a natural economic interpretation because the instability arises from an **externality**. Each participant does not fully internalize the effect that its adaptive behavior has on the environment faced by the other adaptive participants.

## 7. Empirical Structure

The existing multi-dealer simulator gives the paper a direct experimental structure.

The experiments could systematically examine:

- **Number of learning agents**
  - How does systemic behavior change as the number of dealers increases?

- **Individual stability**
  - Are the individual agents themselves within their respective stability conditions?

- **Shared-environment amplification**
  - How does the interaction through the common pool change the dynamics?

- **Retraining cadence**
  - Can changing update frequency reduce systemic instability?

- **Performative correction**
  - Can the structurally anchored correction reduce the instability created by the shared environment?

The central comparison would always remain between **agent-level stability** and **market-level stability**.

## Overall Contribution

The paper would ultimately position REFLEX as the source of the multi-agent mechanism while shifting the research question toward economics:

> **REFLEX shows that multiple dealers interacting through a shared endogenous flow can amplify learning dynamics. This paper develops that result as a framework for understanding learning externalities and systemic instability among competing adaptive agents.**

The main conceptual contribution is therefore the distinction between **private stability** and **systemic stability**.

An individual AI agent can be well behaved. A collection of individually well-behaved agents can still become unstable because their decisions are coupled through a shared environment. That makes the paper less about whether a single model is safe or stable and more about how **markets populated by adaptive models can generate new forms of endogenous fragility**.
"""

Path("/mnt/data/Paper_1_ML_x_OR.md").write_text(paper1, encoding="utf-8")
Path("/mnt/data/Paper_2_Econ_x_ML.md").write_text(paper2, encoding="utf-8")

print("Created:")
print("/mnt/data/Paper_1_ML_x_OR.md")
print("/mnt/data/Paper_2_Econ_x_ML.md")
