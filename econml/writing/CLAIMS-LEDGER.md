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

Proofs in [`../math/derivations/01-alignment-spectrum.md`](../math/derivations/01-alignment-spectrum.md)
and [`../math/derivations/02-supply-chain-concentration.md`](../math/derivations/02-supply-chain-concentration.md).

| # | Claim | Status | Evidence |
|---|---|---|---|
| 4.0 | **Reduction:** `J = -m_1[(1-kappa)I + kappa R]` follows from the response Jacobians under (H1) to (H4) | `[VERIFIED]` | `derivations/01` Lemma 1; C22, agreement `5.6e-17` |
| 4.1 | `m_N = m_1 (1 + kappa(lambda_max(R) - 1))` for equal moduli | `[VERIFIED]` | `derivations/01` Thm 1; C1, C2, C3, C23. 384 configurations |
| 4.2 | Monoculture corner recovers the base law | `[VERIFIED]` | C1 |
| 4.3 | Orthogonal responses give `m_N = m_1` | `[VERIFIED]` | C3 |
| 4.4 | Simplex spectrum contains `m_1(1-kappa)`; radius is `m_1(1+kappa/(N-1))` | `[VERIFIED]` | C4, run. **Plan of record corrected to match** |
| 4.5 | The binding mode is the common one iff `R` has nonnegative entries | `[DERIVED]` | Perron-Frobenius; `derivations/01` Prop 2; C22 |
| 4.6 | Supply chain: `N_eff = 1 + kappa*s*(N-1)` | `[VERIFIED]` | `derivations/02`; C2, C6 |
| 4.7 | `r_ij -> s` with `O(1/d)` fluctuation, **as a probability bound** | `[VERIFIED]` | `derivations/02` Lemma 5 and Prop 6; C6, fitted exponent `-1.018`. **Open item closed** |
| 4.8 | Clustered counterexample: `N_eff` 2.60 against 1.48 by the mean index | `[VERIFIED]` | C5, run. Factor 1.757 |
| 4.9 | Mean alignment does not order configurations correctly | `[VERIFIED]` | C4, run. Simplex against orthogonal at `N` in {5,10,30} |
| 4.10 | Heterogeneous moduli: `max_i m_i <= rho(J) <= max_i m_i * N_eff` | `[VERIFIED]` | `derivations/01` Prop 4; C7, 300 draws, exact in three limits |
| 4.11 | Share-weighted alignment, fully heterogeneous reduction | `[DEFERRED]` | named, not attempted |
| 4.12 | **`N_eff >= 1`, so `rho(J) >= m_1`:** interaction never stabilizes a market below what its members achieve alone | `[VERIFIED]` | `derivations/01` Cor 1.2; C23. Notation table corrected |
| 4.13 | **The mean index errs with a sign:** `N_eff >= 1 + kappa(N-1)*mean` for every `R`, so it under-states risk and never over-states it | `[VERIFIED]` | `derivations/01` Prop 3; C24, 360 draws, zero violations |
| 4.14 | The sharp operator-norm concentration rate `sqrt(N)/d` | `[DEFERRED]` | crude `N/d` bound proved; sharp rate measured, not proved |

## Section 5, Theorem 2

Proof in [`../math/derivations/03-cadence-composition.md`](../math/derivations/03-cadence-composition.md).

| # | Claim | Status | Evidence |
|---|---|---|---|
| 5.0 | **Inner loop:** `K` gradient steps contract to the frozen best response by `c^K`, `c = 1 - eta*gamma` | `[VERIFIED]` | `derivations/03` Lemma 7; measured from actual GD |
| 5.1 | `mu_N(K) = -m_N + c^K(1+m_N)`, from `M_K = c^K I + (1-c^K)J` | `[VERIFIED]` | `derivations/03` Thm 2; C12, C25 |
| 5.2 | `K_max = ln((m_N-1)/(m_N+1))/ln c`, decreasing in `m_N` and in `s` | `[VERIFIED]` | C8 (51600 cases), C9 |
| 5.3 | Critical crowding at `m_N = (1+c)/(1-c)`, factor 9 at `c = 0.8` | `[VERIFIED]` | `derivations/03` Cor 10.3; C10, sharp at five `c` |
| 5.4 | Worked window: `20.68 / 5.28 / 2.53` at `s = 0.25 / 0.5 / 1`, at `c = 0.8` | `[VERIFIED]` | C11 |
| 5.5 | `c` is invariant to `N` | `[VERIFIED]` | C12, spread `4.4e-16`. **The one place the composition could fail** |
| 5.6 | **The upper side of `\|mu_N\| < 1` never binds, and the lower binds at `lambda_max`,** by monotonicity rather than by sign pattern | `[VERIFIED]` | `derivations/03` Prop 9; C25 |
| 5.7 | Equivalent form: stable iff `m_N < (1+c^K)/(1-c^K)`, of which critical crowding is the `K = 1` case | `[VERIFIED]` | `derivations/03` Thm 10; C8 |
| 5.8 | Realized window is `floor(K_max)`, the plotted frontier continuous | `[VERIFIED]` | C8 |
| 5.9 | The simulated joint loop lands on the predicted side of the frontier | `[VERIFIED]` | C26, 59 decisive trials, zero disagreements |
| 5.10 | Heterogeneous `K_i` across firms | `[DEFERRED]` | breaks the eigenvector sharing the proof uses |

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

1. ~~**4.7** is stated in expectation and needs a concentration bound.~~
   **Closed.** `../math/derivations/02` proves the entrywise bound and its
   spectral consequence with an explicit failure probability. The sharp
   operator-norm rate is now tracked separately as 4.14, `[DEFERRED]`.
2. **6.7** and **6.8** are the two outstanding pieces of Theorem 3. 6.8 is the
   more important one, because a failure changes what the paper claims rather
   than only what it proves.
3. **7.1** and the welfare page are the whole of Theorem 4's remaining work.
4. Every `[TO BUILD]` experiment. Until a panel runs, the claim it tests holds
   at `[DERIVED]` and the paper must not imply measurement.

## Note on the Section 4 and 5 upgrades

Sections 4 and 5 moved from `[DERIVED]` to `[VERIFIED]` on 18 Aug 2026, when the
proofs in `../math/derivations/` landed with assertion-based certificates rather
than report-printing scripts. The standing rule is satisfied: each upgraded claim
names a certificate that fails loudly, and every one of them has been run. Claims
still resting on argument rather than computation (4.5's Perron-Frobenius
condition) stay at `[DERIVED]`, and the two genuinely open pieces (4.14, 5.10) are
tracked as `[DEFERRED]` rather than quietly dropped.

## Standing rule

**A closed form that reaches the paper without a passing certificate ships at
`[DERIVED]`, never at `[VERIFIED]`.** The temptation to round up appears during
the writing week, which is why the rule is written down now.
