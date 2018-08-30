#!/usr/bin/env python
from __future__ import print_function
import sys
import os

data = {
    "filename": sys.argv[1],
    "level": int(sys.argv[2])
    

}

print ("Adjusting headers {filename} -> {level}".format(**data))
print (79 * "=")

os.system("rm -f /tmp/convert.md")
os.system("pandoc {filename} --base-header-level={level} -o /tmp/convert.md".format(**data))


os.system("head  /tmp/convert.md")

os.system ("cp /tmp/convert.md {filename}".format(**data))
os.system("echo >> {filename}".format(**data))

