# Assignments

We have three graded assignments all other activities are geard towards
supporting these assignments. The assignments are created in such a
way that they could (but do not have to or may not) support your class project. 
The assignments are posted in piazza in the `assignments` folder.

Besides the account creation you will have the following assignments:

* Section contributions
* Chapter contributions
* Project

We will introduce you to more details next.


## Account Creation

As setting up your computer is not really an assignment but a
precondition, we do not grade you on this. Furthermore posting the Bio
is not such a complex task and serves not only to showcase us that you
have access to Piazza and can post to it, but also allows you to let
others in the class to know them about you which may be helpful for
finding a project partner.

As part of the class you will need a number of [accounts]{.index}

* piazza.com (used for communication)
* github.com (used for project and other class artifacts)
* futuresystems.org (free docker account)
* chameleoncloud.org (free cloud account)
* google.com (optional)
* aws.com (optional)
* azure.com (optional)
* Watson from IBM (optional)
* google Iaas (optional)

A survey is to be filled out in the first week of class. It includes
your github.com account that we need to create your github directory
in which you will submit your open source project.

## Sections, Chapters with Examples

As part of the class, we expect you to get familiar with topics
related to cloud computing beyond what we have written in the lecture
notes. This is done in Sections, Examples, and Chapters. These
assignments are done so you do not have to do other weekly homework or
tests. They showcase your understanding of the field.

**Section:**

: A section is a small section that explains a topic that is not yet
  in the handbook or improves an existing section significantly. It is
  typically multi-paragraphs long and can even include an example if
  needed. Sections can be theoretical, or programming related
  sections.
  Typically an A+ student contributes more than 5
  such sections. 

:  Sample sections contributed by students include:

   * The  Microsoft Nafik  data center :o: add link, see Table of
     content for now.
   * [Lambda Expressions](#lambda-expressions)

**Chapter with Example:**

: A chapter is a much longer topic and is a coherent
  description of a topic related to cloud computing. A chapter could
  either be a review of a topic or a detailed technical
  contribution. Several Sections (10+) may be a substitute for a
  chapter.
  You will be contributing a unique **significant** chapter that can be used
  by other students in the class and introduces the reader to a
  general topic related to the topic of the class. 
  You will create a unique non existing chapter that can be shared
  with other students of this class. Chapters can be theoretical, but
  most often students prefer the creation of practical
  contributions.  When doing a practical section, it is
  expected to develop a practical example demonstrating
  how to use a technology. The chapter and the practical example can
  be done together. We do not like to use the term tutorial in our
  writeup but sometimes we refer to it in our assignments as
  such. Chapters that focus on theory may not have an example and it
  can be substituted by a longer text. In case no example is provided
  the example can be substituted in some cases by a review.

  An example is a document that showcases the use of a
  particular technology. Typically it is a console session or a
  program. Examples augment Chapters as well as Sections.

:  A sample of a student contributed chapter is * [GraphQL](#s-graphql).


:warning: It is expected from you that you self identify a section
or a chapter as this shows competence in the area of cloud
computing. If however you do not know what to select, you must attend
an online hour with us in which we identify sections and chapters with
you. The emphasize here is that we do not decide them for you, but we
identify them **with** you.

Sample Topics that could form a section or chapter are clearly marked
with a :question: or a :o:. There are plenty in the handbook, but you are
welcome to define your own contributions. Discuss them with us in the
online hours. To guarantee that they are unique and others know about
it you will file a github issue for it once it is approved by us via a
discussion either in an online hour or piazza.

## Mini Projects that could Substitute a Chapter 

In some special cases it is possible to substitute the chapter and/or
section contributions with an additional mini project, that however
still has to be documented. An example fo such a mini project is our 
`cm-burn` command that creates Raspberry PI OS based on
manipulation of the file system

* <https://github.com/cloudmesh-community/cm-burn>
* <https://github.com/cloudmesh-community/cm>

Please note that this is not less work than developing a chapter
and/or sections. You still will have to do a class project as the mini
project does not substitute the class project.

A mini project may be related to topics such as:

* Raspberry PI 
* Sechi Disk Partial Image Analysis
* NIST OpenAPI definition and implementation

Mini projects must be suggested and approved by Dr. Gregor von Laszewski.

## Project

Project

:  You will create a significant non trivial project related to cloud
   computing and cloud engineering. Up to three people can
   collaborate. The project could be build on top of a previous
   project but must have significant additions or
   modifications. If a previous project is used a detailed discussion
   is to be held of what has been improved. We will discuss projects
   in one of our future lectures. There are aa lot of examples in our
   other class publications.


Project:

: A project is the major activity that you chose
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

  -   6 pages, one student in the project
  -   8 pages, two students in the project
  -   10 pages, three students in the project

  Please note that the format will be markdown, so the word
  count will be used instead.
  We estimate that a single page is between 1000-1200 words in ePub format.
  How to use figures is explained in the
  Section Notation of the handbook. We use bibtex for bibliographies.

  We will at a later time describe how and weher the project code and
  report is stored.

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

: All bibliography has to be provided in a bibtex file that **MUST**
    either be validated with **jabref** or with **emacs**. There
    is **NO EXCEPTION** to this rule. Please be advised doing
    references right takes some time so you want to do this
    early. Please note that exports of Endnote or other bibliography
    management tools do not lead to properly formatted bibtex files,
    despite they claiming to do so. You will have to clean them up and
    we recommend to do it the other way around. The easies is to manage your
    bibliography with jabref. Make sure **labels** only include characters
    from [a-zA-Z0-9-]. Use dashes and not underscore and colons (`_` ,`:`) in the
    label. We will deduct points if you submit an invalid bibtex file
    to github. So please make sure your file is validated. You can
    even create your own checks with tools such as biber.

### Project Deliverables

The objective of the project is to define a clear problem statement
and create a framework to address that problem as it relates to cloud
computing. In this class it is especially importnat to address the
reproducibility of the deployment. A test and benchmark possibly
including a dataset must be used to verify the correctness of your
approach. Projects related to NIST focus on the specification and
implementation. The report here can be smaller, but the contribution
must be includable in the specification document.

In general any project must  be 
deployable by the TA. If it takes hours to deploy your project, please
talk to us before final submission. Also if it takes 100 steps, we are
sure you can automate them ...

You have plenty of time to execute a wonderful project but you need to
work consistently on it. Starting one week before the deadline will
not work. 

The deliverables include but need to be updated according to your
specific project, for example if you do Edge Computing some
deliverables will be different. In general your deliverables will
include the following:

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

- For python use a requirements.txt file also, develop a setup.py so
  your code can be installed with `pip install .`

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

* Your paper will not have a *Future Work* section as this implies
   that you will do work in future and your paper is incomplete, instead
   you can use an optional "Limitations" section.

* Do communicate your status add a *Todo* section in which you outline
   in pulled form which tasks need to be done, once yo u have done it
   remove it from the todo list. 

## Project: Virtual Cluster

All students can contribute and participate on the creation of the
Virtual Cluster software project that we will be using throughout the
class to improve and interface with cloud and container frameworks.
This project is managed at

* <https://github.com/cloudmesh-community/cm>

Residential students will work on this project and meet in a
discussion group to work on it while having weekly assigned tasks they
define with us. Online students are welcome to join this project and
their tasks will be discussed in online hours, also here you will need
weekly time to work on it.  Online students that are in the
Bloomington area, are welcome to join our residential meetings (Please
contact Gregor via piazza).

Work on cloudmesh cm4, cm-burn or the NIST REST Specification document
can reduce the project report deliverable (in size) while substituting
it with a **significant** larger programming contribution.

* In case of cm4 we will write collaboratively a report
* In case of cm-burn we will work on a report that we publish in the
  Raspberry community
* In case of NIST you will be expected to contribute to the NIST
  Specification.

In addition to interfacing with clouds via an API, we are also
interested to display the interactions in Javascript. So if you have
Javascript skills this may be a good opportunity for you to contribute
to the project with your previous knowledge. 


## Submission of sections and chapters and projects

Sections and subsections are to be added to the `book` github repo. Do
a pull request. Initially they will be managed in your own github repo
that we will set up for you. Only after they have been reviewed and
are approved they may be added to the book, 

The headline of the section needs to be marked with a
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
group: fa18flys-523-62 fa18-523-69
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
give point deductions. Any invalid yaml file will result in point
deductions. Please keep your yaml file valid at any time. Our scripts
depend on it. The yaml file will also be used to create a list for TAs
to review your deliverables, If its not in the yaml file it will not
be reviewed.

More details will be posted throughout the semester.

## Participation 

In addition to these artifacts, there will also be a participation
component in class that will be determined based on your productive
contributions to piazza to help others in case of questions and
contributions to the books to for example improve sections with
spelling, grammer or content. We can see from the github history if
you conducted such improvements. Make sure that in case of technical
contributions, they do work on all OSes and are not just targeting a
single OS if the improvement is of general nature (exceptions apply).

