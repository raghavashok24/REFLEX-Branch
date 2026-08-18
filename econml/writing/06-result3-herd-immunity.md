# 6. Result 3: herd immunity, and diversity as its substitute

**Status: planned, and restructured.** Target 1.25 pages. Source:
[`../math/derivations/04-mixed-market-secular.md`](../math/derivations/04-mixed-market-secular.md),
which supersedes `../math/03-theorem3-herd-immunity.md` where they disagree.

**This is the paper.** If the build slips, everything else gives way before this
section does.

**What changed, and it changes the section.** The strong-correction limit is
**optimistic, not conservative**: it under-states the spectral radius, so it can
call a market stable that is unstable at any finite correction strength. The
clean `rho* = 1 - 1/m_N` law can therefore no longer be presented alone. The
repair is better than the damage: the exact threshold at `kappa = s = 1` is
`(1 - 1/m_N)/(1 - theta)` with `theta = gamma/gamma_PO`, which is the standard
epidemiological coverage requirement for an **imperfect vaccine**, and it comes
with a critical efficacy past which no corrected fraction works at all. Present
the imperfect-correction law as the theorem and the clean law as its
perfect-efficacy corner.

---

## What this section does

Two things that must not be separated. The herd-immunity threshold is the
memorable result and the one that gives talks and reviews a handle. The
substitution frontier is the useful one, and it exists only because Section 4
and this section are expressed in the same quantity. Present the threshold
first, then the frontier as its consequence.

## Content, in order

**The setup.** A mixed market: `N_b` blind firms with response slope `m_1`, and
`N - N_b` corrected firms whose response is damped by `gamma/gamma_PO < 1`.
Corrected fraction `rho = 1 - N_b/N`. One short paragraph, noting that the
corrected update is published machinery (Izzo et al., 2021; REFLEX for the
structurally anchored version) and that what is new is running it in the game.

**Theorem 3, stated exactly.** The mixed-market Jacobian is a diagonal plus a
positive rank-one term, so its spectrum solves a secular equation that collapses
to a quadratic when there are two correction levels. The radius is the larger
root, in closed form. Give the quadratic, not a limit. [VERIFIED, exact to
`2.5e-14` against dense eigensolves on 6000 draws]

**The strong-correction limit, as a corollary and with its error direction
stated.** As `gamma_PO -> infinity` the unstable cycle runs through blind firms
only:

```
   m_1 ( 1 + kappa * s * (N_b - 1) )  <  1 ,
   N_b  <  N_c(s)  =  1 + (1/m_1 - 1)/(kappa*s) .
```

State this as the limit of the exact root rather than as its own argument, and
**say in the same breath that it errs optimistic.** The radius is nondecreasing
in `gamma/gamma_PO`, so the limit under-states it; on random draws the limit
calls about one configuration in eight stable that is not. One sentence, one
number, no hedging. A referee who finds this unaided will not trust the rest.
[VERIFIED]

**The collapse, and then the honest version.** At `kappa = s = 1`, `N_c = 1/m_1`
and the limit gives

```
   rho*  =  1 - 1/m_N ,
```

**exactly the epidemiological herd-immunity threshold `1 - 1/R_0`.** A market of
10 firms at `m_N = 2.5` needs 60% of them un-blinded, *if correction is perfect*.
At efficacy `e = 1 - gamma/gamma_PO` the exact requirement is

```
   rho*(e)  =  ( 1 - 1/m_N ) / e ,
```

**the standard coverage requirement for an imperfect vaccine.** This is the
section's strongest moment and it should be written as such: the analogy is not
merely preserved under the correction, it predicts the correction. A structural
correspondence transfers the refinements of the law it borrows; a decorative one
does not. [VERIFIED, exact to `1.8e-15`]

**Critical efficacy.** `rho*(e)` exceeds one when `gamma_PO/gamma < m_N`, so
correction is a usable lever at all only above that ratio. At `m_N = 2.5` the
corrected update must deliver a `2.5x` curvature improvement or no fraction of
un-blinded firms stabilizes the market. This is the exact structural parallel of
Section 5's critical crowding, and saying so ties the two levers together before
the substitution frontier asks the reader to trade them off. [VERIFIED]

**Earn the analogy in two sentences.** In heterogeneous populations `R_0` is
*defined* as the spectral radius of a next-generation operator (Diekmann et al.,
1990), and `m_N` is the spectral radius of the joint retraining Jacobian, so the
two thresholds are the same statement about a linearized operator rather than a
resemblance. Note also, following Fine et al. (2011), that the clean `1 - 1/R_0`
form assumes homogeneous mixing, and that the collapse here assumes the
`kappa = s = 1` corner for the same reason. Stating the assumption in the same
breath as the formula is what separates this from a slogan.

**The synthesis result.** `rho*(s)` is increasing in `s`, so a market reaches
stability along either axis. At `N = 20`, `m_1 = 0.15`, `kappa = 0.8`: a
monoculture needs about 60% of agents corrected, at `s = 0.5` about a quarter
suffices, and at `s = 0.2` the threshold is zero, meaning the market is stable
with no corrected agents at all.

**The economic reading, which is what makes it a policy object.** Correction is
a public good: an un-blinded firm captures a private benefit while the stability
it contributes accrues to everyone, so the market free-rides below the threshold
and will not reach `rho*` unaided (Bergstrom, Blume and Varian, 1986). Model
diversity has the same structure. **The substitution is therefore between two
goods that are both under-supplied**, not between a good and a bad, and that
sentence is what makes the frontier something a regulator can move along rather
than a menu of two policies plotted on shared axes.

**The exact version is no longer optional.** It was fourth in the de-scope order.
It cannot be, now that the limit is known to err in the unsafe direction:
shipping the limit alone would state a stability criterion that is optimistic
without saying so. The de-scope order is amended in the plan of record.

## Figures 3 and 4

**Figure 3, herd immunity.** Measured stability against corrected fraction in an
`m_N > 1` regime, with predicted `rho*` marked. Plot the exact threshold at the
simulated `gamma_PO` alongside the perfect-correction limit, since the gap
between them is a result rather than an error bar.

The realized threshold is a whole number of firms, and it is
`N - ceil(N_c(s)) + 1`, not `ceil(rho* N)`. The two agree except when `N_c` is
exactly an integer, where `ceil(rho* N)` is off by one. At the small `N` the
experiment runs at, one firm is several percentage points, so use the formula.

**Figure 4, the substitution frontier.** The `(rho, s)` iso-stability curve,
measured against predicted. **The headline figure and the one that goes on the
poster.**

**The free-riding diagnostic** (private P&L of corrected against blind firms)
sits in the appendix or in Figure 3's second panel, and is fourth in the
de-scope order.

## Checklist

**Structure and honesty, all new since the exact root landed:**

- [ ] The exact two-block root is the theorem; the limit is its corollary
- [ ] The limit's optimism stated with a number, in the same paragraph as the
      limit itself, never in a later caveat
- [ ] The imperfect-correction law present, framed as the analogy predicting its
      own refinement
- [ ] Critical efficacy stated, and tied to Section 5's critical crowding

**Carried over from the original plan:**

- [ ] The threshold and the frontier presented together, threshold first
- [ ] Diekmann et al. cited where the analogy is claimed, not elsewhere
- [ ] The homogeneous-mixing assumption stated alongside the clean formula
- [ ] Both-goods-under-supplied sentence present
- [ ] Integer threshold uses `N - ceil(N_c) + 1`, not `ceil(rho* N)`
- [ ] The experiment is new in kind: the corrected loop has never run inside a
      multi-agent game

## Note for the writing pass

**The section got better, not worse.** The instinct on finding that a headline law
is only a limit is to bury the qualification. Do the opposite here. The paper now
has a threshold law, its imperfect-efficacy generalization, and a critical
efficacy past which the lever dies, all in closed form and all matching
epidemiology's own structure. That is more content than the clean law alone, and
it forecloses the obvious referee attack, which is to ask what happens at finite
`gamma_PO` and watch the paper have no answer.
