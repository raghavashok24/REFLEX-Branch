# 5. Scope and fit: EconML @ NeurIPS 2026, Atlanta

## 5.1 The venue, re-verified 25 Aug 2026

Checked against the workshop site (econml26-workshop.github.io, read via
web search; the site itself is egress-blocked from this environment, so
details were cross-checked across the search index, the NeurIPS 2026
workshop announcement, and the OpenReview group page listing):

- **Name**: Economics for Machine Learning (EconML), NeurIPS 2026 workshop,
  Atlanta, 12 or 13 Dec 2026. Matches `\workshoptitle` exactly.
- **Tracks**: the call organizes the workshop around two complementary
  directions:
  1. **Economic Tools for Machine Learning**: economic ideas improving
     learning and alignment, revealing limitations of existing algorithms
     and paradigms, aligning incentives in local interactions around AI
     systems.
  2. **Machine Learning Ecosystems with Interacting Models**: what economic
     phenomena emerge when many models interact in shared environments, and
     how interventions can improve ecosystem-level outcomes.
- **Formats**: long (nine content pages) and short (four); no theory track,
  reviewers not required to read beyond the main text; empirical evaluation
  of theoretical models listed among encouraged directions. This matches
  `paper/README.md`'s two do-not-act items, which remain correct.
- **Deadline**: 29 Aug 2026 AoE. The site's "30 Aug, 11:59/12:00 UTC" is
  the same instant expressed in UTC (AoE is UTC-12), so the repo's date is
  right and there is no extra day. Plan the submission for 28 Aug local to
  be safe.
- **In-person presentation** required; the repo already plans for it.

## 5.2 Fit assessment

The paper is close to a definitional match for Track 2: many models, one
shared environment, an emergent economic phenomenon (the learning
externality), and interventions evaluated at the ecosystem level (cadence
caps, correction mandates, diversity floors, a Pigouvian fee). It also
reaches into Track 1 through the externality/public-good machinery. Few
submissions will sit this squarely on the workshop's second axis; the risk
is not fit but legibility of fit.

Two low-cost moves make the fit impossible to miss:

1. **Speak the call's language once in the introduction.** The call's
   phrase is "ecosystem-level outcomes"; the paper's is "market of models."
   One clause tying them ("the market-level, ecosystem-scale question of
   what happens when many adaptive models share an environment") lets a
   program-committee skim place the paper in Track 2 without inference.
   (Not applied in proposed-v5: wording of the intro is voice-sensitive;
   the one-clause version costs no lines if it replaces "the market it
   runs in" in the first paragraph of the introduction.)
2. **Keep the economics load-bearing, which it already is.** The wedge,
   the public-good reading, Weitzman, and the HHI critique are exactly the
   kind of genuine economic content the call wants from an ML-ecosystems
   paper, not decoration. No change needed.

## 5.3 Compliance, re-verified on the build

- Nine content pages ending with the conclusion; references, appendix, and
  checklist from page 10. Rebuilt from source in this environment and
  re-checked; also re-checked on the proposed-v5 candidate.
- `dblblindworkshop` option, style file unmodified, no `final`/`preprint`,
  line numbers on. The footer's generic "Do not distribute" notice is
  correct behaviour for the submission build (documented in
  `paper/README.md`; two external reviews have already tripped on this,
  and the do-not-act instruction there is right).
- Blind: no author block, no URLs in the bibliography, metadata clean,
  third-person self-citation. The commented-out artifact URL stays
  commented until camera-ready.
- Checklist: 16 of 16 answered; the two "no" answers are justified and
  defensible.

## 5.4 Audience calibration

Expect reviewers from the performative-prediction and algorithmic-
monoculture communities (the citation graph of the call's organizers and
the two tracks point there). That audience will: recognize and value the
containment against Narang et al.; know Piliouras-Yu and Li-Yau-Wai, which
is why `01-novelty.md` item 1.2 is not optional; accept dry-run framing if
stated confidently; and push hardest on (H1) and on the absence of any
measured alignment, which is why the measured-alignment panel is the
highest-impact addition. The economics half of the audience will find the
wedge section familiar in shape and novel in the N_eff amplification; the
provenance-channel asymmetry is the sentence to say out loud in the talk.
