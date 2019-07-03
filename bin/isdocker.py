#!/usr/bin/env python

import os.path
if os.path.exists("/.dockerenv"):
    print ("True")
else:
    print ("False")
