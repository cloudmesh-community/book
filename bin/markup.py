#!/usr/bin/env python
import sys

def convert(filename):
    with open(filename, 'r') as f:
        content = f.read()

    print (filename)

    link = '[[:cloud:](https://github.com/cloudmesh/book/edit/master/cloud-clusters/' + filename + ')]\{style=="float:right"\}'
    print(link)
    content = content.replace("{github}", link)

    with open("dest/" + filename, 'w') as f:
        f.write(content)

        
filename = sys.argv[1]
convert(filename)
