# Paper 2 (Econ × ML): Learning Externalities and Systemic Instability Among Competing Adaptive Agents

## Core Research Question

**When does competition among individually stable learning agents create instability at the market level?**

This paper takes the multi-dealer component of REFLEX and makes the **economic interaction itself** the central object of study. The key distinction from Paper 1 is one of scope: Paper 1 asks how to characterize and control stability **within an endogenous learning system**, while this paper asks how **multiple learning systems interact through a shared endogenous environment**.

## 1. From Individual Stability to Systemic Stability

The starting point is the distinction between two different questions:

- Is each learning agent stable when considered individually?
- Is the collection of learning agents stable when they interact?

REFLEX's multi-dealer extension provides the basis for showing that these need not be the same. Suppose each dealer satisfies its individual stability condition:

$$
m_1 < 1.
$$

Considered in isolation, the individual learner lies within the stable regime. However, dealers do not operate in isolation. Their actions affect a **shared endogenous flow**, which changes the environment observed by the other dealers, creating a feedback channel that does not appear in the single-agent condition.

Under the symmetric shared-pool structure considered in REFLEX, this produces the effective relationship:

$$
m_N = N_{\mathrm{eff}}\, m_1,
$$

with a corresponding critical population size:

$$
N_c = \frac{1}{m_1}.
$$

The economic interpretation is that **the number of interacting adaptive agents becomes part of the stability problem**.

## 2. Learning Externalities

The paper frames this as a **learning externality**. Each dealer makes a decision based on its own objective, but that decision changes the shared environment. That creates a sequence such as:

1. Dealer A changes its behavior.
2. The shared market environment changes.
3. Dealer B observes the changed environment.
4. Dealer B adapts.
5. Dealer B's adaptation further changes the shared environment.
6. Dealer A subsequently retrains on that changed environment.

The important point is that each agent can behave rationally and satisfy its own stability condition while the **interaction between agents amplifies the feedback loop**. This makes systemic instability qualitatively different from individual instability.

## 3. Common-Mode Amplification

The common mode is an important part of the economic interpretation. Under the shared-pool structure, the learning agents are coupled through a common environment, so coordinated or common changes can be amplified across the population. REFLEX already provides empirical observations that make this particularly useful as the central experiment:

- For two dealers, the observed amplification was approximately $1.74\times$.
- For three dealers, the observed amplification was approximately $3.16\times$.

The paper uses these results to study the relationship between the number of adaptive agents and the amplification of shared feedback. The goal is not to claim that these exact amplification values constitute a universal law; they are results from the existing REFLEX multi-dealer simulator that motivate and test the proposed systemic-stability interpretation.

## 4. Population Size as a Systemic Risk Variable

The critical population relationship provides a particularly clean economic result:

$$
N_c = \frac{1}{m_1}.
$$

This gives the paper a simple interpretation:

- If individual learning is weakly responsive, the system may tolerate more interacting learners.
- If individual learning is already close to the stability boundary, relatively few interacting agents may be sufficient to create a market-level problem.

Thus **agent count is not merely a descriptive market characteristic**. Under the shared-pool structure, it directly enters the stability condition, creating a connection between the micro-level behavior of an individual learner and the macro-level behavior of the learning ecosystem. The paper can therefore present systemic instability as an **emergent property of interacting adaptive agents**, rather than something that must be present in any one agent individually.

## 5. Interventions

After establishing the instability mechanism, the paper asks whether the externality can be reduced. The main interventions remain those already motivated by REFLEX:

- **Retraining cadence.** Slowing or controlling updates could reduce the strength of the feedback loop.
- **Structurally anchored performative correction.** The correction mechanism developed in REFLEX is examined as another way of reducing the destabilizing effect of endogenous feedback.

The important framing is that these interventions operate on the **interaction structure**, rather than merely improving an individual learner's predictive performance.

## 6. Why Individual Model Evaluation Is Insufficient

This provides the broader economic motivation for the paper. Traditional evaluation of an AI system might ask:

> Is this model stable when deployed?

The paper instead argues that in a shared endogenous environment, another question is necessary:

> Is the ecosystem of interacting models stable?

A dealer can pass an individual stability test while the market containing many such dealers fails a market-level stability test. This has a natural economic interpretation because the instability arises from an **externality**: each participant does not fully internalize the effect that its adaptive behavior has on the environment faced by the other adaptive participants.

## 7. Empirical Structure

The existing multi-dealer simulator gives the paper a direct experimental structure. The experiments systematically examine:

- **Number of learning agents.** How does systemic behavior change as the number of dealers increases?
- **Individual stability.** Are the individual agents themselves within their respective stability conditions?
- **Shared-environment amplification.** How does the interaction through the common pool change the dynamics?
- **Retraining cadence.** Can changing update frequency reduce systemic instability?
- **Performative correction.** Can the structurally anchored correction reduce the instability created by the shared environment?

The central comparison always remains between **agent-level stability** and **market-level stability**.

## Overall Contribution

The paper ultimately positions REFLEX as the source of the multi-agent mechanism while shifting the research question toward economics:

> **REFLEX shows that multiple dealers interacting through a shared endogenous flow can amplify learning dynamics. This paper develops that result as a framework for understanding learning externalities and systemic instability among competing adaptive agents.**

The main conceptual contribution is the distinction between **private stability** and **systemic stability**. An individual AI agent can be well behaved, yet a collection of individually well-behaved agents can still become unstable because their decisions are coupled through a shared environment. That makes the paper less about whether a single model is safe or stable and more about how **markets populated by adaptive models can generate new forms of endogenous fragility**.
