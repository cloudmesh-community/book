# Writing a Scientific Article  {#S:writing}

An important part of any scientific research is to communicate and document it.
Previously we used LaTeX in this class to provide the ability to
contribute professional looking documents. As part of this we also
noticed that **any*document from **any*student that ever submitted a
document in MSWord was inferior to those using structured
documents such as provided by LaTeX or mrkdown. Although we would have loved to 
continue our work in LaTeX, a small number of students made the full 
adoptation of LaTeX as document system not possible. Thus we have adopted an even
simpler approach. All documents written for this class are written in
structured markdown. As we use a uniform format all documents in the class 
will be made available online, including your project reports. This allows 
anyone giving feedback to the class artifacts and not only by the
instructors. IT also allows open sharing of ideas as any project in class 
must be unique and must not have been previously done. If it has been, a 
significant enhancement must be made.

While using markdown and github, you will also be able to
collaboratively write documents in a group, while the instructors can
inspect who has contributed to the document what while utilizing the
history of the document.

In addition we will be able to use bibtex as refernce manager and
leverage hundrets of thousends professionaly curated bibliography
citations while not needing to worry about IEEE, ACM, or APA style
formating requirements. The bibliograhy format is automatically
created for you. In particular markdown is very useful for creating
deployment and code documentations though easy to use verbatim
modes. At the same time it allows us to use mathematical equations as
defined in LaTeX and avoid images for equation includsion.

Having a uniform report format not only helps us to be able to
integrate the papers into a proceedings so you can yourslef compare
the paper length and effort as part of teaching a course with other
students contributions.  As such we have made available many previous
projects through publically available proceedings. We will furthermore
explain how you can create such proceedings yourself.


## Format


We distinguish typically two different artifacts. Such documents could 
be integrated in our book. Therfore you must not use the term *project*, *paper*, 
or *chapterin the text or title. The artifacts are:

1. a small technology overview
2. a project report

A technology overview is a document that is multiple pages long and 
contains an overview about the technology, and a number of references. 
It is used to prepare you for writing a project report. Such technology 
overviews can be integrated as chapters into our book. You can look for 
example at the *graphqlsection in the 
[Cloud Computing](https://github.com/cloudmesh-community/book/blob/master/vonLaszewski-cloud.epub) book] for an example 
on how such a section looks like 

A template for such a section is provided at 

<https://github.com/cloudmesh-community/proceedings-fa18/tree/master/paper>

The second format is the format for a report which is provided at 

<ttps://github.com/cloudmesh-community/proceedings-fa18/tree/master/report>

and you will be using for your project report. To use them you must copy the md files precisely 
as a raw file and not just copy and paste from the rendered github output. 
We provide in the markdown section presice documentation on how to add images, citations and refernces.

## Github limitations

Please note that github does not render your document precisely. 
Instead you need to install pandoc and create the document yourslef if you like to see it. 
However, do never add the pdf or docx file to your github repository, as our proceedings script will outomatically 
create the final version and your versions in github will conflict with them.

You will have exactly one md file and one bib file in the directory you manage, 
as well as an images directory that contains all images.

## Working in a Team

Today research is done in potentially large research teams. This also
include the writing of a document and code. In order for you not to learn additional systems 
you will be using github for collaboratively writing code and the document with your team mates.

## Time Management {#timemanagement}

Obviously writing a paper takes time and you need to carefully make sure
you devote enough time to it. The important part is that the paper
should not be an after-thought but should be the initial activity to
conduct and execute your research. Remember that

1.  It takes time to read the information
2.  It takes time understand the information
3.  It takes time to do the research

For deadlines the following will get you in trouble:

1.  *There are still 10 weeks left till the deadline, so let me start in
    4 week ...*. Procrastination is your worst enemy.
2.  If you work in a team that has time management issues address them
    immediately
3.  Do not underestimate the time it takes to prepare the final
    submission into the submission system. Prepare automated scripts
    that can deliver the package for submission in minutes rather than
    hours by hand.

## Paper and Report Checklist

In this section we summarize a number of checks that you may perform to
make sure your paper is properly formatted and in excellent shape.
Naturally this list is just a partial list and if you find things we
should add here, let us know.

One good way is to either copy the checklist into a file or print out
just this pages and check with a pen if the particular issue occurs.

### Team

1.   If you work in a team make sure you only store the document once in github. 
     Remove all duplicates. E.g. select one HID under which the report is stored.
2.   Update your README.yml files `group:` where the first HID is the HID  
     in which your report or paper is stored. Do this as soon as you have 
     identified your team.
3.   Once you have your team identified create the approriate directory and copy the template 
     into it. Upload it to github.com in your dedicated repository.

### Content

1.  Is the paper formal paper and not an experience report?
1.  Do not include phrases such as "In week 1 we did this"
1.  Do not include the words paper, chapter, or report in your text to refer 
    to itself. Instead use general terms such as "We describe ...". It is not 
    important if it is a chapter, report, or paper. In fact if your pepre would 
    be selected to be put in the book a paper becoms a chapter and you would have to change it. 
    Therepre, we avoid it altogether.
1.  When writing the *proposaldo not use the word "proposal" write the
    document as if it would be the final paper. We see too many reports
    at the end forgetting to remove the word proposal in the final
    paper, so we can not tell if you did it or if it is still a
    proposal. As the final paper is not a proposal we reject such papers
    and you get a 1/3 grade reduction. To avoid this, just do not use
    the word proposal.
1.  When writing the abstract do not make it a proposal. Abstracts are
    no proposals. Avoid phrases such as We propose to do, We intend to
    show and so on. If the paper intends to show things you are still in
    the draft phase of the paper. However, if you say We show, that you 
    later will not have to chnage the text.
    Let us just assume you intended to show something but
    did not achieve then you can say "We intended to show this but we it
    was not possible to verify. We have provided reasons for this in the
    section A". As you can see not only the intention is communicated, but
    the result. If you just focus on the intent that is just a proposal
    and is not a proper abstract.
1.  Add meaningful up to 5 keywords to the paper
1.  Do not add the class or your HID to the keywords. Instead, 
    just add the HID after the title. THis way it can be easily seen 
    in the proceedings.
1.  If your paper is an introduction or overview paper, please do not
    assume the reader to be an expert. Provide enough material for the
    paper to be useful for an introduction into the topic.
1.  A typical report has about :o: number of words
1.  If your paper limit is x number of words but you want to hand in > x + x 10
    words this is an issue. If however you page limit is 2 pages and you hand in
    4 or 6 pages that is no issue.

### Submission

1.  Do not make changes to your paper during grading, when your
    repository should be frozen.
1.  Do not use filenames and directory names that have spaces in them
    only use `[a-z0-9-]`. Have all directory names be lower case.
1.  Make all file names lower case other than Makefile and README.yml
1.  You are required to run 

    ```bash
    $ yamllint README.yml 
    ```

    on all team members
    README.yml including your own and correct mistakes other than line length.
    Whenever you make modifications, please rerun yamllint.
    Do not add unnecessary spaces. Take a look at the previous class for examples.
    If you do not have yamllint you can
    write one in python. Its 3 lines of code. It is part of the class requirement 
    to know how to write a yml file. We will deduct 10% of your grade if you 
    repeatedly make mistakes in the yaml file.
1.  Have you included the paper in the submission system (In our case
    git). This includes all images, bibliography files and other
    material that is needed to build the paper from scratch?
1.  Have you made sure your paper compiles with *makeand the provided
    Makefile before you committed? :o: a makefile will be provided to you 
    so you can check if the document is correct
1.  Are all images checked in?
1.  Did you submit the report.bib file?
1.  Remember that your document will be integrated in a proceeedings that requires unique 
    bibtex labels image labels and other references. THus you could append 
    them with your hid to make them unique.
    
We may experiment this year with a joint bibliography so you can reuse existing bibtex 
files and citations. :o: stay tuned on this.

### Bibliography

1.  Are you managing your references in jabref 
1.  In the author field, authors are separated with an *andand not a
    comma.
1.  The filename for the bibliography ends in .bib.
1.  Bibtex labels must not have any spaces, \_ or & in it
1.  Fix citations in text that show as \[?\]. This means either your
    bib file is not up-to-date or there is a spelling error in the
    label of the item you want to cite.
1.  Urls in citations are never placed in howpublished, instead we use
    url = { }. `howpublished` is just used for a text sting such as *Web
    page*, *Blog*, Repository and others like that. Do not use just the
    word Web. To be uniform use the word *Web Page*. 
1.  Do not use the only urls in the text, instead use a citation behind the url.
1.  Are you references correct? References to a paper are no
    afterthought, they should be properly cited. Use jabref and make
    sure the citation type of the reference is correct and fill out as
    many fields as you can. Some journals and conferences have for
    example special requirements that go beyond the requirements of for
    example jabref. One example is that many conferences require you
    that wne you cite papers form another conference to augment the
    conferences not only with the location where the conference took
    place, but also with the dates the conference took place.
    Unfortunately, this is information that is often only available
    through additional google queries and many reference entries you
    find in the internet do not have this information readily available.

### Writing

1.  Have you spellchecked the paper?
1.  Have you grammar chacked the paper?
1.  Use proper capitaliztion in the title, see:
    <https://capitalizemytitle.com/>
1.  Are you using *aand *theproperly?
1.  Short form of verbs is for spoken language. Do not use them in
    scientific writing. Example: can't is incorrect, cannot is correct.
1.  Do not use phrases such as *shown in the Figure bellow*. Instead, use
    *as shown in Figure 3*, when referring to the 3rd figure, but use
    the *ref*labelmacros. How to automatically use figure numbers is 
    explained in our template. You must use this automated figure numbering. 
1.  Do not use the word *Iinstead use *weeven if you are the sole
    author. In many cases you may want to avoid using the word *we*
    also.
1.  Do not use the phrase *In this paper/report/chapter we showinstead use *We
    show*. It is not important if this is a paper or a report and does
    not need to be mentioned.
1.  If you want to say *anddo not use *&but use the word *and*.
1.  Use a space after `. , :`
1.  Headers are never just capitalized, E.g. `## INTRODUCTION` is wrong but 
    `## Introduction` is correct.
1.  Use proper indentation of the headers with `#` characters. The title has one `#` 
    All others will have more
1.  All headers are not numbered. numbers will be automatically added by our scripts

### Citation Issues and Plagiarism

1.  It is your responsibility to make sure no plagiarism occurs.
1.  When stating claims you added the proper citations.
1.  Do avoid paraphrasing long quotations (whole sentences or longer)
    form other papers.
1.  Double check your paper if you have quote from other papers and
    included the citation.
1.  The `[@label]` command must not be in the beginning of the sentence
    or paragraph, but in the end, before the period mark. Example: ...a
    library called Message Passing Interface (MPI) `[7]`.
1.  Put a space between the citation mark and the previous word.
1.  There must not be any citation in the abstract or conclusion.
1.  Citations cannot be included in section headings they need to be
    included in the text.

### Character Errors

The following errors are very often found and must be avoided.

1.  To emphasize a word, use *emphasizeand not "quote". Quotes are
    reserved for quotes from other papers and must not be used to
    emphasize words or phrases. to put around a word that you like to
    emphasize.
1.  When quoting we want you not only to use the `""` chars, but also the `>` char

    `> "This is a proper quote" [@label]`

1.  Generally we do not us **bold*text. Instead use *italic*.
1.  When using `<text>` in a text it must be quoted `<` `>` without quotes are interpreted as html and will 
    likely render wrongly.
1.  Pasting and copying from the Web often results in non-ASCII
    characters to be used in your text, please remove them and replace
    accordingly. This is the case for **all*quotes, dashes and all the other
    special characters such as three dots, copyright and so on.

### Structural Issues

1.  Does your paper include an Acknowledgement section.
1.  Is the acknowledgment including all the people appropriately that
    helped you in your activity.
1.  In case of a class and if you do a multi-author paper, you need to
    add an appendix called *Workbreak Downdescribing who did what in
    the paper,after the bibliography
1.  Do you fullfill the minimum page length such as defined in the
    submission guideline. Remember that images, tables and figures do
    not count towards the page length.
1.  Do not artificially inflate your paper if you are below the page
    limit.
1.  In case you have an appendix it is included after the bibliography

### Figures and Tables

1.  Images must be at least 300dpi if they are not in a scalable format
    such as PDF which you can generate from Powerpoint and other drawing
    programs.
1.  If you use Microsoft products, use ppt 4:3 ratio for drawing correct
    images. In case there is a powerpoint in the submission, the image
    must be exported as PDF.
1.  If you have OSX, you are allowed to use omnigraffle.
1.  Make sure you capitalize Table 1 when used in a sentence.
1.  Do use `@fig:yourfigurelabel` to automatically refer to the figure in the text.
1.  Table captions must be above the image.
1.  Do not include the titles of the figures in the figure itself but
    instead use the caption or that information.
1.  All images must be in native format, e.g. `.graffle`, `.pptx`,
    `.png`, `.jpg` in the images directory
1.  Do not submit eps images. Instead, convert them to PDF
1.  The image files must be in a single directory named *images*.
1.  Make the figures large enough so we can read the details. If needed
    make the figure over two columns
1.  Do not worry about the figure placement if they are at a different
    location than you think. Figures are allowed to float. 
1.  In case you copied a figure from another paper you need to ask for
    copyright permission. In case of a class paper, you must include a
    reference to the original in the caption. In general we like to
    avoid this for the reports and like that you produce original
    pictures. In case you can not, make sure to put a citation in the caption.
1.  Remove any figure that is not referred to explicitly in a sentence. 

If you observe something missing let us know.

## Acknowledgements {#S:acknowledgements}

In many cases you not only want but must to include an acknowledgement
section. In some cases you may be tempted to eliminate this section as
you think you are out of space and the acknowledgement section may give
you some additional space. This however is the wrong strategy and you
should not do this. Instead you should shorten your paper elsewhere and
leave enough space for acknowledgements.

In some cases where you get financial support from a university or a
funding agency for a project such as from NIH or NSF specific
information **must** be included. The best way is to verify with your
coauthors. Additional acknowledgements may have to be added and you need
te evaluate if for example significant help on the paper or the work
that lead up to the paper warrants co-authorship.

An issue that we have seen often is for example when a professor has
helped significantly on the paper but is not properly acknowledged. This
can even lead to the professor asking you to remove him from the
acknowledgement. A bad acknowledgement example is the following:

> We like to thank Professor Zweistein for his help in teaching me how
> to write the paper.

We do not think that the professor will be happy with this
acknowledgement as it sounds like the only thing that was provided was
the help on that you should have done anyways without the help of the
professor. Ask yourself, if he introduced you to the field, has helped
you with preparing the text, has given you insights, has corrected
things in your paper, made suggestions. So instead of the above maybe
a more general term such as *helped with the paper* would be more
appropriate. If you feel like your professor did not help you, leaving
it off is more appropriate. In some cases you may wan to invite your
professor to become a co-author. In some cases you may want to even
include this handbook as a citation.



Exercises
---------

Report.1: 

: Install pandoc and jabref on your system

Report.2: 

: Check out the report example directory. Create a PDF with pandoc and view it. Modify and recompile.

Report.4: 

: Learn about the different bibliographic entry formats in bibtex

Report.5: 

: What is an article in a magazine? Is it really an Article or a Misc?

Report.6: 

: What is an InProceedings and how does it differ from Conference?

Report.7: 

: What is a Misc?

Report.8: 

: Why are spaces, underscores in directory names problematic and 
  why should you avoid
  using them for your projects

Report.10: 

: Why is it advantageous that directories are lowercase have no underscore or space
  in the name?
