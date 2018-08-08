#! /usr/bin/env python
"""Markdown to tex converter

Usage:
  md-to-tex.py FILENAME
  md-to-tex.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
import re
import sys
import subprocess

def substitute_section(name, origText):

    finished = False    
    newText = origText
    while not finished:
        sectionBlockPtstr = '(.*?)(\\\hypertarget(.*?)\\\label(.*?)}})(.*)'

        pt1 = re.compile(sectionBlockPtstr, re.M | re.I | re.S)
        try:
            sectionBlockMatch = re.match(pt1, origText).group(2)

            sectionOnlyPtstr = '\\\hypertarget(.*?)\\\{section}(.*?)\\\label(.*?)}}'.format(section=name)
            pt1 = re.compile(sectionOnlyPtstr, re.M | re.I | re.S)
            sectionOnlyMatch = '\{section}%s'.format(section=name) % re.match(pt1, sectionBlockMatch).group(2).replace('\n', ' ')

            newText = origText.replace(sectionBlockMatch, sectionOnlyMatch)
            origText = newText
        except:
            finished = True
    return newText



if __name__ == '__main__':
    arguments = docopt(__doc__)
    output = ''
    filename = arguments['FILENAME']

    data = subprocess.check_output(["pandoc","-t", "latex", filename]).decode("utf-8")  

    original = data.replace("{verbatim}", "{lstlisting}").replace("\\tightlist\n","")
    original = original.replace("\\includegraphics", "\includegraphics[width=0.8\columnwidth]")

    
    #Hack to get all the sections out

    while 'hypertarget' in original:
        tmp_section = substitute_section("section", original)
        tmp_subsection = substitute_section("subsection", tmp_section)
        tmp_subsubsection = substitute_section("subsubsection", tmp_subsection)
        tmp_paragraph = substitute_section("paragraph", tmp_subsubsection)

        output = tmp_paragraph
        original = output

    print (79* "%")
    print ("% DO NOT MODIFY THIS FILE")
    print (79* "%")
    print ()
    print (output)
