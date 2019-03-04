# Notation {#sec:notation}

The material here uses the following notation. If you like to see the details
on how to create them, you will have to look at the file source while clicking
on the cloud in the heading of the Notation section (@sec:notation).

:cloud: `:cloud:`

> If you click on the :cloud: in a heading, you can go directly to the
> document in github that contains the next content. This is
> convenient to fix errors or make additions to the content.

$

> Content in bash is marked with verbatim text and a dollar sign
>
>  ```bash
>  $ This is a bash text
>  ```

[@las14cloudmeshmultiple]

> References are indicated with a number and are included in the
> reference chapter [@las14cloudmeshmultiple]


:o: `:o:`

> Chapters marked with this emoji are not yet complete or have some issue
> that we know about. These chapters need to be fixed. If you like to
> help us fixing this section, please let us know. 


[:clapper: REST 36:02](https://youtu.be/xjFuA6q5N_U) 

> Example for a video with the `:clapper:` emoji


[:scroll: Slides 10](TBD) 

> Example for slides with the `:scroll:` emoji. These slides may or
> may not include audio.

[:pencil: Slides 10](TBD)

> Slides without any audio. They may be faster to download. 

:mortar_board:

> A set of learning objectives with the `:mortar_board:` emoji.


:white_check_mark:

> A section is release when it is marked with this emoji in the syllabus.

:question:

> Indicates opportunities for contributions.

:hand:

> Indicates sections that are worked on by contributors

:smiley:

> Sections marked by the contributor with this emoji when they are
> ready to be reviewed.

:wave:

> Sections that need modifications are indicated with this emoji.

:warning:

> A warning that we need to look at in more detail.


:bulb:

> Notes are indicated with a bulb


Other emojis

> Other emojis can be found at <https://gist.github.com/rxaviers/7360908>


## Figures

Figures have a caption and can be refereed to in the epub simple with a number. We show such a refernce 
pointer while refering to @fig:code-example. 

![Figure example](images/code.png){#fig:code-example width=1in}

Figures must be written in the md as 

```markdown
![Figure example](images/code.png){#fig:code-example width=1in}
```

You can refer to them with `@fig:code-example`. Please note in order for numbering to work 
figure refernces must include the `#fig:` followed by a unique
identifier. Please note that identifiers must be realy unique and that
identifies such as `#fig:cloud` or similar simple identifiers are a
poor choice and will likely not work. To check, please list all lines
with an identifier such as

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

```$$a^2+b^2=c^2$${#eq:pytagoras}```

and used in text: 

$$a^2+b^2=c^2$${#eq:pytagoras}

It will render as: As we see in @eq:pytagoras. 

The equation number is optional. Inline equations just use one dollar
sign and do not need an equation number:

```This is the pythagoras theorem: $a^2+b^2=c^2$```

Whch renders as:

This is the pythagoras theorem: $a^2+b^2=c^2$.

## Tables {#sec:tables}

Tables can be placed in text as follows: 

```
: Sample Data Table {#tbl:sample-table}
  
x   y   z
--- --- ---
1   2   3
4   5   42
```

As usual make sure the label is unique. When compiling it it will
result in

: Sample Data Table {#tbl:sample-table}
  
x   y   z
--- --- ---
1   2   3
4   5   42

The data in @tbl:sample-table was gathered from all the experiments we
conducted in the cloud and the overall result was $42$.
