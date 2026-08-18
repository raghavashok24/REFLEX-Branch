# 5. Result 2: the crowding-cadence frontier

**Status: planned.** Target 1.00 page. Source: `../math/02-theorem2-cadence.md`.

---

## What this section does

Composes two published pieces that have never been composed: the multi-agent
amplification law and the single-learner lazy-deployment slope. The composition
is an afternoon of algebra; the content is the frontier and the critical
crowding level, neither of which exists anywhere. Say that plainly rather than
dressing the algebra up.

## Content, in order

**The inherited piece, in two lines.** A learner taking `K` gradient steps per
deployment realizes outer-map slope `mu(K) = -m + c^K(1+m)`, with
`c = 1 - eta*gamma` the inner per-step contraction (Mendler-Dunner et al., 2020,
and REFLEX for the structural version). `c` is own-objective curvature, so it
does not depend on `N`, and that independence is what makes the composition
work.

**Theorem 2.** `mu_N(K) = -m_N + c^K(1 + m_N)`, so an `m_N > 1` market is stable
under lazy retraining if and only if

```
   K  <  K_max  =  ln( (m_N - 1)/(m_N + 1) ) / ln c ,
```

and `K_max` is decreasing in `m_N`. [DERIVED]

Proof sketch in three lines: the upper side of `|mu_N| < 1` never binds because
`c < 1`; the lower side gives the stated bound; the common mode binds because
differential modes have `|slope| = m_1(1-kappa) < 1`.

**Critical crowding.** `K` is a positive integer, so a window exists only if
`K_max > 1`, which reduces to `m_N < (1+c)/(1-c)`. Past that, the market is
unstable at every retraining frequency. Equivalently, minimum-cadence operation
multiplies the sustainable effective crowding by exactly `(1+c)/(1-c)`, a factor
of 9 at `c = 0.8`.

**The supply-chain reading, with the table.** At `m_1 = 0.15`, `kappa = 0.8`,
`N = 30`, `c = 0.8`, the window runs `K_max = 20.7` at `s = 0.25`, `5.3` at
`s = 0.5`, and `2.5` at `s = 1`. **State `c = 0.8` in the caption.** The table is
not reproducible without it, and the plan of record omits it.

Then the paper's best one-line statement of the market failure: the externality
is not merely that **your competitor's entry consumes your retraining budget**
but that **your competitor's choice of vendor does too**, without their entering
at all and without either firm doing anything wrong.

**The lever's price, in one sentence.** Cadence buys stability with model
staleness: the same `c^K` that delivers stability is the lag between the
deployed model and the current best response. Quantify it rather than presenting
the lever as free. A reviewer who notices this before the paper says it will
assume the paper missed it.

## Figure 2

The `(N_eff, K)` plane. Measured joint-loop stability, converge or diverge per
cell on common-random-number seeds, against the predicted frontier, with `s`
contours overlaid and the critical-crowding column where the window closes. One
panel, fully falsifiable.

Note in the caption that `K` is an integer, so the realized window is
`floor(K_max)` while the plotted frontier is continuous.

## Checklist

- [ ] `c = 0.8` stated wherever the worked numbers appear
- [ ] The composition credited as a composition, not presented as difficult
- [ ] Critical crowding given in both forms, the `m_N` bound and the `(1+c)/(1-c)`
      multiplier
- [ ] The staleness tradeoff stated, not omitted
- [ ] Integer-`K` caveat in the figure caption
