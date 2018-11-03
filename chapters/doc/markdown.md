Markdown
--------

The content form this section originates from see:

-   <https://en.wikipedia.org/wiki/Markdown>

Markdown is a simple markup language, however there is no precise
standard defined for it and implementations may have features not
supported by other implementations. Nevertheless, it provides a simple
and easy way to quickly develop clean looking documents.

There are several tools that make markdown attractive allowing to write
the text in one window while at the same time seeing the rendered out
put in another.

This includes

Macdown

:   An editor for markdown targeted on macOS

To convert the markdown to other formats with `pandoc`

    # Heading

    ## Sub-heading

    ### Another deeper heading
     
    Paragraphs are separated
    by a blank line.

    Two spaces at the end of a line leave a  
    line break.

    Text attributes _italic_, *italic*, __bold__, **bold**, `monospace`.

    Horizontal rule:

    ---

    Bullet list:

      * apples
      * oranges
      * pears

    Numbered list:

      1. apples
      2. oranges
      3. pears

    A [link](http://example.com).

    ```bash
    $ echo "a bash script"
    ```

    ```python
    print("a pythion script")
    ```

### Editing Tools

Dilinger

:   A HTML5 based cloud enabled editor <https://dillinger.io/>. It
    allows to download the created Markdown.

Macdown

:   MacDown is an open source Markdown editor for macOS that is
    available at <https://macdown.uranusjr.com/>

Haropad

: Haropad is a cross platform markdown editor. It asks for donation for
  its further development. It can be downloaded from
  <http://pad.haroopress.com/>

Markdown plus

: Markdown with lots of extensions. We are not supporting all of the
  extensions at this time. We just use mostly regular markdown.
  It is located at <https://mdp.tylingsoft.com/>. The source code is
  on github <https://github.com/tylingsoft/markdown-plus>. A
  precompiled version is available for $15. A possible local install
  could be working as follows (untested)

  ```bash
  $ git colone https://github.com/tylingsoft/markdown-plus.git
  $ cd markdown-plus
  $ brew install yarn
  $ yarn install
  $ yarn watch
  $ open open dist/index.html
  ```

### Presentations in Markdown

Please find some links on hwo to use markdown to create slides

-   <https://yhatt.github.io/marp/>
-   <http://slidify.org/>
-   <https://rmarkdown.rstudio.com/lesson-11.html>
-   GitPitch <https://github.com/gitpitch/gitpitch/wiki/Slide-Markdown>

### Conversion with pandoc

Pandoc is a tool to convert file formats between each other. According
tho the Web page Pandoc can convert "Markdown, reStructuredText,
textile, HTML, DocBook, LaTeX, MediaWiki markup, TWiki markup,
TikiWiki markup, Creole 1.0, Vimwiki markup, OPML, Emacs Org-Mode,
Emacs Muse, txt2tags, Microsoft Word docx, LibreOffice ODT, EPUB, or
Haddock markup".

The Web page is located at.

* <https://pandoc.org/>

To convert files simply use the following commandline option `-o` to
specify the output format

    pandoc filename.md -o filename.tex

In our example we converted the md file to latex.

As this document is created with pandoc we encourage you to review our
Makefile to see how we use some more advanced features


### Mermaid

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



