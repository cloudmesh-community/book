# Assignments

For more details see the course syllabus and overview pages. We give
here just some summary.

## Account Creation

As part of the class you will need a number of [accounts]{.index}

* piazza.com
* github.com


Optional accounts include (only apply for them if you know you need
them.  Note that applying for some accounts may take 1 - 2 weeks to
complete, you should have identified before the middle of the semester
if you need some of them.

* futuresystems.org (optional)
* chameleoncloud.org (optional)
* aws.com (optional)
* google.com (optional)
* azure.com (optional)
* watson from IBM (optional)
* google Iaas (optional)

In our piazza we have details how to submit them to us. We split the
submission in multiple sub-assignments as the github.com and piazza.com
are needed within the first week.


## Sections, Chapters, Examples

As part of the class, we expect you to get familiar with topics
related to intelligent systems engeneering. Thos that like to go for
an A+ are also expected to contribute significantly to this document
or have a truly outstanding project.  This is done in Sections,
Examples, and Chapters, or excelent Project reports and code.
 
**Section:**

: A section is a small section that explains a topic that
  is not yet in the handbook or improves an existing section
  significantly. It is typically multi-paragraphs long and can even
  include an example if needed. Example sections that have been
  provided are for example the Lambda section in the python chapter

:  Sample of student contributed sections include:

   * [Project Natic](#S:natick)
   * [Lambda Expressions](#lambda-expressions)

:o: please fix links

**Chapter:**

: A chapter is a much longer topic and is a coherent
  description of a topic related to cloud computing. A chapter could
  either be a review of a topic or a detailed technical
  contribution. Several Sections (10+) may be a substitute for a
  chapter.

: You will be contributing a **significant** chapter that can be used
  by other students in the class and introduces the reader to a
  general topic related to the topic of the class. In addition it is
  expected if applicable to develop a practical example demonstrating
  how to use a technology. The chapter and the practical example can
  be done together. We do not like to use the term tutorial in our
  writeup but sometimes we refer to it in our assignments as
  such. Chapters that focus on theory may not have an example and it
  can be substituted by a longer text.

:  A sample of a student contributed chapter is * [GraphQL](#s-graphql).

**Example:**

: An example is a document that showcases the use of a
  particular technology. Typically it is a console session or a
  program. Examples augment chapters and Sections.


:warning: It is expected from you that you self identify a section
or a chapter as this shows competence in the area of cloud
computing. If however you do not know what to select, you must attend
an online hour with us in which we identify sections and chapters with
you. The emphasize here is that we do not decide them for you, but we
identify them with you.

Sample Topics that could form a section or chapter are clearly marked
with a :question:. There are plenty in the handbook, but you are
welcome to define your own contributions. Discuss them with us in the
online hours.

A list of topics identified by students is maintained in a spreadsheet.

See <https://piazza.com/class/jgxybbf5rnx5qd?cid=201> for details.

You are expected to signup in this spreadsheet. THis is done to 
ab=void overlap and foster uniqueness of the assignment for sections 
and chapters. 

## Project

Project:

: We refer with the term project to the major activity that you chose
  as part of your class. The default case is an implementation project
  that requires a *project report* and project code.

License:

: All projects are developed under an open source license such as
  Apache 2.0 License. You will be required to add a LICENCE.txt file
  and if you use other software identify how it can be reused in your
  project. If your project uses different licenses, please add in a
  README.md file which packages are used and which license these
  packages have.
    
Project Report:

: A project report is an enhanced topic paper that includes not just
  the analysis of a topic, but an actual code, with **benchmark** and
  demonstrated application use. Obviously it is longer than a term
  paper and includes descriptions about reproducibility of the
  application. A README.md is provided that describes how others can
  reproduce your project and run it. Remember tables and figures do
  not count towards the paper length. The following length is
  required:

  -   4 pages, one student in the project
  -   6 pages, two students in the project
  -   8 pages, three students in the project

  We estimate that a single page is between 1000-1200 words.
  Please note that for 2018 the format will be markdown, so the word
  count will be used instead. How to use figures is explained in the
  Notation of the handbook. We use bibtex for bibliographies. Please
  be reminded that images and tables as well as code is excluded from
  the page length. Make sure that your text is mostly developed by
  midterm time. 

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

: All bibliography has to be provided in a jabref/bibtex file. There
    is **NO EXCEPTION** to this rule. Please be advised doing
    references right takes some time so you want to do this
    early. Please note that exports of Endnote or other bibliography
    management tools do not lead to properly formatted bibtex files,
    despite they claiming to do so. You will have to clean them up and
    we recommend to do it the other way around. Manage your
    bibliography with jabref. Make sure labels only include chracters
    from [a-zA-Z0-9-]. Use dashes and not underscore or : in the label.

### Project Deliverables

The objective of the project is to define a clear problem statement
and create a framework to address that problem as it relates to cloud
computing. In this class it is especially importnat to address the
reproducibility of the deployment. A test and benchmark possibly
including a dataset must be used to verify the correctness of your
approach. Projects related to NIST focus on the specification and
implementation. The report here can be smaller, but the contribution
must be includable in the specification document.

In general any project must be deployable by the TA. If it takes hours
to deploy your project, please talk to us before final submission.

You have plenty of time to make execute a wonderful project.

The deliverables include but need to be updated according to your
specific project, for example if you do Edge Computing some
deliverabl;es will be different:

- Provide benchmarks.

- Take results in two different cloud services and your local PC (ex:
  Chameleon Cloud, echo kubernetes). Make sure your system can be
  created and deployed based on your documentation. 

- Each team member must provide a benchmark on their computer and a cloud IaaS, 
  where the cloud is different from each team member.

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
  * Design
    * Architecture
  * Implementation
    * Technologies Used
  * Results
    * Deployment Benchmarks
    * Application Benchmarks
  * (Limitations)
  * Conclusion
  * (Work Breakdown)

- Your paper will not have a *Future Work* section as this implies
  that you will do work in future and your paper is incomplte, instead
  you can use an optional "Limitations" section.

### Project Topic

As part of this class you will be developing a OpenAPI based
Artificial Intelligence REST service and demonstrate its use. YOu will
be developing a documentation and a report that showcases the use of
the service. The OpenAPI service must be non trivial, e.g. you shoudl
show upload of data, sbmission of parameters including the function to
be executed, potential development of a GUI for the service.

We will work with you to solidify the project throughout the semester.



## Alternate Project: Virtual Cluster

All students can contribute to the creation of the Virtual Cluster code
that we will be using throughout the class to improve and interface
with cloud and container frameworks. This project is typically done in
a graduate class, but interested undergraduates can contribute
also. Those that like to contribute must have significant programming
experience in either Python or Javascript. This project could replace
the regilar AI REST service project. A weekly meeting and demonstrated
progress has to be shown to Gregor von Laszewski.

* <https://github.com/cloudmesh-community/cm>

The residential students have been assigned this task, but online
students can join and contribute.

## Alternative Project: 100 node Raspberry Pi cluster.

In this project you will be developing a 100 node Raspberry PI
cluster. THis includes putting the hardware together, and developing
software that allows to uses all 100 nodes as a cluster. Software is
to be use to make management easiy. It is not sufficient to just
install the software but to develop a framework that allows us to
easily share this resource with other users.

A documentation has to be written for this project so others can
replicate your cluster build. A good start for this is to look at 
our  `cm-burn` command that creates Raspberry PI OS based on
manipulation of the file system

* <https://github.com/cloudmesh-community/cm-burn>
* <https://github.com/cloudmesh-community/cm>

Substantial contributions are expected beyond the hardware build. We
also like to design a case with a Laser cutter for the 100 nodes.
Building the cluster would take place in MESH and transportation to
and from it is provided by the university. You will be able to work in
an office there to put the cluster together. A weekly meeting with
Gregor von Laszewski or the TAs is needed to showcase progress.

## Submission of sections and chapters and projects

Sections and subsections are to be added to the `book` github repo. Do
a pull request.  The headline of the section needs to be marked with a
:hand: if you still work on it, marked with a :smiley: if you want it
to be graded. and have all hids for people that contribute to that
section.

In addition, simply add them to your README.yml file in your github repo.
Add the following to it (I am using a18-516-18 as example). 

Please look at <https://github.com/cloudmesh-community/fa18-516-18> and <https://raw.githubusercontent.com/cloudmesh-community/fa18-523-62/master/README.yml>
for an examples. Please note that in case you work in a group the code and report is supposed to be only stored 
in the first hid mentioned in the group field. If you store it in multiple directories your project will be rejected.

    section:
        - title: title of the section 1
          url: https://github.com/cloudmesh-community/book/chapters/...
        - title: title of the section 2
          url: https://github.com/cloudmesh-community/book/chapters/...    
        - title: title of the section 3
          url: https://github.com/cloudmesh-community/book/chapters/...         
    chapter:
        - title: title of the chapter
          url: https://github.com/cloudmesh-community/fa18-516-18/blob/master/chapter/whatever.md
          group: fa18-523-62 fa18-523-69
          keyword: whatever
    project:
        - title: title of the project
          url: url in your hid space or that of your partner
          group: fa18-523-62 fa18-523-69
          keyword: kubernetes, NIST, Database
          code: the url to the code
    other:
        - activity: spell checked md document
          url: put url here


You **MUST** run yamllint on the README.yml file. YAML errors will
give point deductions

