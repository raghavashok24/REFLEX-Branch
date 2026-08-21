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

  Note from the user - Do NOT cut any figures. Preserve all remaining figures, and figure out other ways to free space, maybe by cutting nonessential text (text that the paper will still read fine and be great without). Maybe don't add an entire half page to the Narang citation, and instead make it 0.35 pages or something a bit less - just an idea, you make the call.

## Suggested order

Decide R1 in or out first, because it changes the abstract and Section 9. Then
R2 and R3, which are the two that move the acceptance estimate. Then R5 and the
PEBSA sentence, which are close to free. Then W8's relocation. Reconcile the four
status surfaces last, as its own pass, exactly as v1 did.

If the days run short, **R3 before R2**: the review calls it the most likely
fatal criticism, and it is cheaper.

---

# v2, as built

**Implemented 19 Aug 2026.** `main.tex` in this folder is now v2. v1 is archived
unchanged in [`v1/`](v1/) and frozen at commit `486d213`. Content still ends on
page 9 and references start on page 10, verified from a clean three-pass build.

## Implemented

| Item | What was done |
|---|---|
| **R2** | Lemma 1 (Reduction) now sits at the end of Section 3 with (H1) to (H4) stated compactly, the `J = -m_1[(1-kappa)I + kappa R]` display, and a three-line proof sketch. (H2) is labelled as (A2) restated in the new object rather than duplicated. Theorem 2 now cites the display instead of restating it |
| **R3** | The Section 2 Narang paragraph carries the containment statement: their scalar condition, our spectral one, and the verdict that ours is **strictly sharper on the class their constants describe and not implied by theirs**, with the reason for each half. Built to ~0.35 pg, not the 0.50 the review estimated |
| **R5 / W4** | The dry-run defense no longer claims a dry run establishes something no algebra check covers. It now says what is true: the runs check that the closed forms were derived from the map we think they were, a check on the derivation that has caught real errors |
| **R5 / W7** | Section 7 leads with the provenance channel, which now sits before Corollary 8. The corollary is followed by the statement that `N_eff` cancels from the ignored fraction, so Corollary 8 is the generic commons result and the provenance asymmetry is the paper-specific one |
| **W8** | (A5) is out of the standing assumption block, which now runs (A1) to (A4). It is restated in Section 7 attached to the reading of Lemma 6 that actually needs it, prefaced by the fact that Theorem 2's radius needs no sign condition at all. Section 5's remark was reworded, since there is no longer an (A5) for it to disclaim an analogue of |
| **PEBSA** | Still one sentence, still one citation. It now says what follows from the difference: an exogenous-signal estimator's accuracy does not depend on the state of the system it measures, the Section 9 estimator sharpens as the system approaches instability, so the two face opposite sample-complexity problems near the event of interest |
| **W5** | Section 8 is folded into the closing section as its opening paragraph. The paper is nine sections rather than ten |
| **W11** | Meta-commentary cut throughout: "which is what the gate is for", "stated plainly", "we do not re-derive it", "The choice is defended rather than assumed", "We quantify it rather than presenting it as free", the "Naming" paragraph (which duplicated a Related-work sentence verbatim), and the commentary sentences closing the herd-immunity and analogy paragraphs |

## Deliberately not done

- **R1**, measuring `s` on real models. Out. The repo has no `transformers`,
  `peft` or LoRA infrastructure, the experimental stack is CPU-only and
  deterministic, and the panel would cost 0.30 pg the budget cannot fund. The
  abstract and the closing section keep their v1 framing.
- **R4**, the style file and footer. Out, and acting on it would be harmful.
  `neurips_2026.sty` is untouched. See W10 above.
- **No figure or table was cut.** All five figures and both tables survive.
  Every page of space came from prose, plus figure *sizing*: the two-panel rows
  went from `0.49` to `0.40\textwidth` and the wedge figure from `0.88` to
  `0.60`. Panels are smaller, none is missing.
- **No status flag moved.** Reconciled against `../writing/CLAIMS-LEDGER.md` as
  a separate pass: one `[MEASURED]` panel and six `[DRY RUN]` rows in the body,
  matching E1 and E2 through E6 in the ledger. Since R1 is out, nothing should
  have moved, and nothing did.
- **Sections 4 to 6 were not compressed**, as the v1 rule requires.

Two ledger-backed numbers were dropped from the body for space and remain in the
ledger: the per-`N` common-mode moduli behind panel 1's amplification (E1.1, the
amplification figures themselves stay in Table 2) and the fee's `1.7e-13`
implementation error (E6.2). Neither supports a claim the body still makes.

## One build change

`main.tex` now sets `\hypersetup{draft=true}`. A cross-reference link straddling
the page 2/3 break aborts pdfTeX with "\pdfendlink ended up in different nesting
level than \pdfstartlink"; neither `breaklinks` nor a larger `pdf_mem_size`
avoids it, and the layout that triggers it is the one that fits nine pages.
Making hyperref inert leaves the printed page identical and costs only
clickability, which a double-blind submission does not need. **Drop the line for
the camera-ready**, where the layout differs anyway.

The build now needs **three passes**, not two: the added Lemma 1 shifts the
theorem numbering that the cross-references resolve against.

---

# The appendix, added 20 Aug 2026

v2 shipped with an appendix that was one paragraph long and pointed at
supplementary material for every proof. That is backwards for this venue.

**The policy, checked at the source.** The workshop's call caps the main text at
nine content pages, excludes references, appendices and the checklist from that
count, and defers to the NeurIPS 2026 main track handbook for format. The
handbook puts paper content, references, appendices and the checklist in a
**single PDF**, and reserves the separately uploaded ZIP for **data and source
code**. Proofs belong in the appendix of the submission itself. Nothing in the
workshop's call mentions a supplementary upload at all, so the material the
pointer promised had no guaranteed route to a reviewer.

**What was added.** `appendix.tex`, ten appendices, typeset from the derivation
files in `../math/`:

| Appendix | Content |
|---|---|
| A | Notation and the standing assumptions, with (A5) placed where it is used |
| B | The reduction, the properties of the alignment matrix, the spectrum, the three anchors, the signed error of mean-based indices, the heterogeneous-modulus bound |
| C | Concentration of the alignment matrix to the supply-chain limit, entrywise and spectral |
| D | The cadence composition: inner contraction, lazy deployment, hypothesis (C), the frontier, critical crowding |
| E | The mixed market: the secular equation, the two-block quadratic, the optimism of the strong-correction limit, the imperfect-correction law, the threshold in whole firms |
| F | The wedge: the welfare object, the marginal crowding share, both first-order conditions, over-adaptation, the provenance channel |
| G | Supervision from public prices, deferred and stated as such |
| H | The certificate inventory: seven files, 525 assertions, and the two certificates that falsified rather than confirmed |
| I | Experimental specifications: the two environments, the inherited protocol, the six panels, and why five of six are dry runs |
| J | The deferred register |

Body results keep their numbers and are proved in the appendix by name, so
Lemma~1 and Theorems 2, 3, 4 and 7 are proved under those headings. Results
stated only in the appendix carry appendix-local numbers, B.1 through F.2, so
nothing collides.

**What changed in the body.** Two sentences, both rewritten to the same length so
the nine-page fit is untouched: Section 8 now points at the appendix for proofs
and specifications and reserves supplementary material for code, and the
supervision paragraph no longer implies the real-data panel was run, since it is
scoped in Appendix G and deferred. Three checklist answers were repointed at the
appendix: question 3 on proofs, question 4 on the protocol, question 5 on what
goes to reviewers.

**Verified.** Clean three-pass build, 31 pages, content still ending on page 9
with references starting on page 10. One overfull hbox remains, 13.6 points in
the body's anchor table, and it predates this change.

---

# v3, as built

Built 20 Aug 2026. A small, targeted pass on top of v2: four changes, one
deliberate non-change, and one table cut to pay for the space. No status flag
moved, no figure was cut, and Sections 4 to 6 were not touched.

## What v3 implemented

**1. The abstract no longer states a corner case as a general law.** It read
that the market is stable "exactly when the corrected fraction exceeds
`(1-1/m_N)/e`". That closed form is exact only at `kappa = s = 1`; away from
that corner the exact threshold is the larger root of the two-block quadratic,
as `math/derivations/04-mixed-market-secular.md` Section 7 and Appendix E both
say. The sentence now carries the qualifier "exact in the fully shared limit and
accurate away from it" and keeps the imperfect-vaccine framing. Checklist
question 1's justification records the qualifier.

**2. Panel 1 is no longer called external validation.** Table 2's caption said
"external validation against a prior published run". The prior run is
`reflex2026`, this paper's own base work cited in the third person, so
"external" is a claim about independence that third-person citation cannot
support. Two further copies of the same overreach were found and fixed: the
same phrase in Appendix I's panel description, and "externally validated" in
checklist question 1.

The caption now says panel 1 is measured in the order-flow simulator rather than
in the reference environment, and that it reproduces the base result this paper
generalizes, so it validates the inherited scaffolding rather than any of the
four new results. Section 8's paragraph gained one sentence naming the claim as
the monoculture corner `R = 1 1'`. **The flag did not move.** Panel 1 is still
`[MEASURED]` and still the paper's one measured result; what changed is what the
paper says that measurement is evidence for.

**3. Two references added, closing a gap in this workshop's own community.**
Related work covered algorithmic monoculture and multiplayer performative
prediction but cited nothing from the line of work on competition between model
providers. Added, both verified against the published proceedings on 20 Aug 2026:

| Reference | Authors | Venue |
|---|---|---|
| Monoculture in Matching Markets | K. Peng, N. Garg | NeurIPS 2024 |
| Supply-Side Equilibria in Recommender Systems | M. Jagadeesan, N. Garg, J. Steinhardt | NeurIPS 2023 |

**Two, not five.** A padded bibliography is its own tell, and three further
candidates were left out because no sentence needed them. The monoculture
paragraph was extended rather than replaced, in the same register as the Narang
containment: Peng and Garg is named as the nearest neighbour and the first of
these to carry market effects, Jagadeesan et al. as the supply-side move, and
the delta is that all of them are equilibrium statements read at the market's
resting point, so none expresses a stability boundary or a rate and none carries
an object for which direction each firm perturbs the environment. The
bibliography is 24 entries, still alphabetical, still uniform, still no URLs.

**4. `\workshoptitle` matches the call exactly.** The trailing "(EconML)" is
gone. The string prints only at camera-ready, so the submission build is
unchanged; matching the call costs one edit and removes an argument.

## The deliberate non-change

**The page footer is still the generic notice, and that is correct.** An
external review reads "Submitted to 40th Conference on Neural Information
Processing Systems (NeurIPS 2026). Do not distribute." as proof the workshop
option is missing. It is not. `main.tex` line 4 sets `dblblindworkshop` and line
5 sets `\workshoptitle`; in `neurips_2026.sty` the `\@trackname` string is used
only inside `\if@neuripsfinal`, so with `final` and `preprint` both unset the
style file prints the generic notice in every track. The workshop title appears
at camera-ready. **The style file was not modified**, since modifying it is
grounds for desk rejection and would cause the exact outcome the "fix" claims to
prevent.

## What paid for the space

The body was nine content pages with zero slack, and items 1 to 3 add material.
Three sources, in the order the space was needed:

1. **Table 1, the anchors table, deleted.** Appendix B gives all three corner
   anchors and Appendix C the supply-chain row, both with more detail than the
   table carried, so the body now states the four values inline in one sentence
   and points at the appendices. This was the largest single recovery and it
   loses nothing a reader needs in the body.
2. **The related-work addition tightened** after the first build spilled three
   lines, removing a sentence that restated the paragraph's closing point.
3. **Section 8's protocol sentences deferred to Appendix I**, which already
   carried them close to verbatim: determinism from a (config, seed) pair, and
   stability estimated from realized trajectories rather than from an eigensolve.
   The "why the rest are not measured" paragraph was compressed against the same
   appendix.

No figure was cut, Sections 4 to 6 were not compressed, and no `[DRY RUN]` was
rounded up.

## Verified

Clean three-pass build from a deleted `main.aux`. 31 pages. Content ends on
page 9 and `pdftotext -f 10 -l 10` prints the References heading. **Zero
overfull boxes:** the 13.6 point box that predated v3 lived in the anchors
table and went with it. The only remaining log warning is the deliberate
`hyperref` draft mode. Style file unmodified, PDF metadata empty, no author
block, no repository URL, line numbers present.

Status surfaces reconciled against the built PDF: no flag moved anywhere, the
nine section numbers are unchanged so the checklist's cross-references still
resolve, and the two checklist justifications touched were reworded for the
panel 1 framing rather than repointed.

## Archive

v1 and v2 now sit side by side under `archive/`. v1 is unchanged from commit
`486d213`; v2 is `main.tex`, `appendix.tex` and `main.pdf` as they stood before
this pass. The former `v1/` directory is gone.
