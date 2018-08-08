#!/usr/bin/env python

import glob
from pprint import pprint
import os
from pathlib import *

d = set()
for path, subdirs, files in os.walk('.'):
    for name in files:
        entry = os.path.dirname(os.path.join(path, name))
        if entry.endswith("images"):
            filename = os.path.join(path, name)
            d.add(os.path.dirname(filename))

d = sorted(d)

for entry in d:
    print (entry)
    
