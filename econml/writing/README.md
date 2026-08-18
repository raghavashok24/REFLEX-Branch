# Writing

Paper content in markdown, one file per section. LaTeX happens once at the end,
from these files. Nothing here is LaTeX.

## Page budget (9 pages main body)

| File | Section | Pages | State |
|---|---|---|---|
| [`00-abstract.md`](00-abstract.md) | Abstract | 0.15 | drafted |
| [`01-introduction.md`](01-introduction.md) | Introduction | 1.25 | **complete** |
| [`02-related-work.md`](02-related-work.md) | Related work | 0.75 | planned |
| [`03-model-and-framing.md`](03-model-and-framing.md) | Setup, private vs systemic stability | 1.25 | planned |
| [`04-result1-effective-learners.md`](04-result1-effective-learners.md) | Theorem 1, the supply chain | 1.25 | planned |
| [`05-result2-cadence-frontier.md`](05-result2-cadence-frontier.md) | Theorem 2 | 1.00 | planned |
| [`06-result3-herd-immunity.md`](06-result3-herd-immunity.md) | Theorem 3, the substitution frontier | 1.25 | planned |
| [`07-result4-pigouvian-wedge.md`](07-result4-pigouvian-wedge.md) | Theorem 4 | 0.75 | planned |
| [`08-supervision.md`](08-supervision.md) | Supervision from public prices | 0.20 | planned, first to cut |
| [`09-experiments.md`](09-experiments.md) | Six panels | 1.00 | planned |
| [`10-limitations-conclusion.md`](10-limitations-conclusion.md) | Limitations, conclusion | 0.60 | planned |
| | **Total** | **9.45** | over budget by 0.45, see below |

Overflow is expected at this stage and is absorbed in the following order:
proofs and derivation sketches move to the appendix first, then Section 8
collapses to two sentences, then Section 7's comparative statics move to the
appendix. Result sections 4 through 6 are not compressed.

## Figures

Five figures in the body, one per result plus the headline. Figure budget is
tight at 9 pages, so each figure earns its place by being the falsifiable test
of exactly one closed form.

| Fig | Content | Section |
|---|---|---|
| 1 | The `(N, s)` phase diagram, measured `m_N` against the predicted boundary | 4 |
| 2 | The `(N_eff, K)` stability grid against predicted `K_max`, `s` contours overlaid | 5 |
| 3 | Herd immunity: measured stability against corrected fraction `rho`, predicted `rho*` marked | 6 |
| 4 | **The substitution frontier**, `(rho, s)` iso-stability curve. The poster figure | 6 |
| 5 | Over-adaptation: decentralized against socially optimal aggressiveness | 7 |

The amplification replication (experiment 1) is a table, not a figure. It is an
external validation checkpoint against a prior published run, and a table makes
the comparison to the published `1.74x / 3.16x` easier to check than a plot.

## Claims

Every numbered claim in the paper is tracked in
[`CLAIMS-LEDGER.md`](CLAIMS-LEDGER.md) with its status flag and its evidence.
Nothing ships at a status stronger than its ledger entry.

## Rules for this folder

- ASCII math, matching the plan of record and `../math/00-notation.md`.
- No em dashes. Run `prose-guard` before any commit that touches prose.
- Double-blind: no first-person reference to REFLEX or PEBSA, ever. Both are
  cited as ordinary third-party references.
- Every claim carries a status flag inline the first time it is stated.
