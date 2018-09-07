#!/usr/bin/env python

from pathlib import Path
import subprocess
import os
from itertools import chain

files = chain(Path('section').glob('**/*.md'),
              Path('section').glob('**/*.tex'),                  
              Path('tutorial').glob('**/*.md'),
              Path('tutorial').glob('**/*.tex'),              
              Path('bib').glob('**/*.bib'))

for f in files:
    print(str(f))
    os.system('perl -ane "{ if(m/[[:^ascii:]]/) { print  } }" ' + str(f))
    




