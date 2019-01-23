import glob

with open("../chapters.yaml") as file: 
   chapters = file.read()


for filename in glob.iglob('../chapters/**/*.md', recursive=True):
    name = filename.replace("../","")
    if name not in chapters:
        print("- [ ]", name, "[link](https://github.com/cloudmesh-community/book/blob/master/" + name +")")

