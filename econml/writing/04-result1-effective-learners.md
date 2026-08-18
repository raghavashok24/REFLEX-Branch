# 4. Result 1: the effective number of independent learners

**Status: planned.** Target 1.25 pages. Source:
`../math/01-theorem1-alignment.md`, which holds the full derivation, the anchors
and the corrections.

---

## What this section does

Replaces headcount with alignment, and in doing so brings monoculture and the AI
supply chain into the paper. Everything downstream is stated in `m_N`, so this
section is what makes Sections 5 through 7 inherit the supply-chain parameter
`s` for free.

## Content, in order

**The alignment object.** `r_ij`, `R`, and the reading of `lambda_max(R)` as
running from 1 (orthogonal responses) to `N` (monoculture). One paragraph.

**Theorem 1.** `m_N = N_eff * m_1` with `N_eff = 1 + kappa(lambda_max(R) - 1)`,
with a two-line proof sketch: the substitution `1 1' -> R` makes the Jacobian's
spectrum a function of `R`'s spectrum, and the base result is the `R = 1 1'`
corner. [DERIVED]

**The anchors, as a compact table.** Monoculture recovers the base law and its
measured `1.74x / 3.16x`. Orthogonal responses give `m_N = m_1`, so a hundred
firms perturbing in a hundred orthogonal directions are dynamically one firm.
The simplex configuration puts `m_1(1-kappa)` in the spectrum, matching the base
theory's differential-mode eigenvalue derived by an entirely different route.

**State the simplex anchor correctly.** `m_1(1-kappa)` is in the spectrum, on
the all-ones direction, and is not the spectral radius, which is
`m_1(1 + kappa/(N-1))`. The plan of record has this wrong and the math note
records the correction. Two consequences belong in the body: the common mode
stops binding under anti-alignment, so the claim carries a Perron-Frobenius
condition ("no firm's feedback anti-aligns with another's", satisfied whenever
`R` has nonnegative entries, which shared vendors and shared corpora guarantee);
and the simplex becomes a second counterexample to mean-based diversity indices.

**The supply chain.** The decomposition
`E_i = sqrt(s) E_shared + sqrt(1-s) Xi_i`, the concentration `r_ij -> s` with
`O(1/d)` relative fluctuation, and

```
   N_eff  =  1 + kappa * s * (N - 1) .
```

Then the sentence the section exists for: **the effective number of learners is
the number of independent models, not the number of firms.**

**Why the naive index fails, with numbers.** The clustered topology, three
aligned firms among ten, gives `N_eff = 2.60` against `1.48` from the
mean-alignment index at `kappa = 0.8`, so a market at `m_1 = 0.5` is unstable
and the mean index calls it safe with margin. Add the simplex case in one
clause, because it makes a stronger point in fewer words: the mean does not
merely understate risk, it does not order configurations correctly. **Rule,
stated explicitly: all stability claims use the spectral form, never a mean.**

**The Herfindahl paragraph.** Concentration in the product market and
concentration in the model supply chain are different quantities, and only the
second enters the stability condition. Fifty equal-share firms have a minimal
HHI and, sharing one vendor, an `N_eff` of `1 + 49 kappa`. This is the most
policy-legible paragraph in the paper and it is cheap. It may arrive from
Section 1 if that section runs long.

**The scope line, stated honestly.** Theorem 1 is exact for equal moduli. The
mean-modulus generalization is provably false, since orthogonal responses give
`max_i m_i`. The correct object is `M^{1/2} R M^{1/2}`, giving
`max_i m_i <= rho(J) <= max_i m_i * N_eff`, exact in three stated limits, with
tightness measured rather than asserted. One remark, not a subsection.

**Deferred extensions, named in one sentence.** Share-weighted alignment needs a
majorization condition on the share vector, since the naive claim is false. The
fully heterogeneous block-secular reduction is journal material. Naming these
and moving on is what keeps the build inside its schedule, and a reviewer reads
it as scope control rather than as a gap.

## Figure 1

The `(N, s)` phase diagram: measured `m_N` over firms by shared-model fraction,
against the predicted boundary. The clustered companion panel sits beside it if
space allows and is fifth in the de-scope order.

## Checklist

- [ ] Simplex anchor stated correctly, not as the plan of record has it
- [ ] Perron-Frobenius condition on the binding mode stated in the body
- [ ] Both counterexamples to mean-based indices present, clustered and simplex
- [ ] The naming footnote lives in Section 2, not repeated here
- [ ] Heterogeneous-modulus bound stated as a remark with its three exact limits
- [ ] Deferred extensions named, not attempted
