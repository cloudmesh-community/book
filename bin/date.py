#!/usr/bin/env python
import os
import sys
import subprocess

r = str(subprocess.check_output(['git', 'log', '-1'])).split('\\n')

print("# Version")
print()

for line in r:
    if "Date:" in line:
        print (line)

print()


