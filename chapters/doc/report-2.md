# Report Format

Although we provide **trivial** but detailed report format requirements,
we observed over the years that some students still asked us can I make
my report shorter, or can i use a different format? The answer to these
questions is **no**. Furthermore, we observed that the same students
than went ahead and played with the formatting and introduced empty
lines, increased tables or figures, or worse modified the fontsize to
circumvent the page limit requirement.

Thus we have adopted a much simpler approach that is easy to summarize

1.  We provide you with a **high quality** report template format that
    you must not change and is used by millions of researchers.

2.  All references must be managed with jabref as reference management
    tool and must be provided in addition to the document.

3.  If your document does not follow the format or we find that you have
    modified the style of the template we provide will return the
    document without review.

4.  It is in the students responsibility to use the template format from
    the beginning on. In fact, our assignments will use the template for
    all assignments and not just your term paper or term report.

The template for the report is available from:

-   <https://github.com/cloudmesh/classes/tree/master/docs/source/format/report>

Convenient compressed files are available at

-   <https://github.com/cloudmesh/classes/tree/master/docs/source/format/report.tar.gz>

-   <https://github.com/cloudmesh/classes/tree/master/docs/source/format/report.zip>

You have two choices. A good one and a bad one.

The good choice is to use the LaTeX template and write your document in
LaTeX. The bad one is to use the Word template and write the document in
Word. Both templates are included in our git repository.

Hence, it is in your best interest to use LaTeX. The good news is that
we have made it simple for you to use it. Furthermore, you are allowed
to use online services. An example report in PDF format is available:

-   [report.pdf](https://github.com/cloudmesh/classes/blob/master/docs/source/format/report/latex/report.pdf)

We provide a very simple
[Makefile](https://github.com/cloudmesh/classes/blob/master/docs/source/format/report/latex/Makefile)
that allows you to do editing with immediate preview as documented in
the LaTeX lesson. Due to LaTeX being a **trivial** ASCII based format
and having a superior bibliography management you will save yourself
many hours of work that you will face while fighting with Word. We got
feedback from those that tried it and they thanked us later.
Furthermore, in case you are in a team, you can use either git while
collaboratively developing the LaTeX document, use sharelatex, or
overleaf.

However, we allow you to use word under the following conditions:

1.  You accept the risk that Word may crash and you may find yourself in
    last minute in the situation that you lost your work and your
    document is broken. We will not be sympathetic to this situation as
    we recommended that you use LaTeX.

2.  You must use not only Endnote, but also jabref when managing your
    references, so you have to do the management of references twice.
    This is so that your document could be converted to LaTeX in case we
    think it suitable for publication in a conference or workshop.

3.  You do not modify the theme.

4.  All images and tables are placed at the end of the paper.

5.  Git wil be used to submit all documents with regular updates.

For LaTeX you will encounter a much more smooth experience.

1.  Your final document must be committed in git and as LaTeX is ASCII
    based you can do thous throughout the semester and have backups via
    git.

2.  You will be using jabref to manage your bibliography and as LaTeX
    has build in support for bibliography management there is not much
    you need to pay attention to, all Format of the references is done
    for you in case you entered them correctly

3.  You do not modify our theme.

4.  All images and tables are placed at the end of the paper.

5.  Git wil be used to submit all documents.

6.  You are allowed to use sharelatex or overleaf so you do not have to
    install LaTeX on your computer, but see 5. and the next paragraph.

Whatever format you use, your final submission must be in **the class**
git. We will not review any documents stored on sharelatex or overleaf
or in any git repository not belonging to the class. Your final
submission will include the bibliography file(s) as a separate
document(s). All images must be placed in an images folder and submitted
in your repository with the originals. When using sharelatex or overleaf
you must replicate the directory layout carefully from our template and
include your final documents in git with a Makefile that can recreate
the document. It is in your responsibility that this works. We will
regenerate the document from source before we grade it. Thus it is not
sufficient to just check in the final PDF. The report must be spell
checked.

There will be **NO EXCEPTION** to this. We will not

:   review your report if its submission is incomplete.

Leverage parallel editing
-------------------------

In most cases you will be able to work in groups on class projects. This
allows you to develop the report collaboratively. Here are some options:

1.  LaTeX and git: THis option will likely safe you time as you can use
    jabref also for managing collaborative bibliographies and

2.  MS onedrive: It allows you to edit a word document in collaboration.
    We recommend that you use a local installed version of Word and do
    the editing with that, rather than using the online version. The
    online editor has some bugs. See also (untested):
    <http://www.paulkiddie.com/2009/07/jabref-exports-to-word-2007-xml/>,
    <http://usefulcodes.blogspot.com/2015/01/using-jabref-to-import-bib-to-microsoft.html>

3.  Google Drive: google drive could be used to collaborate on text that
    is than pasted into document. he final document will not accept as
    google document. You must use the 2 column ACM template. We observed
    that students that use google docs lack structure and we no longer
    allow it as final document format. It also does not allow us to
    uniformly compare the documents between each other. It is easy to
    transfer it to LaTeX.

Time management Tips {#timemanagement-tips}
--------------------

Obviously taking a class takes time

1.  It takes time to read the information

2.  It takes time understand the information

3.  It takes time to do the project

4.  This will get you in trouble: *There are still 10 weeks left till
    the project is due so let me start in 4 weeks ...*. Postponing the
    project till the last moment

5.  Do not spend significant time on unimportant documentation and
    setup. Instead spend time to develop cmd5 commands and scripts that
    do these things automatically

Report Checklist
----------------

This partial list may serve as a way to check if you follow the rules

1.  Have you written the report in the specified format?

2.  Have you included an acknowledgement section?

3.  Have you included the report in git?

4.  Have you specified the HID, names, and e-mails of all team members
    in your report. E.g. the Real Names that are registered in Canvas?

5.  Have you included the project number in the report?

6.  Have you included all images in native and PDF format in git in the
    images folder?

7.  Have you added the bibliography file that you managed with jabref

8.  In case you used word have you also provided the endnote file

9.  Have you added an appendix describing who did what in the project or
    report?

10. Have you spellchecked the paper?

11. Are you using **a** and **the** properly?

12. Have you made sure you do not plagiarize?

13. Have you not used phrases such as shown in the Figure below, but
    instead used as shown in Figure 3 when referring to the 3rd figure?

14. Have you capitalized "Figure 3", "Table 1", ... ?

15. Any figure that is not referred to explicitly in the text must be
    removed.

16. Are the figure captions bellow the figures and not on top. (Do not
    include the titles of the figures in the figure itself but instead
    use the caption or that information?

17. When using tables have you put the table caption on top?

18. Make the figures large enough so we can read the details. If needed
    make the figure over two columns?

19. Do not worry about the figure placement if they are at a different
    location than you think. Figures are allowed to float. If you want
    you can place all figures at the end of the report?

20. Are all figures and tables at the end?

21. Do not use the word "I" instead use we even if you are the sole
    author?

22. Do not use the phrase "In this paper/report we show" instead use "We
    show". It is not important if this is a paper or a report and does
    not need to be mentioned.

23. Do not artificially inflate your report if you are bellow the page
    limit and have nothing to say anymore.

24. If your paper limit is 12 pages but you want to hand in 120 pages,
    please check first with an instructor ;-)

25. Check in your current work of the report on a weekly basis to show
    consistent progress.

26. Please use the dedicated report format for class. It may not be the
    ACM or IEEE format, but may have some additions that make management
    of bibliographies easier. Do follow our instructions for
    bibliographies.

27. Do not use the characters & \# % in the paper if you use LaTeX. If
    you use them you probably need a in front of them.

28. If you want to say and do not use & but use the word and.

29. (I524) Is in your report directory a README.rst file in it as shown
    in the example project that we introduced you to?

30. (I523) you do not have to place a readme in your report or paper
    directories. Instead create a README.md in your hid or pid
    directories.

If you observe something missing let us know.

In case you are allowed to use word The following applies in addition

1.  Are you managing your references in jabref and endnote (we need
    both)

2.  Are you using the right template we have a special 2 column template
    for the class that is a modified version from the 2 column ACM
    template

3.  Are you using build in numbered section management? MSWord has
    Sections that must be used

4.  Are you using real bulleted lists in Word and not just a "\*" or a
    "-"?

5.  Have you carelessly pasted and copied into the document without
    using proper formats. E.g. in MSWord this is a problem. You need to
    fix the format and use the build in format. Not that if you paste
    wrong you effect the format styles.

6.  Have you created not only a docx document but also the PDF.

7.  Make sure you use .docx and not .doc

If you have other things to add, send them via piazza and we will add
them here.

README.md
---------

For I523, Fall 2017, we will manage all papers via github.com. You will
be added to our github at

-   <https://github.com/bigdata-i523>

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

-   <https://raw.githubusercontent.com/bigdata-i523/sample-hid000/master/README.md>

As the format may have been updated over time it does not hurt to
revisit it and compare with your README.md and make corrections. It is
important that you follow the format and not eliminate the lines with
the three quotes. The text in the quotes is actually yaml. yaml is a
data format the any data scientist must know. If you do not, you can
look it up. However, if you follow our rules you should be good. If you
find a rule missing for our purpose, let us know. We like to keep it
simple and want you to fill out the *template* with your information.

Simple rules:

-   replace the hid number with your hid number.

-   naturally if you see sample- in the directory name you need to
    delete that as your directory name does not have sample- in it.

-   do not ignore where the author is to be placed, it is in a list
    starting with a -

-   there is always a space after a -

-   do not introduce empty lines

-   do not use TAB and make sure your editor does not bay accident
    automatically creates tabs. This is probably the most frequent error
    we see.

-   do not use any : & \_ in the attribute text including titles

-   an object defined in the README.md must have on a single type field.
    for example in the project section. Make sure you select only one
    type and delete the other

-   in case you have long paragraphs you can use the \> after the
    abstract

-   Once you understood how the README.md works, please delete the
    comment section.

README.rst (for I524, Spring 2017)
----------------------------------

In the directory that contains the report, please include the following
README.rst file. Without this file we will not review your document:

    Title: The title of your paper (one line)

    Author: The author s of the paper (one line)

    HID: The HID of the authors in the order as specified in authors (one line)

    PID: The PID of the paper (there will be exactly one)

    E-mail: The e-mails of the authors in the order of the author list (one line)

    Format: latex or word (specify one)

Please note that all information has an empty line between them and all
information is stored in one line

This information is used to autogenerate the class proceedings.

Exercise
--------

Report.1:

:   Install latex and jabref on your system

Report.2:

:   Check out the report example directory. Create a PDF and view it.
    Modify and recompile.

Report.4:

:   Learn about the different bibliographic entry formats in bibtex

Report.5:

:   What is an article in a magazine? Is it really an Article or a Misc?

Report.6:

:   What is an InProceedings and how does it differ from Conference?

Report.7:

:   What is a Misc?

Report.8:

:   Why are spaces, underscores in directory names problematic and why
    should you avoid using them for your projects

Report.9:

:   Write an objective report about the advantages and disadvantages of
    programs to write reports.

Report.10:

:   Why is it advantageous that directories are lowercase have no
    underscore or space in the name?
