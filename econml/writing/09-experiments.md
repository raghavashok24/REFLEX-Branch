# 9. Experiments

**Status: planned.** Target 1.00 page. Source:
`../ml-contributions/EXPERIMENT-SPECS.md`, which holds the full specs.

---

## What this section does

Six panels, each mapping to exactly one result. **State the mapping as a table**
so a referee can check coverage at a glance rather than reconstructing it from
prose. That table is worth the space it costs.

## The setup paragraph

All experiments run in a genuine `N`-dealer simulator that reduces bit-for-bit
to the single-dealer market at `N = 1`. CPU-only, deterministic from
`(config, seed)`, common random numbers on paired probes, every closed form
certified numerically against the theory module.

Under double-blind the simulator is described generically, with an
anonymized-artifact promise and no repository URL.

## The panels

| # | Panel | Tests | Figure |
|---|---|---|---|
| 1 | Amplification replication | base result | table |
| 2 | The `(N, s)` phase diagram | Theorem 1 | Fig 1 |
| 3 | The crowding-cadence frontier | Theorem 2 | Fig 2 |
| 4 | Herd immunity | Theorem 3 | Fig 3 |
| 5 | **The substitution frontier** | Theorem 3 | **Fig 4** |
| 6 | Over-adaptation | Theorem 4 | Fig 5 |

**Panel 1 is external validation, not a self-consistency check**, and the
section says so in those words. It reproduces the published `1.74x` at `N = 2`
and `3.16x` at `N = 3` against predicted `2` and `3`. Ships as a table, because
comparing to published numbers is easier to check in a table than in a plot.

**Panel 2** needs the heterogeneous-response environment, the one piece of new
infrastructure the paper requires. Its acceptance test is that it reduces to the
existing homogeneous environment at `R = 1 1'`, and that reduction is checked
before any measurement is taken from it. Say this in one sentence; it is the
kind of detail that buys a reviewer's trust cheaply.

**Panel 4 is new in kind.** The corrected retraining loop has only ever been run
single-dealer. This is the first time it runs inside a multi-agent game, and
either outcome is a result.

**Panel 5 is the paper.** Protected time in the build, never cut, and the figure
that goes on the poster.

## Reporting rules

Inherited and stated once, in a compact paragraph:

- Sweep the feedback gain, never the confounded adversariality parameter.
- Probe at the operating spread, with common random numbers.
- Multi-dealer runs can saturate the informed-flow cap; the liquidity boost is
  scaled down per the environment's guidance and never de-saturated silently.
- Beyond-boundary probe readings are diagnostics, not slopes.

State `c = 0.8` and every other parameter of the worked examples in the captions.
A table a reader cannot reproduce is worse than no table.

**Report disagreement where it occurs.** If a measured frontier departs from the
predicted one, the departure is the scope boundary of the linearized theory and
is reported as a result, not smoothed. The companion paper takes the same line on
its nonlinear drift curve, and it is the right one.

## Checklist

- [ ] Coverage table present
- [ ] Panel 1 labeled external validation
- [ ] Environment reduction test mentioned
- [ ] Every worked-example parameter stated in a caption, `c` included
- [ ] Protocol rules stated once, compactly
- [ ] Simulator described generically, no repository URL
