# Numerical certificates

Every closed form in the paper ships a numerical certificate in the base
project's verification layer, which currently holds 66. This paper adds the
following. The count is deliberately small: one certificate per closed form,
plus one per anchor that could regress.

A certificate is a deterministic check with a stated tolerance that fails loudly.
It is not a unit test of the implementation; it is evidence that the closed form
is the thing the simulator does.

## Theorem 1

| # | Checks | Tolerance | State |
|---|---|---|---|
| C1 | `n_eff(1 1', kappa)` equals the base law `1 + kappa(N-1)`, `N` in `2..50` | machine | **run** |
| C2 | `n_eff_supply_chain` equals `n_eff(supply_chain_R(...))`, two routes to one number | machine | |
| C3 | `n_eff(I, kappa) == 1`, so orthogonal responses are dynamically one firm | machine | **run** |
| C4 | **Simplex spectrum.** `lambda_max(R_simplex) == N/(N-1)`, and `m_1(1-kappa)` is in the Jacobian's spectrum but is not its radius. Also the ordering failure: simplex has lower mean alignment and higher `lambda_max` than orthogonality | machine | **run** |
| C5 | **Clustered counterexample.** `N_eff` from `lambda_max` exceeds `N_eff` from the mean-alignment index by 1.757 at `kappa = 0.8` | `1e-12` | **run** |
| C6 | **Concentration.** `r_ij -> s` as `d` grows, with the residual scaling as `O(1/d)` | fit, `R^2 > 0.95` | |
| C7 | Heterogeneous-modulus bounds hold: `max_i m_i <= rho(J) <= max_i m_i * N_eff`, on random draws, exact in the three stated limits | machine at limits | |

C1, C3, C4 and C5 are implemented in
[`certificates/verify_theorem1_anchors.py`](certificates/verify_theorem1_anchors.py)
and have been run. C4 exists because the plan of record stated this anchor
incorrectly; the plan has since been corrected, so C4 is now a regression guard
against reverting to the wrong version rather than a live disagreement.

The script checks the simplex two independent ways: analytically from
`R_simplex`, and constructively from actual unit response vectors summing to
zero. The constructive path is the load-bearing one, since it rules out the
result being an artifact of how the matrix was written down, and it reproduces
the analytic form to `4e-16`.

**Outstanding on this file:** the script is written as a standalone report, not
as an assertion-based check that fails loudly, which is what the definition at
the top of this document requires. Convert it and fold it into the base
project's verification layer. [TO BUILD]

## Theorem 2

| # | Checks | Tolerance |
|---|---|---|
| C8 | `is_stable_lazy(m_N, c, K)` agrees with `K < k_max(m_N, c)` on every integer `K` in `1..200` across an `(m_N, c)` grid | exact, boolean |
| C9 | `k_max` is decreasing in `m_N` | exact, monotone |
| C10 | No integer `K >= 1` is stable once `m_N > (1+c)/(1-c)` | exact, boolean |
| C11 | The worked table reproduces: `K_max` of `20.68 / 5.28 / 2.53` at `s = 0.25 / 0.5 / 1` with `m_1 = 0.15`, `kappa = 0.8`, `N = 30`, `c = 0.8` | `1e-2` |
| C12 | `c` is invariant to `N`, so the inner contraction is genuinely own-objective curvature | `1e-10` |

C12 is the one that catches a broken composition, and it is the certificate the
open item in the math note asks for.

## Theorem 3

| # | Checks | Tolerance |
|---|---|---|
| C13 | Limit case: `mixed_market_radius` with `gamma_ratio -> 0` converges to the blind-block radius | `1e-8` |
| C14 | `rho_star` predicts the stability sign change on 4000 random `(m_1, kappa, s, N_b)` draws against dense eigensolves, zero mismatches | exact, boolean |
| C15 | Herd-immunity collapse: at `kappa = s = 1`, `rho_star == 1 - 1/m_N` | machine |
| C16 | `rho_star` is increasing in `s`, which is what makes diversity and correction substitutes | exact, monotone |
| C17 | The worked thresholds reproduce: `0.596 / 0.242 / 0` at `s = 1 / 0.5 / 0.2` with `N = 20`, `m_1 = 0.15`, `kappa = 0.8` | `1e-3` |
| C18 | The strong-correction limit is approached from the stable side, so the limit theorem is conservative | sign check |

C14 was already run before the plan of record was written, with zero mismatches.
It is recorded here so it ships with the paper rather than living only in the
plan's prose.

C18 answers an open item in the math note. If it fails, the paper must state
which direction the approximation errs in, so a failure is informative rather
than fatal.

## Theorem 4

| # | Checks | Tolerance |
|---|---|---|
| C19 | The common mode's stationary variance equals `sigma^2/(1 - m_N^2)`, including the sign convention on `-m_N` | `1e-6` |
| C20 | `pigouvian_wedge` is increasing in `N`, in `kappa`, and in `m_N` | exact, monotone |
| C21 | Over-adaptation: the decentralized equilibrium exceeds the social optimum for every `N >= 2` on a grid | exact, sign |

## Running total

21 new certificates against the base project's 66, for 87. Every one of them is
deterministic, CPU-only, and runs from `(config, seed)`.

## Rule

A closed form that reaches the paper without a passing certificate is stated at
`[DERIVED]`, never at `[VERIFIED]`. The claims ledger in `../writing/` is the
enforcement point, and the status flag in the paper must match the ledger entry,
which must match this table.
