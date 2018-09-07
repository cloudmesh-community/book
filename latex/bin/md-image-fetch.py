#! /usr/bin/env python
"""Markdown image fetcher

Usage:
  md-image-fetch.py FILENAME
  md-image-fetch.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt

import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
import sys
import os
import errno
import urllib.request

# This program uses python markdown to find the images. It is inspired from 
# https://stackoverflow.com/questions/29259912/how-can-i-get-a-list-of-image-urls-from-a-markdown-file-in-python

# Gregor von Laszewski, laszewski@gmail.com

class ImgExtractor(Treeprocessor):
    def run(self, doc):
        "Find all images and append to markdown.images. "
        self.markdown.images = []
        for image in doc.findall('.//img'):
            self.markdown.images.append(image.get('src'))

class ImgExtExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        img_ext = ImgExtractor(md)
        md.treeprocessors.add('imgext', img_ext, '>inline')


if __name__ == '__main__':
    arguments = docopt(__doc__)

    filename = arguments['FILENAME']

    if filename is None:
        print("ERROR: filename missing")
        sys.exit(1)
        
    md = markdown.Markdown(extensions=[ImgExtExtension()])

    with open(filename, "r") as f:
        data = f.read()    

    html = md.convert(data)

    #
    # PRINT IMAGES FOUND IN FILE
    #
    print(79*'#')
    print("# Original images are from")
    print(79*'#')

    for image in md.images:
        print("* ", image)
    print()

    #
    # FETCH THE IMAGES
    #

    try:
        os.mkdir('images')
    except FileExistsError:
        pass
    except Exception as e:
        #print ("Warning:", e)
        pass

    
    for image in md.images:
        print(image)
        destination = "images/" + os.path.basename(image)
        print(destination)
        if image.startswith('http') and not os.path.isfile(destination):
            
            print ('fetch')
            urllib.request.urlretrieve(image, destination)

