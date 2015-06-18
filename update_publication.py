#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bibtexparser


def format_author(author_string):
    authors = [a.strip() for a in author_string.split("and")]
    s = ", ".join(authors[0:-1])
    if len(authors) > 1:
        s += " and " + authors[-1]
    return s


# Martin Giese, Peter Haase, Ernesto Jiménez-Ruiz, Davide Lanti, Özgür Özçep, Martin Rezk, Riccardo Rosati,
# Ahmet Soylu, Guillermo Vega-Gorgojo, Arild Waaler, and Guohui Xiao.
# Optique -- zooming in on big data access. IEEE Computer, Accepted, 2014. [ paper ]


def output_journals(publications, f):
    global i, record, author, title, journal, year, ref

    f.write("<h2>Journals</h2>")

    years = sorted(set([int(x["year"]) for x in publications]))

    for y in years:
        f.write(str(y))
        f.write("\n")
        f.write("<ol>")
        for (i, record) in enumerate(publications):
            author = format_author(record["author"])
            title = record['title']
            journal = record['journal']
            year = record['year']
            ref = "<li> {author}. \n <br/> <em>{title}</em>. <br/> {journal}, {year}. </li> \n" \
                .format(author=format_latex(author), title=title, journal=journal, year=year)
            f.write(ref)
            f.write("\n")
        f.write("</ol>")
        f.write("\n")



def output_inproceedings(in_proceedings, f):
    #global i, record, author, title, year, ref
    f.write("<h2>Conference Papers</h2>")
    f.write("\n")
    f.write("<ol>")
    for (i, record) in enumerate(in_proceedings):
        author = format_author(record["author"])
        title = record['title']
        book_title = record['booktitle']
        year = record['year']
        ref = "<li> {author}. \n <br/> <em>{title}</em>. <br/> {book_title}, {year}. </li> \n" \
            .format(author=author, title=title, book_title=book_title, year=year)
        f.write(ref)
        f.write("\n")
    f.write("</ol>")



################################################################
# LaTeX accents replacement
latexAccents = [
    [ u"à", "\\`a" ], # Grave accent
    [ u"è", "\\`e" ],
    [ u"ì", "\\`\\i" ],
    [ u"ò", "\\`o" ],
    [ u"ù", "\\`u" ],
    [ u"ỳ", "\\`y" ],
    [ u"À", "\\`A" ],
    [ u"È", "\\`E" ],
    [ u"Ì", "\\`\\I" ],
    [ u"Ò", "\\`O" ],
    [ u"Ù", "\\`U" ],
    [ u"Ỳ", "\\`Y" ],
    [ u"á", "\\'a" ], # Acute accent
    [ u"é", "\\'e" ],
    [ u"í", "\\'\\i" ],
    [ u"ó", "\\'o" ],
    [ u"ú", "\\'u" ],
    [ u"ý", "\\'y" ],
    [ u"Á", "\\'A" ],
    [ u"É", "\\'E" ],
    [ u"Í", "\\'\\I" ],
    [ u"Ó", "\\'O" ],
    [ u"Ú", "\\'U" ],
    [ u"Ý", "\\'Y" ],
    [ u"â", "\\^a" ], # Circumflex
    [ u"ê", "\\^e" ],
    [ u"î", "\\^\\i" ],
    [ u"ô", "\\^o" ],
    [ u"û", "\\^u" ],
    [ u"ŷ", "\\^y" ],
    [ u"Â", "\\^A" ],
    [ u"Ê", "\\^E" ],
    [ u"Î", "\\^\\I" ],
    [ u"Ô", "\\^O" ],
    [ u"Û", "\\^U" ],
    [ u"Ŷ", "\\^Y" ],
    [ u"ä", "\\\"a" ],    # Umlaut or dieresis
    [ u"ë", "\\\"e" ],
    [ u"ï", "\\\"\\i" ],
    [ u"ö", "\\\"o" ],
    [ u"ü", "\\\"u" ],
    [ u"ÿ", "\\\"y" ],
    [ u"Ä", "\\\"A" ],
    [ u"Ë", "\\\"E" ],
    [ u"Ï", "\\\"\\I" ],
    [ u"Ö", "\\\"O" ],
    [ u"Ü", "\\\"U" ],
    [ u"Ÿ", "\\\"Y" ],
    [ u"ç", "\\c{c}" ],   # Cedilla
    [ u"Ç", "\\c{C}" ],
    [ u"œ", "{\\oe}" ],   # Ligatures
    [ u"Œ", "{\\OE}" ],
    [ u"æ", "{\\ae}" ],
    [ u"Æ", "{\\AE}" ],
    [ u"å", "{\\aa}" ],
    [ u"Å", "{\\AA}" ],
    [ u"–", "--" ],   # Dashes
    [ u"—", "---" ],
    [ u"ø", "{\\o}" ],    # Misc latin-1 letters
    [ u"Ø", "{\\O}" ],
    [ u"ß", "{\\ss}" ],
    [ u"¡", "{!`}" ],
    [ u"¿", "{?`}" ],
    [ u"\\", "\\\\" ],    # Characters that should be quoted
    [ u"~", "\\~" ],
    [ u"&", "\\&" ],
    [ u"$", "\\$" ],
    [ u"{", "\\{" ],
    [ u"}", "\\}" ],
    [ u"%", "\\%" ],
    [ u"#", "\\#" ],
    [ u"_", "\\_" ],
    [ u"≥", "$\\ge$" ],   # Math operators
    [ u"≤", "$\\le$" ],
    [ u"≠", "$\\neq$" ],
    [ u"©", "\copyright" ], # Misc
    [ u"ı", "{\\i}" ],
    [ u"µ", "$\\mu$" ],
    [ u"°", "$\\deg$" ],
    [ u"‘", "`" ],    #Quotes
    [ u"’", "'" ],
    [ u"“", "``" ],
    [ u"”", "''" ],
    [ u"‚", "," ],
    [ u"„", ",," ],
]

#translation_table = dict([(ord(k), unicode(v)) for k, v in accents])
translation_table = dict(latexAccents)
translation_table = dict([(unicode(v), k) for k, v in latexAccents])

def format_latex(s):
    s = unicode(s)
    for k,v in latexAccents:
        s = s.replace(unicode(v),k)
    return s


with open('/Users/xiao/Dropbox/Papers/biblio.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

journals = sorted([x for x in bib_database.entries
                   if x["type"].lower() == "article" and 'Xiao' in x["author"]],
                  key=lambda x: x['year'],
                  reverse=True)

in_proceedings = [x for x in bib_database.entries
                  if x["type"].lower() == "inproceedings" and 'Xiao' in x["author"]]




f = open('pub.html', 'w')

output_journals(journals, f)
output_inproceedings(in_proceedings, f)

f.close()