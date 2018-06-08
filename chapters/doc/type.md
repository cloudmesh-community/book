Communicating Research in Other Ways
------------------------------------

Naturally, writing papers is not the only way to communicate your
research with others. We find that today we see additional pathways for
communication includine blogs, twitter, facebook, e-mail, Web pages, and
electronic notebooks. Let us refisit some of them and identify when they
are helpful.

### Blogs

blog:

> noun, a regularly updated website or web page, typically one run by an
> individual or small group, that is written in an informal or
> conversational style.

Advantages:

-   encourages spontaneous posts
-   encourages small short contributions
-   chronologically ordered
-   standard software exists to set up blogs
-   online services exists to set up blogs

Disadvantages:

-   structuring data is difficult (some blog software support it)
-   not suitable for formal development of a paper
-   often lack of sophisticated track change features
-   no collaborative editing features

### Sphinx

Sphinx (<http://www.sphinx-doc.org/>) is a tool that to create
integrated documentation from a markup language.

Advantages:

-   output formats: html, LaTeX, PDF, ePub
-   integrates well with directory structure
-   powerful markup language (reStructuredText)
-   can be hosted on github via github pages
-   can integrate other renderers such as Markdown
-   automatic table of content, table of index
-   code documentation integration
-   search
-   written in python and using bash, so extensions and custom
    automation are possible

Disadvantage:

-   requires compile step
-   When using markdown github can render individual page

Others:

-   Read the Docs (<https://readthedocs.org/>)
-   Doxygen (<http://www.stack.nl/~dimitri/doxygen/>)
-   MkDocs (<http://www.mkdocs.org/>)

### Notebooks

#### Jupyter

The Jupyter Notebook (<http://jupyter.org/>) is an open-source web
application allowing users to create and share documents that contain
live code, equations, visualizations and explanatory text. Use cases
include data cleaning and transformation, numerical simulation,
statistical modeling, machine learning.

Advantages:

-   Integrates with python
-   Recently other programming languages have been integrated
-   Allows experimenting with settings
-   Allows a form of literate programming while mixing documentation
    with code
-   automatically renders on github
-   comes with web service that allows hosting

Disadvantage:

-   mostly encourages short documents
-   mark up language is limited
-   editing in ASCII is complex and Web editing is prefered

#### Apache Zeppilin

A Web-based notebook that enables data-driven, interactive data
analytics and collaborative documents with SQL, Scala and hadoop. It
integrates a web-based notebook with data ingestion, data exploration,
visualization, sharing and collaboration features to Hadoop and Spark.

Advantages:

-   integration to various framework
-   Web framework
-   integration with spark, hadoop

Disadvantages:

-   larger framework
-   must leverages existing deployments of spark, hadoop
