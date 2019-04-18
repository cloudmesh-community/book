#!/usr/bin/env python

import oyaml as yaml
from pprint import pprint
from cloudmesh.common.Shell import Shell
import os


def url_link(line):

    print ("LLL", line, type(line))

    try:
        where = line.split("]")[1].strip()
        topic = os.path.basename(where).replace(".md", "")
        url = f" [{topic}](https://github.com/cloudmesh-community/book/blob/master/{where})"
        line = line.replace(where, url)
    except:
        pass

    return line


lines = Shell.execute("../bin/manifest-parser.py tree BOOK_516 ", shell=True).split("\n")

pprint (lines)

result = []
for line in lines:
    if 'chapters/SECTION/' in line:
        line = line.replace("chapters/SECTION/","")
        line = line.replace("├──", "- [ ]")
        line = line.replace("└──", "- [ ]")
    else:
        line = line.replace("├──","- [ ]")
        line = line.replace("└──", "- [ ]")
    line = line.replace("│"," ")
    print (line)
    result.append(url_link(line))

print ('\n'.join(result))

#toc = yaml.load("chapters.yml")

#pprint(toc)

# BOOK_516