#!/usr/bin/env python

import json
from pprint import pprint
import os

# os.system("curl -s https://api.github.com/repos/cloudmesh/book/issues > issues.json")

file = open("issues.json", "r")
data = file.read()
issues = json.loads(data)


def assignee(issue):
    name = None
    try:
        name = issue['assignee']['login']
    except:
        pass
    return name

if len(issues) > 0:
    # print("\section{Github Issues}")
    print("\\begin{center}")    
    print("\\begin{tabular}{llll}")
    print ("Status & No & title & Assignee\\\\")
    print ("\hline")
    for issue in issues:
        if issue['state'] == 'open':
            line = "{state} & \href{{{html_url}}}{{{number}}} & {title} & ".format(**issue) + str(assignee(issue)) + "\\\\"
            print (line)
    print("\\end{tabular}")
    print("\\end{center}")    
