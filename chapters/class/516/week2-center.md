# Week 2: Cloud Data Centers

## Lecture Material

A new version of the following books have been released:

* [e516 Lecture Notes Engineering Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/e516/) [@las19e516]:
* [Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]:

Please read the section in [Cloud Computing](https://laszewski.github.io/book/cloud/)[@las19cloudcomputing]:
about **Data Centers**. We decided not to do a video as the material
in this section frequently changes, and videos became too quickly
outdated. 


Do the following assignments:

Due: two weeks, share your findings on PIazza and improve based on the
discussions and other students' contributions. We recommend you start in
the first week. Gregor will than integrate the contributions into a
document that we can then use in the second week for improvements.
Please also note that this assignment is used for you to learn markdown
with references, links, and BibTeX entries. Note that GitHub does not
support this version of markdown.

* E.Datacenter.2.a
* E.Datacenter.2.b
* E.Datacenter.3
* E.Datacenter.4
* E.Datacenter.5
* E.Datacenter.8

Optional:

* E.Datacenter.9

Optional :o2:

We may post on Piazza examples from last semester that you can leverage
and improve. Remember, they may already be outdated by now and could need
updates. It will take us some time to publish them. But you can find
them already yourself if you look in previous students' repositories.

## Lab Activities

### Receive your HID

Due: one week (needs survey to be filled out)

Make sure you have received an HID on GitHub. Look it up at 

* <https://github.com/cloudmesh-community>

Make sure to accept the GitHub invitation and try to add a file. You can
use either the GUI way with *Create new File* or if you are familiar
with GitHub use the command line tools. Next week we will introduce you
to convenient tools so you can develop your programs more easily in
GitHub.

### README.yml

Due: one week

Make sure the information in your README.yaml file is accurate. Make
sure to change the value in the community attribute and use your class number. This
will be either e516 or b649 or similar. Please note when we ask you for your hid
number, it is the entire hid number, not just the last three digits.


```
---
owner:
  firstname: Gregor
  lastname: von Laszewski
  hid: hid-000
  community: e516
  semester: sp20
```

### Chameleon Cloud

Due: Now

Make sure you have completed the application for the chameleon cloud as
we will use that in our lab soon.

### Review Python

Due: throughout the semester

This activity will go on throughout the entire semester. You do not have
to be a Python expert within one day, but if you have knowledge gaps,
please review and consult our Python Book. Start with the language features.

* [Python for Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/python/) [@las19python]:

We typically use Python 3.8; the book may be a bit outdated in that aspect.

### Setup your Computer

#### Python

Due: One Week

Make sure you have Python set up. Read up on virtualized python
environments as used in Python 3.8. Its super simple. Understand what
the command

```bash
$ cd ~ 
$ python -m venv ENV3
$ source ENV3/bin/activate
```
 
Those using Windows, please find out how to do it on Windows, provide a
document venv-windows.md in your HID directory describing it.

Those using conda/anaconda, please find out how to do it with
conda/anaconda, provide a document venv-conda.md in your HID directory
describing it.

Make sure you create a separate venv for this class called ENV3 that we
will use for this class and should not be used for other classes as we
do not want to create side effects. Please also be aware that at times
it may be necessary to delete your python environment in case you do
something wrong and it would be unwise to combine all your python
activities into one python install.

As you can see, this is super easy.

We recommend PyCharm for an IDE if you have not yet picked one. PyCharm
automated code improvements will be used for most of our projects. It
really helps you! We will teach you throughout the semester how to use
it.

### Ubuntu Multipass

Due: one week

Locate the Section about Multipass in the book

* [Cloud Computing, Gregor von Laszewski](https://laszewski.github.io/book/cloud/) [@las19cloudcomputing]:

and read it.

Install ubuntu multipass on your computer. Note that you must have at
least 8GB of main memory on your computer. However, you may need to close
chrome or PyCharm. Please monitor your consumption of memory to
determine if you like to buy more memory for your computer and upgrade
it. A computer with 4GB is likely not to be usable for this assignment.

In case you do not have a computer on which you can execute this, please
consult with us in Piazza. You may have to do more work than other students.

For example (a) you may have to immediately start using chameleon cloud
and learn OpenStack as an alternative; (b) you may need to use a virtual
box; (c) or you may have to buy yourself a cheap up to date computer on
which you can execute the class. You must be able to be
superuser/administrotor of that computer. The computer must support
virtual machines and Docker.

Please also note that if you have Windows Home 10 on your system, you
need to upgrade it to Pro or EDU. Make sure to configure it as 64 bit.

It is in your responsibility to have the proper equipment. 

Analogy: When you play tennis, you get yourself a tennis racket, and you do
not show up with a pingpong paddle to play it. 

Do Assignments:

* E.Multipass.1
* E.Multipass.5

### Optional: Plagiarism Certificate

Due: optional, but if you do not understand what plagiarism is, please find out.


---

[![Warning](images/warning.png)]()

At IU you are required to know these concepts before you take any
class. Thus the excuse: "I did not know that this is plagiarism" does
not apply to any class at IU including this one.

---

When writing contributions that can be integrated into the class
material, it is important that it is not plagiarized. It is most
important that you not just copy content from Web pages, but make
appropriate modifications and provide credit to where you found this
information.

As you certainly will have learned from other classes what plagiarism is
and how not to plagiarize, you will probably be fine. However, we often
find one or two students in a class that does not know what it is. Therefore
we **STRONGLY RECOMMEND** that you take the plagiarism certificate
offered by IU. This has the advantage that you can show it in other
classes and show you are informed. Please also read the code of conduct
rules at IU.
 
For this reason, we included this material also in part in the Book

* [Scientific Writing with Markdown](https://laszewski.github.io/book/writing/)

Please read the chapter about Plagiarism.

Please be aware that we may conduct superior plagiarism tests. Our tests
are even better than  *Turn-it-in* while we are able to identify
*translations* from other languages, copies of text from non-public
external university servers, and company archives that turn-it-in does
not check. IU has a strict policy that we must follow.
Plagiarism/cheating could lead to expulsion from the university. The
argument *I did not know what plagiarism is* does not count according to
IU rules. You must know what it is prior to you taking a course at IU.
 
It is not the subject of this class to teach you what plagiarism is. We do
this just to remind you to avoid any uncertainty about it.

## Online Meeting Recording :o2:

:o2: this is a recording from last semester. A new recording will be
published here for this semester once it becomes available.

The online meeting recording from Tue Sep 3, 2019 is available from this
link:

* [![Video](images/video.png) Online Meeting Recording for Week 2 (48:38)](https://www.youtube.com/watch?v=kezPx0QHrt8)

This meeting lasted actually half an hour longer but included duplicated
questions that we removed.
