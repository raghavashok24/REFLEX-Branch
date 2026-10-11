# Paper 1 (ML × OR): Certifying and Controlling Stability in Endogenous Learning Systems

## Core Research Question

**How can we certify and control the stability of learning systems whose own decisions change the data-generating environment they subsequently learn from?**

The key idea is to take the feedback mechanism developed in REFLEX for performative market making and turn it into a **general framework for endogenous learning systems**. Rather than treating the corporate-bond market as the main contribution, the paper treats REFLEX as the motivating derivation and demonstrates that its stability machinery can be expressed more generally. The level of abstraction shifts from performative market making to general endogenous stochastic optimization, while retaining the structural quantities and deployment insights that make the original framework operational.

## 1. Generalizing the REFLEX Stability Condition

REFLEX provides a scalar stability modulus:

$$
m = \frac{\varepsilon\beta}{\gamma}
$$

whose components capture:

- **environment sensitivity** through $\varepsilon$,
- **objective smoothness** through $\beta$,
- **curvature** through $\gamma$.

The paper begins by explaining why this decomposition is useful beyond the specific market-making setting. The central abstraction is a **best-response map** describing how the learner's decision changes in response to an environment that itself depends on the learner's previous decision.

Instead of relying only on a scalar modulus, the generalized system is represented through a **learner–environment Jacobian**, and stability is characterized through the **spectral radius** of that Jacobian. The scalar REFLEX condition then appears as the special case where the system effectively reduces to one dimension.

This gives the paper a natural progression:

1. REFLEX establishes the feedback mechanism.
2. The paper abstracts that mechanism.
3. The scalar stability condition becomes a special case.
4. The Jacobian formulation handles higher-dimensional systems.

## 2. A Finite-Sample Stability Certificate

The next contribution moves from theoretical stability to **certification from estimated quantities**.

In practice, the environment response and relevant structural quantities must be estimated from finite data, so an estimated stability modulus or Jacobian does not provide an exact statement about the underlying system. The paper constructs an **uncertainty radius** around the estimated environment response, which allows the system to be classified into three regimes:

- **Stable:** the estimated uncertainty region remains within the stable regime.
- **Unstable:** the uncertainty region lies in the unstable regime.
- **Undecided:** the uncertainty region crosses the stability boundary.

The important point is that the method does not force a binary stable/unstable decision when the available data cannot support one. This builds directly on the **robust boundary construction already developed in REFLEX**, rather than introducing an unrelated statistical procedure. The resulting certificate connects the theoretical stability condition to an operational question: **given finite observations, can we confidently say that the learning system is stable?**

## 3. Stability as Something That Can Be Controlled

The paper then moves beyond diagnosis. REFLEX's lazy-deployment result is reframed as a general **control principle for endogenous learning systems**.

The underlying observation is that instability is not necessarily determined only by the learner or the environment. It can also depend on **how frequently the learner updates itself**. The paper studies retraining cadence as an operational parameter and characterizes a **stability window** in which optimization or retraining occurs frequently enough to achieve the desired adaptation but slowly enough to avoid destabilizing feedback.

Rather than simply declaring a system unstable, the framework answers a more useful operational question: **what deployment or retraining regime keeps the system inside the stable region?** The closed-form stability window derived from the REFLEX lazy-deployment result serves as the motivating example for this broader principle.

## 4. Empirical Validation

The existing OTC corporate-bond environment remains important, but its role changes. It primarily serves as a **validation environment for the generalized framework**, rather than being the entirety of the paper's scientific contribution.

The experiments are organized around three questions:

1. **Does the certificate predict the observed stability boundary?**
   Compare the theoretically predicted boundary against observed behavior in the simulator.

2. **Does the finite-sample procedure behave appropriately near the boundary?**
   In particular, examine whether the procedure distinguishes clear cases from situations where uncertainty makes a definitive classification inappropriate.

3. **Can retraining cadence actually control stability?**
   Test whether changing optimization cadence can move a system from an unstable regime into a stable regime, as suggested by the REFLEX result.

## 5. Multi-Dimensional Extension

The multi-bond setting provides the natural higher-dimensional test. A scalar stability condition becomes less sufficient once several related decisions or instruments interact, and the generalized Jacobian formulation provides the mathematical representation of those interactions.

The paper investigates whether the stability certificate remains computationally tractable as dimensionality increases. The proposed route is to exploit **low-rank structure**, preserving the computational character of the original REFLEX framework. This demonstrates that the generalization is not merely theoretical: it can still produce a usable certificate when the endogenous system has multiple interacting components.

## Overall Contribution

The paper is ultimately positioned as:

> **REFLEX provides a concrete derivation of endogenous feedback and a scalar stability condition. This paper extracts that mechanism into a general framework for analyzing, certifying, and controlling endogenous learning systems.**

The strongest distinction from REFLEX is therefore not simply adding another experiment. It is changing the level of abstraction from **performative market making** to **general endogenous stochastic optimization**, while retaining the structural quantities and deployment insights that make the original framework operational.
