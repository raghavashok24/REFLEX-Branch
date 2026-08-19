# Heterogeneous-response simulator port: the modeling decision

**Written 18 Aug 2026.** This is the design record for the port that panels 2,
2b, 4 and 5 need before any of them can reach `[MEASURED]`. It fixes the
mechanism and states what the mechanism does not cover. The skeleton that
implements it is
[`../experiments/hetero_simulator_port.py`](../experiments/hetero_simulator_port.py).

Nothing under the base project is modified. The port subclasses the base
simulator from inside this repository, the same arrangement
[`../experiments/reflex_anchor.py`](../experiments/reflex_anchor.py) already
uses.

---

## The problem, stated exactly

The base project's `env/multi_dealer.py` couples dealers through one line:

```python
own_resp  = [exp(-c_t * h_j) for j in dealers]      # per bond
sum_resp  = sum(own_resp)
spread_resp_i = own_resp[i] + kappa * (sum_resp - own_resp[i])
```

Collect that into a matrix acting on the vector of per-dealer responses:

```
spread_resp = [(1 - kappa) I + kappa * 1 1'] own_resp
```

Compare Theorem 1's joint Jacobian `J = -m_1[(1-kappa) I + kappa R]`. The base
market is the theorem at `R = 1 1'` and at nothing else. Every dealer
contributes to the informed pool identically and senses it identically, so
there is no object in the simulator that could carry a per-dealer response
direction. A knob does not exist to be turned; the channel has to be widened
first.

## The decision

**Give each dealer a bond-space exposure profile, and route both the
contribution to the informed pool and the sensing of that pool through it.**

Write `u_i in R^{n_bonds}` for dealer `i`'s exposure profile, normalized so that
its mean square across bonds is one. Replace the coupling line with

```
pool(b)          = sum_j  own_resp_j(b) * u_j(b)
spread_resp_i(b) = u_i(b) * [ (1 - kappa) * own_resp_i(b) * u_i(b)
                              + kappa * pool(b) ]
```

Read in words: the informed pool's attractiveness at bond `b` is the sum of
every dealer's spread response there, each weighted by how much of that dealer's
book sits in that bond, and dealer `i` feels that pool only to the extent that
its own book sits there too.

### Why this mechanism

Four reasons, in the order they mattered.

**It is the same construction the theory already uses, read in the simulator's
own coordinates.** In
[`hetero_response_env.py`](hetero_response_env.py) firm `i` senses the shared
pool projected on its own unit response direction, its own contribution at full
weight and every competitor's at weight `kappa`. That is line-for-line what the
expression above does, with the abstract response direction `E_i` replaced by
the concrete thing a bond dealer actually differs in, namely which bonds it
quotes seriously. The port therefore does not introduce a second, competing
notion of alignment that would then have to be reconciled with Theorem 1.

**It produces the alignment matrix rather than assuming one.** Differentiating
`spread_resp_i` in `h_j` at a common reference spread, then averaging over bonds
the way `_measure_toxic_levels` already does, gives a sensitivity matrix

```
M_ij  proportional to  mean_b[u_i(b) u_j(b)] * (kappa + (1 - kappa) delta_ij)
```

With the mean-square normalization the diagonal is one and the off-diagonal is
`kappa * R_ij` with `R_ij = mean_b[u_i(b) u_j(b)]`, a Gram matrix of unit-norm
vectors. So `M = (1 - kappa) I + kappa R`: the alignment matrix comes out of the
flow generation rather than being written into it. This is the same discipline
`hetero_response_env.py` enforces by separating `jacobian()` from
`predicted_jacobian()`, and the port keeps it by measuring `R` back off the
realized profiles instead of trusting the constructor.

**The bond dimension is already there and already correlated.** `bonds.py`
builds a sector-block plus global-factor structure over the universe, and that
structure is the environment's only existing account of why two instruments move
together. Specializing dealers by sector exposure therefore borrows an object
the ground truth already commits to, rather than bolting a new latent space onto
the simulator. It also gives the supply-chain parameter `s` an economic reading
that a referee can hold: `s` is overlap of coverage, and the global factor puts
a floor under how disjoint two dealers can be even when their sectors do not
intersect, which is the right qualitative statement about a market where
everything shares a rates factor.

**It leaves every other channel untouched.** Uninformed flow, spread capture,
inventory, price impact, the liquidity field and the draw order are all
unchanged. That matters for the reduction test below, and it means a
disagreement between the port and the closed form cannot be blamed on a
microstructure edit made at the same time.

### Rejected alternatives, briefly

*Separate informed-flow segments per dealer.* Cleanest economically, but it
requires inventing a segment-arrival process and a routing rule, and both of
those are new structural ground truth that nothing validates. It also does not
reduce to the base market at any parameter setting without a further argument.

*Different signal channels, that is per-dealer `info_signal_noise` or a
per-dealer signal draw.* This changes how well a dealer sees the mispricing, not
which direction its response points. It moves moduli, not alignment, so it
models correction (Theorem 3's `gamma_ratio`) and not crowding. Useful later,
wrong here.

*Per-dealer `kappa_ij` matrix.* Would give `R` directly and would be one line.
Rejected because it writes the answer in by hand: the alignment matrix would be
a free parameter of the environment rather than a consequence of what dealers
do, and the panel would then be checking the closed form against a restatement
of itself.

## The reduction to `R = 1 1'`, exactly

Set `u_i(b) = 1` for every dealer and every bond, which is the mean-square
normalization applied to a dealer that quotes the whole universe uniformly.
Then `pool(b) = sum_j own_resp_j(b) = sum_resp(b)` and

```
spread_resp_i = 1 * [ (1 - kappa) * own_resp_i * 1 + kappa * sum_resp ]
              = own_resp_i + kappa * (sum_resp - own_resp_i)
```

which is the base project's line character for character, and `R_ij =
mean_b[1 * 1] = 1` for every pair, so `R = 1 1'`.

The reduction is exact in floating point as well as on paper, not merely equal
in the limit. Multiplication by `1.0` is exact in IEEE arithmetic, and the port
forms `pool` with the same `torch.stack(...).sum(dim=0)` over the same list in
the same order as the base, so the summation rounds identically. The port then
writes the bracket in the base's own associativity, `own + kappa * (pool -
own)`, rather than an algebraically equal regrouping. That is why the acceptance
test can demand bit-for-bit reproduction of the published anchors instead of
agreement to some tolerance, and why a failure of that test is informative
rather than a tolerance argument.

The structural constructor is parametrized so the monoculture is a *value* of
the parameter, not a special case in the code: `sector_profiles(..., tilt=0)`
returns all-ones profiles. There is no separate monoculture code path to keep in
sync.

## Drift guard

The port reimplements the base `step` in order to change one expression inside
it, so the copy can go stale if the base project changes. The port therefore
inspects the base source at import and fails loudly if the coupling line it was
written against is no longer there. A silently stale copy that still reproduces
the old anchors is the failure mode worth spending ten lines to prevent.

## What this does not yet handle

Open, and left open.

1. **Only the informed-intensity channel carries the exposure profile.** The
   liquidity field is still driven by total gross flow and by the *tightest*
   dealer's spread across the whole universe, and price impact is still driven
   by total net flow. Both remain fully shared no matter what the profiles are.
   At `u = 1` that is exactly right, since everything is shared there anyway. Away
   from it there is a second coupling channel whose alignment is `1 1'` and not
   `R`, so the realized joint modulus should be expected to sit *above* the
   closed form's prediction by an amount that grows as the profiles separate.
   Whether that residual is small enough to leave the panels interpretable is an
   empirical question this session does not answer, and it is the first thing the
   heterogeneous sweep has to measure.

2. **The reachable set of `R` is constrained by the universe.** The default
   config has `n_bonds = 8` and `n_sectors = 2`. Sector-tilted profiles live in
   an 8-dimensional space, so at most 8 dealers can be placed independently, and
   with two sectors the sector-tilt constructor can only realize a two-block
   alignment. A genuine `(N, s)` sweep needs either a larger universe or the
   free-profile constructor. Enlarging the universe changes `BondUniverse` and
   therefore changes the market, so panel 1's anchor does not transfer to a
   config with different `n_bonds`. Any heterogeneous panel must either run at
   `n_bonds = 8` or re-anchor.

3. **The global factor puts a floor on separation, and it is not quantified.**
   Two dealers with disjoint sectors still overlap through `global_factor`, so
   `R_ij` cannot be driven to zero by sector choice alone. The exact floor as a
   function of `global_factor` and the sector partition is not worked out here.
   Orthogonal responses, claim 4.3, are therefore not reachable by the
   structural constructor, only by the free-profile one.

4. **Profiles are static and exogenous.** A dealer's coverage does not respond to
   crowding. Endogenous specialization is the interesting economics and is out of
   scope for the paper.

5. **Heterogeneous moduli and heterogeneous alignment are not yet combined in the
   simulator.** Theorem 3's mixed market needs per-dealer `gamma`, which is a
   different edit to a different part of the config. Claim 4.10's bounds are
   stated for heterogeneous moduli, and the port as written carries a single
   `toxicity_feedback` for all dealers.

6. **The reduction is proved at the coupling expression, not at the measured
   modulus, for `u != 1`.** At `u = 1` the acceptance test closes the loop
   end to end against a published measurement. Away from it, the argument that
   `M = (1 - kappa) I + kappa R` is a linearization of `_measure_toxic_levels`
   around a common reference spread, and the finite-difference probe at finite
   `delta` in a nonlinear saturating market will not match it exactly. Panel 1
   already measures that gap at `12.9%` and `5.2%` in the monoculture. The
   heterogeneous version of that gap is unmeasured.

## Status

Nothing here upgrades any claim. Panels 2, 2b, 4 and 5 remain `[DRY RUN]` in
[`../../writing/CLAIMS-LEDGER.md`](../../writing/CLAIMS-LEDGER.md). This document
records a design and a skeleton that reproduces the known case; it records no
new measurement.
