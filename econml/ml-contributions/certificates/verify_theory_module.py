"""Acceptance tests for the theory module.

The six tests the spec names, plus the guards. Every experiment checks itself
against this module, so the module is not done until all of these pass.

This file deliberately re-derives its expectations rather than importing them, so
that agreement with the module is a second route to the same number and not a
tautology. Where a closed form is checked, it is checked against a dense
eigensolve or against a brute-force search.
"""
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "theory"))
import econml_theory as T                                    # noqa: E402

PASSED = []


def check(name, condition, detail=""):
    if not condition:
        raise AssertionError(f"FAILED {name}: {detail}")
    PASSED.append(name)
    print(f"  pass  {name}" + (f"   [{detail}]" if detail else ""))


rng = np.random.default_rng(20260818)


# ------------------------------------------------ A1  reduction to the base law

print("\nA1  n_eff of the monoculture equals the inherited base law")

for N in range(2, 51):
    for kappa in (0.0, 0.25, 0.5, 0.8, 1.0):
        got = T.n_eff(T.monoculture_R(N), kappa)
        want = 1 + kappa * (N - 1)
        if abs(got - want) > 1e-10:
            raise AssertionError(f"A1 failed at N={N} kappa={kappa}")
check("A1 monoculture recovers 1 + kappa(N-1)", True,
      "N in 2..50, five values of kappa")

check("A1 measured amplification anchors: N_eff = 2 and 3 at kappa = 1",
      abs(T.n_eff(T.monoculture_R(2), 1.0) - 2) < 1e-12
      and abs(T.n_eff(T.monoculture_R(3), 1.0) - 3) < 1e-12,
      "the 1.74x and 3.16x measurements sit against these")


# --------------------------------------------------- A2  two routes agree

print("\nA2  the supply-chain closed form equals the eigensolve of its limit R")

worst = 0.0
for N in (2, 5, 13, 40):
    for s in np.linspace(0, 1, 11):
        for kappa in (0.0, 0.35, 0.8, 1.0):
            worst = max(worst, abs(T.n_eff_supply_chain(N, s, kappa)
                                   - T.n_eff(T.supply_chain_R(N, s), kappa)))
check("A2 two routes agree to machine precision", worst < 1e-10,
      f"max deviation {worst:.2e} over 176 combinations")


# ------------------------------------------------- A3  the simplex correction

print("\nA3  the simplex spectrum, which the plan of record got wrong")

m_1, kappa = 0.15, 0.8
for N in (3, 5, 10, 30, 50):
    R = T.simplex_R(N)
    check(f"A3 n_eff = 1 + kappa/(N-1) at N={N}",
          abs(T.n_eff(R, kappa) - (1 + kappa / (N - 1))) < 1e-10)
    spec = np.linalg.eigvals(T.joint_jacobian(R, m_1, kappa))
    claimed = m_1 * (1 - kappa)
    check(f"A3 m_1(1-kappa) is in the spectrum at N={N}",
          np.abs(np.abs(spec) - claimed).min() < 1e-10)
    check(f"A3 m_1(1-kappa) is not the radius at N={N}",
          abs(np.abs(spec).max() - claimed) > 1e-6)


# ---------------------------------------------------- A4  cadence agreement

print("\nA4  is_stable_lazy agrees with K < k_max on every integer K in 1..200")

mismatches = 0
for m_N in np.concatenate([np.linspace(1.01, 8.0, 30), [0.5, 0.99, 20.0]]):
    for c in (0.5, 0.7, 0.8, 0.9, 0.95):
        km = T.k_max(m_N, c)
        for K in range(1, 201):
            if T.is_stable_lazy(m_N, c, K) != (K < km) and abs(K - km) > 1e-9:
                mismatches += 1
check("A4 no mismatch", mismatches == 0, "33000 integer cases")

check("A4 critical crowding is the K = 1 case",
      all(abs(T.critical_crowding(c) - (1 + c) / (1 - c)) < 1e-12
          for c in (0.5, 0.8, 0.95)))
check("A4 factor of 9 at c = 0.8", abs(T.critical_crowding(0.8) - 9.0) < 1e-12)


# --------------------------------------------- A5  the herd-immunity limit

print("\nA5  mixed_market_radius against dense eigensolves, and the limit")

def dense_mixed_radius(N, n_blind, m_1, kappa, s, gr):
    J = T.mixed_market_jacobian(N, n_blind, m_1, kappa, s, gr)
    return np.abs(np.linalg.eigvals(J)).max()


worst = 0.0
for _ in range(4000):
    N = int(rng.integers(2, 40))
    nb = int(rng.integers(0, N + 1))
    m_1 = float(rng.uniform(0.02, 0.9))
    kappa = float(rng.uniform(0.05, 1.0))
    s = float(rng.uniform(0.05, 1.0))
    gr = float(rng.uniform(1e-9, 1.0))
    worst = max(worst, abs(T.mixed_market_radius(N, nb, m_1, kappa, s, gr)
                           - dense_mixed_radius(N, nb, m_1, kappa, s, gr)))
check("A5 exact radius on 4000 draws including empty blocks", worst < 1e-9,
      f"max deviation {worst:.2e}")

# the limit, and the sign change rho_star is supposed to mark
mismatches = 0
for _ in range(4000):
    N = int(rng.integers(2, 40))
    nb = int(rng.integers(0, N + 1))
    m_1 = float(rng.uniform(0.02, 0.9))
    kappa = float(rng.uniform(0.05, 1.0))
    s = float(rng.uniform(0.05, 1.0))
    r = T.mixed_market_radius(N, nb, m_1, kappa, s, 1e-14)
    if abs(r - 1) < 1e-9:
        continue
    if (r < 1) != T.is_stable_mixed(N, nb, m_1, kappa, s):
        mismatches += 1
check("A5 is_stable_mixed marks the limit's sign change exactly", mismatches == 0,
      "4000 draws, zero mismatches")

# and the documented caution: the clamped rho form is NOT exact
clamped_bad = 0
for _ in range(4000):
    N = int(rng.integers(2, 40))
    nb = int(rng.integers(0, N + 1))
    m_1 = float(rng.uniform(0.02, 0.9))
    kappa = float(rng.uniform(0.05, 1.0))
    s = float(rng.uniform(0.05, 1.0))
    r = T.mixed_market_radius(N, nb, m_1, kappa, s, 1e-14)
    if abs(r - 1) < 1e-9:
        continue
    if (r < 1) != ((1 - nb / N) > T.rho_star(N, m_1, kappa, s)):
        clamped_bad += 1
check("A5 rho_star's docstring caution is real, not defensive", clamped_bad > 0,
      f"{clamped_bad} draws where rho > rho_star mispredicts, "
      "which is why is_stable_mixed exists")


# --------------------------------------------------- A6  monotonicity

print("\nA6  the monotonicities the paper's arguments rest on")

for c in (0.5, 0.8, 0.95):
    vals = [T.k_max(m, c) for m in np.linspace(1.001, 8.0, 300)]
    check(f"A6 k_max decreasing in m_N at c={c}", np.all(np.diff(vals) < 0))

for (N, m_1, kappa) in ((20, 0.15, 0.8), (10, 0.2, 1.0)):
    vals = T.substitution_frontier(N, m_1, kappa, np.linspace(0.05, 1.0, 300))
    check(f"A6 rho_star nondecreasing in s at N={N}", np.all(np.diff(vals) >= -1e-15),
          f"from {vals[0]:.4f} to {vals[-1]:.4f}")

for _ in range(300):
    N = int(rng.integers(3, 25)); nb = int(rng.integers(1, N))
    m_1 = float(rng.uniform(0.02, 0.5)); kappa = float(rng.uniform(0.1, 1.0))
    s = float(rng.uniform(0.1, 1.0))
    grid = np.linspace(1e-9, 1.0, 40)
    r = [T.mixed_market_radius(N, nb, m_1, kappa, s, g) for g in grid]
    if np.any(np.diff(r) < -1e-12):
        raise AssertionError("A6 radius not monotone in gamma_ratio")
check("A6 mixed radius nondecreasing in gamma_ratio", True,
      "300 configurations, so correction never backfires")


# ------------------------------------- A7  the results that are not in the spec

print("\nA7  closed forms the derivations added after the spec was written")

def random_R(N, D=40):
    """A valid alignment matrix: the Gram matrix of N unit vectors in R^D."""
    X = rng.standard_normal((N, D))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    return X @ X.T


smallest_n_eff = min(T.n_eff(random_R(int(rng.integers(2, 20))), 0.8)
                     for _ in range(200))
check("A7 n_eff >= 1 on random alignment matrices", smallest_n_eff >= 1 - 1e-12,
      f"smallest n_eff seen {smallest_n_eff:.6f}, so interaction never stabilizes")

# the mean index is a lower bound, never an upper one
worst_gap = min(T.n_eff(R, 0.8) - T.n_eff_mean_index(R, 0.8)
                for R in (random_R(int(rng.integers(3, 25))) for _ in range(400)))
check("A7 the mean index never over-states n_eff", worst_gap >= -1e-10,
      f"smallest gap {worst_gap:.2e} over 400 draws")

# heterogeneous-modulus bounds bracket the truth
for _ in range(300):
    N = int(rng.integers(2, 15))
    R = random_R(N)
    m = rng.uniform(0.05, 0.9, size=N)
    kappa = float(rng.uniform(0, 1))
    lo, exact, hi = T.hetero_modulus_bounds(R, m, kappa)
    if not (lo - 1e-10 <= exact <= hi + 1e-10):
        raise AssertionError("A7 heterogeneous bounds violated")
check("A7 heterogeneous-modulus bounds bracket the exact radius", True,
      "300 draws")

# the imperfect-correction law and its critical efficacy
for m_N in (1.5, 2.5, 4.0):
    check(f"A7 perfect correction recovers 1 - 1/m_N at m_N={m_N}",
          abs(T.rho_star_imperfect(m_N, 0.0) - (1 - 1 / m_N)) < 1e-12)
    crit = T.critical_efficacy(m_N)
    check(f"A7 critical efficacy at m_N={m_N}",
          abs(T.rho_star_imperfect(m_N, 1 / crit) - 1.0) < 1e-12,
          f"gamma_PO must exceed {crit:.2f} * gamma")

check("A7 min_corrected beats ceil(rho_star N) at integer n_c",
      T.min_corrected(20, 0.15, 0.8,
                      (1 / 0.15 - 1) / (0.8 * 7)) == 13,
      "the exact-integer corner where the ceil form is off by one")

check("A7 worked thresholds: 12 / 5 / 0 corrected firms",
      (T.min_corrected(20, 0.15, 0.8, 1.0),
       T.min_corrected(20, 0.15, 0.8, 0.5),
       T.min_corrected(20, 0.15, 0.8, 0.2)) == (12, 5, 0))


# ------------------------------------------------------------ A8  the guards

print("\nA8  guards reject what the derivations exclude")

def raises(fn, *a, **k):
    try:
        fn(*a, **k)
    except (ValueError, np.linalg.LinAlgError):
        return True
    return False


check("A8 kappa outside [0,1] rejected", raises(T.n_eff, np.eye(3), 1.5))
check("A8 s outside [0,1] rejected", raises(T.supply_chain_R, 5, -0.2))
check("A8 c outside (0,1) rejected", raises(T.k_max, 2.0, 1.0))
check("A8 cadence K < 1 rejected", raises(T.is_stable_lazy, 2.0, 0.8, 0))
check("A8 n_blind out of range rejected",
      raises(T.mixed_market_radius, 10, 11, 0.15, 0.8, 1.0, 0.5))
check("A8 non-PSD pseudo-alignment rejected",
      raises(T.alignment_matrix, np.zeros((3, 2, 2))))
check("A8 a wrongly shaped E is rejected",
      raises(T.alignment_matrix, np.ones((3, 4))))

# alignment_matrix round-trips against a target it was built to hit
X = rng.standard_normal((6, 25))
X /= np.linalg.norm(X, axis=1, keepdims=True)
E = X.reshape(6, 5, 5)
check("A8 alignment_matrix reproduces the Gram matrix it was built from",
      np.abs(T.alignment_matrix(E) - X @ X.T).max() < 1e-12)

check("A8 pigouvian_wedge is absent until Theorem 4 is derived",
      not hasattr(T, "pigouvian_wedge"),
      "the standing rule: nothing ships ahead of its derivation")


print(f"\n{len(PASSED)} checks passed.")
