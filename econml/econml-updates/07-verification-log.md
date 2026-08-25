# 7. Verification log

Everything below was executed on 25 Aug 2026 in a clean environment
(Python 3, numpy 2.4.6, TeX Live). Nothing in this package is asserted
from memory alone.

## 7.1 Certificates (the repo's own)

```
verify_hetero_env.py              32 checks   pass
verify_theorem1_anchors.py        60 checks   pass
verify_theorem1_proof.py         123 checks   pass
verify_theorem2_cadence.py        59 checks   pass
verify_theorem3_herd_immunity.py  70 checks   pass
verify_theorem4_wedge.py         125 checks   pass
verify_theory_module.py           56 checks   pass
total                            525          matches the paper's count
```

## 7.2 Independent re-derivation (`tools/indep_check.py`)

Written from the paper's formulas only, no imports from the repo. 44 of 44
checks pass, covering: the containment witness numbers; the clustered
topology (2.60 / 1.48 / 1.30 / 0.74 / 1.757x); the full cadence table and
the critical crowding factor 9; the herd table in N_c, rho*, and whole
firms; panel 4's 12/14/16/20 thresholds recomputed by dense eigensolve
and integer search, not the closed form; the three worked strong-correction
cases with critical curvature ratios found by bisection on the true radius
(1.89x / 3.92x / 58.6x against the paper's 1.9 / 3.9 / 58.6); the phantom
root at the empty-block corner; V'(m) against a finite difference; the
imperfect-vaccine law re-derived from the degenerate quadratic; N_eff and
witness-interval arithmetic. The 11.8% flip rate reproduces exactly under
the certificate's documented ranges (2157/18313 on re-run) and moves to
~17% under a slightly different draw, which is why proposed-v5 states the
protocol next to the number.

## 7.3 Build verification

- Committed `main.pdf` rebuilt from source (three pdflatex passes): same
  page structure, references start page 10, content ends page 9, zero
  overfull boxes. The committed PDF was restored untouched afterward.
- `proposed-v5/main.pdf` built the same way: 32 pages (appendix grew),
  content ends page 9 with the conclusion, References first on page 10,
  zero overfull boxes, no undefined citations or references, figures
  regenerated from the committed result JSONs with the rho_c labels.

## 7.4 Web verification (25 Aug 2026)

- Workshop: econml26-workshop.github.io (via search index; the domain is
  egress-blocked here), NeurIPS 2026 workshops announcement, OpenReview
  group `NeurIPS.cc/2026/Workshop/EconML`. Name, Atlanta 12/13 Dec, two
  tracks, long/short formats confirmed. Deadline: NeurIPS-suggested
  29 Aug AoE; the site's 30 Aug 11:59 UTC is the same instant.
- Piliouras and Yu, EC 2023 (arXiv:2201.10483): confirmed via ACM DL and
  OpenReview copies.
- Li, Yau, Wai, NeurIPS 2022 (arXiv:2209.03811): confirmed via NeurIPS
  proceedings page; author list and consensus/greedy-deployment content
  confirmed from the abstract.
- Kim, Garg, Peng, Garg, ICML 2025 (arXiv:2506.07962): confirmed via PMLR
  (v267/kim25e) and the ICML poster page; findings confirmed from the
  abstract (350+ models, 60% agreement when both err on one leaderboard,
  provider concentration).
- 2026 preprints in `01-novelty.md` section 1.4: titles and abstracts only;
  flagged as verify-before-citing.

## 7.5 What was NOT verified, stated plainly

- The REFLEX anchor numbers (1.7428x / 3.1567x, relative error 0.00)
  depend on the base project's simulator, which is not in this repository;
  the certificate that reproduces them skips cleanly when the base is
  absent, and it was absent here. The paper's claim rests on
  `reflex_anchor.py` runs recorded in STATUS.md.
- The three 2026 finance preprints: abstract-level only.
- Full texts of Piliouras-Yu and Li-Yau-Wai were not re-read here
  (arXiv is egress-blocked); the dispatch sentences in proposed-v5 were
  written strictly from claims their abstracts support (common outcome;
  consensus constraint) and should survive a full read, but give each a
  ten-minute skim before submitting.
