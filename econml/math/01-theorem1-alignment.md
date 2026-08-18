# Theorem 1: the effective number of independent learners

The base result counts firms. Counting firms is wrong, and the correction is
where the monoculture and supply-chain content enters the paper.

## The alignment object

Let firm `i` have response Jacobian `E_i`, the `d x d` matrix describing how its
own deployment reshapes the flow it faces. Define

```
   r_ij  =  <vec E_i, vec E_j> / ( ||E_i||_F ||E_j||_F ) ,       R  =  (r_ij) .
```

`R` is a correlation matrix of models' *feedback directions*. It is positive
semidefinite with unit diagonal, so `tr R = N` and `lambda_max(R)` runs from `1`
(all responses orthogonal, every firm perturbs the environment its own way) to
`N` (monoculture, all firms perturb it identically).

## Statement

**Theorem 1.** With equal moduli `m_i = m_1` and heterogeneous response
*directions*, the joint retraining Jacobian is

```
   J  =  -m_1 [ (1 - kappa) I  +  kappa R ] ,
```

whose eigenvalues are `-m_1 [ (1 - kappa) + kappa * lambda_i(R) ]`. Hence

```
   m_N  =  N_eff * m_1 ,        N_eff  =  1 + kappa ( lambda_max(R) - 1 ) ,
```

and the market is stable iff `m_N < 1`, equivalently
`eps < (gamma/beta) / N_eff`. [DERIVED]

The base result is the `R = 1 1'` corner and nothing more.

## Anchors

Each checked independently. Two of the three are as the plan of record states
them. The third is not, and the correction is recorded below.

| Configuration | `R` | `lambda_max(R)` | `N_eff` | `m_N` |
|---|---|---|---|---|
| Monoculture | `1 1'` | `N` | `1 + kappa(N-1)` | matches base result and its measured `1.74x / 3.16x` |
| Orthogonal | `I` | `1` | `1` | `m_1` |
| Simplex (`r_ij = -1/(N-1)`) | `(N/(N-1)) I - (1/(N-1)) 1 1'` | `N/(N-1)` | `1 + kappa/(N-1)` | `m_1 (1 + kappa/(N-1))` |

**Anchor 1 (monoculture).** `lambda_max(1 1') = N`, so
`N_eff = 1 + kappa(N-1)`, recovering the base law exactly. [VERIFIED]

**Anchor 2 (orthogonal).** `lambda_max(I) = 1`, so `N_eff = 1` and `m_N = m_1`.
A hundred firms perturbing the environment in a hundred orthogonal directions
are dynamically one firm. [VERIFIED]

**Anchor 3 (simplex): the plan of record is wrong here, and the correction is
better.** The plan claims maximal diversity gives `m_1(1-kappa)`, "independently
matching the differential-mode eigenvalue". Recomputing:

```
   R_simplex  =  (N/(N-1)) I  -  (1/(N-1)) 1 1'
   spectrum:  0  on the all-ones direction
              N/(N-1)  on its orthogonal complement, multiplicity N-1
```

so the spectrum of `J` is `{ m_1(1-kappa) }` on the all-ones direction and
`{ m_1(1 + kappa/(N-1)) }` on the complement. The value `m_1(1-kappa)` **is**
in the spectrum and **does** match the base theory's differential-mode
eigenvalue, so the consistency check the plan wanted is real. It is not the
spectral radius. The spectral radius is `m_1(1 + kappa/(N-1))`.

Two things follow, both worth keeping.

*The mode labels swap.* Under monoculture the all-ones direction carries the
largest eigenvalue `N`. Under the simplex it carries eigenvalue `0` and is the
*most* stable direction, while the binding modes are the differential ones. So
standing assumption A5, "the common mode binds", is not universal. It holds when
`R` has nonnegative entries, where Perron-Frobenius puts the leading eigenvector
in the nonnegative orthant, and that is exactly the condition "no firm's
feedback anti-aligns with another's". Shared vendors and shared pretraining
corpora produce positive alignment, so the realistic regime satisfies it. State
the condition in the paper rather than assuming it silently. [DERIVED]

*A second, sharper counterexample to mean-based diversity indices.* The simplex
minimizes mean pairwise alignment: `sum_ij r_ij = || sum_i vec E_i ||^2 >= 0`
forces mean off-diagonal alignment `>= -1/(N-1)`, with equality iff the
responses sum to zero. So a mean-alignment index calls the simplex the most
diverse configuration available. Spectrally it is *worse* than orthogonality:
`N/(N-1) > 1`. The mean index does not merely understate risk, it does not order
configurations correctly. [DERIVED]

## The supply chain

Decompose each firm's response into shared and idiosyncratic parts,

```
   E_i  =  sqrt(s) * E_shared  +  sqrt(1-s) * Xi_i ,
```

with `s in [0,1]` the fraction attributable to a shared foundation model,
vendor, or pretraining corpus, and the `Xi_i` independent, mean-zero, and
independent of `E_shared`. Taking Frobenius inner products, the cross terms
vanish in expectation and

```
   r_ij  ->  s   (i != j) ,      R  ->  (1-s) I + s 1 1' ,
   lambda_max(R)  ->  1 + s(N-1) ,
```

with relative fluctuation `O(1/d)`, since the inner products average over `d^2`
matrix entries. Hence

```
   N_eff  =  1 + kappa * s * (N - 1) ,
   m_N    =  m_1 ( 1 + kappa * s * (N - 1) ) .
```

**The effective number of learners is the number of independent models, not the
number of firms.** Fifty dealers fine-tuning one vendor's model are dynamically
about `1 + 49 kappa` learners at `s` near one and barely more than one at `s`
near zero. The critical population generalizes from `N_c = 1/m_1` to a critical
surface in `(N, s)`, which is the paper's first figure. [DERIVED]

## The clustered counterexample, with numbers

The realistic topology is a vendor with a plurality, not a monopoly. Take
`N = 10` with three firms fully aligned and every other pair orthogonal:
`R = blockdiag(1 1' of size 3, I_7)`, so `lambda_max(R) = 3`.

Mean off-diagonal alignment is `3/45 = 0.0667`, since three of the forty-five
pairs are aligned. The uniform configuration with that same mean has
`lambda_max = 1 + 0.0667 * 9 = 1.6`.

At `kappa = 0.8`:

| | `lambda_max(R)` | `N_eff` | destabilizes at |
|---|---|---|---|
| Clustered (true) | `3.0` | `2.60` | `m_1 = 0.385` |
| Uniform, same mean | `1.6` | `1.48` | `m_1 = 0.676` |

A market at `m_1 = 0.5` is unstable, and a mean-similarity index calls it safe
with margin. The understatement in `N_eff` is a factor of `1.76`. This panel is
experiment 2's companion. [DERIVED by counterexample]

**Rule, stated in the paper and enforced in every note here: all stability
claims use the spectral form, never a mean.**

## Heterogeneous moduli: the scope line

With `M = diag(m_i)` the joint Jacobian is `J = -M[(1-kappa)I + kappa R]`, which
is not symmetric but is similar (via `M^{1/2}`, valid for `m_i > 0`) to

```
   A  =  (1 - kappa) M  +  kappa M^{1/2} R M^{1/2} ,
```

so `rho(J) = lambda_max(A)`. The tempting mean-modulus formula is **provably
false**: at `R = I` we get `A = M` and `rho = max_i m_i`, not the mean.

Two-sided bound, from Weyl and from `e_i' A e_i = m_i`:

```
   max_i m_i   <=   rho(J)   <=   ( max_i m_i ) * N_eff .
```

Limits, each checked:

| Limit | Lower | Upper | Truth |
|---|---|---|---|
| `kappa = 0` | `m_max` | `m_max` | exact |
| Equal moduli | `m_1` | `m_1 N_eff` | upper is exact |
| `R = I` | `m_max` | `m_max` | exact |

Stated in the paper as a remark with the bound. Tightness is measured in
simulation, not asserted. [DERIVED]

## Deferred extensions

Named in the body, not attempted. Saying so is what keeps this plan inside
twelve days.

- **Share-weighted alignment** for unequal-sized firms. The honest version needs
  a majorization condition on the share vector, because the naive claim "any
  reweighting raises `lambda_max`" is false.
- **The exact block-secular reduction** for fully heterogeneous ecosystems.
- **Non-separable spillover** `kappa_ij`, which folds into `R` only when it
  factors.

[DEFERRED]

## Naming, and the defensive footnote

`lambda_max(R)` is called the effective number of independent learners, and the
paper does not present the *quantity* as new, only its role. Spectral summaries
of a correlation matrix have a long history as effective counts: participation
ratio and inverse participation ratio in physics, effective rank in signal
processing, Hill numbers in ecology, and the leading-eigenvalue market mode in
the random-matrix-theory finance literature, where `lambda_max` of a return
correlation matrix already reads as the strength of the common factor.

Conceding this costs one footnote and disarms the cheapest available referee
objection, which is "you renamed effective rank". What is new is the object it
is computed from, response Jacobians rather than returns, and the condition it
enters. See literature cluster F.

## Open items

1. Prove the `O(1/d)` concentration statement at the level of a bound, not an
   expectation. Currently stated in expectation. [TO BUILD]
2. Certificate for the simplex spectrum, since it is now a correction to the
   plan rather than a confirmation of it. [TO BUILD]
3. Decide whether the Perron-Frobenius condition on A5 goes in the body or a
   footnote. Leaning body, one sentence, because it is cheap and a spectral
   referee will look for it.
