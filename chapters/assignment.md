# Assignments

For more details see the course syllabus and overview pages. We give
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

As part of the class, we expect you to get familiar with topics related to cloud computing beyond what we have written in the lecture notes. This is done in Sections, Examples, and Chapters. These assignments are done so you do not have to do other weekly homework or tests. They showcase your understanding of the field.

Definitions:

* **Section:** 
  A section is a small section that explains a topic that is not yet in the handbook or improves an existing section significantly. It is typically multi-paragraphs long and can even include an example if needed. Example sections that have been provided are for example the Lambda section in the python chapter

  Sample of student contributed sections include:

  * The Microsoft under water data center :o: add link
  * [Lambda Expressions](#lambda-expressions)

* **Chapter:** A chapter is a much longer topic and is a coherent description of a topic related to cloud computing. A chapter could either be a review of a topic or a detailed technical contribution. Several Sections (10+) may be a substitute for a chapter.

  You will be constributing a **significant**
chapter that can be used by other students in the class and introduces
the reader to a general topic related to teh topic of the class. In addition it is expected if
applicable to develop a practical example demonstrating how to use a
technology. The chapter and the practical example can be done together. We
do not like to use the term tutorial in our writeup but sometimes we
refer to it in our assignments as such. Chapters that focus on theory 
may not have an example and it can be subsitited by a longer text.

  A sample of a student contributed chapter is * [GraphQL](#s-graphql).

  * **Example:** An example is a document that showcases the use of a particular technology. Typically it is a console session or a program. Axamples augment chapters and Sections.


  :warning: It is expected from you that you self identify a section or a 
chapter as this shows competence in the area of cloud computing. If 
howebver you do not know what to select, you must attend an online hour 
with us in which we identify sections and chapters with you. The 
emphasize here is that we do not decite them for you, but we identify 
them with you.

Sample Topics that could form a section or chapter 
are clearly marked with a :question:. There are plenty in the handbook, 
but you are welcome to define your own contributions. Discuss them with 
us in the online hours.

A list of topics identified by students is maintained in a spreadsheet.

See <https://piazza.com/class/jgxybbf5rnx5qd?cid=201> for details.

YOu are expected to signup in this spreadsheet. THis is done to 
ab=void overlap and foster uniqueness of the assignment for sections 
and chapters. 


### Submission of sections and chapters

Sections and subsections are to be added to the `book` github repo. Do a pull request.
THe headline of the section needs to be marked with a :hand: if you still work on it, 
marked with a :smiley: if you want it to be graded. and have all hids for people that 
contribute to that section.

In addition, simply add them to your README.yml file in your github repo.
Add the following to it (I am using a18-516-18 as example). 

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

You **MUST** run yamllint on the README.yml file. YAML errors will give point deductions

