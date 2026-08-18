# 10. Limitations and conclusion

**Status: planned.** Target 0.60 pages.

---

## Limitations

State these in the paper, in the paper's own voice, before a reviewer states
them. Each is a standing assumption from Section 3 with its consequence made
explicit.

- **Linearized stability analysis** around the joint equilibrium, with the
  simulator as the nonlinear check.
- **Theorem 1 is exact for equal moduli.** The heterogeneous-modulus case is a
  two-sided bound whose tightness is measured, not asserted. Share-weighted
  alignment and the fully heterogeneous secular reduction are named extensions,
  not results.
- **The herd-immunity clean form is the strong-correction limit**, and the
  `1 - 1/R_0` collapse additionally assumes the `kappa = s = 1` corner. The
  exact two-block root is reported alongside it.
- **Synchronous deployment and a common cadence.** Asynchronous clocks are named
  as an extension.
- **Theorem 4 prices instability through stationary variance**, a modeling
  choice defended in the text as the smooth proxy for divergence risk.
- **The cadence lever buys stability with model staleness**, quantified rather
  than presented as free.
- **`R` and `s` are not observable to an outsider.** Section 8 is the designed
  answer and its real-data leg is consistency evidence with a placebo, not
  identification of monoculture. Provenance caveats inherited verbatim: public
  proxies, not trade-level TRACE.

## What the conclusion should do

Not summarize. At nine pages with numbered result sections, a summary paragraph
is dead space. Two jobs instead.

**Restate the certification claim, once, as the thing to take away.** Individual
model evaluation cannot certify a market of models, and the quantity that
determines the difference is the effective number of independent learners, which
no individual evaluation can see.

**Name what follows for policy, concretely.** A regulator already writing
systemic-risk obligations for shared general-purpose models has a threshold but
no mechanism connecting model sharing to a measurable systemic quantity. This
paper supplies one, along with two substitutable instruments and a price. The EU
AI Act's general-purpose-model provisions are the concrete hook, cited if the
article numbers verify and dropped if they do not.

Then stop. No future-work list: the deferred items are named where they arise,
in Sections 4, 6 and 8, which is where a reader encounters the gap and is
therefore where the deferral reassures rather than accumulates.

## Anonymization checklist

Run before freeze, as a separate pass, against the built PDF rather than the
source.

- [ ] No author block
- [ ] No repository URL anywhere, including figure paths and captions
- [ ] PDF metadata scrubbed (author, title, producer, creation host)
- [ ] Figure files carry no local paths in their embedded metadata
- [ ] Simulator described generically with an anonymized-artifact promise
- [ ] REFLEX and PEBSA cited as ordinary third-party references, with full
      bibliographic detail
- [ ] **No sentence positions either as the authors' own work.** No "our earlier
      framework", no "we previously showed", no "building on our REFLEX".
      Grep the source for "our" and check each hit
- [ ] Acknowledgments section absent or anonymized
