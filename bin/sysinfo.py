#!/usr/bin/env python
from __future__ import print_function
from sys import platform

if platform == "linux" or platform == "linux2":
    print("linux")
elif platform == "darwin":
    print("osx")
elif platform == "win32":
    print("windows")
