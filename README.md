ghxiao.github.io
================

Source code for my personal website: http://www.ghxiao.org


How to update publications
--------------------------

```
$ cd _includes

$ export TMPDIR=.

$ bib2bib -s ../myunsrt.bst -c 'year=2014 and author:"xiao"' ~/Dropbox/Papers/biblio.bib  | bibtex2html -nodoc -d -r -nofooter -use-keys -nobiblinks -nobibsource -nokeys -noabstract -nokeywords -nf Slides-Url slides -nf Url paper -nf Poster poster -nf arXiv arXiv -nf Link link --output bib2014
```

Copyright (c) 2014 Guohui Xiao