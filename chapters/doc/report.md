Report Format
-------------

We provide a uniform **trivial high quality** report format for this
class that is slightly modified from its original. This was necessary
as we observed over the years that some students increased their paper
length while modifying the format or added empty lines, played with
font sizes and so on. This is all not necessary and wastes not only
your time, but also the reviewers time. We just use all the same
unchanged uniform paper format. As we do such cheating attempts are
easy to detect.

To avoid all this, we have adopted a the following simple **proven**
approach implemented by hundreds of students successfully.

1.  We provide you with a **high quality** report template format that
    you **must not change**. It is a slight improvement to a template
    that is used by millions of researchers.

2.  All references must be managed with **jabref** or **emacs** as
    reference management tool and must be provided in addition to the
    document.

3.  If your document does not follow the format or we find that you have
    modified the template or do not use floating figures (which will be
    placed automatically at the end of the paper) we will return the
    document without review and may give a grade reduction.

4.  It is in the students responsibility to use the template format from
    the beginning on.

5.  If you treat our template simply as a form that you fill out, you
    will succeed. If you modify it you will not. Keep it simple.

The template for the report is available from:

-   <https://github.com/cloudmesh-community/hid-sample/tree/master/paper>

Copy all files from this directory in the directory where you want to
write your report in. Make sure you have the **full** version of LaTeX
installed and can use make. This can be done on macOS, Linux, and Windows
via gitbash. When you say

    make

the document will be created and is called

    report.pdf

However, when submitting the report you just need to submit the
following files and directories with their files in it

    Makefile
    content.tex
    report.bib
    images

You **MUST NOT** commit your pdf file as we will regenerate it for you
as part of a class proceedings. If you commit it, it will lead to
conflicts in git and will slow us down and we will deduct points if
you commit it. Here are some useful tips to what is in the directory:

Images

:   All images must be placed in an images folder and submitted in your
    repository with the originals.

Makefile

:   It is in your responsibility that the document can be compiled with
    make. If your system can not do this, create one that can. Use a
    virtual machine or containers if you fail to set it up on Windows.
    As this is a cloud class this part of your class deliverables as it
    shows to us you can set up such an environment. There will be **NO
    EXCEPTION** to this. This file must not be modified.

context.tex

:   This is your form. Look at it and fill it out with your content. See
    especially how images and tables are placed and referred to.
    Although they will in your context.tex file be close to where they
    should be in our review process we place them on purpose to the end.
    You will see this when you say make and view the pdf document,

report.tex

:   This file must not be modified.

### Parallel Editing

In most cases you will be able to work in groups on class
projects. This allows you to develop the report collaboratively via
github.com.  Learning how to do this properly is part of the class
goals. The rule is commit and pull frequently. The reason we want you
to use git directly is also to prepare you for parallel code
development. Thus we do not encourage using of sharelatex and
overleaf. Instead we recommend you use git directly and communicate
with each other in case yo work in a team.

### Time management

Obviously doing a project takes time

1.  It takes time to read the information
2.  It takes time understand the information
3.  It takes time to do the project
4.  This will get you in trouble: *There are still 10 weeks left till
    the project is due so let me start in 4 weeks ...*. Postponing the
    project till the last moment
5.  Do not spend significant time on unimportant documentation and
    setup. Instead spend time to develop sophisticated scripts that
    you can than easily document in possibly one line ;-) If you can
    use for example cloudmesh cmd5 commands and scripts that help you
    developing commands semi-automatically.

### Report Checklist

This partial list may serve as a reminder on how to make sure your
paper is properly developed. It is based on a collection of issues we
observed over time done by students developing reports.

1.  Have you written the report in the specified format?

2.  Have you included an acknowledgement section?

3.  Have you included the report but not report.pdf in git?

4.  Have you specified the HID, names, and e-mails of all team members
    in your report. E.g. the Real Names that are registered in Canvas?

5.  Have you included the project number in the report?

6.  Have you included all images in native and PDF format in git in the
    images folder?

7.  Have you added the bibliography file that you managed with jabref or
    emacs

8.  Have you made sure that you removed report.pdf in case you
    accidentally added it to github

9.  Have you added an appendix describing who did what in the project or
    report? (only needed when you worked in a team)

10. Have you spellchecked the paper?

11. Are you using **a** and **the** properly?

12. Have you made sure you do not plagiarize?

13. Have you not used phrases such as shown in the Figure below, but
    instead used as shown in Figure \ref{F:coolfigure} when referring to
    the figure, and F:coolfigure is set with the label command?

14. Have you capitalized "Figure ...", "Table ..." ?

15. Any figure that is not referred and explained explicitly in the text
    must be removed.

16. Are the figure captions bellow the figures and not on top. (Do not
    include the titles of the figures in the figure itself but instead
    use the caption or that information?

17. When using tables have you put the table caption on top?

18. Make the figures large enough so we can read the details. If needed
    make the figure over two columns?

19. Do not worry about the figure placement if they are at a different
    location than you think. Figures are allowed to float.

20. Do avoid copy images from others as this would require you to
    contact the publisher and ask for permission. Redraw the figure, but
    use a citation if the figure is not substantially different.

21. Do not use the word "I" instead use "We" even if you are the sole
    author.

22. Do not use the phrase "In this paper/report we show" instead use "We
    show". It is not important if this is a paper or a report and does
    not need to be mentioned.

23. Do not artificially inflate your report if you are bellow the page
    limit and have nothing to say anymore.

24. If your paper limit is 12 pages but you want to hand in 120 pages,
    please check first with an instructor ;-)

25. Check in your current work for the report on a weekly basis to show
    consistent progress.

26. Please use the dedicated report format for class.

27. Do not use the characters & \# % in the paper. If you use them you
    probably need a  in front of them.

28. If you want to say and do not use *&* but use the word *and*.

29. When writing quotes use \`\`quote'' and not "quote".

30. **Do not** include a section *Future improvements* as this implies
    you want an incomplete. Instead use a section Limitations and
    discuss them in detail.

31. Have another student review your paper and give you feedback.

32. Do a self check. Do you think this paper is excellent or do you
    think its just good enough? What are the limitations of the paper?

33. When using directory names use only lower case, do not use spaces or
    underscore in them. Use a dash instead of underscores.

34. bibtex labels **must not have underscores** in them, instead use
    dashes.

35. Make sure to add your hid as a prefix to the bibtex label.

36. howpublished does not contain urls, for that we use a url attribute.
    IN how published you put a noun in that describes what it is. E.g.
    Webpage, Git repository, ...

### Exercise

Report.1:

:   Install emacs, latex and jabref on your system

Report.2:

:   Check out the report example directory. use make and view the PDF.
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

Report.11:

:   Review in a grammar book proper usage of "a" and "the".

Report.11:

:   Memorize: When writing quotes use \`\`quote'' and not "quote". Note
    these are two quotes let to the one to open and two other quotes
    right to the enter (US keyboard) to close a quote.
