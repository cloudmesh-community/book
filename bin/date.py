#!/usr/bin/env python
from __future__ import print_function
import os
import sys

print("# Version")
print()
sys.stdout.flush()
os.system('git log | fgrep "Date:" | head -n 1')
sys.stdout.flush()

print()

