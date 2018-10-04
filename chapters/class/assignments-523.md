# Assignments 

## Due dates

For due dates see the [calendar](#calendar) section.

## Terminology

Dependent on the class you need to do different assignments. The
assignments will be clearly posted. In case of questions, we will
update this document to provide clarifications if needed. We use the
following terminology:

License:

:   All projects are developed under an open source license such as
    Apache 2.0 License. You will be required to add a LICENCE.txt file
    and if you use other software identify how it can be reused in your
    project. If your project uses different licenses, please add in a
    README.md file which packages are used and which license these
    packages have.
    
Sections:

: Sections are written in markdown and include information on a
  particular technical issue that is in general helpful for other
  students. Sections must be about a substantial topic and include an
  introduction a section that teaches a reader a significant issue, as
  well as practical code examples. Multiple small sections can lead
  to a substantial contribution. We expect that the sections are of
  high quality and can be included in our handbooks. Please be careful
  of plagiarism and do not just copy the sections from tutorials or code or from
  elsewhere.

Technology or Review Paper :

: A technology paper is a summary paper about a technology,
  application, or topic that is not yet covered in other technology
  papers delivered by previous students of this class. A review paper
  is a paper that reviews a specific topic related to this class.
  
  In either case includes useful information that provides an overview
  of what you are trying to describe and analyses its relationship to
  the class topic. Be mindful about plagiarism. The paper is written
  in LaTeX or Markdown and uses bibtex for bibliography management. It
  uses the same format as your report paper. The format is discussed
  in the Section [Report Format](#report-format).

  A technology paper is 2 pages long. This will make it between 2000-2400 words. 
  
  Note: that for the 2018 we decided to just us Markdown and not LaTeX.
  We will calculate the exact number of words needed.
  
Project:

: We refer with the term project to the major activity that you chose
  as part of your class. The default case is an implementation project
  that requires a *project report* and project code. In case you have
  issues with code development you can also chose a *term paper* as
  project.


Term Paper:

: A term paper is an enhanced topic paper (only available for
  I523). The difference is in length and depth of
  coverage. Comparative or review papers can also become term papers. In
  case you chose the term paper, you or your team will pick a topic
  relevant for the class.  Term papers should have the quality to be
  publishable either in a workshop or as part of the handbook. Not all
  classes allow you to do a term paper, but require you to do a
  project. Please confirm with your class. For the classes listed here
  the term paper wil result in a quarter reduction in grade for the
  entire class not just the paper. Remember tables and figures do not
  count towards the paper length. A term paper has the following
  length.

  -   8 pages, one student in the project
  -   10 pages, two student in the project
  -   12 pages, three student in the project

  We estimate that a single page is between 1000-1200 words.
  Please note that for 2018 the format will be markdown, so the word
  count will be used instead. 
  
Project Report:

: A project report is an enhanced topic paper that includes not just
  the analysis of a topic, but an actual code, with **benchmark** and
  demonstrated application use. Obviously it is longer than a
  term paper and includes descriptions about reproducibility of
  the application. A README is provided that describes in sectione 
  how others can reproduce your project and run it.  Term papers
  should have the quality to be publishable either in a workshop or as
  part of the handbook. The format is discussed in the Section
  [Report Format](#report-format).  Remember tables and figures do not
  count towards the paper length. The following length is required:

  -   6 pages, one student in the project
  -   8 pages, two students in the project
  -   10 pages, three students in the project

  We estimate that a single page is between 1000-1200 words.
  Please note that for 2018 the format will be markdown, so the word
  count will be used instead. 

Project Code:

: This is the **documented** and **reproducible** code and scripts
  that allows a TA do replicate the project. In case you use images
  they must be created from scratch locally and may not be uploaded to
  services such as dockerhub. You can however reuse vendor uploaded
  images such as from ubuntu or centos. All code, scripts, and
  documentation must be uploaded to github.com under the class
  specific github directory.

Data:

:   Data is to be hosted on IUs google drive if needed. If you have
    larger data, it should be downloaded from the internet. It is in
    your responsibility to develop a download program. The data **must**
    not be stored in github. You will be expected to write a python
    program that downloads the data.



Work Breakdown:

:   This is an appendix to the document that describes in detail who did
    what in the project. This section comes in a new page after the
    references. It does not count towards the page length of the
    document. It also includes explicit URLs to the git history that
    documents the statistics to demonstrate not only one student has
    worked on the project. If you can not provide such a statistic or
    all check-ins have been made by a single student, the project has
    shown that they have not properly used git. Thus points will be
    deducted from the project. Furthermore, if we detect that a student
    has not contributed to a project we may invite the student to give a
    detailed presentation of the project.

Bibliography:

:   All bibliography has to be provided in a jabref/bibtex file. This is
    regardless if you use LaTeX or Word. There is **NO EXCEPTION** to
    this rule. Please be advised doing references right takes some time
    so you want to do this early. Please note that exports of Endnote or
    other bibliography management tools do not lead to properly
    formatted bibtex files, despite they claiming to do so. You will
    have to clean them up and we recommend to do it the other way
    around. Manage your bibliography with jabref, and if you like to use
    it import them to endnote or other tools. Naturally you may have to
    do some cleanup to. If you use LaTeX and jabref, you have naturally
    much less work to do. What you chose is up to you.


### Project Deliverables

The objective of the project is to define a clear problem statement and
create a framework to address that problem as it relates to big data
your project must address the reproducibility of the deployment and
the application. A dataset must be chosen and you can analyze the
data. YOu must make sure your project can be deployed on the TAs
computer through scripts that make your project reproducable.

You have plenty of time to make this choice and if you find you
struggle with programming you may want to consider a term paper
instead of a project.

In case you chose a project your maximum grade for the entire class
could be an A+. However, an A+ project must be truly outstanding and
include an exceptional project report. Such a project and report will
have the potential quality of being able to be published in a
conference or workshop/

In case you chose a term paper your maximum grade for the
*entire* class will be an A-.


##### Deliverables 

- Find a data set with reasonable size (this may depend on your
  resources and needs to include a benchmark in your paper for
  justification).

- Clean up the data set or make it smaller or find a bigger data set

- Identify existing algorithms and tools and technologies that you can
  use to analyze your data

- Provide benchmarks.

- Take results in two different cloud services and your local PC (ex:
  Chameleon Cloud, echo kubernetes). Make sure your system can be
  created and deployed based on your documentation. 

- Create a Makefile with the tags deploy, run, kill, view, clean that
  deploys your environment, runs application, kills it, views the
  result and cleans up after wards. You are allowed to have different
  makefiles for the different clouds and different directories. Keep
  the code and directory structure clean and document how to reproduce
  your results.

- For python use a requirements.txt file also

- For docker use a Dockerfile also 

- Write a report that includes the following sections

  * Abstract
  * Introduction
  * Architecture
  * Implementation
    * Technologies Used
  * Design
  * Implementation
  * Results
    * Deployment Benchmarks
    * Application Benchmarks
  * (Limitations)
  * Conclusion
  * (Work Breakdown)

- Your paper will not have a future work section as this implies that
  you will do work in future, instead you can use an optional
  limitations section.
