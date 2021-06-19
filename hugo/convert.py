import click
from textwrap import dedent
import os
from cloudmesh.common.util import path_expand
from pathlib import Path

# ${CONVERT} --file=${BASE}/google-colab/python-google-colab.md --d=${DEST}/python/first-steps
#https://github.com/cloudmesh-community/book/raw/main/chapters/prg/python/google-colab/images/colab-3.png
# https://github.com/cloudmesh-community/book/raw/main/chapters/prg/python/google-colab/images/colab-3.png

@click.command()
@click.option('--file', help='The file name to convert')
@click.option('--tags', help='The tags')
@click.option('--author', help='The author')
@click.option('--d', help='The directory')
@click.option('--w', help='The weight')
@click.option('--index', help='The weight')
@click.option('--url', help='file url')
@click.option('--crossref', help='apply crossref')
def convert(file, tags, author, d, w, index, url, crossref):
    """
    Convert the file to use yaml front matter
    """


    if crossref is not None:
        print ("FFFF", file)
        name = os.path.basename(file)
        print ("NNNN", name)
        tmp = f"/tmp/{name}"

        os.system(f"cp {file} {tmp}")
        command = f"pandoc --wrap=preserve -M crossrefYaml=prefix.yaml --filter pandoc-crossref --citeproc -t markdown -o {tmp}-tmp {tmp} "
        print("PANDOC", command)
        os.system(command)
        os.system(f"mv {tmp}-tmp {tmp}")
        file = tmp

        # add captions
        result = []
        with open(tmp, "r") as f:
            lines = f.read()
        lines = lines.split("\n")
        for line in lines:
            if "![" in line:
                caption = line.strip().split("]")[0][2:]
                line = line.split("{#")[0]  # remove label
                line = f"{line}\n\n{caption}"  # add caption from alttext
            result.append(line)
        with open(tmp, "w") as f:
            f.write("\n".join(result))

    print (79* "=")

    print("Tags:  ", tags)
    print("Author:", author)
    print("Dir:   ", Path(d).resolve())
    if file:
        print("File:  ", Path(file).resolve())
    if url:
        print("URL    ", url)
        images = os.path.dirname(url)
        print("Base   ", images)

    print()


    if index:
        result  = dedent(f"""
        ---
        title: "{index}"
        linkTitle: "{index}"
        weight: {w}
        authors: "{author}"
        github_url: "{url}"
        ---
        
        {author}
        
        """).strip().splitlines()
        file = "_index.md"

    else:


        result = []

        with (open(file, "r")) as f:
            content = f.readlines()


        matter = []
        ref = None
        title = content[0].split("# ")[1]
        if "{" in title:
            title, ref = title.split("{")
            ref = 'ref: "{' + ref.strip() + '"'
        title = title.strip()

        matter.append(f'title: "{title}"')
        if ref:
            matter.append(ref)


        if tags is not None:
            tags = str (tags.split(",")).replace("'", '"')

            matter.append(f"tags: {tags}")

        if author is not None:
            matter.append(f'authors: "{author}"')
        if w is not None:
            matter.append(f"weight: {w}")
        if url is not None:
            matter.append(f'github_url: "{url}"')

        result.append("---")
        result.append("\n".join(matter))
        result.append("---\n")
        result.append(f"{author}\n\n")

        for line in content[1:]:
            line = line.strip("\n")

            if "![" in line:
                line = line.replace("{width=20%}", "")
                line = line.replace("(images/", f"({images}/images/")
                print ("image", line)

                # Remove {
                if "{#" in line:
                    line, label = line.split("{#")
                # Make alttext caption
            elif line.startswith("#") and "{" in line:
                line = line.split("{")[0]


            result.append(line)

    if d is None:
        print("\n".join(result))
    else:
        name = os.path.basename(file)
        filename = f"{d}/{name}"

        directory = os.path.dirname(filename)

        print ("CONVERT:", filename, "to", directory)

        os.makedirs(directory, exist_ok=True)

        with open(filename, "w") as output:
            output.write("\n".join(result))


if __name__ == '__main__':
    convert()
