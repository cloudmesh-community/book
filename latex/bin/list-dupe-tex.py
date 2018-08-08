#!/usr/bin/env python

import glob
import os.path

'''
Usage: python bin/list-dupe-tex.py | grep True
'''
for md_file in glob.iglob('./**/*.md', recursive=True):
    tex_file = md_file[:-2]+'tex'
    print(os.path.isfile(tex_file), tex_file)
