# Markdown Lint

Markdown does not have a fixed syntax. To define uniform markdown
between multiple contributors it is useful to have some markdown
syntax rules we use.

One such tool is called markdown lint and can be installed on your
system if you have ruby on it with

```bash
$ gem install mdl
```

To run it you can simply use

```bash
$ mdl yourfile.md
```
You will see that it writes down the kind of error it detects. When it
comes to line length some line length can be ignored if they relate to
images and urls or tables. However linelength in paragrapghs you must
use the customary 80 chracter line length.

# Removal of trailing spaces

```bash
$ find . -iname '*.md' -type f -exec sed -i '' 's/[[:space:]]\{1,\}$//' {} \+
```

# Removal of multiple empty lines

```bash
$ cat -s filenamet.md > tmp.md; mv tmp.md filename.md
```
