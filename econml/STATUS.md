# Status: EconML @ NeurIPS 2026

**As of 18 Aug 2026. Submission 29 Aug 2026, 11 days out.**

Paper: "Herd Immunity and Learning Externalities in Markets of Adaptive Models".
9 pages main body, unlimited appendix, double-blind, in-person.

---

## One-paragraph summary

The theory is done and certified: all four results now have complete proofs,
Theorem 4's welfare page having landed on 18 Aug 2026. The infrastructure is done: the
closed-form module and the heterogeneous-response environment both exist and pass
acceptance tests. Five of six panels have run as dry runs against the reference
environment and agree with the closed forms, and **panel 1's anchor is now
measured in the real order-flow market, reproducing the published run bit for
bit**. **The gap is empirical and editorial**: the heterogeneous-response port now has a
fixed design and a skeleton that reduces exactly to the known case, but no
heterogeneous sweep has been run, and seven of eleven paper sections are
unwritten.

## Where the time went, and what it bought

The build found one result that changed the paper. Theorem 3's strong-correction
limit is **optimistic, not conservative**: it under-states the spectral radius and
calls roughly one configuration in eight stable when it is not. That was caught
because the claims ledger flagged it in advance as the claim whose failure would
matter most, and it was checked before the section was written rather than after.

The repair is larger than the damage. The exact threshold is the epidemiological
**imperfect-vaccine coverage law**, and it carries a **critical efficacy** below
which correction stops working at any coverage. So the `R_0` correspondence now
transfers a refinement of the law rather than just the law, which is much stronger
evidence it is structural. The exact two-block root left the de-scope order as a
consequence.

---

## Done

### Theory, all proved and certified

| Theorem | Proof | Certificate |
|---|---|---|
| 1, effective number of independent learners | `math/derivations/01`, `02` | 123 checks |
| 2, crowding-cadence frontier | `math/derivations/03` | 59 checks |
| 3, mixed market and herd immunity | `math/derivations/04` | 70 checks |
| 4, Pigouvian wedge | `math/04-theorem4-wedge.md` | 125 checks |

519 assertions across seven assertion-based files, all passing:

```bash
for f in econml/ml-contributions/certificates/verify_*.py; do python "$f" || break; done
```

### Results the build added beyond the plan of record

The reduction lemma, deriving the joint Jacobian from response Jacobians instead
of asserting the substitution. `N_eff >= 1`, so interaction never stabilizes a
market below what its members achieve alone. The mean-alignment index proved to
be a lower bound with a signed error, so it under-states risk and never
over-states it, which replaces two counterexamples with one theorem. The exact
two-block root. The imperfect-correction law and its critical efficacy. A
supply-chain concentration bound that holds with probability rather than in
expectation.

### Infrastructure

| Piece | State |
|---|---|
| Theory module, `ml-contributions/theory/` | Theorems 1 to 3 complete, 50 acceptance checks. `pigouvian_wedge` still absent by design, until panel 6 exists |
| Heterogeneous-response environment, `ml-contributions/environment/` | 32 acceptance checks, reduction verified |
| Panel harness, `ml-contributions/experiments/` | panels 1 to 5, exits nonzero on disagreement |
| Simulator port, `experiments/hetero_simulator_port.py` | **design fixed, skeleton reduces exactly**; no sweep run |

### Panels, as dry runs only

| Panel | Outcome |
|---|---|
| 1, amplification | reduction exact to `5.6e-16`; **external anchor closed, `[MEASURED]`** |
| 2, `(N, s)` phase diagram | 48 cells, max error `7.1e-15` |
| 2b, clustered companion | measured `m_N` `1.30`, mean index reports `0.74` |
| 3, cadence frontier | 175 cells, zero disagreements |
| 4, herd immunity | `12 / 14 / 16 / 20` firms at efficacy `1.00 / 0.90 / 0.75 / 0.60` |
| 5, substitution frontier | 18 of 18 points exact |

**Panels 2 to 5 are not measurements.** They run in the linearized reference
environment, which has no informed flow, no spread and no inventory. They
establish that the closed forms govern realized dynamics and they fix every
figure's shape. They establish nothing about a market. The ledger tracks them at
`[DRY RUN]`, a status that deliberately does not license the paper to imply
measurement.

### Panel 1's external anchor, the one measured result

`ml-contributions/experiments/reflex_anchor.py` runs the base project's genuine
shared-pool market and **reproduces the published run bit for bit**, relative
error `0.00e+00`:

| `N` | measured `m_N` | amplification | linear prediction | gap |
|---|---|---|---|---|
| 1 | `0.785600` | `1.0000` | `1` | |
| 2 | `1.369162` | `1.7428` | `2` | `12.9%` |
| 3 | `2.479927` | `3.1567` | `3` | `5.2%` |

Differential mode `3.4e-03` against a theoretical `0`, so instability is purely
common-mode, which is the mechanism Theorem 1 generalizes.

This one panel could be closed today because its claim is the monoculture corner
`R = 1 1'`, which the base project already implements. The base project is
read-only throughout and the script skips cleanly when it is absent.

**The gap to the linear prediction is content, not error**, and the body should
say so: the prediction is a linearization and the market is nonlinear with
saturating flow. The reference environment reproduces the prediction exactly
because it omits both, which is the clearest available argument for why the
remaining panels need the simulator.

### Writing

| Section | State |
|---|---|
| 1, introduction | complete |
| 2, related work | drafted, four paragraphs, six named deltas |
| 3, model and framing | drafted, about 1200 words |
| 4, Result 1 | drafted, about 920 words |
| 5, Result 2 | drafted, about 580 words |
| 0, abstract | drafted, rewrite after Result 3's panel lands |
| 6, Result 3 | replanned around the exact root, not drafted |

---

## Not done

### Blocking, in priority order

**1. The simulator port, and it is a design problem rather than a port.** Panel 1
is done because its claim is the monoculture corner the base project already
implements. Panels 2 to 5 are not, and the reason is structural: the base
project's `env/multi_dealer.py` has **no concept of a per-dealer response
direction**. Every dealer shares one scalar toxic channel `exp(-c_t*h_i)` coupled
by a single scalar `kappa`, which *is* `R = 1 1'` and nothing else.

So porting is not wiring an existing knob to a new parameter. It requires
deciding what a heterogeneous response direction *means* in a real order-flow
market, whether that is different bond-factor exposures, different signal
channels, or different informed-flow segments, and then building the flow
generation that realizes a target alignment matrix. That is multi-session design
work, and the branch repository's environment is the specification it must
reduce to at `R = 1 1'`.

**The modeling decision is now made and recorded** in
`ml-contributions/environment/HETERO-SIMULATOR-PORT-DESIGN.md`: each dealer
carries a bond-space exposure profile, and both its contribution to the informed
pool and its sensing of that pool are routed through it, so the coupling matrix
becomes `(1-kappa)I + kappa R` with `R` the Gram matrix of the profiles. The
skeleton in `experiments/hetero_simulator_port.py` implements it and passes its
one acceptance test: at flat profiles it reproduces panel 1's published anchors
bit for bit, relative error `0.00e+00` at `N = 1, 2, 3`.

**No heterogeneous sweep has been run**, nothing is wired into `panels.py`, and
no claim changed status. What remains is the sweep itself, the second coupling
channel the design document flags (liquidity and price impact stay shared no
matter what the profiles are), and the universe-size question, since the default
config has only 8 bonds and 2 sectors and a larger universe would invalidate the
anchor. Every remaining `[MEASURED]` claim still depends on that work.

**2. ~~Theorem 4's welfare page.~~ Done, 18 Aug 2026.** The welfare page is
written in `math/04-theorem4-wedge.md`: the AR(1) welfare object with its sign
convention certified, Lemma 11 giving the marginal crowding share
`d m_N/d m_i = N_eff v_i^2`, both first-order conditions, the wedge, its
comparative statics, and over-adaptation for every `N >= 2`. Ledger claims 7.0 to
7.5 are `[VERIFIED]`; `verify_theorem4_wedge.py` passes with 125 assertions.

What remains on Theorem 4 is **panel 6 only**, which is second in the de-scope
order. `pigouvian_wedge` stays deliberately absent from the theory module, with a
test asserting its absence, so nothing can be measured ahead of its experiment.

**3. Five unwritten sections.** 6 Result 3, 7 Result 4, 8 supervision, 9
experiments, 10 limitations and conclusion. Sections 2 and 3 are drafted. Section
6 is the paper and is replanned but undrafted.

### Known open items, none blocking

The sharp operator-norm concentration rate, deferred to the journal version with
the crude bound proved and the sharp rate measured. Share-weighted alignment and
the fully heterogeneous block-secular reduction, both named and not attempted.
Heterogeneous cadences across firms, which breaks the eigenvector sharing
Theorem 2 uses. Three or more correction levels, which breaks Theorem 3's
two-block collapse.

---

## Risk register

| Risk | Severity | State |
|---|---|---|
| Heterogeneous-response port does not land in time | **high** | Design fixed and the skeleton reduces exactly to the base market. The sweep itself is not built, so the risk stands. Would cost panels 2 to 5 and leave a theory paper with one measured anchor |
| ~~Theorem 4 stays a sketch~~ | **closed** | Welfare page landed 18 Aug 2026 with 125 passing assertions. Only panel 6 is at risk now, and Theorem 4 ships as theory if it is cut |
| Section 6 drafting slips | medium | It is the paper. Replanned, so the drafting is transcription rather than design |
| A referee asks for fully heterogeneous agents | low | Answered as future work with the machinery stated to extend |
| A referee probes finite `gamma_PO` | **now low** | Was the paper's weakest point. The imperfect-correction law answers it directly |

## De-scope order, current

Supervision from public prices, then panel 6, then the free-riding diagnostic,
then the clustered companion in panel 2.

**Never cut:** panel 1's anchor, panel 4, panel 5, the exact two-block root, and
the private-versus-systemic framing.

The exact two-block root was third in this order until the limit was shown to err
unsafe. It is what makes Section 6's criterion honest rather than a refinement of
it.

## Suggested order for the remaining days

Settle the heterogeneous-response modeling decision first, before writing any
code for it, because that decision is the actual bottleneck and it is cheap to
get wrong. Then build the port in parallel with drafting. Draft Section 6 next,
since it is replanned and is the paper. Derive Theorem 4's welfare page after
that, and accept losing panel 6 if it slips. Write Sections 9 and 10 in
that order; 3 and 2 are drafted. Section 8 is already scoped to one paragraph and is first to cut.

If the port does not land, the paper is still submittable: the theory is complete
and certified, panel 1 is measured in a real market, and panels 2 to 5 can be
presented honestly as closed-form predictions with the reference-environment
agreement stated as such. That is a weaker paper and it is not the plan, but it
is not a failed submission, and knowing that should keep the port from being
rushed into something unfalsifiable.

---

## Conventions that are load-bearing

Status flags mean what `writing/CLAIMS-LEDGER.md` says they mean, and the flag in
the paper must match the ledger, which must match `ml-contributions/CERTIFICATES.md`.
A closed form reaching the paper without a passing certificate ships at
`[DERIVED]`, never `[VERIFIED]`. A dry run is not a measurement. All stability
claims use the spectral form, never a mean. Prose carries no em dashes and is
checked with `prose-guard`. Nothing in the double-blind build positions REFLEX or
PEBSA as the authors' own work.
