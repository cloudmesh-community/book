#!/usr/bin/env python

import json
from pprint import pprint
import os

issues = []
for i in range(1,4):
    os.system("curl -s https://api.github.com/repos/cloudmesh/book/issues?page={page} > issues.json".format(page=i))    
    file = open("issues.json", "r")
    data = file.read()
    part_issues = json.loads(data)
    issues = issues + part_issues

# pprint (len(issues))


def assignee(issue):
    name = None
    try:
        name = issue['assignee']['login']
    except:
        pass
    return name

count = 0

if len(issues) > 0:
    print("\section{Github Issues}")
    print("\\begin{center}")    
    print("\\begin{longtable}{llll}")
    print ("Count &  Number & title & Assignee\\\\")
    print ("\hline")
    for issue in issues:
        count = count + 1
        issue['count'] = count
        if issue['state'] == 'open':
            line = "{count} & \href{{{html_url}}}{{{number}}} & {title} & ".format(**issue) + str(assignee(issue)) + "\\\\"
            print (line)
    print("\\end{longtable}")
    print("\\end{center}")    
