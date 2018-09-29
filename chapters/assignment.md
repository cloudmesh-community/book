# Assignments

For more details see the cours syllabus and overview pages. We give
here just some summary.

## Account Creation

As part of the class you will need a number of accounts

* piazza.com
* github.com
* futuresystems.org
* chameleoncloud.org
* google.com
* aws.com (free account)
* azure.com (optional)
* watson from IBM (optional)
* google Iaas (optional)

In our piazza we have details how to submit them to us. We split the
submission in multiple subassignments as the github.com and piazza.com
are needed within the first week.

## Virtual Cluster

All students can contribute on the creation of the Virtual Cluster
that we will be using throughout the class to improve and interface
with cloud and container farmeworks.

* <https://github.com/cloudmesh-community/cm>

The residential students have been assigned this task, but online
students can join and contribute

## Projects that could substitute a chapter 

Develop a cm-burn command that creates Raspberry PI OS based on
manipulation of the file system

* <https://github.com/cloudmesh-community/cm-burn>
* <https://github.com/cloudmesh-community/cm>

Substential contributions are expected.

## Section and Chapter Contributions

As part of the class you will be constributing a **significant**
chapter that can be used by other students in the class and introduces
the reader to a general topic, in addition it is expected if
applicable to develop a practical example demonstrating how to use a
technology. The chapter and the practical example can be the same. We
do not like to use the term tutorial in our writeup but sometimes we
refer to it in our assignments as such.

:warning: it is expected from you that you slf identify a section or a 
chapter as this shows competence in the area of cloud computing. If 
howebver you do not know what to select, you must attend an online hour 
with us in which we identify sections and chapters with you. The 
emphasize here is that we do not decite them for you, but we identify 
them with you.

Topics that could form a section or chapter that we like to integrete 
are clearly marked with a :question: . There are plenty in the handbook, 
but you are welcome to define your own contributions. Discuss them with 
us in the online hours.

A list of topics identified by students is maintained in a spreadsheet.

See <https://piazza.com/class/jgxybbf5rnx5qd?cid=201> for details.

### Sections

The following sections can be contributed by students. Multiple
sections will count towards your fulfillment of contributing a
chapter.

Make sure that you claim a section in piazza and add your hid here when you work on it.
Make sure to add yourself if you know you can complete the section in two days.

* :new: [Lambda Expressions](#lambda-expressions) - already contributed by student
* :hand: [Generators](#generators) - fa18-516-18 works on this
* [Non Blocking Threads](#non-blocking-threads)
* [Subprocess](#subprocess)
* [Queue](#queue)
* [Scheduler](#scheduler)
* MQTT (we already have a chapter on this, but we may want to improve)
* [Python SSL](#python-ssl)

### Chapters

The following require more work and qualify **if done right as a
chapter**. Please suggest chapters you like to contribute:

* [GraphQL](#s-graphql)
* OpenFaaS
* OpenWhisk
* Python Concurrent.futures
* Python Multiprocessing
* [Scala and Cloud Computing](#scala-and-cloud-computing)

### Your own suggestion

We are happy to work with you on your on suggestions. Please note that
we also have some additional mateial that is not yet released that
could be enhanced upon.

### Submission of sections and chapters

Simply add them to your README.yml file in your github repo.
Add the following to it (I am using a18-516-18 as example)

Please look at <https://github.com/cloudmesh-community/fa18-516-18>
for an example

```
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
project:
    - title: title of the project
         url: url in your hid space or that of your partner
other:
    - activity: spell checked md document
         url: put url here
```

run yamllint on the README.yml file. YAML errors will give point deductions

