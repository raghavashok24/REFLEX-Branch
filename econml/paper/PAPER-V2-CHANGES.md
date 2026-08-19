# Paper v2: the review, and what to do about it

**Written 19 Aug 2026, for a later session.** An external review of the compiled
v1 came back at **accept as poster, not spotlight**, with acceptance estimated
around 70% as submitted and high 80s if the top three items below are addressed.
Deadline is 29 Aug 2026, so a session picking this up has ten days or fewer.

**v1 is frozen at commit `486d213`.** Nothing in this document has been
implemented. `main.tex` and `main.pdf` in this folder are still v1: nine content
pages, references from page 10, all certificates passing.

**Step 0 for the next session:** archive v1 before editing. Copy `main.tex` and
`main.pdf` to `v1/` and leave them alone, then edit `main.tex` in place as v2.
This was asked for and deliberately not done here, since doing it without
starting v2 would leave the folder in a half-state.

---

## The verdict, in the reviewer's own terms

What holds it to a weak accept is **W1 combined with W3 and W6**: the technical
step is small, the reduction that makes it work is not derived where reviewers
will look, and the closest prior work is dismissed rather than dispatched. The
variance is driven almost entirely by whether the paper draws a reviewer who
knows the decision-dependent-games literature well.

Two ideas were named as likely to generate argument at a poster: `N_eff` against
HHI, and the substitution frontier. Both survive v2 untouched.

---

## Weaknesses, with an assessment of each

Three of these were checked against the code before being written down. The
assessment column is this session's judgement, not the reviewer's.

| # | Claim | Assessment | Cost |
|---|---|---|---|
| W1 | Novelty is one substitution; technical depth is low for the room | Fair, and structural. Cannot be fixed by writing, only mitigated by W3 and W6 | n/a |
| W2 | The base result is an unrefereed three-month-old preprint, and the one measured panel reproduces that preprint's number in its own simulator | Fair and unfixable in ten days. R1 is the only real answer | see R1 |
| W3 | The reduction to `J = -m_1[(1-kappa)I + kappa R]` is asserted, not derived, in the main text | **The single most fixable high-value gap.** Agreed | ~0.35 pg |
| W4 | The dry runs are close to circular; `7.1e-15` confirms floating-point arithmetic, not dynamics | **Largely correct.** See the note below | ~0 |
| W5 | Section 8 is a promissory note occupying a section | Agreed given the budget | frees ~0.15 pg |
| W6 | Positioning against Narang et al. (2023) is too thin | **Most likely fatal criticism.** Agreed | ~0.5 pg |
| W7 | `N_eff` cancels in the wedge's ignored fraction; Corollary 7 is a generic commons result | **Verified true.** See below | ~0, reordering |
| W8 | (A5) is unnecessary for Theorem 1 | **Verified true.** See below | ~0 |
| W9 | No model is ever run; the `s` decomposition is never measured | Fair, and the same gap as W2 | see R1 |
| W10 | Formatting non-compliance, styled as a main-track paper | **False. Do not act on this** | 0 |
| W11 | The aphoristic register and meta-commentary consume space W3 and W6 need | Fair as a space argument | frees ~0.2 pg |

### W4, what is actually true

The reference environment iterates the retraining map and reads an asymptotic
growth rate, which is close to the power method on the matrix whose radius the
closed form computes. The current defense, that a dry run establishes something
"no algebra check covers", is too strong.

Replace it with what is true: **the dry runs check that the closed forms were
derived from the map we think they were.** That is a real thing to check and it
has caught real errors, but it is a check on the derivation, not evidence about
dynamics. The claims ledger already treats `[DRY RUN]` correctly; only the prose
overstates.

### W7, verified

`t*/(t* + own marginal cost)` is exactly `(N-1)/N` at `chi = 1`, independent of
`kappa` and `s`, checked across `N` in {2, 5, 20} and both parameters. `N_eff`
cancels completely. Crowding enters the wedge's **level** through `V'(m_N)`, not
the distortion's **shape**, so Corollary 7 is a generic commons result.

The paper-specific piece is the **provenance channel**: `dm_N/ds` is linear in
`N` and does not decay, against a private adoption gain that does not grow with
`N`. That asymmetry is a real result and it currently sits at the end of
Section 7. **Lead with it.**

### W8, verified

`R` is PSD with unit diagonal, so every `lambda_i >= 0`, and
`1 + kappa(lambda_i - 1)` is increasing in `lambda_i`, so the radius sits at
`lambda_max` whatever the sign pattern. Checked on 400 random alignment matrices
including strongly negative off-diagonals, plus the simplex at `N` in
{3, 6, 12}: zero mismatches against dense eigensolves.

So (A5) is **not needed for Theorem 1's radius**. It is needed only for the
reading that the binding mode is the common one, which is what Lemma 5's share
interpretation leans on. Move it out of the standing block and attach it to the
interpretation it actually serves. Section 5 already says it needs no analogue of
(A5), which is consistent with this.

### W10, and why not to act on it

The review says the footer reading "Submitted to 40th Conference on Neural
Information Processing Systems (NeurIPS 2026). Do not distribute." shows the
paper is styled as main-track. **It does not.** `main.tex` line 4 already reads
`\usepackage[dblblindworkshop]{neurips_2026}` with
`\workshoptitle{Economics for Machine Learning (EconML)}` on line 5.

The style file prints that generic notice in **every** track when neither `final`
nor `preprint` is set; the track name and workshop title are used only under
`final`. This was verified in v1 by compiling a throwaway camera-ready copy,
which produced "40th Conference on Neural Information Processing Systems
(NeurIPS 2026). Workshop: Economics for Machine Learning (EconML)."

**Acting on W10 would mean modifying the style file, which is grounds for desk
rejection.** Leave it. The only defensible response is that a reviewer might
make the same misreading, and nothing in the authors' control prevents that.

---

## Recommendations, in the reviewer's priority order

### R1. Measure `s` once, on anything real

**Highest value per unit effort, and the one that changes the paper's category.**
Two LoRA fine-tunes of one open base model plus one independently trained model,
finite-difference response Jacobians on a shared synthetic environment, then
report the three pairwise alignments and the resulting `lambda_max`.

Even `N = 3` with a crude environment converts the central empirical claim from
asserted to observed. It is the difference between an interesting formal model
and an interesting formal model with a measurement hook.

**Assessment.** This is the only item that answers W2 and W9 together, and it is
the only one that adds evidence rather than rearranging what is there. It is also
the only item that needs compute and a model, so it is the one most likely to
slip. **Decide early whether it is in or out**, because the paper's framing
around it differs: if it lands, the abstract and Section 9 both change.

If it lands, it is a new panel and a new ledger row at `[MEASURED]` only if it
genuinely measures alignment between real models. A synthetic environment with
real model Jacobians is arguably its own status; do not stretch `[MEASURED]` to
cover it without saying exactly what was measured.

### R2. Move the joint-Jacobian derivation into Section 3

The crux of the paper is not in the main text, and the call for papers says the
main text must be self-contained because reviewers need not read the appendix.
The derivation exists and is certified: `derivations/01` Lemma 1, certificate
C22, agreement `5.6e-17`. It is the reduction lemma, and it is currently one
line in Section 3 saying the substitution is made.

Buy the space from Section 8 (W5) and the meta-commentary (W11).

### R3. Half a page on Narang et al. (2023)

State their condition, state ours, and state the containment relation: implied
by, strictly sharper than, or genuinely orthogonal. Right now the reader has to
take the paper's word that Theorem 1 is not a corollary of their result.

**This is the most likely fatal criticism and it costs half a page to defuse.**
The literature review already has the material in cluster B; it has never been
compressed into the containment statement a reviewer wants.

### R4. Fix the style file and the footer

**Do not do this.** See W10. Already compliant.

### R5. Two smaller edits

Soften the dry-run defense to what it establishes (W4), and lead Section 7 with
the provenance channel (W7). Both are close to free.

---

## PEBSA

Asked for separately: **strengthen the PEBSA connection without spending more
space than it already occupies.** It currently gets one sentence in Section 2,
framed as exogenous against endogenous measurement channels.

The strengthening that costs nothing is to make the contrast do work rather than
sit there. The current sentence says the channels differ. The stronger version
says what follows from the difference: an exogenous-signal estimator has accuracy
that does not depend on the state of the system it measures, while the estimator
in Section 8 sharpens as the system approaches instability, so the two face
opposite sample-complexity problems near the event of interest. That is the same
length and it makes the citation load-bearing instead of decorative.

Do not expand it beyond one sentence, and do not add a second citation to it.

---

## Space arithmetic

v1 is exactly nine content pages with no slack. Content ends on page 9 and
references start on page 10; this was verified from a clean two-pass build.
**Every addition needs an equal subtraction.**

| Item | Direction | Estimate |
|---|---|---|
| R2, the reduction derivation | needs | ~0.35 pg |
| R3, Narang containment | needs | ~0.50 pg |
| R1's panel, if it lands | needs | ~0.30 pg |
| W5, Section 8 into the conclusion | frees | ~0.15 pg |
| W11, meta-commentary trim | frees | ~0.20 pg |
| W7, reorder Section 7 | neutral | 0 |
| W4, W8 rewording | neutral | 0 |

Needs run to roughly `1.15` pages against `0.35` freed, so **R1 through R3
together do not fit without cutting a figure.** The cheapest figure to lose is
the cadence panel in Figure 1, whose result is fully carried by the inline
`20.68 / 5.28 / 2.53` numbers. That frees about `0.25` and leaves the phase
diagram at full width.

That still leaves roughly half a page short. The next candidates, in order:
Section 2's monoculture paragraph compresses to three sentences, and Section 9's
per-panel prose can defer to Table 2 entirely. Neither touches Sections 4 to 6.

**Do not compress Sections 4 to 6.** That rule survives from v1 and the review
does not challenge it.

---

## What not to change

- **The status flags and the claims ledger.** The review explicitly praised the
  honesty about evidential status as rare. Nothing in v2 should round a
  `[DRY RUN]` up.
- **`N_eff` against HHI, and the substitution frontier.** Named as the two ideas
  that will generate argument at a poster.
- **The style file.** See W10.
- **The nine-page discipline.** Content must end on page 9. Verify with a clean
  two-pass build, not an incremental one, since a stale `.aux` hid a
  three-line overflow during the v1 build.

## Suggested order

Decide R1 in or out first, because it changes the abstract and Section 9. Then
R2 and R3, which are the two that move the acceptance estimate. Then R5 and the
PEBSA sentence, which are close to free. Then W8's relocation. Reconcile the four
status surfaces last, as its own pass, exactly as v1 did.

If the days run short, **R3 before R2**: the review calls it the most likely
fatal criticism, and it is cheaper.
