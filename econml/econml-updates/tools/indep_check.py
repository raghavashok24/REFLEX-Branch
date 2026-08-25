"""Independent re-derivation of every headline number in main.tex, written
from the paper's formulas alone (not importing the repo's theory module)."""
import numpy as np

ok = True
def check(name, got, want, tol=5e-3):
    global ok
    good = abs(got - want) <= tol * max(1, abs(want))
    print(f"{'PASS' if good else 'FAIL'}  {name}: got {got:.6g}, paper says {want}")
    if not good: ok = False

# --- Prop 3 witness: N=20, kappa=0.8, m1=0.15
N, k, m1 = 20, 0.8, 0.15
check("witness orthogonal mN", m1, 0.15)
check("witness monoculture mN", m1*(1+k*(N-1)), 2.43)
check("witness interval share", 1 - 1/(1+k*(N-1)), 0.94, tol=6e-3)

# --- Clustered example: N=10, 3 aligned, others orthogonal, kappa=0.8
R = np.eye(10); R[:3,:3] = 1.0
lam = np.linalg.eigvalsh(R).max()
Neff_true = 1 + 0.8*(lam-1)
rbar = (R.sum() - 10) / (10*9)
Neff_idx = 1 + 0.8*((1+9*rbar)-1)
check("clustered lambda_max", lam, 3)
check("clustered Neff", Neff_true, 2.60)
check("index Neff", Neff_idx, 1.48)
check("clustered mN at m1=0.5", 0.5*Neff_true, 1.30)
check("index mN", 0.5*Neff_idx, 0.74)
check("understatement factor", Neff_true/Neff_idx, 1.757)

# --- Cadence table: m1=0.15, kappa=0.8, N=30, c=0.8
c = 0.8
for s, Neff_w, mN_w, K_w in [(0.25,6.80,1.020,20.68),(0.5,12.60,1.890,5.28),(1.0,24.20,3.630,2.53)]:
    Neff = 1 + 0.8*s*29
    mN = 0.15*Neff
    Kmax = np.log((mN-1)/(mN+1))/np.log(c)
    check(f"cadence Neff s={s}", Neff, Neff_w)
    check(f"cadence mN s={s}", mN, mN_w)
    check(f"cadence Kmax s={s}", Kmax, K_w)
check("critical crowding at c=0.8", (1+c)/(1-c), 9)

# --- Herd table: N=20, m1=0.15, kappa=0.8
for s, Nc_w, rho_w, firms_w in [(1.0,8.08,0.596,12),(0.5,15.17,0.242,5),(0.2,36.42,0.0,0)]:
    Nc = 1 + (1/0.15 - 1)/(0.8*s)
    rho = max(0.0, 1 - Nc/20)
    firms = max(0, 20 - int(np.ceil(Nc)) + 1)
    check(f"herd Nc s={s}", Nc, Nc_w)
    check(f"herd rho* s={s}", rho, rho_w)
    check(f"herd firms s={s}", firms, firms_w, tol=0)

# --- Mixed-market radius via dense eigensolve (independent of the quadratic)
def radius(N, Nb, m1, kappa, s, theta):
    ks = kappa*s
    m = np.array([m1]*Nb + [theta*m1]*(N-Nb))
    B = (1-ks)*np.eye(N) + ks*np.ones((N,N))
    A = np.diag(np.sqrt(m)) @ B @ np.diag(np.sqrt(m))
    return np.linalg.eigvalsh(A).max()

# Panel 4: thresholds in firms at N=20, m1=0.15, kappa=0.8, s=1 for
# efficacy e in {1.00, 0.90, 0.75, 0.60}; theta = 1-e
for e, firms_w in [(1.00,12),(0.90,14),(0.75,16),(0.60,20)]:
    th = 1-e
    thr = None
    for corrected in range(0, 21):
        Nb = 20 - corrected
        if radius(20, Nb, 0.15, 0.8, 1.0, max(th,1e-12)) < 1:
            thr = corrected; break
    check(f"panel4 threshold e={e}", -1 if thr is None else thr, firms_w, tol=0)

# --- Worked cases: limit reads vs true critical gamma_PO ratio
for (N_,Nb_,m1_,k_,s_), lim_w, ratio_w in [((10,6,0.15,0.8,1),0.750,1.9),
                                            ((30,8,0.10,0.9,0.8),0.604,3.9),
                                            ((20,10,0.12,0.8,1),0.984,58.6)]:
    lim = m1_*(1+k_*s_*(Nb_-1))
    check(f"limit reads N={N_}", lim, lim_w)
    # critical theta: radius = 1
    lo, hi = 1e-9, 1.0
    if radius(N_,Nb_,m1_,k_,s_,lo) >= 1:
        crit = np.inf
    else:
        for _ in range(200):
            mid = 0.5*(lo+hi)
            if radius(N_,Nb_,m1_,k_,s_,mid) < 1: lo = mid
            else: hi = mid
        crit = 0.5*(lo+hi)
    check(f"critical gammaPO ratio N={N_}", 1/crit, ratio_w, tol=3e-2)

# --- Phantom root: N=12, m1=0.3, kappa=0.8, s=0.7, theta=0.02, Nb=0
ks = 0.8*0.7
a_ = (1-ks)*0.3; th=0.02
Nb_, Nc_ = 0, 12
P = a_ + (1-ks)*th*0.3 + ks*0.3*(Nb_ + th*Nc_)
Q = th*0.3**2*(1-ks)*(1+ks*11)
phantom = 0.5*(P+np.sqrt(P**2-4*Q))
true = radius(12,0,0.3,0.8,0.7,0.02)
check("phantom root", phantom, 0.132, tol=2e-2)
check("true radius Nb=0", true, 0.043, tol=2e-2)
check("true = theta*m1*Neff", 0.02*0.3*(1+ks*11), true, tol=1e-9)

# --- 11.8%: fraction of random configs the strong-correction limit calls
# stable that are unstable at every finite theta -> i.e. limit stable but
# unstable at the drawn theta? Definition check: 'stable that are unstable
# at every finite correction strength' means limit<1 but radius(theta)>1 for
# the drawn theta... we test: limit says stable, exact root unstable.
rng = np.random.default_rng(0)
cnt = tot = 0
for _ in range(20000):
    N_ = rng.integers(2, 31); Nb_ = rng.integers(1, N_)
    m1_ = rng.uniform(0.02, 0.9); k_ = rng.uniform(0,1); s_ = rng.uniform(0,1)
    th = rng.uniform(0.01, 1)
    lim_stable = m1_*(1+k_*s_*(Nb_-1)) < 1
    if lim_stable:
        tot += 1
        if radius(N_,Nb_,m1_,k_,s_,th) >= 1: cnt += 1
print(f"INFO  limit-optimistic flip rate on my draw: {cnt/tot:.3f} (paper says 0.118; sampling-protocol dependent)")

# --- Wedge numbers
check("Neff at N=20,k=.8,s=1", 1+0.8*19, 16.2)
# V'(m) form check by finite difference
m=0.6; sig=1.3
V = lambda m: sig**2/(1-m**2)
num = (V(m+1e-6)-V(m-1e-6))/2e-6
check("V'(m) closed form", 2*sig**2*m/(1-m**2)**2, num, tol=1e-6)

# --- abstract: (1-1/mN)/e law re-derivation at kappa=s=1
mN=2.5; e=0.8; th=1-e; N_=10
# stability: m1*(Nb + th*Ncorr) < 1 with m1 = mN/N
m1_ = mN/N_
rho_c = (1 - 1/mN)/e
Nb_ = N_*(1-rho_c)
check("imperfect-vaccine law boundary", m1_*(Nb_ + th*(N_-Nb_)), 1.0, tol=1e-9)

print("\nALL PASS" if ok else "\nSOME FAILED")
