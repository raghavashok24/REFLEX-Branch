# Claims ledger

Every numbered claim the paper makes, its status flag, and its evidence. **The
flag in the paper must match the flag here, which must match the certificate
table in `../ml-contributions/CERTIFICATES.md`.** Nothing ships at a status
stronger than its ledger entry.

Reviewed as a pass of its own before freeze, against the built PDF rather than
the source, because a status flag that drifted during writing is invisible in a
diff.

## Status flags

- `[VERIFIED]` follows from certified base results, or checked numerically
- `[DERIVED]` worked out for this paper, derivation recorded, low proof risk
- `[TO BUILD]` new experiment or configuration, not yet run
- `[DEFERRED]` stated in the body, completed for the journal version

---

## Section 3, background

| # | Claim | Status | Evidence |
|---|---|---|---|
| 3.1 | Symmetric multi-dealer law, common mode at `-m_1 N_eff` | `[VERIFIED]` | base result, REFLEX |
| 3.2 | Measured amplification `1.74x` at `N=2`, `3.16x` at `N=3` | `[VERIFIED]` | base result; replicated in panel 1 |
| 3.3 | The externality is technological, not pecuniary | argument | Buchanan and Stubblebine, 1962 |

## Section 4, Theorem 1

| # | Claim | Status | Evidence |
|---|---|---|---|
| 4.1 | `m_N = m_1 (1 + kappa(lambda_max(R) - 1))` for equal moduli | `[DERIVED]` | `../math/01`; certificates C1, C2, C3 |
| 4.2 | Monoculture corner recovers the base law | `[VERIFIED]` | C1 |
| 4.3 | Orthogonal responses give `m_N = m_1` | `[VERIFIED]` | C3 |
| 4.4 | Simplex spectrum contains `m_1(1-kappa)`; radius is `m_1(1+kappa/(N-1))` | `[VERIFIED]` | C4, run. **Plan of record corrected to match** |
| 4.5 | The binding mode is the common one iff `R` has nonnegative entries | `[DERIVED]` | Perron-Frobenius; `../math/01` |
| 4.6 | Supply chain: `N_eff = 1 + kappa*s*(N-1)` | `[DERIVED]` | C2, C6 |
| 4.7 | `r_ij -> s` with `O(1/d)` relative fluctuation | `[DERIVED]` in expectation | C6. **Open: needs a bound, not an expectation** |
| 4.8 | Clustered counterexample: `N_eff` 2.60 against 1.48 by the mean index | `[VERIFIED]` | C5, run. Factor 1.757 |
| 4.9 | Mean alignment does not order configurations correctly | `[VERIFIED]` | C4, run. Simplex against orthogonal at `N` in {5,10,30} |
| 4.10 | Heterogeneous moduli: `max_i m_i <= rho(J) <= max_i m_i * N_eff` | `[DERIVED]` | C7, exact in three limits |
| 4.11 | Share-weighted alignment, fully heterogeneous reduction | `[DEFERRED]` | named, not attempted |

## Section 5, Theorem 2

| # | Claim | Status | Evidence |
|---|---|---|---|
| 5.1 | `mu_N(K) = -m_N + c^K(1+m_N)` | `[DERIVED]` | `../math/02`; C12 |
| 5.2 | `K_max = ln((m_N-1)/(m_N+1))/ln c`, decreasing in `m_N` | `[DERIVED]` | C8, C9 |
| 5.3 | Critical crowding at `m_N = (1+c)/(1-c)`, factor 9 at `c = 0.8` | `[DERIVED]` | C10 |
| 5.4 | Worked window: `20.7 / 5.3 / 2.5` at `s = 0.25 / 0.5 / 1` | `[VERIFIED]` by recomputation | C11 |
| 5.5 | `c` is invariant to `N` | `[DERIVED]` | C12. **The one place the composition could fail** |

## Section 6, Theorem 3

| # | Claim | Status | Evidence |
|---|---|---|---|
| 6.1 | Strong-correction limit: stability iff the blind block is stable | `[DERIVED]` | `../math/03`; C13 |
| 6.2 | `rho*(s) = max(0, 1 - N_c(s)/N)` | `[VERIFIED]` numerically | C14, 4000 draws, zero mismatches |
| 6.3 | Collapse to `rho* = 1 - 1/m_N` at `kappa = s = 1` | `[DERIVED]` | C15 |
| 6.4 | The `R_0` correspondence is structural, both being spectral radii | argument | Diekmann et al., 1990 |
| 6.5 | `rho*` increasing in `s`, so diversity and correction are substitutes | `[DERIVED]` | C16 |
| 6.6 | Worked thresholds: `0.596 / 0.242 / 0` at `s = 1 / 0.5 / 0.2` | `[VERIFIED]` by recomputation | C17 |
| 6.7 | Exact two-block secular root | `[TO BUILD]` | third in de-scope order |
| 6.8 | The limit is approached from the stable side | `[TO BUILD]` | C18. **If it fails, say which way it errs** |
| 6.9 | Correction is a public good, under-supplied in equilibrium | argument | Bergstrom, Blume and Varian, 1986 |

## Section 7, Theorem 4

| # | Claim | Status | Evidence |
|---|---|---|---|
| 7.1 | Stationary variance proportional to `1/(1-m_N^2)` | `[TO BUILD]` | C19 |
| 7.2 | Private FOC ignores `(N-1)/N` of marginal cost, plus client exposure | `[DERIVED]` | `../math/04`. **Welfare page outstanding** |
| 7.3 | Wedge increasing in `N`, `kappa`, and proximity to boundary | `[DERIVED]` | C20 |
| 7.4 | Over-adaptation for every `N >= 2` | `[DERIVED]` | C21 |
| 7.5 | Provenance channel `dm_N/ds = m_1 kappa (N-1)` | `[DERIVED]` | `../math/04` |

## Section 8, supervision

| # | Claim | Status | Evidence |
|---|---|---|---|
| 8.1 | PC1 lag-1 autocorrelation tends to one as `m_N -> 1` | `[DEFERRED]` | estimator not yet formal |
| 8.2 | Variance share grows like `1/(1-m_N)` | `[DEFERRED]` | |
| 8.3 | Real-data panel is consistency evidence, not identification | stated as such | placebo required |

## Experiments

| # | Panel | Status |
|---|---|---|
| E1 | Amplification replication | `[TO BUILD]`, external validation |
| E2 | `(N, s)` phase diagram | `[TO BUILD]`, needs the heterogeneous-response environment |
| E3 | Crowding-cadence frontier | `[TO BUILD]` |
| E4 | Herd immunity | `[TO BUILD]`, new in kind |
| E5 | Substitution frontier | `[TO BUILD]`, **never cut** |
| E6 | Over-adaptation | `[TO BUILD]`, second in de-scope order |

---

## Open items blocking a status upgrade

1. **4.7** is stated in expectation and needs a concentration bound before it
   can be called `[DERIVED]` without qualification.
2. **6.7** and **6.8** are the two outstanding pieces of Theorem 3. 6.8 is the
   more important one, because a failure changes what the paper claims rather
   than only what it proves.
3. **7.1** and the welfare page are the whole of Theorem 4's remaining work.
4. Every `[TO BUILD]` experiment. Until a panel runs, the claim it tests holds
   at `[DERIVED]` and the paper must not imply measurement.

## Standing rule

**A closed form that reaches the paper without a passing certificate ships at
`[DERIVED]`, never at `[VERIFIED]`.** The temptation to round up appears during
the writing week, which is why the rule is written down now.
