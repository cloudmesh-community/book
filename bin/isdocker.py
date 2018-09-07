#!/usr/bin/env python
from __future__ import print_function
import os.path
if os.path.exists("/.dockerenv"):
    print ("True")
else:
    print ("False")
