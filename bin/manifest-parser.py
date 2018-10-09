#!/usr/bin/env python
"""Vagrant Manager.
Usage:
  manifest-parser.py info
  manifest-parser.py info no BOOK
  manifest-parser.py list
  manifest-parser.py generate BOOK
  manifest-parser.py dep BOOK
  manifest-parser.py tree BOOK

Options:
  -h --help     Show this screen.

Description:
   info
        gives general information of the lists

   info no BOOK
        prints all entries that are not in the book but in the chapter dir

   dep BOOK
        generates the entries for the makefile

   tree BOOK
        list the booktree for debugging purposes



"""

import oyaml as yaml
from pprint import pprint
from treelib import Node, Tree
from time import time
from docopt import docopt
import sys
from pathlib import Path
import glob
import os

def load_manifest(file):
    mfest = None
    with open(file, 'r') as fs:
        try:
            mfest = yaml.load(fs)
        except yaml.YAMLError as exc:
            print(exc)
    return mfest


# noinspection PyPep8Naming
def expand_def(vardict, varsdict):
    # print ("-" * 80)
    # pprint (vardict)
    # print ("+" * 80)
    var = dict(vardict)
    for title, chaps in var.items():
        allleafs = True
        for idx, chap in enumerate(chaps):
            if type(chap) is dict:
                # pprint (chap)
                chaptitle = list(chap.keys())[0]
                # pprint (chaptitle)
                # chaptitle = chap
                newdic = chap
                if chaptitle.startswith("$ref:"):
                    chaptitle = chaptitle.split("$ref:")[1]
                    predefinedList = varsdict[chaptitle]
                    newList = list(chap.values())[0]
                    # print (predefinedList)
                    # print (newList)
                    newdic = {chaptitle: predefinedList + newList}
                # pprint (newdic)
                allleafs = False
                vardict[title][idx] = expand_def(newdic, varsdict)
            else:
                if not type(chap) is list:
                    if chap.startswith("$ref:"):
                        allleafs = False
                        refchap = chap.split("$ref:")[1]
                        '''
                        print (refchap)
                        print (varsdict)
                        print ("-" * 80)
                        print (varsdict[refchap])
                        print ("+" * 80)
                        '''
                        newdic = {refchap: varsdict[refchap]}
                        vardict[title][idx] = expand_def(newdic, varsdict)
    return vardict


def minimum_one(n):
    if n <= 0:
        return 1
    else:
        return n

def timestamp_node(node):
    # prefix timestamp to tag to preserve the order
    # alternatively use a data field in Node for sorting
    # return "{timestamp}|{node}".format(timestamp=time(),
    #                                   node=node)
    return node


# noinspection PyPep8Naming
def create_tree(adict):
    tree = Tree()
    if type(adict) is dict:
        # print ("procdessing dict to tree...")
        root = list(adict.keys())[0]
        # print (root)
        tree.create_node(timestamp_node(root), root, data=time())
        for node in list(adict.values()):
            # print ("processing a node of the dict values")
            if type(node) is dict:
                newTree = create_tree(node)
                tree.paste(root, newTree)
            elif type(node) is list:
                for item in node:
                    newTree = create_tree(item)
                    tree.paste(root, newTree)
            else:
                tree.create_node(timestamp_node(node), node, parent=root, data=time())
    else:
        tree.create_node(timestamp_node(adict), adict, data=time())
    return tree


class Manifest(object):

    def __init__(self):
        self.mfest = load_manifest("../chapters.yaml")
        self.books = {}
        self.chaps = {}

        for adef in self.mfest:
            for defheader, defs in adef.items():
                if not defheader.startswith("BOOK_"):
                    self.chaps[defheader] = defs
                else:
                    self.books[defheader] = defs
        #
        # nested dict approach, not working very well
        '''
        for title, bookchaps in self.books.items():
            print ("BOOK: {title}".format(title=title))
            print ("+" * 80)
            book = {title: bookchaps}
            pprint (book)
            print ("-" * 80)
            pprint (expand_def(book, self.chaps))
            print ("*" * 80)
        #pprint(books)
        '''

        #
        # tree approach, better
        self.treechap = {}
        for title, chap in self.chaps.items():
            self.treechap[title] = create_tree({title: chap})

        self.treebook = {}
        for title, book in self.books.items():
            self.treebook[title] = create_tree({title: book})

        for title, tree in self.treebook.items():
            # tree.show()
            for node in tree.expand_tree(mode=Tree.DEPTH):
                # print ("+", node)
                realtag = node
                if type(realtag) is Node:
                    realtag = node.tag
                if "|" in realtag:
                    realtag = realtag.split("|")[1]
                if realtag.startswith("$ref:"):
                    chapkey = realtag.split("$ref:")[1]
                    newtree = Tree(tree=self.treechap[chapkey], deep=True)
                    # move up its children to replace totally the root
                    subtree = newtree.subtree(newtree.children(newtree.root)[0].tag)
                    newtree = subtree
                    for anode in tree.children(node):
                        origtag = anode.tag
                        if "|" in origtag:
                            origtag = anode.tag.split("|")[1]
                        # print (origtag)
                        newtree.create_node(timestamp_node(origtag), origtag, parent=newtree.root, data=time())
                    # find parent node of the node to be replaced
                    parent = tree.parent(node)
                    # use the old timestamp data to preserve insertion order
                    newtree.get_node(newtree.root).data = tree.get_node(node).data
                    # remove old node
                    tree.remove_subtree(node)
                    # replace with new expanded node
                    tree.paste(parent.identifier, newtree)

    def info(self):
        variables = self.chaps.keys()
        for title, tree in self.treebook.items():
            print("=" * 80)
            tree.show(key=lambda x: x.data)
            print("-" * 80)
            for node in tree.expand_tree(mode=Tree.DEPTH, key=lambda x: x.data):
                #level = minimum_one(tree.level(node) - 1)
                level = tree.level(node)
                if node not in variables:
                    print(level * "  ", node, level)
                else:
                    print("#", node, level)

    def info_no(self, book):

        #
        # find tree entries
        #
        entries = []
        variables = self.chaps.keys()
        if book not in variables:
            print ("ERROR: book does not exist")
        print (variables)
        for title, tree in self.treebook.items():
            if title == book:
                for node in tree.expand_tree(mode=Tree.DEPTH, key=lambda x: x.data):
                    level = tree.level(node)
                    if node not in variables:
                        entries.append(node)


        dir_entries = list(glob.iglob(os.path.join("../chapters", '**', '*.md')))
        for entry in range(0,len(dir_entries)):
            dir_entries[entry] = dir_entries[entry].replace("../", "")
        print ("#", 79 * "#")
        print ("#", "Md files not includes in", book)
        print ("#", 79 * "#")        
        print ("- MISSING_{}:".format(book))
        for entry in dir_entries:
            if entry not in entries:
                print("    -", entry)


    def list(self):
        for title, tree in self.treebook.items():
            print(title)

    def generate(self, book):
        variables = self.chaps.keys()
        for title, tree in self.treebook.items():
            if title == book:
                # print ("=" * 80)
                # tree.show(key=lambda x: x.data)
                # print ("-" * 80)
                for node in tree.expand_tree(mode=Tree.DEPTH, key=lambda x: x.data):
                    if node not in variables:
                        #level = minimum_one(tree.level(node) - 1)
                        level = tree.level(node)
                        print(node, level)

    def generate_dependencies(self, book):

        def print_rule(name, level):

            print("dest/{name}: ../{name}".format(name=name, level=level))
            # print("\t$(COPY) ../{name} dest/{name}".format(name=name,level=level))
            print("\t../bin/markup-single.py ../{name} {level}".format(name=name, level=level))
            print("\t../bin/header.py dest/{name} {level}".format(name=name, level=level))

        chapterlist = []
        variables = self.chaps.keys()
        for title, tree in self.treebook.items():
            if title == book:
                for node in tree.expand_tree(mode=Tree.DEPTH, key=lambda x: x.data):
                    if node not in variables and node != book:
                        location = "dest/{name}".format(name=node)
                        chapterlist.append(location)
        print("INDEX=\\\n  " + "\\\n  ".join(chapterlist).replace("dest/",""))
        print()
        print("chapterlist: ", " ".join(chapterlist))
        print("\t@echo \"updated modified chapters\"")
        print()

        print()
        variables = self.chaps.keys()
        for title, tree in self.treebook.items():
            if title == book:
                for node in tree.expand_tree(mode=Tree.DEPTH, key=lambda x: x.data):
                    if node not in variables and node != book:
                        level = tree.level(node)
                        print_rule(node, level)
                        print()

    def generate_tree(self, book):
        for title, tree in self.treebook.items():
            if title == book:
                tree.show(key=lambda x: x.data)


def process_arguments(arguments):
    if arguments["info"] and arguments["no"]:
        book = arguments["BOOK"]
        m = Manifest()
        m.info_no(book)
    elif arguments["info"]:
        m = Manifest()
        m.info()
    elif arguments["list"]:
        m = Manifest()
        m.list()
    elif arguments["generate"]:
        book = arguments["BOOK"]
        m = Manifest()
        m.generate(book)
    elif arguments["tree"]:
        book = arguments["BOOK"]
        m = Manifest()
        m.generate_tree(book)
    elif arguments["dep"]:
        book = arguments["BOOK"]
        m = Manifest()
        m.generate_dependencies(book)


def main():
    """
    TODO: doc
    :return:
    """
    arguments = docopt(__doc__, version='Cloudmesh Book Manager 0.1')
    process_arguments(arguments)


if __name__ == '__main__':
    main()
