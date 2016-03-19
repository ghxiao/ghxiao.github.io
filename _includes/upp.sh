#!/usr/bin/env bash
export TMPDIR=.
#bib2bib  -c 'author:"xiao"' ~/Dropbox/Papers/biblio.bib > xiao.bib
rm *.4ct *.4tc *.aux *.bbl *.bcf *.blg *.idv *.div *.lg *.log *.run.xml *.tmp *.xref
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
biber pub_body
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"

