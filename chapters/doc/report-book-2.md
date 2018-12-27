# Writing a Scientific Article or Conference Paper {#S:writing}

An important part of any scientific research is to document it. This is
often done through scientific conferences or journal articles. Hence it
is important to learn how to prepare and submit such papers. Most
conferences accept typically the papers in PDF format but require the
papers to be prepared on MSWord or in LaTeX. While working with many
students in the past we noticed however that those students using Word
often spend unnecessarily countless hours on trying to make there papers
beautiful while actually violating the template provided by the
conference. Furthermore, we noticed that the same students had issues
with bibliography management. Instead of Word helping the student it
provided the illusion to be easier than LaTeX but when adding up the
time spend on the paper we found that LaTeX actually saved time. This
has been especially true with the advent of collaborative editing
services such as sharelatex [@www-sharelatex] and
overleaf [@www-overleaf].

In this section we provide you with a professional template that is used
based on the ACM standard that you can use to write papers. Naturally
this will be extremely useful if the quality of your research is strong
enough to be submitted to a conference. We structure this section as
follows. Although we do not recommend that you use MSWord for your
editing of a scientific paper, we have included a short section about it
and outline some of its pitfalls that initially you may not think is
problematic, but has proven to be an issue with students. Next we will
focus on introducing you to LaTeX and showcasing you the advantages and
disadvantages. We will dedicate an entire section on bibliography
management and teach you how to use jabref which clearly has advantages
for us.

Having a uniform report format not only helps the students but allows
instructors to integrate the comparison of paper length and effort as
part of teaching a course. We have added an entire section to this
chapter that discusses how we can manage a *Class Proceedings* from
papers that are contributed by teams in the class.

Professional Paper Format
-------------------------

The report format we suggest here is based on the standard ACM
proceedings format. It is of very high quality and can be adapted for
your own activities. Moreover, it is possible to use most of the text to
adapt to other formats in case the conference you intend to submit your
paper to has a different format. The ACM format is always a good start.

Important is that you do not need to change the template but you can
change some parameters in case you are not submitting the paper to a
conference but use it for class papers. Certainly you should not change
the spacing or the layout and instead focus on writing content. As for
bibliography management we recommend you use jabref which we will
introduce in
Section [\[S:bibliographies\]](#S:bibliographies){reference-type="ref"
reference="S:bibliographies"}.

We recommend that you carefully study the requirements for the report
format. We would nat want that your paper gets rejected by a journal,
conference or the class just because you try to modify the format or do
not follow the established publication guidelines. The template we are
providing is available from:

You will find in it a modified ACM proceedings templates that you must
use.

Submission Requirements
-----------------------

Although the initial requirement for some conferences or journals is the
document PDF, in many cases you must be prepared to provide the source
when submitting to the conference. This includes the submission of the
original images in an images folder. You may be asked to package the
document into a folder with all of its sources and submit to the
conference for professional publication.

Microsoft Word vs. LaTeX {#microsoft-word}
------------------------

Microsoft word will provide you with the initial impression that you
will safe lots of time writing in it while you see the layout of the
document. This will be initially true, but once you progress to the more
challenging parts and later pages such as image menagement and
bibliography management you will see some issues. This include that
figure placement in Word need sto be done just right in order for images
to be where they need. We have seen students spending hours with the
placement of figures in a paper but when they did additional changes the
images jumped around and were not at the place where teh students
expected them to be. So if you work with images, make sure you
understand how to place them. Also always use relative caption counters
so that if an image gets placed elsewhere the counter stays consistent.
So nefer use just the number, but a reference to the figure when
referring to it. Recently a new bibliography management system was added
to Word. However, however it is not well documented and the references
are placed in the system bibliography rather than a local managed
bibliography. This mah have severe consequences when working with many
authors on a paper. The same is true when using Endnote. We have heard
in many occasions that the combination of endnote and Word destroyed
documents. You certainly do not want that to happen the day before your
deadline. Also in classes we observed that those using LaTeX deliver
better structured and written papers as the focus is on text and not
beautiful layout.

For all these reasons we do not recommend that you use Word.

In LaTeX where we have an easier time with this as we can just ignore
all of these issues due to relative good image placement and excellent
support for academic reference management. Hence, it is in your best
interest to use LaTeX. The information we provide here will make it easy
for you to get started and write a paper in no time as it is just like
filling out a form.

Working in a Team
-----------------

Today research is done in potentially large research teams. This also
include the writing of a document. There are multiple ways this is done
these days and depends on the system you chose.

In MSWord you can use onedrive, while for LaTeX you can use sharelatex
and overleaf. However, in many cases the use of github is possible as
the same groups that develop the code are also familiar with github.
Thus we provide you here also with the introduction on how to write a
document in github while group members can contribute.

Here are the options:

LaTeX and git:

:   This option will likely safe you time as you can use jabref also for
    managing collaborative bibliographies and

sharelatex:

:   an online tool to write latex documents

overleaf:

:   an online tool to write latex documents

MS onedrive:

:   It allows you to edit a word document in collaboration. We recommend
    that you use a local installed version of Word and do the editing
    with that, rather than using the online version. The online editor
    has some bugs. See also (untested):
    <http://www.paulkiddie.com/2009/07/jabref-exports-to-word-2007-xml/>,
    <http://usefulcodes.blogspot.com/2015/01/using-jabref-to-import-bib-to-microsoft.html>

Google Drive:

:   google drive could be used to collaborate on text that is than
    pasted into document. However it is just a starting point as it does
    not support typically the format required by the publisher. Hence at
    one point you need to switch to one of the other systems.

Time Management {#timemanagement}
---------------

Obviously writing a paper takes time and you need to car-fully make sure
you devote enough time to it. The important part is that the paper
should not be an after thought but should be the initial activity to
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

Paper and Report Checklist {#paper-checklist}
--------------------------

In this section we summarize a number of checks that you may perform to
make sure your paper is properly formatted and in excellent shape.
Naturally this list is just a partial list and if you find things we
should add here, let us know.

One good way is to either copy the checklist into a file or print out
just this pages and check with a pen if the particular issue occurs.

Content
-------

-   Is the paper formal paper and not an experience report?

-   Do not include phrases such as "In week 1 we did this"

-   When writing the *proposal* do not use the word "proposal" write the
    document as if it would be teh final paper. We see too many reports
    at the end forgetting to remove the word proposal in the final
    paper, so we can not tell if you did it or if it is still a
    proposal. As the final paper is not a proposal we reject such papers
    and you get a 1/3 grade reduction. To avoid this, just do not use
    the word proposal.

-   When writing the abstract do not make it a proposal. Abstracts are
    no proposals. Avoid phrases such as We propose to do, We intend to
    show and so on. If the paper intends to show things you are still in
    the draft phase of the paper. However, if you say We show, that
    would be good. Let us just assume you intended to show something but
    did not achieve then you can say "We intended to show this but we it
    was not possible to verify. We have provided reasons for this in the
    paper". As you can see not only the intention is communicated, but
    the result. If you just focus on the intent that is just a proposal
    and is not a proper abstract.

-   Add keywords to the paper, where the first two are your HID, and
    your class number.

-   If your paper is an introduction or overview paper, please do not
    assume the reader to be an expert. Provide enough material for the
    paper to be useful for an introduction into the topic.

-   If your paper limit is x number of pages but you want to hand in x
    plus 100 pages. If however you page limit is 2 pages and you hand in
    4 or 6 pages that is no issue.

Submission
----------

-   Do not make changes to your paper during grading, when your
    repository should be frozen.

-   Do not use filenames and directory names that have spaces in them
    only use \[a-z0-9\]\*

-   Make all file names lower case other than Makefile and README.yml

-   You are required to run yamllint README.yml on all team members
    README.yml including your own. All of them must pass. Do this on the
    first day you start writing the paper. Only push and commit the
    files when they pass this test. If you do not have yamllint you can
    write one in python. Its 3 lines of code.

-   Have you included the paper in the submission system (In our case
    git). This includes all images, bibliography files and other
    material that is needed to build the paper from scratch?

-   Have you made sure your paper compiles with *make* and the provided
    Makefile before you committed?

-   Are all images checked in?

-   Did you submit the report.bib file?

Bibliography
------------

-   Are you managing your references in jabref and endnote (we need
    both)

-   In the author field, authors are separated with an *and* and not a
    comma.

-   The filename for the bibliography is report.bib.

-   Bibtex labels must have any spaces, \_ or & in it

-   Fix citations in text that show as \[?\]. This means either your
    report.bib is not up-to-date or there is a spelling error in the
    label of the item you want to cite, either in report.bib or in
    report.tex

-   Urls in citations are never placed in howpublished, instead we use
    url = { }. `howpublished` is just used for a text sting such as Web
    Page, Blog, Repository and others like that. Do not use just the
    word Web, as it could be a Web Site or a Web Page. You need to be
    specific.

-   Do not use the `\url={ ]` in teh text, instead use a citation.

-   Are you references correct? References to a paper are no
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

Writing
-------

-   Have you spellchecked the paper?

-   Have you grammar chacked the paper?

-   Use proper capitaliztion in the title, see:
    <https://capitalizemytitle.com/>

-   Are you using *a* and *the* properly?

-   Short form of verbs is for spoken language. Do not use them in
    scientific writing. Example: can't is incorrect, cannot is correct.

-   Do not use phrases such as *shown in the Figure below*. Instead, use
    *as shown in Figure 3*, when referring to the 3rd figure, but use
    the *ref* *label* macros.

-   Do not use the word *I* instead use *we* even if you are the sole
    author. In many cases you may want to avoid using the word *we*
    also.

-   Do not use the phrase *In this paper/report we show* instead use *We
    show*. It is not important if this is a paper or a report and does
    not need to be mentioned.

-   If you want to say *and* do not use *&* but use the word *and*.

-   Use a space after `. , :`

-   When using a section command, the section title is not written in
    all-caps as the LaTeX template will do this automatically for you.
    Thus it is `\section{Introduction}` and NOT
    `\section{INTRODUCTION}`.

Citation Issues and Plagiarism
------------------------------

-   It is your responsibility to make sure no plagiarism occurs.

-   When stating claims you added the proper citations.

-   Do avoid paraphrasing long quotations (whole sentences or longer)
    form other papers.

-   Double check your paper if you have quote from other papers and
    included the citation.

-   The `\cite{}` command must not be in the beginning of the sentence
    or paragraph, but in the end, before the period mark. Example: ...a
    library called Message Passing Interface (MPI) \[7\].

-   Put a space between the citation mark and the previous word or
    better use `~`.

-   There must not be any citation in the abstract or conclusion.

-   Citations cannot be included in section headings they need to be
    included in the text.

Character Errors
----------------

The following errors are very often found and must be avoided.

-   To emphasize a word, use *emphasize* and not "quote". Quotes are
    reserved for quotes from other papers and must not be used to
    emphasize words or phrases. to put around a word that you like to
    emphasize.

-   Generally we do not us **bold fett** text. Instead use *em*.

-   Erroneous use of quotation marks, i.e. use ``` ``quotes'' ```, but
    not the double quote that you find on your keyboard such as `" "`.

-   When using the characters & \# % \_ put a backslash before them so
    that they show up correctly.

-   Pasting and copying from the Web often results in non-ASCII
    characters to be used in your text, please remove them and replace
    accordingly. This is the case for quotes, dashes and all the other
    special characters.

-   If you see a figure and not a figure in text you copied from a text
    that has the fi combined as a single character. It happens often
    with combinations of f such as fi fl ff

Structural Issues
-----------------

-   Does your paper include an Acknowledgement section.

-   Is the acknowledgment including all the people appropriately that
    helped you in your activity.

-   In case of a class and if you do a multi-author paper, you need to
    add an appendix called *Workbreak Down* describing who did what in
    the paper,after the bibliography

-   Do you fullfill the minimum page length such as defined in the
    submission guideline. Remember that images, tables and figures do
    not count towards the page length.

-   Do not artificially inflate your paper if you are below the page
    limit.

-   In case you have an appendix it is included after the bibliography

Figures and Tables
------------------

-   Images must be at least 300dpi if they are not in a scalable format
    such as PDF which you can generate from Powerpoint and other drawing
    programs.

-   If you use Microsoft products, use ppt 4:3 ratio for drawing concet
    images. In case there is a powerpoint in the submission, the image
    must be exported as PDF.

-   If you have OSX, you are allowed to use omnigraffle.

-   Make sure you capitalize Figure 1, Table 2 when used in a sentence.

-   Do use `\label{}` and `\ref{}` to automatically create figure
    numbers.

-   Figure caption must be bellow the image.

-   Table captions must be above the image.

-   Do not include the titles of the figures in the figure itself but
    instead use the caption or that information.

-   All images must be in native format, e.g. `.graffle`, `.pptx`,
    `.png`, `.jpg` in the images directory

-   Do not submit eps images. Instead, convert them to PDF

-   The image files must be in a single directory named *images*.

-   Make the figures large enough so we can read the details. If needed
    make the figure over two columns

-   Do not worry about the figure placement if they are at a different
    location than you think. Figures are allowed to float. To illustrate
    this case we force all images to be placed at the end of the paper,
    although you may have included it at a special location in the
    paper. This forces you to avoid the phrases as seen in teh following
    image, but you need to use the ref and label features in LaTeX.

-   In case you copied a figure from another paper you need to ask for
    copyright permission. In case of a class paper, you must include a
    reference to the original in the caption. In general we like to
    avoid this for the reports and like that you produce original
    pictures.

-   Remove any figure that is not referred to explicitly in the text
    with a ref command. Again just putting in the number will not be
    good enough. This allows you to place the figure in the final
    submission at a location without needing to fix the numbers.

-   Do not use textwidth as a parameter for includegraphics, but instead
    use `\columnwidth` as demonstrated in our template.

-   Figures should be reasonably sized and often you just need to add
    columnwidth e.g.

    `/includegraphics[width=1.0\columnwidth]{images/myimage.pdf}`

    Do not play with the size, just leave it with 1.0.

If you observe something missing let us know.

Example Paper
-------------

An example report in PDF format is available:

Creating the PDF from LaTeX on your Computer
--------------------------------------------

Latex can be easily installed on any computer as long as you have enough
space. Furthermore if your machine can execute the make command we have
provided in the standard report format a simple

[Makefile](https://github.com/cloudmesh-community/hid-sample/blob/master/paper/Makefile)

that allows you to do editing with immediate preview as documented in
the LaTeX lesson.

Draft: Class Specific README.md {#class-specific-readme.md}
-------------------------------

For the class we will manage all papers via github.com. You will be
added to our github at

Previously we used

and assigned an hid (homework index directory) directory with a unique
hid number for you. In addition, once you decide for a project, you will
also get a project id (pid) and a directory in which you place the
projects. Projects must not be placed in hid directories as they are
treated differently and a class proceedings is automatically created
based on your submission.

As part of the hid directory, you will need to create a README.md file
in it, that **must** follow a specific format. The good news is that we
have developed an easy template that with common sense you can modify
easily. The template is located at

As the format may have been updated over time it does not hurt to
revisit it and compare with your README.md and make corrections. It is
important that you follow the format and not eliminate the lines with
the three quotes. The text in the quotes is actually yaml. Yaml is a
data format the any data scientist must know. If you do not, you can
look it up. However, if you follow our rules you should be good. If you
find a rule missing for our purpose, let us know. We like to keep it
simple and want you to fill out the *template* with your information.

Simple rules:

-   replace the hid number with your hid number.

-   naturally if you see sample- in the directory name you need to

    delete that as your directory name does not have sample- in it.

-   do not ignore where the author is to be placed, it is in a list
    starting with a `-`

-   there is always a space after a `-`

-   do not introduce empty lines

-   do not use TAB and make sure your editor does not bay accident
    automatically creates tabs. This is probably the most frequent error
    we see.

-   do not use any `: & _` in the attribute text including titles

-   an object defined in the README.md must have on a single type field.
    For example in the project section. Make sure you select only one
    type and delete the other

-   in case you have long paragraphs you can use the \> after the
    abstract

-   Once you understood how the README.md works, please delete the
    comment section.

-   Add a chapter topic that your paper belongs to

Exercises
---------

[\[E:Report.1\]]{#E:Report.1 label="E:Report.1"} Install latex and
jabref on your system

[\[E:Report.2\]]{#E:Report.2 label="E:Report.2"} Check out the report
example directory. Create a PDF and view it. Modify and recompile.

[\[E:Report.4\]]{#E:Report.4 label="E:Report.4"} Learn about the
different bibliographic entry formats in bibtex

[\[E:Report.5\]]{#E:Report.5 label="E:Report.5"} What is an article in a
magazine? Is it really an Article or a Misc?

[\[E:Report.6\]]{#E:Report.6 label="E:Report.6"} What is an
InProceedings and how does it differ from Conference?

[\[E:Report.7\]]{#E:Report.7 label="E:Report.7"} What is a Misc?

[\[E:Report.8\]]{#E:Report.8 label="E:Report.8"} Why are spaces,
underscores in directory names problematic and why should you avoid
using them for your projects

[\[E:Report.9\]]{#E:Report.9 label="E:Report.9"} Write an objective
report about the advantages and disadvantages of programs to write
reports.

[\[E:Report.10\]]{#E:Report.10 label="E:Report.10"} Why is it
advantageous that directories are lowercase have no underscore or space
in the name?
