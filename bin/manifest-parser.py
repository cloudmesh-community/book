#!/usr/bin/env python

import oyaml as yaml
from pprint import pprint
from treelib import Node, Tree
from time import time

def load_manifest(file):
    mfest = None
    with open(file, 'r') as fs:
        try:
            mfest = yaml.load(fs)
        except yaml.YAMLError as exc:
            print(exc)
    return mfest

def expand_def(vardict, varsdict):
    #print ("-" * 80)
    #pprint (vardict)
    #print ("+" * 80)
    var = dict(vardict)
    for title, chaps in var.items():
        allleafs = True
        for idx, chap in enumerate(chaps):
            if type(chap) is dict:
                #pprint (chap)
                chaptitle = list(chap.keys())[0]
                #pprint (chaptitle)
                #chaptitle = chap
                newdic = chap
                if chaptitle.startswith("$ref:"):
                    chaptitle = chaptitle.split("$ref:")[1]
                    predefinedList = varsdict[chaptitle]
                    newList = list(chap.values())[0]
                    #print (predefinedList)
                    #print (newList)
                    newdic = {chaptitle: predefinedList + newList}
                #pprint (newdic)
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

def timestamp_node(node):
    # prefix timestamp to tag to preserve the order
    # alternatively use a data field in Node for sorting
    #return "{timestamp}|{node}".format(timestamp=time(),
    #                                   node=node)
    return node

def create_tree(adict):
    tree = Tree()
    if type(adict) is dict:
        #print ("procdessing dict to tree...")
        root = list(adict.keys())[0]
        #print (root)
        tree.create_node(timestamp_node(root), root, data=time())
        for node in list(adict.values()):
            #print ("processing a node of the dict values")
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

def main():
    mfest = load_manifest("../chapters.yaml")
    books = {}
    chaps = {}
    for adef in mfest:
        for defheader, defs in adef.items():
            if not defheader.startswith("BOOK_"):
                chaps[defheader] = defs
            else:
                books[defheader] = defs
    #
    # nested dict approach, not working very well
    '''
    for title, bookchaps in books.items():
        print ("BOOK: {title}".format(title=title))
        print ("+" * 80)
        book = {title: bookchaps}
        pprint (book)
        print ("-" * 80)
        pprint (expand_def(book, chaps))
        print ("*" * 80)
    #pprint(books)
    '''

    #
    # tree approach, better
    treechap = {}
    for title, chap in chaps.items():
        treechap[title] = create_tree({title: chap})

    treebook = {}
    for title, book in books.items():
        treebook[title] = create_tree({title: book})

    for title, tree in treebook.items():
        #tree.show()
        for node in tree.expand_tree(mode=Tree.DEPTH):
            #print ("+", node)
            realtag = node
            if type(realtag) is Node:
                realtag = node.tag
            if "|" in realtag:
                realtag = realtag.split("|")[1]
            if realtag.startswith("$ref:"):
                chapkey = realtag.split("$ref:")[1]
                newtree = Tree(tree=treechap[chapkey],deep=True)
                for anode in tree.children(node):
                    origtag = anode.tag
                    if "|" in origtag:
                        origtag = anode.tag.split("|")[1]
                    #print (origtag)
                    newtree.create_node(timestamp_node(origtag), origtag, parent=newtree.root, data=time())
                # find parent node of the node to be replaced
                parent = tree.parent(node)
                # use the old timestamp data to preserve insertion order
                newtree.get_node(newtree.root).data=tree.get_node(node).data
                # remove old node
                tree.remove_subtree(node)
                # replace with new expanded node
                tree.paste(parent.identifier, newtree)

    for title, tree in treebook.items():
        print ("=" * 80)
        tree.show(key=lambda x: x.data)
        print ("-" * 80)
        for node in tree.expand_tree(mode=Tree.DEPTH, key=lambda x: x.data):
            print (node, tree.level(node))

if __name__ == '__main__':
    main()