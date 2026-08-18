# 3. Model, and private versus systemic stability

**Status: planned.** Target 1.25 pages. Sources: `../math/00-notation.md`, plan
of record Sections 3 and 4.

---

## What this section does

Two jobs, and the order matters. The framing comes first because it is the
paper's reason to exist at this venue, and the setup follows because it is what
makes the framing precise. A reviewer who reads only this section should be able
to state the paper's thesis and check its stability condition.

## 3.1 The base result, cited not derived

`N` symmetric dealers sharing one pool of informed flow with spillover
`kappa in [0,1]` have joint retraining Jacobian

```
   J  =  -m_1 [ (1 - kappa) I  +  kappa 1 1' ] ,
```

with a common mode at `-m_1 * N_eff`, `N_eff = 1 + kappa(N-1)`, and differential
modes at `-m_1(1-kappa)`. The common mode dominates, so the market destabilizes
a factor `N_eff` before any individual dealer's own loop would. Measured in a
shared-pool simulator: amplification `1.74x` at `N = 2` and `3.16x` at `N = 3`
against predicted `2` and `3` (REFLEX, arXiv:2608.16155). [VERIFIED, base
result]

Half a page at most. This is inherited scaffolding, and every line spent
re-deriving it is a line Section 4 does not get. State it, cite it, and move.

## 3.2 Private against systemic stability

The framing paragraph, and the one to write most carefully.

Two different questions: is each agent stable considered alone (`m_1 < 1`), and
is the collection stable when they interact (`m_N < 1`)? The shared environment
makes these different. Dealer A adapts, the pool changes, dealer B observes a
changed environment and adapts, which changes the pool again, which A retrains
on. **Agent count is not a descriptive market characteristic; it enters the
stability condition.** Systemic instability is an emergent property of the
interaction structure, not a property of any agent.

Then the externality reading, which is what makes it economics rather than
dynamics: no participant internalizes the effect of its adaptive behavior on the
environment other adaptive participants face. This is why "is this model stable
when deployed?" is the wrong certification question in a shared endogenous
environment, and why "is the ecosystem of interacting models stable?" is the
right one.

**Include here, in one sentence each:**

The externality is **technological, not pecuniary** (Buchanan and Stubblebine,
1962). The coupling runs through the data-generating process each learner faces,
not through the price at which the firms trade. Competitors affecting each other
through prices is not a market failure, and an economics reviewer will check
that the paper knows the difference.

Acknowledge the ancestor here rather than only in Section 2, because this is
where the reader will think of it: Beale et al. (2011) posed exactly this
question for banks that do not learn.

## 3.3 The reproduction number

`m_N` is the **feedback reproduction number** of the market: the factor by which
a common perturbation is amplified per retraining round. Below one, perturbations
die out; above one, they compound. Everything that follows is the economics of
controlling `R_0`, and Section 4 is about what actually determines it.

Introduce the name here, once, and let Sections 4 through 7 use it without
re-explaining. Planting it before Theorem 1 rather than after means the
herd-immunity result in Section 6 arrives as a consequence of a name the reader
already accepted, rather than as a surprise that needs defending.

## 3.4 Setup for the general case

The objects Theorem 1 needs, stated but not yet used: the per-firm response
Jacobian `E_i`, the alignment matrix `R`, and the replacement of `1 1'` by `R`
in the Jacobian. Keep this to a paragraph. The work happens in Section 4; this
is the definition list.

Standing assumptions get one compact paragraph: linearization around the joint
equilibrium with the simulator as the nonlinear check, equal moduli for the
exact identity, synchronous deployment on a common cadence, and a single shared
pool with scalar spillover. Each is repeated in Section 10 with its consequence.
Stating them here and honoring them later is cheaper than defending an omission.

## Figure budget

None. Section 4 gets the first figure. If a schematic of the six-step
externality loop would help a reader, it goes in the appendix, because at nine
pages a diagram that carries no measurement is not worth a column inch.

## Checklist

- [ ] Base result stated in half a page, cited, not re-derived
- [ ] Private-versus-systemic paragraph written before any algebra
- [ ] Technological-not-pecuniary sentence present
- [ ] The feedback reproduction number named before Theorem 1
- [ ] Standing assumptions listed compactly, each with a Section 10 counterpart
- [ ] The Perron-Frobenius condition on "the common mode binds" stated, per
      `../math/01-theorem1-alignment.md`
