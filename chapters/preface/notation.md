# Notation {#sec:notation}


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

Slides without any audio. They may be faster to download. 

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

---

:bulb: *Notes are indicated with a bulb and are written in italic and
surrounded by bars* using the `:bulb:` emoji

---

Figures have a caption and can be refereed to in the epub simple with a number. We show such a refernce 
pointer while refering to +@fig:code-example. 

![Figure example](images/code.png){#fig:code-example width=1in}

Figures must be written in the md as 

```
![Figure example](images/code.png){#fig:code-example width=1in}
```

You can refer to them with `+@fig:code-example`. Please note in order for numbering to work 
figure refernces must include the `#fig:` followed by a unique
identifier. Please note that identifiers must be realy unique and that
identifies such as `#fig:cloud` or similar simple identifiers are a
poor choice and will likely not work. To check, please list all lines
with an identifier such as

```bash
$ grep -R "#fig:" chapters
```

and see if your identifier is truly unique.

Other emojis

> Other emojis can be found at <https://gist.github.com/rxaviers/7360908>

---

:warning: *Please note that there is currently a bug when our document
is exported to html or to PDF, as emojis are for sme reason not
properly embedded. Hence to read the document we recommend that you
use an ePub reader.*

---

## Hyperlinks in the document

To create hyperlinks in the document other than images, we need to
use proper markdown syntax in the source. This is achieved with a
refernce for example in sections headers. Let us discuss the
refernce header for this section, e.g. Notation. We have augmented
the section header as follows:

```# Notation {#sec:notation}```

Now we can use the refernce in the text as follows:

```In [Section Notation](#sec:notation) we explain ...```

It will be rendered as: In [Section Notation](#sec:notation) we
explain ...


