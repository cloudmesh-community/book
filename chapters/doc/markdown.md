# Markdown

Markdown is a simple markup language, however there is no uniform
precise standard defined for it and implementations may have features
not supported by other implementations. Nevertheless, when using the
basic features, it provides a simple and easy way to quickly develop
clean structured documents. The emphasize here is on structure, as in
contrast to WYSIWYG editors it is not only important that your
document looks good, but that the structure of the document is
reflected in its layout. Thus you need to use headings and not just
make headings look like headings with a bold font.


## Markdown format

To convert the markdown to other formats with `pandoc`

    # Heading

    ## Sub-heading

    ### Sub Sub Heading heading
     
    Paragraphs are separated
    by a blank line. This is important. There must be one after the heading also

    Text attributes include: *italic*, **bold**, `monospace`.

    Horizontal rule:

    ---

    Bullet list:

      * item 1
      * item 2
      * item 3

    Numbered list:

      1. first
      2. second
      3. third

    A [link](http://example.com).

    ```bash
    $ echo "a bash script"
    ```

    ```python
    print("a python script")
    ```

    Images must all be local and must not have an http reference
    All images must be placed in a directory called images/ as
	shown in @fig:labelwithoutspaces.
    
    ![This is the caption](images/example.png){#fig:labelwithoutspaces}
    
    Any figure used in the text must be referred to with a figure
	cation and label as shown next
    

## Editors

There are several tools that make writing documents in markdown
easy. If you do not just look at the output of these documents but
follow the structure guides properly.

Examples for such editors are:

Macdown

:   MacDown is an open source Markdown editor for macOS that is
    available at <https://macdown.uranusjr.com/>

Emacs

: The most universal editor that has ever been written. It allows you
  to edit markdown text.  Emacs comes in different flavors dependent
  on the OS. For macOS we have made good experiences with Aquamacs,
  CarbonEmacs

PyCharm

: As we do a lot of python programming, we recommend that your learn
Emacs and/or PyCharm. Both come with Markdown editing modes.

Dilinger

:   A HTML5 based cloud enabled editor <https://dillinger.io/>. It
    allows to download the created Markdown.

Markdown plus

: :warning: We are not using the many extensions that are provided by
  markdown plus.  We recommend that you use emacs or PyCharm. However,
  those that want to do advanced markdown outside the class may
  benefit from markdown plus.  Markdown plus ahs lots of extensions.
  It is located at <https://mdp.tylingsoft.com/>. The source code is
  on github <https://github.com/tylingsoft/markdown-plus>. A local
  install can be achieved as follows:

  ```bash
  $ git clone https://github.com/tylingsoft/markdown-plus.git
  $ cd markdown-plus
  $ brew install yarn
  $ yarn install
  $ yarn watch
  $ open dist/index.html
  ```
Remarkable
 
: see <https://remarkableapp.github.io/>

Visualstudio

: see <https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one>

## Converters

In addition to editors you can often convert text to markdown. However
you need to be careful that the documents you created your text from
may not produce the clean markdown you need and you may need to
cleanup the text by for example replacing some characters, including
proper spaces and other things.

The most powerful converter is pandoc and we recommend that you use
it. Pandoc is also able to convert markdown in other formats such as
ePub, PDF, HTML.

A word of warning: Although pandoc can convert from MSWord, Word has
some limitations in its character sets that require you to clean the
markdown after conversion.  Experience shows that it cost less time
and is far easier to write the document directly in markdown with
emacs or pyCharm.


### Conversion with pandoc

Pandoc is a tool to convert file formats between each other. According
tho the Web page Pandoc can convert "Markdown, reStructuredText,
textile, HTML, DocBook, LaTeX, MediaWiki markup, TWiki markup,
TikiWiki markup, Creole 1.0, Vimwiki markup, OPML, Emacs Org-Mode,
Emacs Muse, txt2tags, Microsoft Word docx, LibreOffice ODT, EPUB, or
Haddock markup".

The Web page is located at.

* <https://pandoc.org/>

To convert files simply use the following command line option `-o` to
specify the output format

    pandoc filename.md -o filename.tex

In our example we converted the md file to latex.

As this document is created with pandoc we encourage you to review our
Makefile to see how we use some more advanced features


### Advanced Pandoc

pandoc can integrate extensions and filters. We have not made yet use
of them but like to explore them over time.

Packages of interest include:

* Include files <http://pandoc.org/filters.html#include-files>
* Integration of R <https://github.com/cdupont/r-pandoc>
* Figure numbers <https://github.com/tomduck/pandoc-fignos>
* Equation numbers <https://github.com/tomduck/pandoc-eqnos>
* Table numbers <https://github.com/tomduck/pandoc-tablenos>
* Cross refs with lots of numbering <https://github.com/lierdakil/pandoc-crossref>
* section numbering <https://github.com/chdemko/pandoc-numbering>
* CSV table <https://github.com/baig/pandoc-csv2table>
* inline CSV table <https://github.com/mb21/pandoc-placetable>

#### Mermaid

Mermaid is a graph generation tool that lets you create graphs and
diagrams with the help of a description language. It includes graphviz
and UML like diagrams, as well as gantt charts

A live editor is available at 

  * [Mermaid live editor](https://mermaidjs.github.io/mermaid-live-editor/)

A markdown plugin for pandoc is available

* Mermaid 
* <https://github.com/raghur/mermaid-filter>

Installation is done with

```bash
$ npm install --global mermaid-filter
```

A sequence diagram example is shown next

```
~~~mermaid
sequenceDiagram
Alice->>John: Hello John
    John-->>Alice: Hallo Allice
~~~
```

~~~mermaid
sequenceDiagram
    Alice->>John: Hello John
    John-->>Alice: Hallo Allice
~~~

A flowchart looks like

```
~~~mermaid
graph LR
    Start --> End
~~~
```

~~~mermaid
graph LR
    Start --> End
~~~

## Presentations in Markdown

Please find some links on hwo to use markdown to create slides

* <https://yhatt.github.io/marp/>
* <http://slidify.org/>
* <https://rmarkdown.rstudio.com/lesson-11.html>
* GitPitch <https://github.com/gitpitch/gitpitch/wiki/Slide-Markdown>


### Markdown to PPTX

`Pandoc` provides the ability to simply export markdown to power
point. This could be useful for transitioning or first developing
content in markdown to powerpoint. Simply use

```
pandoc filename.md -o fiename.pptx
```

and you will convert the markdown to a simple powerpoint that you can
than improve. The initial improvement is best done in the overview
mode of powerpoint so you can organize the bullet points and slides
better in case the pagination is not done right.

## Checking if the Markdown is valid?

After using this tool we found significant limitations, that do not
include the syntactic and semantic checks that we need for our
papers. So we recommend that if you use the tool to also inspect the
file by hand.

Markdown is such a simple format that you should not have any
issue. We recommend that you do a local checkout of the epub and
compile it and look at your section contribution.  To work on a single
file you can just use markdown editors.

A lint program is available at

* <https://github.com/remarkjs/remark-lint>

However, we recommend to copy your file into a separate directory and
check it there as it installs some other programs into the directory
where you do the checking.

## References

*   <https://en.wikipedia.org/wiki/Markdown>


## Writing Papers and Reports with Markdown


### Proper use of `<>`

In this section we summarize a couple of issues that you will
typically not find in general markdown documentation, that however are
very important for us.

One of the frequent mistakes we see is that authors use the greater
and smaller characters without proper quoting.  THis is for example
done when referring to command line parameters or keys.

Such as `<key>` and `command <parameter>`

If they are not done in quotes they break any markdown as they are
interpreted as raw html Thus it is important that you quote them
properly


### Urls in markdown

Urls must be wrapped in proper markdown syntax this is done through 
`[text](url)` or `<url>` work. If you just use the url in the text without the `<>` 
it will not render properly


### Use star instead of underscore

As we do some translations of the markdown, we noticed that whan you
use `_` instead of `*` in your markdown this may lead to issues. please
use `*italic*` and `**bold**` only.


### Hyperreferences to other sections in markdown

PLease note that you must not 

```
# This is my header {#s-this-is-my-label}
```

Now, I can refer to [Section](#s-this-is-my-label). References, must not have spaces in it.


### Code in markdown

COde in markdown is easy to integrate with 

````md
```python
code
```
````

to see if syntax highlighting works. I have not tried this yet though
When doing bash, we also like to try


````md
```bash
$ script
```
````

Note that in order to indicate a new line in bash we use the `$` sign
as prefix which indicates the prompt sign.


### Citations in markdown

As we manage many references it is unnecessary to duplicate them. 
You can reuse them from others. IF you use them and notice errors, we 
require you to not only fix them in your bib, but also in the bib where 
you found it. Furthermore, we like you to use the same label and do not 
use a different label.

The best way to manage bibliographies is with jabref or emacs. We have
seen students that try to avoid them while making their life
unnecessarily complicated.

You must make sure that your bibliography entries are syntactically correct 
which either emace or jabref can do.

We will deduct points every time we notice that a bibliography is
syntactically wrong.  you will place the bibliography dependent on the
artifact into a bib file. For papers it is placed in a file called
`paper.bib`, for reports it is places in a file called
`report.bib`. The markdown file is accordingly called `paper.md` or
`report.md` all images must be placed in an `images/` directory
 

When you cite Then you can cite a references you can simply do this
with for example `[@www-google]`. Please not that citation keys must
not have spaces or underscore in them.

Example:


```
@Misc{www-google,
   author={{Google}},
   title={Google Home Page},
   howpublished={Web page},
   url={https://google.com}
}
```

Now you can use:

A good way to search on the internet is to use
Google [@www-google].

### Markdown and bibtex

As you know we do not use LaTeX for this class but simply
markdown. you can use pandoc to create your epubs locally if you wish
while following the paradox manual.

However, it is much simpler than that, as we create the proceedings
with all your markdown papers for you once a week, so you can check
it. OFten we create it multiple times a day.

So you do not have to do much than once in a while looking at the
epubs.



As part of this we like to remind you that we did distribute on day
one of the class a document located in



<https://github.com/cloudmesh-community/book/blob/master/README.md>



That is called Scientific Writing II. This includes a section about
LaTeX which you can ignore, but it also includes a section about
bibtex and how to do bibtex entries that you may be benefitting
from. So take a quick look at the Section 3. It also explains how to
improve bibtex entries which is important for your projects.



http://cyberaide.org/papers/vonLaszewski-latex.pdf



Also, we noticed that some do not follow our tips posed as part of the
FAQ's we send out here.

So we do recommend that you inspect them. TAs are assigned to also
move the FAQs into the handbook. So you can also find them there
(after a week).



Please also be reminded that there is an empty line before and after a
heading or a quote or

a list or any paragraph. paragraphs are not indented with tabs or spaces

### Please check your bibtex files

We continue to see that some have unnecessary issues with
bibtex. Mostly the reason is they are not using emacs or jabref which
come with validation that assures that commas are placed at the right
location.

We highly recommend that you use them. In addition, we recommend that
if you are familiar with the command line to install and run biber as
documented in our Scientific Writing II handbook. Typically this is
not needed when using emacs or jabref correctly.

You still need to ensure that there are no spaces in a label, the
types are correctly done, and that company authors have two
brackets. Please be reminded that an entry may only take you a minute
with such tools, but if you do not use them you may spend hours trying
to find a space in a label or a missing comma. bibtex is easy when
using the right tool.


### Using pandoc to check your files

It is easy to install pandoc on your operating system. PLease see the Pandoc web page and 
install it 

Once installed and you have in a directory the files

```
report.md
report.bib
images/test.png
```

You can easily generate for example a ePuB, PDF, or html output with 
Make sure to also install pandoc-fignos

```bash
$ pandoc --verbose --filter pandoc-fignos -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml -o paper.epub paper.md
```

:o: Assignment: provide documentation for Linux, OSX, Windows to do this.

A sample report is available at:

* <https://github.com/cloudmesh-community/proceedings-fa18/tree/master/project-report>

A sample 2 page paper is available at:

* <https://github.com/cloudmesh-community/proceedings-fa18/tree/master/paper>

Note that the formats of both are different. A two page paper is often
too short to justify an abstract or even a conclusion.

## Original Reference are a must

It came to our attention that some students forgot to cite the
original reference to their technologies.

The first time you mention your technology is a good location for that
example

Goggle [@www-google] is a company that offers cloud services.

where www-google is the label to the bibtex entry representing the
Google home page

