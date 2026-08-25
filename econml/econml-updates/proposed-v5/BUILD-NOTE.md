# Rebuilding the v5 candidate

The repository copy of this directory carries the candidate as a patch
(`v5.patch`) against the committed `econml/paper/`, plus `CHANGES.md`
explaining every edit. The fully built files (`main.tex`, `appendix.tex`,
`make_figures.py`, compiled `main.pdf`) ship in the review-package zip
delivered alongside this branch; the compiled PDF is a binary and is not
committed here.

To reproduce from the patch, from the repository root:

```bash
git apply econml/review-2026-08-25/proposed-v5/v5.patch
cd econml/paper
python make_figures.py
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
pdftotext -f 10 -l 10 main.pdf - | head -2   # must print "References"
```

Verified on 25 Aug 2026: the patch applies cleanly, the build completes
with zero overfull boxes and no undefined references, content ends on
page 9, and References start page 10.
