# Week 3: Cloud Computing Architectures

Goals:
   
* Start of Chapter Selection  
* Start of Project Selection
* Review Python
* Use cloudmesh-installer
* Generate a command with cms sys

## Lecture Material

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/e516/) [@las19e516]
* [Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]
* [Introduction to Python for Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/python/) [@las19python]

Reading Assignments:

1. Read in the book [Cloud Computing](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing] the chapter about Cloud Architectures.
2. Read in the book [Introduction to Python for Cloud Computing](https://laszewski.github.io/book/python/) [@las19python] the chapter about the Python langugae
3. Focus on refreshing your python knowledge about lists, set, dict, and classes.
4. Deadlines in the [e516 Lecture Notes Engineering Cloud Computing](https://laszewski.github.io/book/e516/) [@las19e516] were updated.

## Lab Activities

You should have set up in the first week of the class set up python 3.10.4
on your computer. If you have not yet done so, please do. We recommend
that you use python from python.org. 

We found out over the last two weeks that some students rely on anaconda
for other classes but do not know how to use it in anaconda a virtual env. Please find out.
 
If you can not, we found it may be easier to create for this class a
different user as your other teachers may have given you wrong
instructions on how to install python or anaconda. To avoid this, you
may just start fresh in a new user and do this class in that user. Make
sure the user has administrative privileges.

E.g., If you use conda or anaconda it is up to you to figure out how to
do this. You can post guides to that in piazza, and we will try to
include them in future lecture notes.

Whatever you do, you **must** use a python virtual environment. 

### Review: venv in python 3 (Graded)

To create a venv please use the command

```bash
$ python -m venv ~/ENV3
```

Please understand the following concepts (no submission needed):

* How do you activate the virtual env in your OS?
* How do you modify your `.bashrc` file so that the python venv is loaded automatically upon the start of a new terminal?
* In case you use zsh, either switch to bash or describe how do you modify zsh so that the python venv is loaded.
* Why do you need to use `venv` for this class? Provide a one-paragraph answer in your notebook.md file.

### Review: Anaconda (Graded)

Due: before the semester break

This lab only has to be done by those using anaconda/conda. Those using
python from python.org do not have to do this assignment.

Please provide your answers in the notebook.md file.

* What problems may you encounter when using anaconda as python developer?

* Let us assume you use anaconda on your virtual machines in the cloud. Let
  us assume you start 1000 vms all using anaconda. What is the overhead in
  wasted space on these machines if you just wanted to use as simple
  regular python program on these VMs?

* How do you find out how much space is used by your program and its
  libraries?

* How do you switch between anaconda and regular python 3.10.4

* What is the difference between conda, miniconda, anaconda?

* Does anaconda provide a virtual environment?

* Why do you want to use a virtual environment even for conda/anaconda?

* Is anaconda modifying your bashrc, zshprofile, or registry?

* Showcase how to install cloudmesh under andaconda.


### Python Language review

#### Dicts

We like to remind you about dicts in python.

Read up on dicts and experiment with them.

* How do you merge the content of two dicts?

#### f-Strings in Python 3

Python 3 provides some very nice way of using variable names as part
of string manipulations.

* Locate the PEP 498 and study it:
<https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498>

Try out the following

```python
test = "Gregor"
msg = f"This is a test {test}"
print (msg)
```

```python
def f(test):
    msg = "This is a test {test}".format(**locals())
    print (msg)
```

```python
from cloudmesh.common.debug import VERBOSE
d = {"test": "Gregor"}
VERBOSE(d)
```

In one of the examples `locals()` is used.

* What does locals() do?
* What does ** in the format statement do?


#### Python Classes 

This can be completed at a later time throughout the class:

* What is `self` in classes?
* Why does `self` need to be used in regular method definitions in classes?
* What can I do with __init__ and why is it used?
* What is `cls` and `@classmethods`?
* Why would one use `@staticmethod`?
* Write a Provider.py class to interface with multipass. If you can for some reason not use multipass, emulate its behavior 
  while using print statements.

#### Python Modules

This can be completed at a later time throughout the class:

* What is a setup.py file (use google)
* What is the difference between `pip install .` and `pip install -e .`
* How do I uninstall a python module?
* My python virtual environment is broken, What do you do now?
* Use the command `cms sys generate comamnd` and create a new command. 
  Inspect the code that is generated. Take a look at setup.py
  We create this all for you automatically ;-)
  
We will be discussing these questions in the Labs (online/and residential).

### Graded Activities

In the book [Introduction to Python for Cloud Computing](https://laszewski.github.io/book/python/) [@las19python] please do the following assignments

* E.Cloudmesh.Common.1
* E.Cloudmesh.Common.2
* E.Cloudmesh.Common.3
* E.Cloudmesh.Common.4
* E.Cloudmesh.Common.5
* E.Cloudmesh.Shell.1
* E.Cloudmesh.Shell.2
* E.Cloudmesh.Shell.3

## Chapter Selection

As part of this class you will be conducting a technology review while
writing a chapter that looks at a topic related to cloud computing.
The chapter is written in markdown and placed in your HID directory at

```
chapter/report.md
```

Please note that all characters of the filename are lower case.

This year's topic focusses mostly around *Cloud AI Services* but we also
accept other topics that you may find interesting and are not covered in
substantial length in any of our books.

We have posted here some initial ideas for chapter contributions.
Remember that you **must** not write an introductory paragraph to your
contributions as they are most likely already covered in the books.
Instead, you **must only** focus on the topic at hand. 

So please visit the link and select a topic or suggest your own

<https://docs.google.com/spreadsheets/d/1QxlFCSQI66-zR9H6uI9-N5F99fi23o3enrU51QJdQ7c/edit?usp=sharing>

Please only fill out the white lines and leave the yellow once
untouched. If there are more than two people in a category, please
coordinate with each other how to write it while only providing a single
document. Depending on what the topic is about, you may have to expand
it. Please note that this is a multipage activity and not a one-sentence
activity. References must be included as proper references at the end; we will teach you in time on how to do that. Examples are given in the
markdown book.

All chapters need to include

* a writeup that introduces the technology without plagiarism and 
  advertisement claims by the developers of that technology.
* an example on how to use it that can be replicated and you have 
  tried yourself, if possible.
* references in BibTeX format

Due dates:

* Feb 3rd: Last date to propose a chapter 
* Feb 10th: Last date to submit the first draft 
* Feb 17: Last date to return a peer review 
  (you get a grade from the author of the chapter, 
   the reviewer will also check your examples)
* Feb 24: Last date the hand in the final version of the chapter 


## Project Selection

Deadline: Feb 16 last day to hand in your project proposal

You will be selecting a cloud-related project over the next 2 weeks that
you will be developing until the end of the semester. The project must
have the following requirements:

* Programming must be done using python if another programming language
  is used, please contact us and justify the use. You will also have to do part of your programming, to, for example, coordinated the deployment or the benchmark likely in python. We also accept
  JavaScript if you like to develop a GUI for Cloudmesh. 
  We also have some start using electron.

* The project must use OpenAPI 3.0 to define a REST service. We will
  teach you how to do that in future activities.

* The project must use conexion to automatically generate the rest
  service (please do not use swagger codegen). We will teach you how to 
  do that in a future activity.

* The project must use at least 1 + n clouds for each team member. where
  n is the number of team members with maximum 3 team members. We will
  teach you how to do that in a future activity.

* The code must use pytests. We will
  teach you how to do that in a future activity.

* The code must use `cms sys generate`. This is one of the lab
  assignments for this week.

* The code must use the `cloudmesh benchmark/stopwatch` class. This is
  one of the lab assignments for this week.

* If an AI service is used we recommend to use scikit-learn or Kearos
  and contrast it with AI services offered by cloud providers. This will
  be discussed in upcoming lectures.

* You must provide a report with meaningful benchmarks. The report is 
  written in markdown. We will discuss with you how to do
 that in a future lecture.

Please note that the above requirements also hold true if you use
technologies such as Hadoop, Spark, Kubernetes, AWS, Azure, Google,
OpenStack, ...

Certain projects will have custom deliverables that we will refine with
you once you have chosen such a project. For example, if you were to chose a 
cloudmesh project you will be asked to develop a manual instead of a report.
However, you still have to do the benchmarks.

A preliminary list of projects is available at.

* <https://cloudmesh.github.io/cloudmesh-manual/projects/>

Others are also posted in Piazza. We will add additional project ideas
once they become available. Please note that we consider the Cloudmesh
related projects easy as we introduce you gradually in all aspects as
part of the class to deliver a successful project.

Those wanting to chose the Raspberry PI Cluster or the Robot Boat, please
contact the instructors via piazza. We want to set up a meeting to
better discuss this project. 

When it comes to the scope of the project, remember a project takes up
to 12 weeks to be completed. It is not allowed to just search on
`github` or another book and *replicate* a project done by someone
else. Your project must have a novel component. Please note this class
is called Engineering Cloud Computing we must see clearly an aspect
that you engineer the cloud, e.g., the setup of a reproducible cloud
environment is mandatory. Please ask questions and understand
this. While you are able to use all services, all images must be
created from scratch, and we must be able to reproduce them. We will
decline all projects that point us to images that you ask us to
download and uploaded by you on github, dockerhub or similar. Instead,
you must provide us with scripts, dockerfiles, makefiles or similar
that create the images. You are allowed to use images hosted by major
vendors such as an ubuntu19.04 image or on chameleon cloud the images
starting with cc-* and so on ...

## Working Ahead

Obviously, we will be introducing you to some more advanced concepts that
are not yet finalized in the books. You can certainly use documents from
the internet to learn about such concepts.

The concepts we will need are listed in the Syllabus.  

On the python side, we will introduce you to 

* pytest
* GitHub API as an example for a REST service
* Azure python API
* AWS boto
* OpenstackSDK API
* Google cloud API
* ...

On the Cloudmesh side we will introduce you soon to

* cloudmesh.yaml as preliminary documented in the cloudmesh manual
* cloudmesh cloud bundle
* cloudmesh storage bundle

## Online Meeting Recording


Lab meeting: 

1. [![Video](images/video.png) Online Meeting Recording discussing Projects, multipass,  cloudmesh  (2:16:40)](https://www.youtube.com/watch?v=I-k8QuuFfJY)
2. [![Video](images/video.png) Online Meeting Recording discussing Projects, Twillo project discussion, bibtex jabref, cloudmesh  (1:05:40)](https://www.youtube.com/watch?v=Vm65mP8st9I)

I have only written down some of the topics if you find additional
topics we talked about, please correct them via a pull request in github.

FYI. Twillo has not been chosen by the student.

This is a recording from last year. This meeting took place Sep 10, 2019, 8-9pm EST

* [![Video](images/video.png) Online Meeting Recording for Week 3 (1:54:01)](https://www.youtube.com/watch?v=DD5rBVk3kZw)

