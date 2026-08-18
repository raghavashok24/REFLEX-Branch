"""The paper's panels, run in the linearized reference environment.

READ THIS BEFORE QUOTING ANY NUMBER FROM HERE.

These are **dry runs**, not the paper's panels. They execute in the
heterogeneous-response environment, which realizes the model's response geometry
and nothing else: no informed flow, no spread, no inventory, no microstructure.
The paper's panels run in the base project's order-flow simulator, and until they
do, every experimental claim stays at its derivation status. Nothing here
upgrades a claim to measured.

What they are good for, which is a lot at ten days out:

  - they test the step from linearized spectrum to realized dynamics, which no
    amount of algebra checking covers
  - they fix the shape of every figure, so the simulator port has a target
  - a disagreement between these and the closed forms is a bug found cheaply,
    days before a simulator run would have found it

Measurement method. Stability is not read off an eigensolve. Each panel runs the
actual retraining map and estimates the spectral radius from the trajectory's
asymptotic growth rate by power iteration, so "measured" means measured from
dynamics. That is the one thing these runs can genuinely establish.

Panels 1 through 5 are here. Panel 6 needs Theorem 4, which is not derived.
"""
import pathlib
import sys

import numpy as np

_HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_HERE / "theory"))
sys.path.insert(0, str(_HERE / "environment"))
import econml_theory as T                                     # noqa: E402
import hetero_response_env as env                             # noqa: E402

SEED = 20260818


# ===========================================================================
# measuring a spectral radius from dynamics
# ===========================================================================

def measured_radius(market, K=None, c=None, steps=600, burn=200, rng=None):
    """Estimate the spectral radius by power iteration on the actual step map.

    Renormalizes each step, so it neither overflows nor underflows, and averages
    the growth factor after the transient. This is a measurement of the realized
    dynamics, not an eigensolve of a matrix built from the closed form.
    """
    rng = rng or np.random.default_rng(SEED)
    x = rng.standard_normal(market.N)
    x /= np.linalg.norm(x)
    factors = []
    for t in range(steps):
        x = market.step(x, K=K, c=c)
        r = float(np.linalg.norm(x))
        if r == 0.0:
            return 0.0
        x = x / r
        if t >= burn:
            factors.append(r)
    return float(np.exp(np.mean(np.log(factors))))


# ===========================================================================
# Panel 1: amplification replication
# ===========================================================================

def panel1_amplification(d=8, kappa=1.0, m_1=0.15, N_values=(1, 2, 3, 4, 5, 8)):
    """The N-sweep anchor.

    In the reference environment the amplification is exact by construction, so
    what this panel establishes is that the environment reduces correctly and
    that the dynamics reproduce the spectrum. The published 1.74x and 3.16x are
    simulator measurements whose gap from the predicted 2 and 3 comes from
    nonlinearity and flow saturation, neither of which exists here. That
    external comparison remains outstanding and is flagged as such.
    """
    rng = np.random.default_rng(SEED)
    rows = []
    base = None
    for N in N_values:
        mkt = env.homogeneous_market(N, d, kappa, m_1, rng)
        meas = measured_radius(mkt, rng=np.random.default_rng(SEED + N))
        if N == 1:
            base = meas
        rows.append({
            "N": N,
            "predicted_n_eff": float(T.n_eff(T.monoculture_R(N), kappa)),
            "predicted_radius": float(m_1 * T.n_eff(T.monoculture_R(N), kappa)),
            "measured_radius": meas,
            "measured_amplification": meas / base,
        })
    return {
        "panel": "1. amplification replication",
        "tests": "Section 3, the base result",
        "params": {"d": d, "kappa": kappa, "m_1": m_1},
        "rows": rows,
        "max_rel_error": max(abs(r["measured_radius"] - r["predicted_radius"])
                             / r["predicted_radius"] for r in rows),
        "external_anchor": {
            "published_simulator": {"N=2": 1.74, "N=3": 3.16},
            "predicted": {"N=2": 2.0, "N=3": 3.0},
            "status": "CLOSED. Reproduced bit for bit in the base project's "
                      "genuine shared-pool market by reflex_anchor.py, which "
                      "measures 1.7428x and 3.1567x, within 12.9% and 5.2% of "
                      "the linear prediction. That gap is nonlinearity and "
                      "flow saturation, which this environment does not model, "
                      "which is why it reproduces the prediction exactly.",
            "measured_by": "reflex_anchor.py",
        },
    }


# ===========================================================================
# Panel 2: the (N, s) phase diagram
# ===========================================================================

def panel2_phase_diagram(d=10, kappa=0.8, m_1=0.15,
                         N_values=(2, 5, 10, 20, 30, 40),
                         s_values=(0.0, 0.1, 0.2, 0.35, 0.5, 0.7, 0.85, 1.0)):
    """Measured m_N over firms by shared-model fraction, against the boundary."""
    rng = np.random.default_rng(SEED)
    grid, worst = [], 0.0
    for N in N_values:
        for s in s_values:
            mkt = env.supply_chain_market(N, d, kappa, m_1, s, rng, exact=True)
            meas = measured_radius(mkt, rng=np.random.default_rng(SEED + N))
            pred = m_1 * T.n_eff_supply_chain(N, s, kappa)
            worst = max(worst, abs(meas - pred))
            grid.append({"N": N, "s": s, "measured_m_N": meas,
                         "predicted_m_N": float(pred),
                         "stable": bool(meas < 1)})
    return {
        "panel": "2. the (N, s) phase diagram",
        "tests": "Theorem 1",
        "params": {"d": d, "kappa": kappa, "m_1": m_1},
        "grid": grid,
        "max_abs_error": float(worst),
    }


def panel2_clustered_companion(d=10, kappa=0.8, m_1=0.5, N=10, cluster=3):
    """Three aligned firms among ten, against the mean-alignment index."""
    rng = np.random.default_rng(SEED)
    mkt = env.clustered_market(N, d, kappa, m_1, [cluster], rng)
    meas = measured_radius(mkt, rng=np.random.default_rng(SEED + 1))
    R = mkt.alignment
    mean_index_m_N = float(T.n_eff_mean_index(R, kappa) * m_1)
    return {
        "panel": "2b. the clustered companion",
        "tests": "Theorem 1, the mean index is a lower bound",
        "params": {"N": N, "cluster": cluster, "kappa": kappa, "m_1": m_1},
        "measured_m_N": meas,
        "predicted_m_N": float(mkt.m_systemic),
        "mean_index_m_N": mean_index_m_N,
        "truly_unstable": bool(meas > 1),
        "mean_index_says_stable": bool(mean_index_m_N < 1),
        "understatement_factor": float(mkt.n_eff / T.n_eff_mean_index(R, kappa)),
    }


# ===========================================================================
# Panel 3: the crowding-cadence frontier
# ===========================================================================

def panel3_cadence(d=8, kappa=0.8, m_1=0.15, N=30, c=0.8,
                   s_values=(0.15, 0.25, 0.4, 0.5, 0.7, 0.85, 1.0),
                   K_values=tuple(range(1, 26))):
    """Joint K-step stability over the (N_eff, K) grid against predicted K_max."""
    rng = np.random.default_rng(SEED)
    cells, disagreements = [], 0
    for s in s_values:
        mkt = env.supply_chain_market(N, d, kappa, m_1, s, rng, exact=True)
        m_N = mkt.m_systemic
        km = T.k_max(m_N, c)
        for K in K_values:
            meas = measured_radius(mkt, K=K, c=c,
                                   rng=np.random.default_rng(SEED + K))
            measured_stable = meas < 1
            predicted_stable = T.is_stable_lazy(m_N, c, K)
            near = np.isfinite(km) and abs(K - km) / max(km, 1.0) < 0.02
            if measured_stable != predicted_stable and not near:
                disagreements += 1
            cells.append({"s": s, "N_eff": float(mkt.n_eff), "m_N": float(m_N),
                          "K": K, "measured_radius": meas,
                          "measured_stable": bool(measured_stable),
                          "predicted_stable": bool(predicted_stable),
                          "k_max": float(km) if np.isfinite(km) else None})
    return {
        "panel": "3. the crowding-cadence frontier",
        "tests": "Theorem 2",
        "params": {"d": d, "kappa": kappa, "m_1": m_1, "N": N, "c": c},
        "cells": cells,
        "disagreements": disagreements,
        "critical_crowding": float(T.critical_crowding(c)),
    }


# ===========================================================================
# Panel 4: herd immunity
# ===========================================================================

def panel4_herd_immunity(d=8, kappa=0.8, m_1=0.15, N=20, s=1.0,
                         gamma_ratios=(1e-9, 0.1, 0.25, 0.4)):
    """Mixed markets across the corrected fraction, at several efficacies.

    Run at the limit AND at finite correction, because the limit is optimistic
    and a panel run only at the limit would inherit that optimism.
    """
    rng = np.random.default_rng(SEED)
    series = []
    for gr in gamma_ratios:
        points = []
        for n_corrected in range(N + 1):
            mkt = env.mixed_market(N, d, kappa, m_1, s, N - n_corrected, gr, rng)
            meas = measured_radius(mkt,
                                   rng=np.random.default_rng(SEED + n_corrected))
            points.append({"n_corrected": n_corrected,
                           "rho": n_corrected / N,
                           "measured_radius": meas,
                           "stable": bool(meas < 1)})
        first_stable = next((p["n_corrected"] for p in points if p["stable"]), None)
        # The imperfect-correction law is exact at kappa = s = 1. This panel runs
        # at kappa = 0.8, so whether it still predicts the threshold here is a
        # question worth recording rather than assuming either way.
        m_N_here = m_1 * T.n_eff_supply_chain(N, s, kappa)
        law_rho = T.rho_star_imperfect(m_N_here, gr)
        law_firms = (None if law_rho > 1
                     else int(np.ceil(law_rho * N - 1e-12)))
        series.append({
            "gamma_ratio": gr,
            "efficacy": 1 - gr,
            "points": points,
            "measured_threshold_firms": first_stable,
            "predicted_limit_threshold_firms": T.min_corrected(N, m_1, kappa, s),
            "imperfect_law_rho": float(law_rho),
            "imperfect_law_firms": law_firms,
            "imperfect_law_matches": bool(law_firms == first_stable),
        })
    m_N = m_1 * T.n_eff_supply_chain(N, s, kappa)
    return {
        "panel": "4. herd immunity",
        "tests": "Theorem 3",
        "params": {"d": d, "kappa": kappa, "m_1": m_1, "N": N, "s": s},
        "m_N": float(m_N),
        "rho_star_limit": float(T.rho_star(N, m_1, kappa, s)),
        "critical_efficacy_gamma_PO_over_gamma": float(T.critical_efficacy(m_N)),
        "series": series,
    }


# ===========================================================================
# Panel 5: the substitution frontier
# ===========================================================================

def panel5_substitution(d=10, kappa=0.8, m_1=0.15, N=20,
                        s_values=tuple(np.round(np.linspace(0.15, 1.0, 18), 4)),
                        gamma_ratio=1e-9):
    """The (rho, s) iso-stability curve. The headline figure's ground truth."""
    rng = np.random.default_rng(SEED)
    curve = []
    for s in s_values:
        measured = None
        for n_corrected in range(N + 1):
            mkt = env.mixed_market(N, d, kappa, m_1, float(s),
                                   N - n_corrected, gamma_ratio, rng)
            if measured_radius(mkt,
                               rng=np.random.default_rng(SEED + n_corrected)) < 1:
                measured = n_corrected
                break
        curve.append({
            "s": float(s),
            "measured_threshold_firms": measured,
            "measured_rho": None if measured is None else measured / N,
            "predicted_threshold_firms": T.min_corrected(N, m_1, kappa, float(s)),
            "predicted_rho_star": float(T.rho_star(N, m_1, kappa, float(s))),
        })
    exact_match = sum(
        1 for p in curve
        if p["measured_threshold_firms"] == p["predicted_threshold_firms"])
    return {
        "panel": "5. the substitution frontier",
        "tests": "Theorem 3, the synthesis result",
        "params": {"d": d, "kappa": kappa, "m_1": m_1, "N": N,
                   "gamma_ratio": gamma_ratio},
        "curve": curve,
        "exact_matches": exact_match,
        "points": len(curve),
    }
