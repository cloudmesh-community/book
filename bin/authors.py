#!/usr/bin/env python
from __future__ import print_function
import subprocess
import textwrap

lines = subprocess.check_output(["git", "shortlog", "-s"]).decode('ascii', 'ignore').split("\n")

names = []
for line in lines[:-1]:
    names.append(line.strip().split("\t")[1])

book = [
    "Geoffrey C. Fox",
    "Ankita Rajendra Alshi",
    "Averill Cate, Jr",
    "Bertolt Sobolik",
    "Bo Feng",
    "Fugang Wang",
    "Gregor von Laszewski",
    "Hyungro Lee",
    "Miao Jiang",
    "Min Chen",
    "Saber Sheybani",
    "Sandeep Kumar Khandelwal",
    "Silvia Karim",
    "Tim Whitson",
    "Tyler Balson",
    "Vibhatha Abeykoon",
    "aralshi",
    "Arnav",
    "Bertholt Sobolik",
    "Fugang Wang",
    "janumudvari",
    "Juliette Zerick",
    "karankotz",
    "Javier Diaz",
    "Swarnima H. Sowani"
]
    
names = names + book
names = list(set(names))

names.sort()

name_string = '\n> '.join(textwrap.wrap(', '.join(names),79, initial_indent="> "))

print("## Contributors")
print()

msg = """

Contributors are sorted by the first letter of their "combined
Firtsname and Lastname and if not available by their github ID.

Please note that the authors are identified through git logs in
addition to some contributors added by hand. The git repository
contains more than the documents included in this section. Thus not
everyone in this list may have directly contributed to this
document. However if you find someone missing that has contributed
(they may not have used this particular git) please let us know. We
will add you.

The contributors that we are aware of include:

"""

print("\n".join(textwrap.wrap(msg, 79)))
print()

print (name_string)
print()
