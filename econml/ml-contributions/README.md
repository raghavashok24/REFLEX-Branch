# ML contributions

Code, experiments and certificates. Specs live here; the implementation lands in
the REFLEX repository under its own module layout and is referenced by path, not
copied.

| File | Covers |
|---|---|
| [`THEORY-MODULE-SPEC.md`](THEORY-MODULE-SPEC.md) | The closed-form module: every function, its signature, its certificate |
| [`EXPERIMENT-SPECS.md`](EXPERIMENT-SPECS.md) | Six panels, each mapped to exactly one result |
| [`CERTIFICATES.md`](CERTIFICATES.md) | Numerical certificates added to the base project's verification layer |

## Inherited infrastructure

From REFLEX, used as cited scaffolding rather than re-derived:

- Closed-form theory modules for the single-dealer modulus `m_1 = eps*beta/gamma`
  and the symmetric multi-dealer law
- A genuine `N`-dealer simulator that reduces bit-for-bit to the single-dealer
  market at `N = 1`
- Four retraining loop modes including `perfgd_structural`, the corrected update
  that Result 3 puts into the game for the first time
- A verification layer of 66 numerical certificates, extended by this paper
- Real-data calibration on a 212-CUSIP corporate-bond panel, 1990 to 2026, with
  honest provenance: public proxies, not trade-level TRACE

## Protocol rules, inherited and non-negotiable

These are carried over verbatim because violating any of them silently
invalidates a panel.

- Sweep the feedback gain, never the confounded adversariality parameter.
- Probe at the operating spread, with common random numbers.
- Multi-dealer runs can saturate the informed-flow cap. Scale the liquidity
  boost down per the environment's guidance and never de-saturate silently.
- Beyond-boundary probe readings are diagnostics, not slopes.
- Everything is CPU-only and deterministic from `(config, seed)`.

## Build order

The theory module first, because every experiment checks itself against it. Then
the heterogeneous-response environment, whose acceptance test is that it reduces
to the existing homogeneous environment at `R = 1 1'`. Then the panels, in the
order given in the experiment specs.
