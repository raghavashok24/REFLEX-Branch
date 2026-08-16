"""Numerical check of the two load-bearing identities of idea M2.

Run:  python research/workshops/verify_m2_identity.py

Stdlib only (no numpy) so it runs anywhere; ASCII output only (Windows console).

Local model at a performatively stable point h* (notation as in
research/math-theory/01-analytic-stability-boundary.md):

    h_{t+1} - h*  =  -m (h_t - h*)  +  s_e * xi_t        xi_t ~ iid N(0,1)
    tau_t         =  tau(h*) - eps (h_t - h*) + zeta_t   zeta_t ~ iid N(0, sig^2)

Claim 1 (information saturation).  With s_e = 0 and m < 1 the excitation
    sum_t (h_t - h*)^2  ->  (h_0 - h*)^2 / (1 - m^2)
is BOUNDED in the horizon, so Fisher information for the response slope eps
saturates: running a converging retraining loop longer buys no identification.

Claim 2 (the uncertainty principle).  With s_e > 0, in the stationary regime
    Var(eps_hat) * C  =  (1/2) * gamma_PO * sig^2
where C = (1/2) gamma_PO sum_t (h_t - h*)^2 is the INCREMENTAL exploration
cost -- the excess performative risk of the jittered loop relative to the
jitter-free loop at its operating point h*.  The product is independent of
s_e, of the horizon, and of m.

Claim 3 (the anchoring is load-bearing).  Anchoring the cost at the
performative optimum h_PO instead (gap g = h* - h_PO != 0) inflates the
product to (1/2) gamma_PO sig^2 (1 + g^2/v), v = s_e^2/(1-m^2): the
invariance is destroyed (the product now depends on s_e and m, and diverges
as the jitter shrinks).  The systematic T*(h*-h_PO)^2 term is the sunk
echo-chamber cost of blindness (theory 1.2, 6b), not a cost of exploration,
and must not be charged to the information budget.
"""

from __future__ import annotations

import random

SEED = 0
SIGMA_TAU = 0.7    # response-channel noise
GAMMA_PO = 1.3     # curvature of the performative objective (theory 1.2)


def excitation_no_jitter(m: float, h0: float = 1.0, horizon: int = 20000) -> float:
    """Sum of squared deviations of the noiseless cobweb h_t - h* = (-m)^t h0."""
    return sum(((-m) ** t * h0) ** 2 for t in range(horizon))


def excitation_closed_form(m: float, h0: float = 1.0) -> float:
    return h0 ** 2 / (1.0 - m ** 2)


def product_with_jitter(m: float, s_e: float, n: int = 400000) -> float:
    """Monte-Carlo Var(eps_hat) * cost for the jittered loop."""
    rng = random.Random(SEED)
    h = 0.0
    path = []
    for _ in range(n):
        h = -m * h + s_e * rng.gauss(0.0, 1.0)
        path.append(h)
    mean = sum(path) / n
    sxx = sum((v - mean) ** 2 for v in path)
    var_eps = SIGMA_TAU ** 2 / sxx          # OLS slope variance
    cost = 0.5 * GAMMA_PO * sxx             # excess performative risk paid
    return var_eps * cost


def product_wrong_anchor(m: float, s_e: float, gap: float, n: int = 400000) -> float:
    """Same product but with the cost anchored at h_PO (offset by gap)."""
    rng = random.Random(SEED)
    h = 0.0
    path = []
    for _ in range(n):
        h = -m * h + s_e * rng.gauss(0.0, 1.0)
        path.append(h)
    mean = sum(path) / n
    sxx = sum((v - mean) ** 2 for v in path)
    var_eps = SIGMA_TAU ** 2 / sxx
    cost_po = 0.5 * GAMMA_PO * sum((v + gap) ** 2 for v in path)
    return var_eps * cost_po


def main() -> None:
    target = 0.5 * GAMMA_PO * SIGMA_TAU ** 2
    print("Claim 1: information saturation (no exploration jitter)")
    for m in (0.2, 0.6, 0.9):
        measured = excitation_no_jitter(m)
        closed = excitation_closed_form(m)
        print(
            "  m=%.1f  sum dev^2 = %.6f   closed form = %.6f   abs err = %.2e"
            % (m, measured, closed, abs(measured - closed))
        )

    print("")
    print("Claim 2: Var(eps_hat) * cost is invariant  (target %.6f)" % target)
    for m in (0.2, 0.6, 0.9):
        for s_e in (0.05, 0.2):
            prod = product_with_jitter(m, s_e)
            print(
                "  m=%.1f  s_e=%.2f   product = %.6f   rel err = %.2e"
                % (m, s_e, prod, abs(prod - target) / target)
            )

    print("")
    print("Claim 3: the h_PO anchor destroys the invariance")
    gap = 0.3
    for m, s_e in ((0.6, 0.05), (0.6, 0.2), (0.9, 0.05)):
        v = s_e ** 2 / (1.0 - m ** 2)
        predicted = target * (1.0 + gap ** 2 / v)
        prod = product_wrong_anchor(m, s_e, gap)
        print(
            "  m=%.1f  s_e=%.2f   product = %10.4f   predicted (1+g^2/v) form = %10.4f"
            % (m, s_e, prod, predicted)
        )
    print("  (compare the invariant %.6f above: the wrong anchor depends on" % target)
    print("   s_e and m, and diverges as the jitter shrinks)")


if __name__ == "__main__":
    main()
