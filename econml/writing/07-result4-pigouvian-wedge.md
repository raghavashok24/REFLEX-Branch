# 7. Result 4: the Pigouvian wedge

**Status: planned.** Target 0.75 pages. Source: `../math/04-theorem4-wedge.md`.

---

## Why this section exists

An EconML reviewer reads Section 3's framing and asks where the model of the
externality is. This is the answer: welfare function, wedge, over-adaptation
result. Without it the paper is an ML paper using economics vocabulary, and a
reviewer from economics will say so in those words.

It also unifies the levers into the standard policy triple, which is worth one
explicit sentence because it tells an economics reader exactly what they are
looking at.

## Content, in order

**The welfare object.** In the stable regime the common mode is an AR(1) with
coefficient `-m_N`, so its stationary variance is proportional to
`1/(1 - m_N^2)`, a smooth cost diverging at the boundary. Defend the choice in
one clause rather than asserting it: stationary variance is the smooth proxy for
divergence risk, finite everywhere inside the stable region and divergent
exactly at the boundary the rest of the paper is about.

**The private and social problems.** Each firm chooses adaptation
aggressiveness `a_i`, meaning cadence, learning rate, or responsiveness, buying
concave tracking benefit `B(a_i)`. The variance cost is shared: firm `i` bears
its own exposure while its marginal contribution to `m_N` raises everyone's,
plus the client-side exposure it does not bear at all.

**Theorem 4.** The private first-order condition ignores the fraction `(N-1)/N`
of the marginal variance cost plus the entire client-side exposure, and the
corrective fee equals the externalized marginal cost, in closed form, increasing
in `N`, in `kappa`, and steeply in proximity to the boundary since
`dV/dm_N = 2 sigma^2 m_N/(1-m_N^2)^2`. [DERIVED]

**Corollary.** The decentralized equilibrium over-adapts relative to the social
optimum for every `N >= 2`, with the distortion growing as the market crowds.

**The provenance channel, which is what the merge buys.** `dm_N/da_i` decomposes
into an aggressiveness channel through `m_1` and a provenance channel
`dm_N/ds = m_1 * kappa * (N-1)`. The same wedge therefore prices shared-model
adoption directly, turning the monoculture externality into a fee rather than a
warning.

Add the asymmetry, in one sentence, because it explains the whole adoption
dynamic: the provenance channel grows linearly in `N` while a firm's private
quality gain from adopting the market-leading vendor does not, so unregulated
adoption runs toward the unstable configuration rather than away from it.

**The policy triple, named.** Section 5 is quantity regulation (cadence caps),
Section 6 is a technology mandate (correction) or a structural remedy
(diversity), Section 7 is the price instrument. One sentence, and cite Weitzman
(1974) for the instrument-choice question while acknowledging the paper does not
solve it. Omitting Weitzman invites the objection; including him converts it
into acknowledged future work.

## Figure 5

Decentralized against socially optimal aggressiveness on a small grid, with the
wedge's comparative statics in `N`, `kappa` and `s`.

**Second in the de-scope order.** If cut, Theorem 4 ships as theory with no
panel, which is acceptable: the theorem is the contribution and the panel is the
illustration.

## Checklist

- [ ] Variance-as-welfare-cost choice defended, not asserted
- [ ] Both channels of `dm_N/da_i` shown, aggressiveness and provenance
- [ ] The linear-in-`N` asymmetry stated, since it explains the adoption dynamic
- [ ] Policy triple named explicitly, with Weitzman cited and not oversold
- [ ] Client-side exposure assumption stated in one sentence
