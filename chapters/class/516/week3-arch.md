# Week 3: Cloud Computing Architectures

Start of Project Selection



## Online Meeting Recording

This meeting took place Sep 10, 2019, 8-9pm EST

* [![Video](images/video.png) Online Meeting Recording for Week 3 (1:54:01)](https://www.youtube.com/watch?v=DD5rBVk3kZw)



## Lecture Material

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/e516/) [@las19e516]
* [Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]
* [Introduction to Python for Cloud Computing, Gregor von Laszewski, Ed. 2019](https://laszewski.github.io/book/python/) [@las19python]

Reading Assignments:

1. Read in the book [Cloud Computing](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing] the chapter about Cloud Architectures.
2. Read in the book [Introduction to Python for Cloud Computing](https://laszewski.github.io/book/python/) [@las19python] the chapter about Cloudmesh


## Lab Activities

We have the following goals

* install python 3.7.4 on your computer. YOU can either use python.org,
  `conda`, or `pyenv`. Which you chose is your choice. For this class the
  preferred way of installing python is from python.org.

### Ungraded Activities

For the ungraded activities, no submission is needed.

#### Review: venv in python 3

This Lab is inly to be chose by those using python 3 from python.org
which is our preferred environment.

```
python -m venv ~/ENV3
```

Please understand the following concepts (no submission needed):

* How do you activate the virtual env in your OS?
* How do you modify your `.bashrc` file?
* Why do you need to use `venv` for this class?

#### Review: Conda

This Lab has only to be done by those using anaconda/conda.

* What problems may you encounter when using anaconda as python developer?

* Let us assume you use anaconda on your virtual machines in the cloud. Let
  us assume you start 1000 vms all using anaconda. What is the overhead in
  wasted space on these machines if you just wanted to use as simple
  regular python program on these VMs?

* How do you find out how much space is used by your program and its
  libraries?

* How do you switch between anaconda and regular python 3.7.4

* What is the difference between conda, miniconda, anaconda?

* Why do you want to use a virtual environment even for conda/anaconda?

#### Dicts

We like to remind you about dicts in python.

Read up upon dicts and experiment with them.

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
    msg = f"This is a test {test}".format(**locals())
    print (msg)
```

```python
from cloudmesh.common.debug import VERBOSE
d = {"test": "Gregor"}
VERBOSE(d)
```

In one of the examples `locals()` is used.

* What does locals do?
* What does ** in the format statement do?


#### Classes 

This can be completed at a later time

* What is `self` in classes?
* Why does `self` needs to be used in regular method definitions in classes?
* What can I do with __init__ and why is it used?
* What is `cls` and `@classmethods`?
* Why would one use `@statusmethod`?

#### Python Modules

This can be completed at a later time

* What is a setup.py file
* What is the difference between `pip install .` and `pip install -e .`
* How do I uninstall a python module?
* My python virtual environment is broken, What do you do now?

We will be discussing these question in the Labs (online/and residential).

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



## Project selection

You will be selecting a cloud related project over the next 2 weeks that
you will be conducting till the end of the semester. The project must
have the following requirements:

* Programming is conducted in python if another programming language is
  used, please contact us and motivate the use. You will aslo have to do
  part of your programming to for example coordinated the deployment or
  the benchmark likely in python.

* The project must use OpenAPI 3.0 to define a REST service. We will
  teach you how to do that in a future activity.

* The project must use conexion to automatically generate the rest
  service (please do not use swagger codegen). We will
  teach you how to do that in a future activity.

* The project must use at least 1 + n clouds for each team member. Where
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

* You must provide a report with meaningful benchmarks. 

* You will have to write a report. We will discuss with you how to do
 that in a future lecture.

Please note that the above requirements also hold tru if you use,
technologies such as Hadoop, spark, kubernetes, AWS, Azure, Google,
OpenStack, ...

Certain projects will have custom deliverables that we will refine with
you once you have chosen such a project. For example if you were to chose a 
cloudmesh project you will be asked to develop a manual instead of a report.

A preliminary list of projects is available at.

* <https://cloudmesh.github.io/cloudmesh-manual/projects/>

We will add additional project ideas once the become available. Please
note that we consider the cloudmesh related projects easy as we
introduce you gradually in all aspects as part of the class to deliver a
successful project.

Those wanting to chose the Raspberry PI Cluster or the Robot Boat, please
contact instructors via piazza. We want to set up a meeting in MESH to
better discuss this project. 

When it comes to the scope of the project, remember a project takes up
to 12 weeks to be completed. It is not allowed to just search on
`github` or another book and "replicate" a project done by someone
else. Your project must have a novel component. Please note this class
is called Engineering Cloud Computing we must see clearly an aspect
that you engineer the cloud, e.g. the setup of a reproducible cloud
environment is mandatory. Please ask questions and understand
this. While you are able to use all services, all images must be
created from scratch and we must be able to reproduce them. We will
decline all projects that point us to images that you ask us to
download and uploaded by you on github, dockerhub or similar. Instead
you must provide us with scripts, dockerfiles, makefiles or similar
that create the images. You are allowed to use images hosted by major
vendors such as an ubuntu19.04 image or on chameleon cloud the images
starting with cc-* and so on ...

## Working Ahead

Obviously we will be introducing you to some more advanced concepts that
are not yet finalized in the books. You can certainly use documents form
the internet to learn about such concepts.

Concepts we will need are listed in the Syllabus.  

On the python side, we will introduce you to 

* pytest
* github API as an example for a REST service
* Libcloud
* Azure python API
* AWS boto
* ...

On the cloudmesh side (still developed by current set of students we will introiduce you to 

* cloudmesh.yaml as preliminary documented in the cloudmesh manual
* cloudmesh cloud bundle (untested)
* cloudmesh storage bundle (untested)

