<div align="center">

# PRICE

**Performative Risk In Coupled Environments**

Two papers on what it costs when models retrain on data their own predictions shaped.

<p align="center"><sub><b>Languages & Tools:</b></sub></p>
<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white">
</p>

</div>

PRICE extends REFLEX ([GitHub](https://github.com/vignesh-nagarajan-vn/REFLEX), [arXiv:2608.16155](https://arxiv.org/abs/2608.16155)) from a single learner to dynamic, coupled settings. Both papers put a price on a feedback loop. One prices it privately, as the cost a single decision-maker pays to learn its own influence. The other prices it socially, as the cost each firm's retraining imposes on every other firm in the market.

Built by Shriraghav Ashok and Vignesh Nagarajan.

## Papers

| Paper | Prices the loop | Status | Read |
| --- | --- | --- | --- |
| **Herd Immunity and Learning Externalities in Markets of Shared Foundation Models** | Socially | Submitted to [ABCSS 2026](https://css-japan.com/abcss2026/) at IEEE BigData on Oct 11, 2026. Decision expected Nov 1 | [PDF](econml/ieee-abcss/submission/abcss2026-herd-immunity.pdf) · [folder](econml/) |
| **A Certified Exploration Framework for Pricing Models That Shape Their Own Data** | Privately | IEEE draft complete. Targeting [LRLS](https://lrls.org/), deadline Oct 30, 2026 | [PDF](ml-or/price-ieee.pdf) · [folder](ml-or/) |

## Layout

| Path | Holds |
| --- | --- |
| [`ml-or/`](ml-or/) | The certified-exploration paper, its derivations and the experiment pipeline |
| [`econml/`](econml/) | The herd-immunity paper, its proofs, certificates and experiment harness |
| [`archive/`](archive/) | Earlier submissions, the scrapped MATH-AI paper and the planning notes |

Each paper folder has its own README with the results, the folder map and what is and is not verified.

## Run the checks

Every closed form in both papers has a numerical check that fails loudly on disagreement. Both suites need only Python and NumPy.

```bash
python ml-or/mlxor-derivations/verify/verify_all.py
```

```bash
python ml-or/posk-pipeline/tests/test_posk.py
```

```bash
for f in econml/ml-contributions/certificates/verify_*.py; do python "$f" || break; done
```

The first runs 38 derivation checks, the second 9 unit tests, and the third 542 assertions across eight certificate files.

## Archive

Both papers were first submitted to NeurIPS 2026 workshops and rejected, and a third reframing for MATH-AI was scrapped. That material is kept under [`archive/`](archive/) with its own [README](archive/README.md). Nothing there is maintained.
