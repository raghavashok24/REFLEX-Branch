# Abstract

**Status: drafted.** Rewrite once experiment 5 lands, because the abstract
should quote a measured number rather than only predicted ones. Target 150 to
200 words.

---

## Draft

A learning agent can satisfy every single-agent stability criterion and still
help destabilize the market it operates in. When adaptive agents share an
environment that reacts to their decisions, each agent's retraining reshapes the
data every other agent learns from next, a **learning externality** that no
agent internalizes. We show its strength is governed not by the number of firms
but by the **effective number of independent learners**, the leading eigenvalue
of the correlation matrix of firms' response Jacobians, so foundation-model
concentration enters the stability condition as a term rather than as a concern:
fifty firms fine-tuning one vendor's model are dynamically close to one large
learner. Three closed-form levers follow. A crowding-cadence frontier bounds how
often a market can retrain, and closes past a critical crowding level. A
herd-immunity threshold makes the market stable if and only if the fraction of
agents running feedback-aware updates exceeds `1 - 1/m_N`, exactly the
epidemiological `1 - 1/R_0` law with the systemic modulus as the reproduction
number. A Pigouvian wedge prices the externality. The second and third trade off:
model diversity and corrected learning are substitutes, along a frontier we
compute and measure.

---

## Notes

**Word count.** 197 as drafted. At the ceiling, so any addition displaces
something.

**What is missing and why.** No measured number appears yet. The abstract should
end on a measurement, not on a prediction, and the candidate is experiment 5's
agreement between the measured and predicted substitution frontier. Reserve the
final sentence for it.

**Rejected openings.** Anything beginning with the field ("Machine learning
systems increasingly...") or with the venue's vocabulary ("Algorithmic
monoculture has emerged as..."). The first sentence is the paper's claim, and it
is the sentence a reviewer decides on.

**Title check.** "Herd Immunity for Markets of Adaptive Models: Learning
Externalities and the Effective Number of Independent Learners" is long. It
survives because both halves earn their place: the first is the memorable law
and the second is the object that makes it computable. Reconsider only if the
submission form imposes a length limit.
