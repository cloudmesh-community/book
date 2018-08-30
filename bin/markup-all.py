#!/usr/bin/env python
from __future__ import print_function
import os
import glob
from pprint import pprint

import fnmatch

gitbase = "https://github.com/cloudmesh-community/book/edit/master/chapter/"

def mkdir_p(newdir):
    """works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well
    """
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("a file with the same name as the desired " \
                      "dir, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            mkdir_p(head)
        #print "_mkdir %s" % repr(newdir)
        if tail:
            os.mkdir(newdir)
        
def recursive_glob(rootdir='.', pattern='*.md'):
	"""Search recursively for files matching a specified pattern.
	
	Adapted from http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
	"""

	matches = []
	for root, dirnames, filenames in os.walk(rootdir):
	  for filename in fnmatch.filter(filenames, pattern):
		  matches.append(os.path.join(root, filename))

	return matches

# {gitissue}{12}


    
def convert(filename):
    
    with open(filename, 'r') as f:
        content = f.read()


    link = '[[:cloud:](' + gitbase + filename + ')]{style="float:right"}'
    gitcoderoot = 'https://github.com/cloudmesh/book/tree/master/examples'
    lines = content.split("\n")
    if "{.unnumbered}" in lines[0]:
        pass
    else:
      if lines[0].startswith("# "):
          lines[0] = "\n# [" + lines[0][2:] + "]{.part}"        
      if "{github}" not in lines[0]:
          lines[0] = lines[0] + " {github}"
    content = "\n".join(lines)
    content = content.replace("{github}", link)
    content = content.replace("{gitcode}", gitcoderoot)
    content = content + "\n"
    filename = filename.replace("../", "")
    with open("dest/" + filename, 'w') as f:
        f.write(content)
        
files = recursive_glob(rootdir="../chapters")

        
for file in files:
    if '#' not in file and '~' not in file:
        d = 'dest/' + os.path.dirname(file).replace("../", "")
        print(file, '->', d)
        mkdir_p(d)
        convert(file)
        
