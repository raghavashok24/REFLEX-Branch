# 6. Writing style, conventions, clarity

## 6.1 The voice, assessed

The house style (short declaratives, claim-first paragraph heads, no em
dashes, sentences that state their own error direction) is distinctive and,
at its best, exceptional: "The substitution of R for 11' is the whole
paper, so it is derived rather than posited" and "optimistic rather than
conservative" are better sentences than most published papers contain. The
style is an asset. The notes below are about its failure modes, not about
flattening it.

## 6.2 Systematic issues

**Bold saturation.** The body carries roughly fifteen bolded phrases.
Emphasis is a budget: at this density the genuinely load-bearing ones (the
effective number of learners is the number of independent models; the limit
errs optimistic; correction never backfires) compete with ornamental ones
("the substitution frontier" in a caption, "measured" in a table key
sentence). Recommend cutting to six or seven, keeping: the two-question
split in Section 3, the independent-models sentence in Section 1, the
optimistic-limit sentence, the never-backfires sentence, the
individual-evaluation sentence in the conclusion. This is a judgment pass
for the authors, not applied in proposed-v5.

**Aphorism density.** Roughly one paragraph in three ends on an epigram.
Most earn it; a few stack two epigrams where one would land harder (the
critical-crowding paragraph ended on two before v5's trim; the provenance
paragraph ends on three clauses of increasing abstraction). When cutting
for space, cut the second epigram first.

**Long appositive chains.** A recurring construction: claim, comma,
qualifier, comma, re-statement in new vocabulary. Example (Section 2):
"The relation is strict refinement rather than corollary, and
Proposition 3 gives the witness: two markets agreeing on every scalar of
that kind, differing in stability, and so indistinguishable to any
criterion built from those scalars alone." This one works. The pattern
fails when the vocabulary is introduced by the sentence itself, e.g. the
Section 8 sentence defining dry runs, which introduces "reference
environment," "response geometry," and "the map" in one breath. Where a
sentence defines two or more new terms, split it.

## 6.3 Line-level defects found and fixed (applied in proposed-v5)

| Where | Defect | Fix |
|---|---|---|
| Sec 3, base result | "crosses into instability a factor N_eff earlier": category slip, factor vs time | "at a response strength a factor N_eff smaller than any individual dealer's own loop tolerates" |
| Sec 6, first paragraph + Thm 5 | rho = corrected fraction and rho(J) = spectral radius in the same theorem; appendix uses rho_c for the fraction | body unified to rho_c; figure axis labels regenerated to match |
| Sec 8, opening | "Six panels, one per result": the table has seven rows and there are four results | "Six panels, each with its evidential status..." |
| Sec 7, scope sentence | "covers the monoculture, orthogonal and supply-chain configurations": orthogonal is wrong (see `02-technical-rigor.md`) | scope corrected, reason stated |
| Appendix A table | gamma_PO "> gamma" contradicts theta in (0,1] | ">= gamma" |
| Appendix D | 11.8% without its sampling protocol | ranges stated in place |

## 6.4 Line-level suggestions left to the authors (not applied)

- **Abstract length** (~260 words). If trimmed: merge sentences one and
  two; keep every number. The final sentence's "bit for bit" is a strong
  close and correct (relative error 0.00); keep.
- **"The intuition is not new."** After v5's merge this paragraph is tight;
  no further cut recommended.
- **Repetition of "and it errs in the unsafe direction" family.** The
  error-direction motif appears five times (mean index, strong-correction
  limit, twice in Section 5, once in Section 8). It is the paper's
  signature move; five is one or two too many. The mean-index and
  strong-correction instances are the essential ones.
- **Paragraph heads as sentences** ("What determines it is not how many
  firms there are.") work well; the two that are full clauses with internal
  commas ("The collapse, and its honest generalization.") read as titles
  trying to be prose. Harmless; standardize only if convenient.
- **Spelling register**: the paper is UK throughout (defence, favour,
  neighbour, modelled) except for two stray US "modeling" (Sec 9 and
  App F). Standardized to "modelling" in proposed-v5; audited with grep,
  no other UK/US mixes found.
- **"un-blinded"**: hyphenated verb used five times; "corrected" is
  already the paper's own term and reads better in three of the five.

## 6.5 Conventions audit

- No em dashes found in body prose (house rule holds after v5 edits, which
  were written to respect it).
- Citation style uniform; the two new v5 entries follow it (no URLs, no
  DOIs, venue-abbreviated).
- Theorem numbering: body results at Theorem 2, 4, 5, 8 after Lemma 1 and
  Proposition 3 is unusual but internally consistent and explained by the
  shared counter; leave it.
- Figure captions state parameter values and status flags; the v5 caption
  edit keeps that.
