# Notation {#sec:notation}

The material here uses the following notation. This is especially
helpful, if you contribute content, so we keep the content consistent.

if you like to see the details on how to create them in the markdown
documents, you will have to look at the file source while clicking on
the cloud in the heading of the Notation section (@sec:notation). This
will bring you to the markdown tex, but you will still have to look at
the [raw content](https://raw.githubusercontent.com/cloudmesh-community/book/master/chapters/preface/notation.md)
to see the details.

:cloud: or ![Github](images/github.png) `![Github](images/github.png)`

> If you click on the :cloud: or ![Github](images/github.png) in a heading, you can go directly to the >
document in github that contains the next content. This is > convenient
to fix errors or make additions to the content. The cloud will be
automatically added upon inclusion of a new markdown file that includes
in its first line a section header.

$

> Content in bash is marked with verbatim text and a dollar sign
>
>  ```bash
>  $ This is a bash text
>  ```

[@las14cloudmeshmultiple]

> References are indicated with a number and are included in the >
reference chapter [@las14cloudmeshmultiple]. Use it in markdown with >
`[@las14cloudmeshmultiple]`. References must be added to the
`refernces.bib` file in BibTex format.

:o2: or [![No](images/no.png)]()

> Chapters marked with this emoji are not yet complete or have some
> issue that we know about. These chapters need to be fixed. If you like
> to help us fixing this section, please let us know. Use it in markdown
> with `:o2:` or if you like to use the image with `![No](images/no.png)`.


[![Video](images/video.png) REST 36:02](https://youtu.be/xjFuA6q5N_U)

> Example for a video with the `![Video](images/video.png)` emoji. Use it in markdown with
> `[![Video](images/video.png) REST 36:02](https://youtu.be/xjFuA6q5N_U)`

[![Presentation](images/presentation.png) Slides 10](TBD)

> Example for slides with the `![Presentation](images/presentation.png)` emoji. These slides may or
> may not include audio.

[![Audio](images/audio.png) Slides 10](TBD)

> Slides without any audio. They may be faster to download. Use it in
> markdown with `[![Presentation](images/presentation.png) Slides 10](TBD)`.

[![Learning](images/learning.png)]()

> A set of learning objectives with the `![Learning](images/learning.png)` emoji.

[![Ok](images/ok.png)]()

> A section is release when it is marked with this emoji in the
> syllabus. Usie it in markdown with `![Ok](images/ok.png)`.

[![Question](images/question.png)]()

> Indicates opportunities for contributions. Usie it in markdown with
> `![Question](images/question.png)`.

[![Construction](images/construction.png)]()

> Indicates sections that are worked on by contributors. Use it in
> markdown with `![Construction](images/construction.png)`.

[![Smiley](images/smile.png)]()

> Sections marked by the contributor with this emoji `![Smiley](images/smile.png)`
> when they are ready to be reviewed.

[![Comment](images/comment.png)]()

> Sections that need modifications are indicated with this emoji `![Comment](images/comment.png)`.

[![Warning](images/warning.png)]()

> A warning that we need to look at in more detail `![Warning](images/warning.png)`

[![Idea](images/idea.png)]()

> Notes are indicated with a bulb `![Idea](images/idea.png)`


Other emojis

> Other emojis can be found at
<https://gist.github.com/rxaviers/7360908>. However, note that emojis
may not be viewable in other formats or on all platforms. We know that
some emojis do not show in calibre, but they do show in macOS iBooks and
MS Edge

This is the list of emojis that canbe converted to PDF. So if you like a
PDF, please limit your emojis to

`:cloud:` :cloud:
`:o2:` :o2:
`:relaxed:` :relaxed:
`:sunny:` :sunny:
`:baseball:` :baseball:
`:spades:` :spades:
`:hearts:` :hearts:
`:clubs:` :clubs:
`:diamonds:` :diamonds:
`:hotsprings:` :hotsprings:
`:warning:` :warning:
`:parking:` :parking:
`:a:` :a:
`:b:` :b:
`:recycle:` :recycle:
`:copyright:` :copyright:
`:registered:` :registered:
`:tm:` :tm:
`:bangbang:` :bangbang:
`:interrobang:` :interrobang:
`:scissors:` :scissors:
`:phone:` :phone:

## Figures

Figures have a caption and can be refereed to in the ePub simple with a
number. We show such a reference pointer while referring to
@fig:code-example.

![Figure example](images/code.png){#fig:code-example width=1in}

Figures must be written in the md as

```markdown
![Figure example](images/code.png){#fig:code-example width=1in}
```

Note that the text must be in one line and must not be broken up even if
it is longer than 80 characters. You can refer to them with
`@fig:code-example`. Please note in order for numbering to work figure
references must include the `#fig:` followed by a unique identifier.
Please note that identifiers must be really unique and that identifies
such as `#fig:cloud` or similar simple identifiers are a poor choice and
will likely not work. To check, please list all lines with an identifier
such as.

```bash
$ grep -R "#fig:" chapters
```

and see if your identifier is truly unique.

## Hyperlinks in the document

To create hyperlinks in the document other than images, we need to
use proper markdown syntax in the source. This is achieved with a
refernce for example in sections headers. Let us discuss the
refernce header for this section, e.g. Notation. We have augmented
the section header as follows:

```# Notation {#sec:notation}```

Now we can use the refernce in the text as follows:

```In @sec:notation we explain ...```

It will be rendered as: In @sec:notation we
explain ...


## Equations {#sec:equations}

Equations can be written as

```$$a^2+b^2=c^2$${#eq:pythagoras}```

and used in text:

$$a^2+b^2=c^2$${#eq:pythagoras}

It will render as: As we see in @eq:pythagoras.

The equation number is optional. Inline equations just use one dollar
sign and do not need an equation number:

```This is the Pythagoras theorem: $a^2+b^2=c^2$```

Which renders as:

This is the Pythagoras theorem: $a^2+b^2=c^2$.

## Tables {#sec:tables}

Tables can be placed in text as follows:

```
: Sample Data Table {#tbl:sample-table}

x   y   z
--- --- ---
1   2   3
4   5   42
```

As usual make sure the label is unique. When compiling it will
result in an error if labels are not unique. Additionally there are
several md table generators available on the internet and make
creating table more efficient.
