import glob
import os
import sys
from cloudmesh.common.util import str_banner
from multiprocessing import pool
from cloudmesh.common3.Shell import Shell
import time
from multiprocessing import Pool

def clean():
    os.system(f"rm -f *.blg")
    os.system("rm -f *_bibertool.bib")
    os.system("rm -rf `biber --cache`")


def biber(file):
    result = ""
    banner = str_banner(file)
    output = Shell.run(f"biber -V --tool {file} | fgrep WARN")
    if len(output) > 0:
        result = banner + output
    return result

clean()

files = sorted(list(glob.glob("*.bib")))

res = Pool().map(biber, files)

print ('\n'.join(res))

clean()
