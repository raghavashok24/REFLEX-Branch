#!/bin/sh
# Build the tarball to upload to arXiv.
#
# arXiv rejects a submission that carries both TeX source and a compiled PDF, so
# main.pdf is deliberately excluded, as is this directory's README, which is
# repository documentation rather than part of the paper. Everything else here
# is needed: arXiv's TeX Live has every \usepackage the build calls for, but
# neurips_2026.sty is a local style file and must ship with the source.
#
#     sh package.sh
#
# Then upload arxiv-submission.tar.gz. arXiv runs pdfLaTeX (forced by the
# \pdfoutput=1 on line 2 of main.tex) and does not need a BibTeX pass: the
# bibliography is a thebibliography environment inside main.tex.
set -eu

cd "$(dirname "$0")"
OUT=arxiv-submission.tar.gz
rm -f "$OUT"

tar czf "$OUT" \
    main.tex \
    appendix.tex \
    checklist.tex \
    neurips_2026.sty \
    figures/fig_cadence.pdf \
    figures/fig_herd.pdf \
    figures/fig_phase.pdf \
    figures/fig_substitution.pdf \
    figures/fig_wedge.pdf

echo "wrote $OUT"
tar tzf "$OUT"
