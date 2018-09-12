#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import shutil


data = {
    "filename": sys.argv[1],
    "level": int(sys.argv[2])
    

}

# print ("Adjusting headers {filename} -> {level}".format(**data))
# print (79 * "=")

os.remove("/tmp/convert.md")
os.system("pandoc {filename} --base-header-level={level} -o /tmp/convert.md".format(**data))


# os.system("head  /tmp/convert.md")

shutil.copyfile("/tmp/convert.md", "{filename}".format(**data))
os.system("echo >> {filename}".format(**data))



convert = open("/tmp/convert.md") 
line = convert.readline()
print (line)
line = line.replace("\\#","#")
print(line)

to_file = open("{filename}".format(**data),mode="w")
to_file.write(line)
shutil.copyfileobj(convert, to_file)
