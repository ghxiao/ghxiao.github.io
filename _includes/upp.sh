#!/usr/bin/env bash

htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"
biber pub_body
htlatex pub_body.tex  "xhtml, charset=utf-8" " -cunihtf -utf8"

