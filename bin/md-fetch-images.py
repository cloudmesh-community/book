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

# Inspired from
# https://stackoverflow.com/questions/29259912/how-can-i-get-a-list-of-image-urls-from-a-markdown-file-in-python




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

    print("# Original images are from\n")
    for image in md.images:
        print("# ", image)


    for image in md.images:
        print("wget", image)
        destination = "images/" + os.path.basename(image)
        destination = destination.replace("?raw=true", "")
        img = os.path.basename(image)
        print ("mv", img, destination)

