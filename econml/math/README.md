# Math

One note per theorem: statement, derivation, anchors that pin it, and the open
issues. These notes are where the algebra is settled before any of it reaches
`../writing/`.

| File | Covers |
|---|---|
| [`00-notation.md`](00-notation.md) | Symbol table, standing assumptions, what is inherited from REFLEX |
| [`01-theorem1-alignment.md`](01-theorem1-alignment.md) | The alignment matrix `R`, `N_eff`, the supply-chain map, the heterogeneous-modulus scope line |
| [`02-theorem2-cadence.md`](02-theorem2-cadence.md) | `mu_N(K)`, the cadence window `K_max`, critical crowding |
| [`03-theorem3-herd-immunity.md`](03-theorem3-herd-immunity.md) | Mixed-market stability, `rho*(s)`, the substitution frontier |
| [`04-theorem4-wedge.md`](04-theorem4-wedge.md) | Stationary variance, the Pigouvian wedge, over-adaptation |
| [`05-supervision.md`](05-supervision.md) | Critical slowing down, the public-price estimator (deferred) |

## Standing rules

**All stability claims use the spectral form, never a mean.** Mean alignment
understates clustered alignment and, as `01` shows, does not even order
configurations correctly: the configuration minimizing mean alignment is not
the configuration minimizing `lambda_max(R)`. Two independent counterexamples
are recorded there.

**Anchors before proofs.** Every closed form is checked against at least two
independently derived limits before it is written into the paper. Where an
anchor in the plan of record fails, the note says so and the claims ledger
records the correction.

**Nothing is claimed beyond what is derived or measured at submission time.**
Status flags are `[VERIFIED]`, `[DERIVED]`, `[TO BUILD]`, `[DEFERRED]`, and
they mean what `../README.md` says they mean.

## Corrections to the plan of record

Recorded here so they are not lost between the plan and the paper.

| Where | Issue | Resolution |
|---|---|---|
| Plan Section 5, Theorem 1 anchors | "maximal diversity (simplex responses) gives `m_1(1-kappa)`" is not the spectral radius | The simplex configuration matches `m_1(1-kappa)` on one eigenvalue, not on `lambda_max`. Its spectral radius is `m_1(1 + kappa/(N-1))`. Verified numerically and **the plan of record has been corrected**. Detail in [`01`](01-theorem1-alignment.md), evidence in [`verify_theorem1_anchors.py`](../ml-contributions/certificates/verify_theorem1_anchors.py) |
