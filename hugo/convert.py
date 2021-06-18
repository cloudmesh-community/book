import click
from textwrap import dedent
import os



@click.command()
@click.option('--file', help='The file name to convert')
@click.option('--tags', help='The tags')
@click.option('--author', help='The author')
@click.option('--d', help='The directory')
@click.option('--w', help='The weight')
@click.option('--index', help='The weight')
def convert(file, tags, author, d, w, index):
    """
    Convert the file to use yaml front matter
    """

    if index:
        result  = dedent(f"""
        ---
        title: "{index}"
        linkTitle: "{index}"
        ---
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
            matter.append(f'author: "{author}"')
        if w is not None:
            matter.append(f"weight: {w}")

        result.append("---")
        result.append("\n".join(matter))
        result.append("---")


        for line in content[1:]:
            line = line.strip("\n")
            result.append(line)

    if d is None:
        print("\n".join(result))
    else:
        name = os.path.basename(file)
        filename = f"{d}/{name}"
        print ("NAM:", filename)
        
        with open(filename, "w") as output:
            output.write("\n".join(result))
        
            
if __name__ == '__main__':
    convert()
