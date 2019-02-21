#!/usr/bin/env python
"""Usage: issues.py [--cache] [--linksonly] [--nolinks] [--markdown] [--state=STATE] [--label=LABEL...] [--small] [--header=HEADER] [--pages=PAGES]

Process issues from github and put them in a table, no parameter is tex

Options:
  -h --help
  --markdown        put the table in markdown format.
  --state=STATE     the state [default: open].
  --label=LABEL...  prins only if the issue has all of the labels specified
  --cache           if set the data is taken from a local cached issue.json file.
  --nolinks         do not print the links [default: False].
  --linksonly       only print the links [default: False].
  --small           make the table smaller [default: False].
  --header=HEADER   the header
  --pages=PAGES     the number of maximum pages to be fetched from github [default: 5].
  
"""

from docopt import docopt
import json
from pprint import pprint
import os
import oyaml as yaml



if __name__ == '__main__':
    arguments = docopt(__doc__)
    cache = arguments['--cache']
    markdown = arguments['--markdown']
    LABELS = arguments['--label']
    linksonly = arguments['--linksonly']
    nolinks = arguments['--nolinks']
    small = arguments['--small']
    header = arguments['--header']    
    PAGES = int(arguments['--pages'])    

    issues = []
    download = not cache or not os.path.isfile('issues.json')
    if  download:
        for i in range(1,PAGES):
            os.system("curl -s https://api.github.com/repos/cloudmesh-community/book/issues?page={page} > issues.json".format(page=i))
            with open("issues.json", "r") as file:
                data = file.read()
            part_issues = json.loads(data)
            issues = issues + part_issues
        # pprint (len(issues))        if '--markdown' not in arguments:
        with open("issues.json", "w") as file:
            file.write(json.dumps(issues, indent=4))
        with open("issues.yaml", "w") as file:
            file.write(yaml.dump(issues, indent=2, default_flow_style=False))
    else:
        with open("issues.json", "r") as file:
            data = file.read()
        issues = json.loads(data)


    def assignee(issue):
        name = None
        try:
            name = issue['assignee']['login']
        except:
            pass
        return name

    count = 0

    def labels(issue):
        labels = []
        for label in issue['labels']:
            labels.append(label['name'])

        return labels

    def found_state(LABELS, issue):
        _labels = labels(issue)
        return set(LABELS) <= set(_labels)
        
        
    if len(issues) > 0:

        if markdown:
            print("")
            print("\section{Github Issues}")
            print()
            print("\\begin{center}")    
            print("\\begin{longtable}{llll}")
            print ("Count & Number & Title & Assignee & Labels\\\\")
            print ("\hline")
            for issue in issues:
                count = count + 1
                issue['count'] = count
                if issue['state'] == 'open':
                    line = "{count} & \href{{{html_url}}}{{{number}}} & {title} & ".format(**issue) + str(assignee(issue)) + " & " + " ".join(labels(issue)) + "\\\\"
                    print (line)
            print("\\end{longtable}")
            print("\\end{center}")    
            print("")
        elif not markdown:
            print("")
            if header:
                print (header)
            print()
            if not linksonly:
                if small:
                    print()
                    print()                                    
                    print('.<div class="smalltable">')
                    print()                
                print ("| N | # | Title | Assignee | Labels |")
                print ("| ---: | ---: | :-------------------- | :-------- | :-------- |")            
            for issue in issues:
                count = count + 1
                issue['count'] = count
                if issue['state'] == 'open':
                    line = "| {count} | {number} | [{title}][i{number}] | ".format(**issue) + str(assignee(issue)) + " | " + " ".join(labels(issue)) + " |"
                    if found_state(LABELS, issue) and not linksonly:
                        print(line)
            print("")
            if small:
                print()                                
                print('.</div>')
                print()                
            

            if not nolinks or linksonly:
                for issue in issues:
                    count = count + 1
                    issue['count'] = count
                    if issue['state'] == 'open':
                        line = "[i{number}]: {html_url}".format(**issue)
                        print (line)
                print("")

