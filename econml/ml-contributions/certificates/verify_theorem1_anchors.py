"""Verify the Theorem 1 anchors, especially the simplex case the plan states.

Plan of record claims: "maximal diversity (simplex responses) gives
m_1(1-kappa), independently matching the differential-mode eigenvalue the base
theory derives by a completely different route."

We test that claim two ways:
  (A) analytically, from R_simplex built by hand
  (B) constructively, from actual response Jacobians E_i forming a simplex in
      vec-space, so the alignment matrix is measured, not assumed.
"""
import numpy as np

np.set_printoptions(precision=6, suppress=True)


def J_of(R, m1, kappa):
    """Joint retraining Jacobian under the generalized law J = -m1[(1-k)I + kR]."""
    N = R.shape[0]
    return -m1 * ((1 - kappa) * np.eye(N) + kappa * R)


def radius(M):
    return max(abs(np.linalg.eigvals(M)))


def simplex_R(N):
    """N unit vectors with pairwise alignment -1/(N-1): the mean-minimizing set."""
    return (N / (N - 1)) * np.eye(N) - (1.0 / (N - 1)) * np.ones((N, N))


def simplex_vectors(N, d, seed=0):
    """Construct N actual unit vectors in R^d summing to zero (a regular simplex).

    Take the N-1 dim orthogonal complement of the all-ones vector in R^N,
    embed it in R^d via a random orthonormal map. Gram matrix is then exactly
    the simplex R, measured rather than assumed.
    """
    rng = np.random.default_rng(seed)
    # Columns of Q span 1-perp in R^N
    A = np.eye(N) - np.ones((N, N)) / N
    Q, _ = np.linalg.qr(A[:, : N - 1])          # d0 = N-1 orthonormal cols
    # rows of Q are the N points, already summing to zero
    V = Q                                       # (N, N-1)
    # embed into R^d with a random orthonormal basis
    G = rng.standard_normal((d, N - 1))
    B, _ = np.linalg.qr(G)                      # (d, N-1) orthonormal cols
    X = V @ B.T                                 # (N, d)
    X = X / np.linalg.norm(X, axis=1, keepdims=True)
    return X


def gram(X):
    Xn = X / np.linalg.norm(X, axis=1, keepdims=True)
    return Xn @ Xn.T


print("=" * 72)
print("(A) ANALYTIC: simplex R built by hand")
print("=" * 72)
for N in (3, 5, 10, 50):
    R = simplex_R(N)
    ev = np.sort(np.linalg.eigvalsh(R))
    print(f"N={N:>3}  diag={R[0,0]:.6f}  offdiag={R[0,1]:+.6f}  "
          f"lam_min={ev[0]:+.6e}  lam_max={ev[-1]:.6f}  N/(N-1)={N/(N-1):.6f}")

print()
print("=" * 72)
print("(B) CONSTRUCTIVE: alignment matrix measured from actual vec(E_i)")
print("=" * 72)
for N, d in ((3, 16), (5, 25), (10, 64)):
    X = simplex_vectors(N, d)
    R = gram(X)
    R_hand = simplex_R(N)
    ev = np.sort(np.linalg.eigvalsh(R))
    print(f"N={N:>3} d={d:>3}  max|R_measured - R_analytic| = "
          f"{np.abs(R - R_hand).max():.3e}   lam_max={ev[-1]:.6f}  "
          f"sum of vectors = {np.linalg.norm(X.sum(axis=0)):.3e}")

print()
print("=" * 72)
print("(C) THE CLAIM UNDER TEST: is the spectral radius m1*(1-kappa)?")
print("=" * 72)
m1, kappa = 0.15, 0.8
print(f"m1={m1}  kappa={kappa}   plan claims radius = m1(1-kappa) = "
      f"{m1*(1-kappa):.6f}\n")
print(f"{'N':>4} {'radius(J)':>12} {'m1(1+k/(N-1))':>15} {'m1(1-k)':>10} "
      f"{'in spectrum?':>13} {'is radius?':>11}")
for N in (3, 5, 10, 30, 50):
    R = simplex_R(N)
    J = J_of(R, m1, kappa)
    spec = np.linalg.eigvals(J)
    rad = max(abs(spec))
    pred_radius = m1 * (1 + kappa / (N - 1))
    claimed = m1 * (1 - kappa)
    in_spec = np.min(np.abs(np.abs(spec) - claimed)) < 1e-12
    is_rad = abs(rad - claimed) < 1e-12
    print(f"{N:>4} {rad:>12.6f} {pred_radius:>15.6f} {claimed:>10.6f} "
          f"{str(in_spec):>13} {str(is_rad):>11}")

print()
print("=" * 72)
print("(D) ALL THREE ANCHORS, N_eff = 1 + kappa(lam_max(R) - 1)")
print("=" * 72)
N = 10
anchors = {
    "monoculture  R=11'": np.ones((N, N)),
    "orthogonal   R=I  ": np.eye(N),
    "simplex           ": simplex_R(N),
}
for name, R in anchors.items():
    lam = max(np.linalg.eigvalsh(R))
    n_eff = 1 + kappa * (lam - 1)
    rad = radius(J_of(R, m1, kappa))
    print(f"{name}  lam_max={lam:>8.6f}  N_eff={n_eff:>8.6f}  "
          f"m_N={m1*n_eff:>8.6f}  radius(J)={rad:>8.6f}  "
          f"match={abs(rad - m1*n_eff) < 1e-12}")
print(f"\nbase-law check: monoculture N_eff should be 1+kappa(N-1) = "
      f"{1 + kappa*(N-1):.6f}")

print()
print("=" * 72)
print("(E) ORDERING FAILURE: does minimizing MEAN alignment minimize lam_max?")
print("=" * 72)
for N in (5, 10, 30):
    Rs, Ri = simplex_R(N), np.eye(N)
    def meanoff(R):
        return (R.sum() - np.trace(R)) / (N * (N - 1))
    ls, li = max(np.linalg.eigvalsh(Rs)), max(np.linalg.eigvalsh(Ri))
    print(f"N={N:>3}  simplex: mean={meanoff(Rs):+.6f} lam_max={ls:.6f}   "
          f"orthogonal: mean={meanoff(Ri):+.6f} lam_max={li:.6f}   "
          f"-> lower mean, higher lam_max: {meanoff(Rs) < meanoff(Ri) and ls > li}")

print()
print("=" * 72)
print("(F) CLUSTERED COUNTEREXAMPLE numbers quoted in the math note")
print("=" * 72)
N = 10
R_clust = np.zeros((N, N))
R_clust[:3, :3] = 1.0
R_clust[3:, 3:] = np.eye(7)
lam_c = max(np.linalg.eigvalsh(R_clust))
mean_c = (R_clust.sum() - np.trace(R_clust)) / (N * (N - 1))
R_unif = (1 - mean_c) * np.eye(N) + mean_c * np.ones((N, N))
lam_u = max(np.linalg.eigvalsh(R_unif))
neff_c, neff_u = 1 + kappa * (lam_c - 1), 1 + kappa * (lam_u - 1)
print(f"clustered:  lam_max={lam_c:.6f}  mean_offdiag={mean_c:.6f}  "
      f"N_eff={neff_c:.4f}  destabilizes at m1={1/neff_c:.4f}")
print(f"uniform:    lam_max={lam_u:.6f}  mean_offdiag={mean_c:.6f}  "
      f"N_eff={neff_u:.4f}  destabilizes at m1={1/neff_u:.4f}")
print(f"understatement factor in N_eff: {neff_c/neff_u:.4f}")
print(f"at m1=0.5:  clustered m_N={0.5*neff_c:.4f} (unstable={0.5*neff_c>1}), "
      f"uniform m_N={0.5*neff_u:.4f} (unstable={0.5*neff_u>1})")
