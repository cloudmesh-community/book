#!/usr/bin/env python

from pathlib import Path
import subprocess
import os

from itertools import chain

files = chain(Path('section').glob('**/*.md'),
              Path('tutorial').glob('**/*.md') )



for md in files:
    
    tex = str(md)
    tex = tex.replace(".md", ".tex")
    if os.path.isfile(tex):
        content = open(tex, 'r').read()
        if "DO NOT MODIFY THIS FILE":
            print (tex)
            os.remove(tex)
