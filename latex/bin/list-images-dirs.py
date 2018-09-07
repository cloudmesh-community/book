#!/usr/bin/env python

from pathlib import Path
import subprocess
import os
from itertools import chain

files = Path('.').glob('**/images/')
notebooks = chain(Path('.').glob('notebooks/**/*.png'),
                  Path('.').glob('notebooks/**/*.jpeg'),
                  Path('.').glob('notebooks/**/*.jpg'))                      


s = set()
for f in notebooks:
    s.add(os.path.dirname(f)+"/")
    s.add(os.path.dirname(os.path.dirname(f))+"/")



print("\\graphicspath{%")
print("{.}%")

for f in files:
    d = str(f)
    if d == "images":
        print("{images/}%")
    else:
        d = d.replace("/images","/")
        print ("{",d,"}%", sep="")

for entry in s:
    print ("{",entry,"}%", sep="")

        
print ("}")

