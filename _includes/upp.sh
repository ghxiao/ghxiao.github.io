#!/usr/bin/env bash
export TMPDIR=.
#bib2bib  -c 'author:"xiao"' ~/Dropbox/Papers/biblio.bib > xiao.bib
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
biber pub_body
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"

