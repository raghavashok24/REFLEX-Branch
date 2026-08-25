# 5. Verification log

Everything below was executed on 25 Aug 2026 on Windows 11, Python 3.12.10,
numpy 2.4.6, scipy 1.18.0, pytest 9.1.1, MiKTeX 25.12. Nothing in this package
is asserted from memory.

## 5.1 The repository's own suites

| Suite | Claimed | Actual | Runtime | Verdict |
|---|---|---|---|---|
| `mlxor-derivations/verify/verify_all.py` | 34 checks | **34 PASS, 0 FAIL** | 31s | matches |
| `mlxor-derivations/verify/check_docs.py` | document consistency, "in CI" | **crashes**, exit 1 | 0.3s | **fails to run** |
| `posk-pipeline/experiments/run_all.py` | 36 rows, 35 PASS + 1 DRIFT, 0 FAIL | **36 rows, 35 PASS, 1 DRIFT, 0 FAIL** | 7m49s | matches |
| `posk-pipeline/experiments/run_open1.py` | OPEN-1 premise check | completes, min CR ratio 1.0050 | 2.5s | matches |
| `posk-pipeline/experiments/run_realdata.py` | 10/10 cells | **skips**: REFLEX tree absent | 0.6s | **not verifiable here** |
| `posk-pipeline/tests/test_posk.py` | 9 tests | **9 passed** | 12s | matches |

The two headline counts the paper prints, 34 and 36, both reproduce exactly,
including the single DRIFT cell and its measured value
(0.0062244 vs predicted 0.0053539, the +16 percent the body quotes).

### check_docs.py crashes

```
== C4: workflow YAML ==
Traceback (most recent call last):
  File ".../verify/check_docs.py", line 211, in main
    c4_workflow()
  File ".../verify/check_docs.py", line 163, in c4_workflow
    txt = open(path, encoding="utf-8").read()
FileNotFoundError: ... mlxor-derivations\.github\workflows\verify.yml
```

`c4_workflow()` opens the workflow file outside a `try`. There is no
`.github/` directory anywhere in the repository (`find` over the whole tree
returns no `.yml` or `.yaml` file at all). Because `main()` calls `c4_workflow()`
before `c5_file_graph()`, the crash also skips C5, so the assumption-register
completeness check (A1 through A6 defined) and the derivation file graph never
execute. The nine checks that do run before the crash all pass.

### run_realdata.py skips

```
REFLEX tree not found - skipping real-data leg
```

The script needs `endo_market_v4/data/calibration/` and
`research/results/07-12-2026/calibrated/calibrated_boundaries.csv` from the
REFLEX tree, which is not in this repository. The committed `REALDATA.md` is
therefore the only evidence for the 10/10 claim, and it was not re-derived here.
This is the same class of gate as the REFLEX-anchor numbers flagged in the
EconML review's log. Confidence in the 10/10 claim: **unverified**, not
disputed.

### run_all.py rewrites two committed result files

The run left `results/e5_anchor_mse.csv` and `results/e7_ablations.csv`
modified. Both were restored with `git checkout` before any further work; the
diff is reported here because it is a finding, not an accident of the review.

`e5_anchor_mse.csv` moved in the ninth significant figure (1.070748630643e-02 to
1.070748629863e-02): ordinary floating-point drift, no consequence.

`e7_ablations.csv` moved materially in two of eight cells:

| cell (design, anchor, gate) | committed final_err | re-run final_err | committed c_err | re-run c_err |
|---|---|---|---|---|
| 1, 0, 1 | 0.2598 | **0.1092** | 0.1025 | 0.0454 |
| 0, 0, 1 | 0.0567 | **0.2264** | 0.2105 | 0.0153 |

This is not run-to-run nondeterminism. Three consecutive re-runs of
`e7_ablations` in a scratch copy produced bit-identical output. The cause is
that the reported quantity is a *last-iterate* error, `abs(ag.h - hpo)`, on
trajectories that are still oscillating. Perturbing only the horizon shows it:

```
cell    T=4498  T=4499  T=4500  T=4501  T=4502
D1A1G1  0.0115  0.0053  0.0058  0.0057  0.0057
D1A0G1  0.2667  0.3791  0.1092  0.4978  0.1302
D0A0G1  0.3346  0.4118  0.2264  0.5507  0.0921
D1A0G0  0.1950  0.0594  0.1940  0.0595  0.1942
D0A0G0  0.2044  0.0406  0.2051  0.0405  0.2053
```

Every anchored cell is stable to four decimals. Every anchor-off cell is not:
the gate-off cells alternate with period two (a limit cycle), and the gated ones
range over a factor of six. The fix was verified rather than guessed: replacing
the last iterate with a 300-step tail average over the deployed path pins every
cell to three decimals across the same five horizons, and separates anchored
from unanchored more cleanly than the last iterate does.

```
cell     tail-avg(path, 300) over T=4498..4502
D1A1G1   0.0436 0.0436 0.0437 0.0437 0.0438
D0A1G1   0.0178 0.0170 0.0182 0.0212 0.0197
D1A0G1   0.1970 0.1969 0.1968 0.1967 0.1966
D0A0G1   0.2837 0.2849 0.2838 0.2804 0.2827
D1A0G0   0.1215 0.1215 0.1216 0.1216 0.1216
D0A0G0   0.0934 0.0928 0.0939 0.0965 0.0949
```

The asserted row, `best_unanchored > best_anchored`, passes at every horizon
tested, so no verification row is at risk. What is at risk is the committed CSV
and the Appendix E sentence "All results are deterministic from seeds."

## 5.2 onward

The independent re-derivation, the proof-reading record, the build check, the
web verification and the list of what could not be checked follow in the
next commits.
