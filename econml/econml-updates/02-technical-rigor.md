# 2. Technical rigor and mathematical novelty

## 2.1 What was verified, and how

Three independent layers, all run on 25 Aug 2026:

1. **The repo's own certificates**: all seven files re-run, 525 assertions,
   all passing (numpy 2.4.6).
2. **A from-scratch script** (`tools/indep_check.py`) that re-implements the
   paper's formulas with no import from the theory module and checks every
   worked number in body and appendix against them, including dense
   eigensolves for the mixed market. 44 of 44 checks pass, among them the
   cadence table (20.68 / 5.28 / 2.53), the herd table (8.08 / 15.17 /
   36.42 and 12 / 5 / 0 firms), panel 4's thresholds (12 / 14 / 16 / 20 at
   the four efficacies, via eigensolve, not the closed form), the three
   worked strong-correction cases (1.9x / 3.9x / 58.6x critical curvature
   ratios, via bisection on the true radius), the phantom root (0.132
   against 0.043), and the witness pair.
3. **Proof reading**: every proof in the appendix read line by line. The
   reduction, the spectrum, the containment witness, the mean-bound
   proposition, the heterogeneous-moduli congruence, the concentration
   argument, the cadence composition, the secular quadratic, the
   theta-monotonicity, and the wedge FOCs are all correct as stated.

## 2.2 One real defect found: the wedge's orthogonal corner

The body (Section 7) claims Theorem 8 "covers the monoculture, orthogonal
and supply-chain configurations." The orthogonal claim is false, and the
appendix's own hypotheses show it:

- Lemma 6's proof requires a **simple** leading eigenvalue ("For a simple
  eigenvalue with unit eigenvector v..."), and Proposition A.4 delivers
  simplicity from Perron-Frobenius under irreducibility. At R = I the
  coupling matrix is the identity: reducible, leading eigenvalue degenerate
  with multiplicity N.
- The formula fails there, not just the proof. At R = I firms decouple and
  the radius is max_i m_i. Perturbing one firm's modulus at the symmetric
  point moves the radius one-for-one (the one-sided derivative is 1), while
  the claimed exchangeable share N_eff/N = 1/N. Off by a factor of N.
- Economically the corner is degenerate anyway: decoupled firms have no
  common mode, so there is nothing to price and no commons problem. The fix
  costs nothing substantive.

Fix (applied in proposed-v5, three touches): the body scope sentence now
reads "covers the monoculture and supply-chain configurations at any s > 0,
but excludes the orthogonal corner, where the leading eigenvalue is
degenerate and firms decouple"; the body statement of Lemma 6 gains "with
kappa > 0 and lambda_max(R) simple"; and appendix hypothesis (W3) gains the
simplicity requirement with the reason. Note kappa > 0 is needed too: at
kappa = 0 the coupling matrix is the identity whatever R is.

## 2.3 Small precision items (all applied in proposed-v5)

- **Notation collision**: the body defines the corrected fraction as rho
  while the appendix calls the same object rho_c, and the body then writes
  rho(J) for a spectral radius in the same theorem. Unified to rho_c in the
  body and in the two figure axis labels (figures regenerated).
- **Notation table**: gamma_PO listed as "> gamma" while theta = gamma/
  gamma_PO has range (0,1], which includes equality. Changed to ">= gamma".
- **The 11.8% figure** is sampling-protocol dependent (an independent
  uniform draw with slightly different ranges gives 17%). The number itself
  reproduces exactly under the certificate's documented ranges. The
  appendix now states the ranges where the number lives, plus the sentence
  that the direction, unlike the fraction, is protocol-free.
- **"A factor N_eff earlier"** (Section 3) mixes magnitude and time; made
  precise as "at a response strength a factor N_eff smaller."
- **"Six panels, one per result"** contradicts the seven-row table and the
  four results; reworded.

## 2.4 Mathematical novelty, honestly graded

The paper's mathematics is well-chosen rather than deep, and the paper
mostly says so itself, which is the right posture. Grading each tool:

- The reduction lemma: elementary, but doing the right thing (deriving the
  substitution instead of positing it), and (H3) own-channel sensing is a
  genuinely good modeling idea with a real market story. This is the
  paper's best mathematical moment.
- Spectral radius via congruence, Rayleigh bounds, Weyl plus Bernstein
  concentration: standard tools, correctly deployed, each doing necessary
  work (the Gram-matrix property closing the absolute-value gap in Theorem
  2's proof is a nice touch and correctly flagged as load-bearing).
- The two-block secular quadratic and its degenerate-block warning:
  standard structure (diagonal plus rank one), but the phantom-root
  observation is exactly the kind of thing implementers hit, and stating it
  is a service.
- Theta-monotonicity via Perron-Frobenius: short, correct, and the source
  of the paper's best self-generated result (the limit errs optimistic).

Where a reviewer could push, and the prepared answer:

- "(H1) rank-one deviation is doing enormous work." True, and the paper
  says so, defers the Kronecker block-secular problem explicitly, and keeps
  the honest phrase "the hypothesis that limits scope." Keep that framing;
  do not soften it.
- "(A2)/(H2) equal moduli." Covered by the two-sided bound (Prop A.7),
  exact at both ends. Adequate for a workshop paper.
- "Linearization (A1)." Panel 1's two-signed gap is the honest exhibit;
  the ablation in `03-benchmarking-results.md` would turn it from an
  exhibit into a measurement.

## 2.5 Journal-strength upgrades (correctly deferred now, listed for later)

In priority order for the journal version:

1. The sharp operator-norm concentration rate sqrt(N)/d via matrix
   Bernstein (the appendix already names it; it is a contained lemma).
2. The block-secular reduction without (H1), even partially (e.g. commuting
   E_i, or E_i sharing a common eigenbasis, which covers the shared-encoder
   case and would be a satisfying halfway house).
3. The asymmetric wedge from the participation-ratio observation in the
   deferred register (d m_N / d m_i = N_eff v_i^2 already does the work;
   what is missing is the welfare statement).
4. The supervision estimator formalized: the AR(1) sign convention and the
   variance-share rate are already certified, so the consistency proof is
   mostly bookkeeping; the sample-complexity statement near the boundary is
   the interesting part (the estimator sharpens as 1/(1-m_N), and saying
   this precisely would make the regulator section a theorem rather than a
   promise).
5. Heterogeneous cadences: the eigenvector-sharing obstruction is real; a
   two-clock special case may be tractable by the same two-block trick used
   for Theorem 5.
