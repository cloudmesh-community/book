# Weekly Activities

In case you like to take the class with weekly activities you can look
at the Syllabus table at the sections that are released for a
particular date. The date means the activity is released on that date
and you have time to conduct the activity. Time sensitive items such
as assignment due dates are listed in another table.

:o: add links to sections

Here we list some of the activities by week.

## Week 1: Activities Jan 10 - 17

1. Get familiar with the class and identify if you prefer to take the
   class in free form or in a more guided fashion. Contact us if you
   like to take it in more guided fashion via a private post to
   instructors. you will be able to use these weekly activity
   announcements to proceed. This weekly progress will be updated
   every Friday.

2. Understand that we have only 3 assignments. One of which is a
   significant project. 

3. Download the Lecture notes epub and install an epub reader to read
   the lecture notes. Although we have a PDF version, this version is
   pretty large and will only be updated once a week. See in piazza the
   resource section to locate them

4. Learn piazza and do your bio post. Start a REAME.yml file (look at
   the assignment in piazza). Create a notebook.md file and keep it up
   to date on weekly basis.

5. Make sure to configure a computer on which you can do python 3.7.1.
   If you have not yet installed python we recommend you use pyenv. See
   our notes in the handbook about that. Pyenv allows you to install
   multiple python versions. Answer the question why anaconda is not a
   good version for python in the cloud. Explain why so many other
   courses recommend you to install and use anaconda. Discuss this on
   piazza if you like. If you do not understand this or question this
   attend the online hour. If you have issues with this talk to the TA's.
   
5. Make sure you have a git client installed from which you can
   interact with git. Initially you can just youse a web browser
   Find a spelling or grammar error in the lecture notes and correct
   it via the github.com Web browser while conducting a pull request.
 
6. Make sure to fill out the survey so we can create a github.com
   repository for your project

7. Start reviewing python. Especially do some language features as
   discussed in the notes and write a python module using setup.py and
   requirements.txt. Do a simple print hello world stat you install with
   `pip install .` What is the difference to `pip install -e .` How can
   you leverage this.

Remark: In this class everyon is allowed to help everyone. Each student
will have if they do not participate in a group have a different
assignment so cheating can be avoided. However if we detect that a
student is not doing their work and it is soly delegated to other
students this is considered cheating and and `F` will be assigned.
Please use git commits. It is not sufficient if just one student of a
group commits the entire project in case of group work.

## Week 2: Jan 17 - 25
 
### Development machine

If you have not yet set up a computer with python 3.7.1 on it please
do so. Remember you can use virtual machines and use virtualbox so you
do not interfere with your base system or use a USB stick to boot into
ubuntu .... If you do not have a system work with the TAs to identify
a solution that works for you

### Data Center

Please look at the data center section (see @#sec:data-center) and
read it. There are plenty of opportunities to contribute. Announce in
piazza if you work on a section so we minimize duplication of effort.
Data Center

#### Datacenter Table

Find concrete evidence for data centers from industry and
  complete the table with the many question marks as much as possible.
  As the information may change over time, please include a year for
  which the data is valid, we may need to add a year column.

#### Data Center sections

As we got already some positive feedback about
this section, I added some additional opportunities for more sections
that can even evolve to a chapter if you like to focus on this.

#### Datacenter Exercises

Some of you asked what Exercises they can do for this week to do some
work bejond reading the section.

We suggest you do 

* E.Carbon.2 (see @sec:operation-impact)
* E.Energy.1 (see @sec:exercises-energy)
* E.Energy.2 (see @sec:exercises-energy)

### Remarks: Sections 

Although it is sufficient to just read the chapter we provide, its fun
to do some google searches including just to look at images ... If you
see something you think we should add, propose a new section if you
like. Please remember that you will need to do some sections that will
be graded. We recommend that you contribute at least 5 sections. This
is equivalend to one section every three weeks which is actually not
much. Typically you will spend the first week reseraching and writing
a draft. The second week experimention or creating an example if
applicable and the thrird week you will engage with other students and
the TAs on reveiws and improvements if needed. 

### Python till rest of the semester
 
Python 3.7.1: Set up a computer on which you can execute python 3.7.1.
Some did not complete that taks yet (see @sec:python-install,
@sec:python-intro, @sec:python-language).

Review Python: start reviewing python. See our handbook. Some of the
chapters are not that important and can be skipped. Focus on classes,
modules, basic language things. learn about pip (possibly from google)
learn how to write requirements.txt and setup.py for your own programs
use pycharm for program development, configure it so it uses python
3.7.1 when executing the python programs do it in a terminal not from
within pycharm (see @sec:python-editors).

We recommend that you install pycharm and use it. We have simple
videos in the python section that showcases this.

You do not have to do some of the more advanced python concepts. Focus
initially on the language and learn how to do classes as this will be
extreamly helpful. 

## Week 3: Jan 25 - Feb 1

### Cloud Architectures

This week we will focus on archie=tectural definitions of cloud
computing. We like that the class engages in a discussion about a very
short definition of *cloud computing* and *mainframes* in piazza.
We will jointly develop an asnwer and add it to the handbook at the
spots marked with a red circle.

Read the sections:

* Architectures (see @sec:cloud-architectures)
* NIST Big Data Reference Architecture (see @sec:nist-bdra)

Students and TA's please complete the red cicles, e.g. mostly bibtex refernces.

### REST services

Read the REST Service section. THi section includes some parts that
are not that relevant for this class and we llike you to focus on
in @sec:rest on the sections

* Overview
* OpenAPI REST Services with Swagger (see @sec:swagger)
* OpenAPI Specification (see @sec:openapi-spec)
* OpenAPI REST Service via Introspection (see sec:openapi-introspection)

YOu do not in thi class need to look at the other Sections about REST,
however, if you like to you can. For the project, all projects will be
using for REST services the framework used in
sec:openapi-introspection.

## Week 4: Feb 1 - Feb 8

### Github as REST service

Read:

* Github REST Services (@sec:Github-REST)

Recommended:

* Do E.github.issues.6 as this is directly relevant for your projects
  and can be generalized to other REST services.

Optional:

* Do excersise E.github.issues.5:

:warning: The week 4 is under construction and additional items will
be added

### Practical OpenAPI

Develop an OpenAPI service with not trivial functionality that uses
GET, PUT, PATCH and other functions. Make sure to properly secure it.
Explore the use of MongoDB as database (MongoDB will be used in your
REST services, so it may take some time to master this). We will
provide additional material throughout the semester on this. So this
task may take multiple weeks and may overlap with your project. Get
started early.

