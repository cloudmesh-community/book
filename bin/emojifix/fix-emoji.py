#!/usr/bin/env python
import sys
from emoji import UNICODE_EMOJI, EMOJI_UNICODE
import ebooklib
from ebooklib import epub

emojimapfile = "emoji2png.txt"

# parameter 'filename' is a text file containing lines of mapping from emoji
# code to img name, e.g.,
# :scroll:|scroll.png
# the png file has to be pre-downloaded and present before running the script
#
# return a map from emoji code to the replacement img URL
def loadmapping(filename):
    emojimap = {}
    with open(filename, 'r') as f:
        for line in f:
            emoji, img = line.strip().split("|")
            imgurl = '<img src="{imgname}" width="16" height="16" />'.format(imgname=img)
            #imgurl = '![](images/{imgname})'.format(imgname=img)
            emojimap[emoji] = imgurl
    return emojimap

emoji2pngurl = loadmapping(emojimapfile)

def convert(filenamein, filenameout):
    with open(filenamein, 'r', encoding='utf-8') as f:
        content = f.read()

    content = emojifix(content)
    with open(filenameout, 'w') as f:
        f.write(content)
    #content.find(u'\U0001f3ac')
    #print (u'\U0001f3ac')

def list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print ("*"*80)
    print ("All standard emojis appeared in the file:")
    print ("-"*50)
    emojilist(content)
    print ("*" * 80)

def emojilist(s):
    for emoji in UNICODE_EMOJI:
        loc = s.find(emoji)
        if loc > 0:
            name = UNICODE_EMOJI[emoji]
            print ("|%s|%s|" % (emoji, name))

def emojifix(s):
    for emoji in UNICODE_EMOJI:
        # emoji in file
        if emoji in s:
            name = UNICODE_EMOJI[emoji]
            #print ("YYY-Found emoji to be replaced: |%s|%s|" % (emoji, name))
            # emoji img downloaded and put into config map
            if name in emoji2pngurl:
                s = s.replace(emoji, emoji2pngurl[name])
            # img file and config missing for emoji
            else:
                print ("XXX-Need png image for emoji - |%s|" % name)
        '''
        loc = s.find(emoji)
        if loc > 0:
            #print (emoji, loc)
            #print ("|%s|" % s[:a+1])
            name = UNICODE_EMOJI[emoji]
            #print ("|%s|" % name)
            if name in emoji2pngurl:
                s = s[:loc] + emoji2pngurl[name] + s[loc + 1:]
            #code = EMOJI_UNICODE[name]
            #print (name, code)
        '''
    return s

def main():
    filenamein = sys.argv[1]
    filenameout = sys.argv[2]
    list(filenamein)
    convert(filenamein, filenameout)

def readebook(name):
    book = epub.read_epub(name)
    return (book)

if __name__ == "__main__":
    main()

    '''
    name = 'all4pdf.epub'
    book = readebook(name)
    print (book)
    #toc = book.toc
    #print (toc)
    #for item in toc:
    #    print (item)
    nav = book.get_items_of_type(ebooklib.ITEM_NAVIGATION)
    #print (nav)
    nav = book.get_item_with_href('nav.xhtml')
    navcontent = str(nav.get_content())
    navcontentnew = navcontent.replace("../media", "./media")
    #print (navcontentnew)

    nav.content=navcontentnew
    #book.get_item_with_href()
    newitems = []
    for item in book.get_items():
        if item == nav:
            print('==================================')
            print('NAME : ', item.get_name())
            print('----------------------------------')
            print(navcontentnew)
            print('==================================')
            item.content=navcontentnew
        newitems.append(item)

    newbook = epub.EpubBook()
    for item in newitems:
        newbook.add_item(item)
    epub.write_epub('test.epub', newbook)
    '''
