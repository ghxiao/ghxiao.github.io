#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bibtexparser


def format_author(author_string):
    authors = [a.strip() for a in author_string.split("and")]
    s = ", ".join(authors[0:-1])
    if len(authors) > 1:
        s += " and " + authors[-1]
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




# Martin Giese, Peter Haase, Ernesto Jiménez-Ruiz, Davide Lanti, Özgür Özçep, Martin Rezk, Riccardo Rosati,
# Ahmet Soylu, Guillermo Vega-Gorgojo, Arild Waaler, and Guohui Xiao.
# Optique -- zooming in on big data access. IEEE Computer, Accepted, 2014. [ paper ]

f = open('pub.html', 'w')


def output_journals(publications, f):
    global i, record, author, title, journal, year, ref

    f.write("<h2>Journals</h2>")

    years = sorted(set([int(x["year"]) for x in publications]))

    for y in years:

        f.write(y)

        f.write("\n")
        f.write("<ol>")
        for (i, record) in enumerate(publications):
            author = format_author(record["author"])
            title = record['title']
            journal = record['journal']
            year = record['year']
            ref = "<li> {author}. \n <br/> <em>{title}</em>. <br/> {journal}, {year}. </li> \n" \
                .format(author=author, title=title, journal=journal, year=year)
            f.write(ref)
            f.write("\n")
        f.write("</ol>")
        f.write("\n")


output_journals(journals, f)

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

f.close()