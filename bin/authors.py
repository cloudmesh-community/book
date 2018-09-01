#!/usr/bin/env python
from __future__ import print_function
import subprocess
import textwrap

lines = subprocess.check_output(["git", "shortlog", "-s"]).decode('ascii', 'ignore').split("\n")

names = []
for line in lines[:-1]:
    names.append(line.strip().split("\t")[1])
names = list(set(names))

names.sort()

name_string = '\n> '.join(textwrap.wrap(', '.join(names),79, initial_indent="> "))

print("## Contributors")
print()

print("\n".join(textwrap.wrap("Contributors are sorted by the first letter of their"
                    "combined Firtsname and Lastname and if not available by their github ID", 79)))
print()

print (name_string)
print()
