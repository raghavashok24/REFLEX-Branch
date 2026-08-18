# 6. Result 3: herd immunity, and diversity as its substitute

**Status: planned.** Target 1.25 pages. Source:
`../math/03-theorem3-herd-immunity.md`.

**This is the paper.** If the build slips, everything else gives way before this
section does.

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

**Theorem 3.** In the strong-correction limit the unstable cycle runs through
blind firms only, so the market is stable if and only if the blind sub-ecosystem
is:

```
   m_1 ( 1 + kappa * s * (N_b - 1) )  <  1 ,
   N_b  <  N_c(s)  =  1 + (1/m_1 - 1)/(kappa*s) ,
   rho  >  rho*(s)  =  max( 0 , 1 - N_c(s)/N ) .
```

The derivation is one line worth giving in full, because it is unusually clean:
the blind block is itself a symmetric shared-pool market of size `N_b` with
effective spillover `kappa*s`, so the base theorem applies to it verbatim.
[DERIVED, and the closed form checked against dense eigensolves on 4000 random
draws with zero mismatches]

**The collapse.** At `kappa = s = 1`, `N_c = 1/m_1` and

```
   rho*  =  1 - 1/m_N ,
```

**exactly the epidemiological herd-immunity threshold `1 - 1/R_0`.** A market of
10 firms at `m_N = 2.5` needs 60% of them un-blinded.

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

**The exact version.** The finite-`gamma_PO` case replaces the clean formula
with the root of a two-block secular equation, a quadratic in closed form. Report
both. If the exact root is cut, the limit theorem plus simulation ships in its
place and the paper says so.

## Figures 3 and 4

**Figure 3, herd immunity.** Measured stability against corrected fraction in an
`m_N > 1` regime, with predicted `rho*` marked. Note that `rho* N` is generally
not an integer, so the realized threshold is `ceil(rho* N)` firms, which matters
at the small `N` the experiment runs at.

**Figure 4, the substitution frontier.** The `(rho, s)` iso-stability curve,
measured against predicted. **The headline figure and the one that goes on the
poster.**

**The free-riding diagnostic** (private P&L of corrected against blind firms)
sits in the appendix or in Figure 3's second panel, and is fourth in the
de-scope order.

## Checklist

- [ ] The threshold and the frontier presented together, threshold first
- [ ] Diekmann et al. cited where the analogy is claimed, not elsewhere
- [ ] The homogeneous-mixing assumption stated alongside the clean formula
- [ ] Both-goods-under-supplied sentence present
- [ ] Exact two-block root reported, or its absence stated
- [ ] Integer-threshold caveat in Figure 3's caption
- [ ] The experiment described as new in kind: the corrected loop has never run
      inside a multi-agent game
