#!/usr/bin/env python
import sys
import glob
import os


directories = [".", "chapters"]


for root, dirs, files in os.walk("../chapters", topdown=False):
    for name in dirs:
        path = os.path.join(root, name)
        if 'images' in path:
            path = os.path.dirname(path)
            # hack to remove ../ should in future use pathlib no time to implement
            path = path.replace("../","")
            path = path.split("/images")[0]
            directories.append(path)

            
print ("\n".join(set(directories)))

