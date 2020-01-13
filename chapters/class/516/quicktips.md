# Quick Tips for the Class

## Requirements

We recommend that you know one programming language. Although most
activities are done in Python, this programming language does not have
to be Python, as it can easily and quickly be learned throughout the
semester. No background in cloud computing is needed.

## Time Commitment

Any class at a university requires a significant time commitment. Due
to the different backgrounds the students have, it is difficult to predict
the actual time needed. On average, we see that students spend 6 hours on
the class if they do participate every week. Students with little
programming experience spend up to 12 hours.

Naturally, you need to balance your course work. If another class has
assignments every week and you do not spend at least 6 hours on this
class, also you will have a hard time with this class. If you spend
less than 6 hours, please, work ahead and do not just spend the 6 hours on another class.

## Course Material List

Course material is distributed as ePubs, PDF, Video, or Presentations.
However, you are required to research some topics on the internet as
Cloud Computing is a rapidly evolving field, and you likely find the
most up to date information on the Web. However, not all information on
the Web is accurate or works. It will be in your responsibility to
filter that information.


Throughout the semester we also ask you to help us updating the ePub and
to use additional resources as appropriate.

The list of resources for the class include:

* [Cloud Computing](https://laszewski.github.io/book/cloud/)[@las19cloudcomputing]
* Introduction to Python [@las19python]
* Linux for Cloud Computing [@las19linux]
* Scientific Writing with Markdown [@las19writing]

Other documents may include:

* Cloud Technologies, Gregor von Laszewski [@las19technologies]
* Project Report Format, Gregor von Laszewski [@e516-report-sample]


## Help

If you take our class, please use Piazza to ask for help. This is
important as different Teaching Assistants may answer questions
(TAs) based on expertise. Please, do not send e-mail to the instructors.
TAs are **not allowed** to answer e-mail send to them personally.
On Piazza always use the send to *instructors* group.

## How to Take this Class

This class is attended by students with greatly different backgrounds
and time schedules. To be most flexible and address all students there
are two different ways on how you can take this class.

* Way 1: *Chronological order.* The lecture notes are ordered
  chronological. Thus you can follow our lecture also in chronological
  order.
  
* Way 2: *Free form.* Here you simply look at the Syllabus table for the
  semester and identity, whatever section you feel like reading (when 
  it becomes available). However, make sure you conduct our weekly **Lab
  activities**.

Please note that we have set aside regular Lab activities. The
activities are pass-fail and will be integrated into your grade. You are
certainly allowed to work ahead, but please be aware that based on
feedback and observation, we may make modifications to the Labs.

Typically,  Lab activities are supposed to be completed within one week
as it alerts us of problems, you might have that we can then address.

Lab activities will not receive any credit if you are a residential
student, and the activity has not been completed within one week.

However, residential students  will get two **Delay a Lab for One
Week** passes that you can apply to any of the Labs and still get credit.

If you are an online student, we recommend that you finish the Labs also
in one week. However, you will get eight **Delay a Lab for One
Week** passes that you can apply to any of the Labs.

Please note that if you would need to postpone a lab for two weeks, you
need to use two passes. Lab passes expire one month before the last day
of class. You will have to complete all the labs at that time. No credit
will be given at that time if this deadline is missed for any delayed
Labs as TAs must focus their attention on project support.

Lab passes do not apply to other assignments and due dates.

## Assignments

Besides the Lab's, we have only a few assignments in this class.
The Lab's will prepare you towards achieving these assignments.

### Technology Review

> *Students doing projects related to Cloudmesh are exempt from writing
> a technology review, but are expected to do more programming and making
> sure the project has a manual and proper documentation.*


As part of cloud engineering, you will be exposed to a large set of
technologies. To sharpen your skills in analyzing and evaluating these
technologies, you will be asked to prepare a to be determined number of
technology reviews that are being added to a class proceeding.

This includes writing a substantial non-plagiarized document that can be
added as a chapter to the lecture notes. The review must be done on a
topic that is not yet included in our book. The review will not include
advertisement statements form those that have developed the technology
but will qualitatively describe the technology and potentially contrast
it to other related technologies. In addition, you will have to develop
an example showcasing how to use the technology. The minimal length of a
review is about 800 words. Others will try out your review and test if
the example works. Your grade will be influenced by the review of other
students. You will also get a grade for the review you provide to other
students. 

An example of such a section is the 

* GraphQL 

in the Cloud Computing book.

Alternatively, you can prepare several different smaller sections (at
least 5) that may not have an example in it but are more of descriptive
nature. Sample sections contributed by students include:

   * Section Microsoft Nafik Data Center in the Datacenter Chapter
   * Section Lambda Expressions in *Introduction to Python*


> ![Warning](images/warning.png) *It is expected from you that you self identify a section
> yourself, as this shows competence in the area of cloud
> computing. If, however, you do not know what to select, you must attend
> an online hour with us in which we identify a topic with
> you. Technologies that are not repeatable due
> to enormous cost or licensing issues need to get prior
> approval.*

This year's technology reviews will center around the use of AI services
from major cloud providers.

### Project

The objective of the project is to define a clear problem statement and
create a framework to address that problem as it relates to multi-cloud
computing and engineering.

A project is the primary activity that you chose as part of your class.
This includes a *project report* or *manual* and working *documented* project code.
You will create a significant non-trivial project related to cloud
computing and cloud engineering. Up to three students can collaborate. The
project could be built on top of a previous project but must have
significant additions or modifications. If a previous project is used, a
detailed discussion is to be held on what has been improved and is different.

In this class, it is especially important to address the reproducibility
of the deployment. A test and benchmark on multiple clouds, possibly
including a downloadable* dataset, must be used to verify the
correctness of your approach.

The project must demonstrate 

1. The use of multiple clouds or cloud services.
2. The implementation of an abstract interface to these clouds or services.
3. The implementation of an OpenAPI Specification and interface.
4. The implementation of an easy deployment. 
5. The implementation of a benchmark.
6. The easy replication of the project from source from your short 
   documentationion  (via the AI's).
7. The integration of the project into Cloudmesh commands. This is super easy.
8. Assume your project has N members then you need to use and 
   provide a testing infrastructure that works on N+1 clouds.


#### License

All projects are developed under an open-source license, such as the
Apache 2.0 License. You are required to add a LICENCE.txt file and
describe how other software if used, can be reused in your project. If
your project uses different licenses, please add a README.md file that
describes which packages are used and what licenses these packages have.

#### Project Report

> For certain projects, the requirement of a report can be waved or is
> significantly reduced while replacing it with more programming
> activities. This includes

> * Any project that enhances Cloudmesh
> * Building a large cloud cluster with Raspberry Pi's 
    (while contributing a manual or a chapter about it)
> * Any Application project showcasing NIST big data reference 
    architecture use.

> However you still have to do a manual and usage examples, benchmarks and
> `pytest`s for them.

For all others the following guideline exists:

A project report is to be delivered and continuously improved throughout
the semester in GitHub. It includes not just the analysis of a topic,
but a short description of the Architecture and code, with
**benchmarks** and demonstrated use. Obviously, it is longer than a term
paper and includes descriptions about the reproducibility of the
application. A README.md is provided that describes how others can
reproduce your project and run it. Remember that tables and figures do
not count towards the paper length. The following minimal length is
required:

*  800 words, one student in the project
* 1200 words, two students in the project
* 1400 words, three students in the project

Projects with more students are expected to do more programming. The
report is written in markdown and checked into GitHub.  The report will
be made available in a class proceeding. A report could be substituted
by a manual and benchmarks upon approval. In this case, a one-page
extended abstract has to be written, which includes the link to the
manual.


#### Project Code

You are expected to deliver a **documented** and **reproducible** code
with unit tests that allows a TA to replicate the project with ease. In
case you use VM or container images, they must be created from **scratch
locally** and may not be uploaded to services such as DockerHub. You
can, however, reuse approved vendor uploaded images such as from ubuntu
or centos or other Linux distributions. All code, scripts, and
documentation must be uploaded to github.com under the class-specific
GitHub directory.

#### Project Data

Data is to be hosted on IU's Google drive if needed. If you have larger
data, it should be downloaded from the internet. It is your
responsibility to develop a download program. The data **must** not be
stored in GitHub. You are expected to write a python program that
downloads the data either from the Web or IU's data storage.

#### Work Breakdown

*Only needed when you have 2 or more members in your team.*

This is a separate document called `breackdown.md` that is included in
your project directory. It describes in a bullet list who did what in
the project. If you are a team of one, such a document is not needed. It
does not count towards the page length of the document. It must include
explicit URLs to the git history that documents the statistics to
demonstrate more than one student has worked on the project. If you can
not provide such a statistic or all check-ins have been made by a single
student, the project has shown that they have not adequately used git.
Thus, points will be deducted from the project. Furthermore, if we
detect that a student has not contributed to a project, we may invite
the student (alone) to an oral presentation of all aspects of the
project, including a live demonstration of the examples in real-time to
determine the project grade. So if you work in a team contribute and do
not have your team members do all your work.

#### Bibliography

All bibliography has to be provided in a BibTex file that **must**
either be validated with **jabref** or with **emacs**. Please be advised
doing references correctly takes some time, so you want to do this early
and throughout the semester. What would take less than 5 minutes a week
could quickly add up to multiple hours at the end of the semester.
Please note that exports of Endnote or other bibliography management
tools do not lead to properly formatted BibTeX files, despite their
claims of doing so. You will have to clean them up, and we recommend to
do it the other way around. Hence, the easiest way to manage your
bibliography is with jabref* or *emacs*. Make sure **labels** only
include characters from [a-zA-Z0-9-]. Use dashes and not underscore and
colons (`_` ,`:`) in the label. Your labels must be meaningful and
unique. We will deduct points if you submit an invalid *BibTex* file to
GitHub. So please make sure your file is validated. You can even create
your own checks with tools such as `biber`.

We will teach you what to do. It is easy.

#### Reproducibility

In general, any project must be deployable by the TAs. If it takes hours
to deploy your project, please talk to us before the final submission.
This should not be the case. Also, if it takes 100 steps to do by hand,
we are sure you can automate them, as you are likely doing something
wrong or have not thought about the engineering aspect of cloud
computing where as we tend to automate most of the steps. A part of your
grade will be how much your project is automated.

The best way to assure reproducibility is to use `pytest`. We will
discuss how to do that in class.

We will teach you what to do. It is easy.


#### List of Deliverables

You have plenty of time to execute a wonderful project, but you need to
work consistently on it. Starting one week before the deadline will
be disastrous.

In general, your deliverables will include the following
(We will address and explain them in a Lab):

* Provide benchmarks.
* Take results in a cloud services and your local PC (ex:
  Chameleon Cloud, echo Kubernetes). Make sure your system can be
  created and deployed based on your documentation.
* Each team member must provide a benchmark on their computer and a
  cloud IaaS, where the cloud is different from each team member.
* We require you to write one or more pytest's that deploys, run,
  kill, view, clean that deploys your environment, runs the application,
  kills it, views the result, and cleans up afterward.
* For python use a requirements.txt file and develop a `setup.py` so
  your code can be installed with `pip install .`
* For docker use a Dockerfile

We will teach you what to do ...

#### Example Outline of a Report

* (If not exempt) write a report that typically includes the following
sections:

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

* Your report will **not** have a *Future Work* section as this implies
   that you will do work in the future, and your paper is incomplete. Hence we would not grade it. Instead, you can use an optional *Limitations*
   section.

* Do communicate your status and add a *Workbreakdown* section in which you outline
  which tasks need to be done and by whom in case of a group
  project. Once you have done a task simply include maker a task as
  follows

  ```* [done, Gregor] This was Gregor's task to showcase how to mark it```

In case you have an exemption for the project report, you need to use
`sphinx` and document your code as part of a manual. We will explain the
details in one of our labs.


## Submission

All submissions are conducted via GitHub if not otherwise instructed.
Technology reviews are to be added to the `book` GitHub repo with the
help of pull requests. The TA's will work with you to integrate them.

As we are working continuously throughout the semester, you must indicate
your activities in a README.yml file in your GitHub repo. The GitHub
Repo, we will define for you in the first 2 weeks of the semester.


An example of the README.yaml file is shown next

```
---
owner:
  firstname: Gregor
  lastname: von Laszewski
  hid: fa18-523-00
  community: i523
  semester: fa18
chapter:
  - keyword: IoT
    title: Role of Big Data in IoT
    url: https://github.com/cloudmesh-community/fa18-523-00/blob/master/chapter1/paper.md
    group: fa18-523-00 fa18-523-01
  - keyword: Datacenter
    title: Green IT data centeres in the US
    url: https://github.com/cloudmesh-community/fa18-523-00/blob/master/chapter2/paper.md
    group: fa18-523-00
project:
  - keyword: Cloud Cluster
    title: Raspberry PI Cloud Cluster
    url: https://github.com/cloudmesh-community/fa18-523-00/tree/master/project-report
    group: fa18-523-00 fa18-523-01
    code: TBD
```

You **MUST** run `yamllint` on the `README.yml` file. YAML errors will
cause point deductions. Any invalid yaml file will result in point
deductions. Please keep your yaml file valid at any time. Our scripts
depend on it. The yaml file will also be used to create a list for TAs
to review your deliverables. If it is not in the YAML file it will not
be reviewed. Please note that it is not sufficient to just run
`yamllint`, but to compare your yaml file carefully with the
`README.yml` examples. Make sure you do the indentation with 2 spaces,
do not use the TAB character and make sure you use the list and
attribute organization with proper dash placement. Work with the TAs if
you have difficulties. If you copy, only copy from the raw content in
GitHub. If you work on more

We will teach you what to do. It is easy.


## Bonus Projects

This class will not have any bonus projects, as all additional
activities should be put in your project or chapter/review contribution.
However, we will recognize extraordinary efforts in these activities.

## Participation

In addition to these artifacts, there will also be a participation
component in class that will be determined based on your productive
contributions to Piazza to help others that have questions and
contributions to the books too, for example, improve sections with
spelling, grammar or content. We can see from the GitHub history if
you conducted such improvements. Make sure that technical
contributions, work on all OSes and are not just targeting a
single OS if the improvement is of general nature (exceptions apply).

## GitHub and Pycharm Markdown

Please be aware that the ePubs use markdown as defined in pandoc.
Neither GitHub nor Pycharm support this version of Markdown. Instead,
they use some enhancements that are not supported. Thus do not assume
that your GitHub will render in our proceedings. We use the most
primitive version of markdown, but use the enhancement for citations and
references in citeproc and citeref. We have a docker image that allows
you to run the version of markdown on your reports and documents.

The TA's will provide you with support on how to do this. It is
trivial.
