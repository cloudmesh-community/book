#!/usr/bin/env python

from pathlib import Path
import subprocess
import os
from itertools import chain

files = chain(Path('section').glob('**/*.md'),
              Path('tutorial').glob('**/*.md') )

for f in files:
    data = subprocess.check_output(["python3", "bin/md-to-tex.py",str(f)]).decode("utf-8")

    tex = str(f)
    tex = tex.replace(".md", ".tex")
    print ("convert:",  f, "->", tex)

    with open(tex, "w") as output:
        output.write("\\MDNAME\\\n")
        output.write(data)
