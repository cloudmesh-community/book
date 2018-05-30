#!/usr/bin/env python

import os
import re
from glob import glob
import fnmatch

metahead = \
'''
|          | {head} |
| -------- | {dash} |
| title    | {title} |
| status   | {status} |
| section  | {section} |
| keywords | {keywords} |
'''

def addheader():
    # adding table header
    # changing section header lien from the underlying '----' to prefixing '##'
    #
    # for all *.md files in the current directory
    mdfiles = glob("*.md")
    findtitlept = re.compile("([^\n]+?)\n-+\n(.*)", re.M | re.I | re.S)
    for amdfile in mdfiles:
        contentin = None
        with open(amdfile) as fin:
            contentin = fin.read()
        matchret = re.match(findtitlept, contentin)
        if matchret:
            title = matchret.group(1)
            content = matchret.group(2)
            nlen = len(title)
            status = 95
            sectitle = 'TBD'
            keywords = 'TBD'
            output = "## %s\n\n%s\n\n%s" % (title,
                                            metahead.format(head=' ' * nlen,
                                                            dash='-' * nlen,
                                                            title=('{0: <%s}' % nlen).format(title),
                                                            status=('{0: <%s}' % nlen).format(status),
                                                            section=('{0: <%s}' % nlen).format(sectitle),
                                                            keywords=('{0: <%s}' % nlen).format(keywords)
                                                            ),
                                            content)
            with open(amdfile, 'w') as fout:
                fout.write(output)

def addurl():
    #
    # adding url link after the header table
    #
    # as we have changed the section header style, we have to redo the matching again
    mdfiles = glob("*.md")
    tableheaderpt = re.compile("(.+?)\| keywords \|(.*?)\|\n(.*)", re.M|re.I|re.S)
    for amdfile in mdfiles:
        print amdfile
        contentin = None
        with open(amdfile) as fin:
            contentin = fin.read()
        matchret = re.match(tableheaderpt, contentin)
        if matchret:
            beforeheader = matchret.group(1)
            headerkwds = matchret.group(2)
            content = matchret.group(3)
            link = "Link to source in github [:cloud:](https://github.com/cloudmesh/technologies/blob/master/chapters/incomming/%s)" % amdfile
            output = "%s| keywords |%s|\n\n%s\n%s" % (beforeheader,
                                                      headerkwds,
                                                      link,
                                                      content)
            print output

            with open(amdfile, 'w') as fout:
                fout.write(output)

def removeurl():
    mdfiles = glob("*.md")
    linkpt = re.compile("(.+?)Link to source in github(.+?)\n(.*)", re.M|re.I|re.S)
    for amdfile in mdfiles:
        print amdfile
        contentin = None
        with open(amdfile) as fin:
            contentin = fin.read()
        matchret = re.match(linkpt, contentin)
        if matchret:
            beforelink = matchret.group(1)
            linkline = matchret.group(2)
            content = matchret.group(3)
            output = "%s%s" % (beforelink, content)
            print output

            with open(amdfile, 'w') as fout:
                fout.write(output)


def recursive_glob(rootdir='.', pattern='*.md'):
    """Search recursively for files matching a specified pattern.

    Adapted from http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
    """
    matches = []
    for root, dirnames, filenames in os.walk(rootdir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))

    return matches

'''
fixing # of slides and time duration of video

Change from this:
[:clapper: Health 15:02 Medical Big Data in the Clouds]
to this:
[:clapper: Medical Big Data in the Clouds (15:02)]

And change from this:
[:scroll: Overview of Data Science 35 Clouds]
to this:
[:scroll: Clouds (35)]
'''
def fixTimeTagLoc():
    mdfiles = recursive_glob(rootdir="../chapters/bigdata/", pattern="*.md")
    clapperpt = re.compile("\[:clapper:.*?(\d+:\d+)(.+?)\]", re.M|re.I|re.S)
    scrollpt = re.compile("\[:scroll:.*?(\d+)(.+?)\]", re.M|re.I|re.S)

    def formatting(matchObj, tag="clapper"):
        if matchObj:
            timenum = matchObj.group(1)
            cap = matchObj.group(2)
            print ("|%s|%s|" % (timenum, cap))
            return "[:%s: %s (%s)]" % (tag, re.sub("\s+", " ", cap.replace("\n"," ")).strip(), timenum)

    def formattingvideo(matchObj):
        return (formatting(matchObj))

    def formattingslides(matchObj):
        return (formatting(matchObj, tag="scroll"))

    for amdfile in mdfiles:
        contentin = None
        with open(amdfile) as fin:
            contentin = fin.read()
        #print contentin

        newcontent = re.sub(clapperpt, formattingvideo, contentin)
        newcontent = re.sub(scrollpt, formattingslides, newcontent)

        #print (newcontent)
        with open(amdfile, 'w') as fout:
            fout.write(newcontent)

if __name__ == "__main__":
    fixTimeTagLoc()
