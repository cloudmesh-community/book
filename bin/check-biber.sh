#!/usr/bin/env python
import sys
from textwrap import indent

changedfiles = sys.argv[1]

with open(changedfiles, "r") as f:
    files = f.read().split()

for file in files:    
    if ".bib" in file:
        print ("B", file)
        os.system ("biber  -V --tool {file} | fgrep WARN".format(file=file))

