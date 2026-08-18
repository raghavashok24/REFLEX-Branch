# 2. Related work

**Status: planned.** Target 0.75 pages. Source:
`../literature/LITERATURE-REVIEW-P2.md`.

---

## The rule for this section

**Prove the deltas, do not assert them.** Six citations get a named-delta
sentence each. Everything else is grouped and cited in bulk. A related-work
section that lists topics tells a reviewer the authors read; one that states
deltas tells them the authors understood. At 0.75 pages there is room for
exactly the second kind.

## Structure: four paragraphs

**Paragraph 1: monoculture is static.** Kleinberg and Raghavan (2021) show
shared algorithms can reduce welfare even when the shared algorithm is better;
Bommasani et al. (2022) formalize outcome homogenization; Toups et al. (2023)
measure it in deployed systems. Delta in one sentence: every one of these
measures a cross-sectional harm on a single allocation round, and a market can
be statically fine and dynamically fragile at the same shared-model fraction.
Add the model-multiplicity inversion, since it is cheap and sharp: multiplicity
asks how much models *could* differ, and this paper measures how much their
feedback directions *do*.

**Paragraph 2: multi-agent performative prediction is blind to direction.**
Narang et al. (2023) and Piliouras and Yu (2023) supply genuine multi-agent
dynamics with equilibrium analysis. Delta, stated at the object level rather
than the topic level: their coupling enters through scalar sensitivity
constants, so two markets with identical constants and opposite alignment
structure are indistinguishable in their conditions and have entirely different
stability here. No directional object means no monoculture, no provenance, no
supply chain, and no policy analysis. Note also that retraining frequency is not
a variable anywhere in this strand, which is what leaves Theorem 2 unposed.

**Paragraph 3: the framing has an ancestor, and it does not learn.** Beale et
al. (2011) named the regulator's dilemma and Wagner (2010) formalized why
individually optimal diversification homogenizes a system. Concede fully: the
private-versus-systemic tension is theirs, and the title of this paper's
Section 3 is theirs. Delta: their agents hold portfolios rather than learn, so
the homogeneity is portfolio overlap rather than alignment of feedback
directions, and there is only one instrument. The second instrument, and
therefore the substitution frontier, exists only because the agents learn.
Khandani and Lo (2007) gets half a sentence as the empirical instance.

**Paragraph 4: the law and the statistic are both borrowed, and both are
conceded.** The herd-immunity threshold is Kermack-McKendrick and Anderson-May;
its spectral form on networks is Wang et al. (2003). Diekmann et al. (1990)
defines `R_0` as the spectral radius of a next-generation operator, which is why
the transfer is exact rather than analogical, and this is the sentence that
converts a suspicious-looking analogy into a structural claim. On the statistic:
`lambda_max` of a correlation matrix as an effective count is standard in
random-matrix finance (Laloux et al., 1999; Plerou et al., 2002), signal
processing (Roy and Vetterli, 2007) and ecology (Hill, 1973). What is new is the
matrix it is computed from and the condition it enters.

## The footnote

One footnote, attached to the first use of "effective number of independent
learners", conceding the naming lineage in full. It costs three lines and
disarms the cheapest available referee objection, which is that the paper
renamed effective rank.

## Held back from the introduction on purpose

The monoculture citations do not appear in Section 1. Their value is the delta,
the delta needs a sentence, and a passing mention in the introduction would
spend the position without buying the argument.

## Do not include

- A survey of performative prediction. Section 3 gives the modulus and that is
  all the setup a reader needs.
- Strategic classification beyond one clause. The response here is aggregate and
  non-strategic, and saying so once is enough.
- The AI-policy literature. It is motivation, belongs in Section 1 or the
  conclusion, and is not prior art for any claim.

## Checklist before this section is called done

- [ ] Six named-delta sentences present, one per load-bearing citation
- [ ] Buchanan-Stubblebine sentence present: the externality is technological,
      not pecuniary, because the coupling runs through the data-generating
      process rather than through prices
- [ ] Weitzman cited for instrument choice, with the acknowledgment that the
      paper does not solve it
- [ ] Herding distinguished from alignment in one sentence: alignment obtains
      even when firms never observe each other
- [ ] No sentence positions REFLEX or PEBSA as the authors' own work
