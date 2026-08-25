# Proposed v5: every change, with rationale

Candidate build carrying the pre-deadline fixes from the review package.
Compiled and gate-checked: content ends page 9, References start page 10,
zero overfull boxes, no undefined references. Figures regenerated from the
committed result JSONs (two axis labels changed, nothing else).

In the repository this candidate lives as `v5.patch` (see `BUILD-NOTE.md`);
the fully built files including the compiled PDF ship in the review-package
zip. Adopt whole or cherry-pick. After any adoption: run `make_figures.py`,
three pdflatex passes, then the page gate
(`pdftotext -f 10 -l 10 main.pdf - | head -2` must print References).

## Additions

| # | Change | Why |
|---|---|---|
| A1 | Related work, multiplayer paragraph: two-sentence dispatch of Piliouras and Yu (EC 2023) and Li, Yau, Wai (NeurIPS 2022); bibliography entries added | Known multi-agent performative prediction papers; uncited is a lit-review strike, cited-and-dispatched strengthens the containment story. See `01-novelty.md` 1.2 |
| A2 | Related work, monoculture paragraph: closing sentence citing Kim, Garg, Peng, Garg (ICML 2025) measuring cross-model error correlation, placed after the "All four" sentence so that count stays unambiguous | Grounds the paper's premise empirically; sets up the measured-alignment panel if built |
| A3 | Appendix D: the 11.8% figure now carries its sampling ranges and a note that the fraction is protocol-dependent while the direction is not | The number is meaningless without the draw; a reviewer who resamples gets a different fraction (an independent draw here gave 17%) |

## Corrections

| # | Change | Why |
|---|---|---|
| C1 | Wedge scope (body Sec 7): "monoculture, orthogonal and supply-chain" corrected to monoculture and supply-chain at any s>0, orthogonal corner excluded; body Lemma 6 gains "kappa>0 and lambda_max(R) simple"; appendix (W3) gains the simplicity requirement and the reason | At R=I the leading eigenvalue is degenerate and the share formula fails (one-sided derivative 1, not 1/N). Worked counterexample in `02-technical-rigor.md` 2.2 |
| C2 | Corrected fraction renamed rho_c in the body (definition and substitution-frontier caption); figure axis labels regenerated to match | Body used rho for the fraction and rho(J) for a radius in the same theorem; appendix already used rho_c |
| C3 | Notation table: gamma_PO ">= gamma" (was ">") | theta in (0,1] includes equality |
| C4 | "crosses into instability a factor N_eff earlier" made precise: "at a response strength a factor N_eff smaller than any individual dealer's own loop tolerates" | Factor-vs-time category slip |
| C5 | "Six panels, one per result" reworded | The table has seven rows and there are four results |
| C6 | Two stray US "modeling" standardized to "modelling" | The paper's register is UK throughout (defence, favour, neighbour, modelled) |

## Trims (paying the page bill; nothing cut carries a claim not stated elsewhere)

| # | Change | Where the content survives |
|---|---|---|
| T1 | Intro: banks/quants sentence tightened | Same claims, same citations, one line saved |
| T2 | Sec 3: technological-externality sentence tightened | Same distinction, same citation |
| T3 | Sec 4: post-Proposition-3 sentence restating the proposition cut | The proposition itself, and the kept closing sentence |
| T4 | Sec 4: hypothesis-(C) verification sentence folded into the independence sentence | Appendix C, certificate C12 |
| T5 | Sec 5: critical-crowding close tightened; "What the lever costs" paragraph folded to one sentence with an appendix pointer | Appendix C carries the staleness statement in full |
| T6 | Sec 6: integer-count sentence (regulator's count vs naive rounding) replaced by an appendix pointer | Appendix D, certificate H4, worked table |
| T7 | Sec 9 limitations: two sentences joined | No content change |
| T8 | Related work: equilibrium-statements sentence tightened | No content change |

## Explicitly NOT changed

- No status flag moved; no DRY RUN language softened.
- The style file, checklist, footer, and blind arrangements untouched
  (see `paper/README.md`'s two do-not-act items; both remain in force).
- The abstract untouched (optional trim notes in `06-writing-style.md`).
- Bold-weight reduction and the internal/external-validity rewording are
  left as judgment calls (`06-writing-style.md`, `04-narrative.md`).
