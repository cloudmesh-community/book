---
title: "e516: Engineering Cloud Computing"
author: [Gregor von Laszewski]
date: "2018-05-10"
subject: "Markdown"
keywords: [Markdown, Example]
subtitle: "Indiana University"
titlepage: true
titlepage-color: "06386e"
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "FFFFFF"
titlepage-rule-height: 2
...

# e516: Engineering Cloud Computing

* Lecture Notes: [ePub](https://github.com/cloudmesh-community/book/blob/master/vonLaszewski-cloud.epub)
* Indiana University
* Faculty: Dr. Gregor von Laszewski (laszewski@gmail.com)
* Credits: 3
* Hardware: You will need a computer to take this class, a phone,
  tablet, or chrome book is not sufficient.
* Prerequisite(s): Knowledge of a programming language, the ability to
  pick up other programming languages as needed, willingness to
  enhance your knowledge from online resources and additional
  literature. You will need access to a *modern* computer that allows
  using virtual machines and/or containers. If such a system is not
  available to you can also use cloud vms we provide and if you opt to
  do so one or more Raspberry's PI. All residential students will have
  access to a total of 200 Raspberry PIs. Online students can opt to
  purchase one or more based on our materials list that we will
  release throughout the semester. All students will have access to a
  cloud.
* Course Description: [Link](https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-engineering-cloud-computing.md)

This is an introductory class. In case you like to do research and
more advanced topics, consider taking an independent study with
Dr. von Laszewski.

## Course Description

This course covers basic concepts on programming models and tools of
cloud computing to support data intensive science
applications. Students will get to know the latest research topics of
cloud platforms, parallel algorithms, storage and high level language
for proficiency with a complex ecosystem of tools that span many
disciplines.

## Course Objectives

The course has the following objectives:

* Provide a basic introduction to cloud computing
* Introduce the concept of cloud data centers 
* Get familiar with cloud infrastructure as a Service such as
  OpenStack, Azure, or AWS
* Get familiar with cloud infrastructure such as Docker and Kubernetes
* Program cloud services
* Understand the differences between virtual machines and containers
* Develop sophisticated programming language independent REST services
* Learn advanced programming models for clouds such as Map/Reduce,
  Messaging, and GraphQl
* Exploration of Go for cloud computing
* Demonstrate knowledge of clouds while developing a significant project
* Explore state-of-the-art cloud technologies and services while
  providing a section and summary and commenting on its use for the
  cloud
* Learn how edge computing is enhancing cloud services and
  infrastructure
* Learn how to set up a cloud based on using commodity hardware

## Learning Outcomes

* Be able to explain the concepts of the cloud computing paradigm
  including its paradigm shift, its characteristics, and the
  advantages. Contrast them with the challenges and disadvantages.
* Be able to identify infrastructure and programming models needed to
  support real world applications.
* Be able to implement a real world application or deploy a cloud and
  its services.
* Be able to conduct sophisticated performance analysis of cloud
  services.
* Be able to communicate the results through tutorials, manual, and
  reports.
* Be able to work in a team to develop collaboratively software or
  contribute collaboratively to develop sections explaining how to use clouds.

## Syllabus

The topics are subject to change.


|     | Dates  | Unit | Title  | Description |
| --- |------ | --- | ------- | --------------------- |
|   | Week 1    | 1   | Introduction       | [Gregor von Laszewski](#research-interests)[:cloud:][gregor.md] |
|   |           |     |                    | [Class summary](E516 Summary)[:cloud:][e516-summary.md] |
|   |           |     |                    | [Definition of Cloud Computing](#definition-of-cloud-computing)[:cloud:][e516-definition.md] |
|   | Week 2    | 2   | Tools              | **Tools and Services** |
|   |           |     |                    | - [Virtual Box](#virtual-box)[:cloud:][virtualbox.md] |
|   |           |     |                    | - [Vagrant](#vagrant)[:cloud:][vagrant.md] |
|   |           |     |                    | - [Github](#github)[:cloud:][github.md] |
|   |           |     |                    | - [Linux](#s-linux)[:cloud:][linux.md] |
|   | Week 3    | 3   | Python             | **Python** |
|   |           |     |                    | - [Introduction](#s-python-intro)[:cloud:][python-intro.md] |
|   |           |     |                    | - [Installation](#s-python-install)[:cloud:][python-install.md] |
|   |           |     |                    | - [Interactive Python](#interactve python)[:cloud:][python-interactive.md] |
|   |           |     |                    | - [Editors](#s-python-editor)[:cloud:][python-editor.md] |
|   |           |     |                    | - [Basic Language Features](#s-python-language)[:cloud:][python.md] |
|   |           |     |                    | - [Modules](#s-python-modules)[:cloud:][python-libraries.md] |
|   |           |     |                    | - [Data Management](s-python-data)[:cloud:][python-data.md] |
|   |           |     |                    | - [Matplotlib](#matplotlib)[:cloud:][python-matplotlib.md] |
|   |           |     |                    | - [Cloudmesh Commandshell CMD5](#cloudmesh-commandshell-cmd5)[:cloud:][python-cmd5.md] |
|   |           |     |                    | - [OpenCV](#s-opencv)[:cloud:][opencv.md] |
|   |           |     |                    | - [Secchi Disk](#s-secchi-disk)[:cloud:][secchi.md] |
|   | Week 4    | 4   |                    | [Data Center][datacenter.md] |
|   | Week 5    | 5   | Architectures      | - [NIST Big Data Reference Architecture](#nist-big-data-reference-architecture)[:cloud:][bdra.md] |
|   |           |     |                    | - [Cloud Architectures](#s-cloud-architectures) [:cloud:][arch.md]
|   |           |     |                    | - [NIST Big Data Reference Architecture](#nist-big-data-reference-architecture)[:cloud:][bdra.md] |
|   | Week 6    | 6   | Virtualization     | [Virtualization, Qemu, KVM, Virtual machines](#s-virtualization)[:cloud:][virtualization.md] |
|   |           |     | Virtualization I   | - [Qemu](#s-qemu)[:cloud:][qemu.md] |
|   | Week 7    | 7   | Infrastructure     | [Infrastructure as a Service](#infrastructure-as-a-service)[:cloud:][iaas.md] |
|   |           |     |                    | - [Azure](#microsoft-azure) [:cloud:][azure.md] |
|   |           |     |                    | - [AWS](#amazon-web-services) [:cloud:][aws.md] |
|   |           |     |                    | - [OpenStack](#s-openstack) [:cloud:][openstack.md] |
|   |           |     | Chameleon Cloud    | - Chameleon Cloud |
|   |           |     |                    | - [Resources](#chameleon-cloud-security-warning)[:cloud:][resources.md] |
|   |           |     |                    | - [Hardware](#chameleon-cloud-hardware)[:cloud:][hardware.md] |
|   |           |     |                    | - [Charge](#chameleon-cloud-charge-rates)[:cloud:][charge.md] |
|   |           |     |                    | - [Quick start](#getting-started-on-chameleon-cloud)[:cloud:][start.md] |
|   |           |     |                    | - [KVM user guide](#openstack-virtual-machines)[:cloud:][user-guide.md] |
|   |           |     |                    | - [CLI](#openstack-command-line-interface)[:cloud:][cli.md] |
|   |           |     |                    | - [Horizon](#openstack-horizon)[:cloud:][horizon.md] |
|   |           |     |                    | - [Heat](#openstack-heat)[:cloud:][heat.md] |
|   |           |     |                    | - [Baremetal](#openstack-baremetal)[:cloud:][baremetal.md] |
|   |           |     |                    | - [FAQ](#chameleon-cloud-frequently-asked-questions)[:cloud:][faq.md] |
|   | Week 8    |   8 | Virtualization  II | Containers, Docker, Kubernetes |
|   | Week 9    | 9   | Programming        | Python for Cloud Computing |
|   |           |     |                    | - [Libcloud](#python-libcloud)[:cloud:][libcloud.md] |
|   |           |     |                    | - [Github as a Cloud Service](#s-github-prg)[:cloud:][githubprg.md] |
|   |           |     |                    | - [REST Services](#rest)[:cloud:][rest.md] |
|   |           |     |                    | - [Rest Services with OpenAPI](#rest-services-with-openapi)[:cloud:][swagger.md] |
|   |           |     |                    | - [OpenAPI Spec](#openapi-spec)[:cloud:][swagger-spec.md] |
|   |           |     |                    | - [OpenAPI Codegen](#openapi-codegen)[:cloud:][swagger-codegen.md] |
|   |  Week 10  | 10  | Map/Reduce         | Map/Reduce, Hadoop, Spark, and others |
|   |  Week 11  | 11  | Messaging          | Messaging |
|   |  Week 12  | 12  | Messaging          | - [MQTT](#mqtt)[:cloud:][mqtt.md]  |
|   |           |     |                    | - [Graphql][graphql.md]  |
|   | Week 13   |  13 | Go                 | Go for the Cloud |
|   | Week 14,15   | 14  | Edge Computing  | Edge Computing and the Cloud |
|   | Week 16 | 15 | Project Selection | Project selection for inclusion in the Proceedings |


 

[arch.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/arch.md
[gregor.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/gregor.md
[e516-summary.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-summary.md
[e516-definition.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/class/e516-definition.md

[virtualbox.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/virtualbox.md
[vagrant.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/vagrant.md
[github.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/git/github.md
[linux.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md

[python-intro.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-intro.md
[python-install.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-install.md
[python-interactive.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-interactive.md
[python-editor.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-editor.md
[python.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python.md
[python-libraries.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-libraries.md
[python-data.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-data.md
[python-matplotlib.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-matplotlib.md
[python-cmd5.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-cmd5.md
[datacenter.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/datacenter.md
[bdra.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/nist/bdra.md
[iaas.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/iaas.md
[openstack.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/openstack/opensatck.md
[azure.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/azure/azure.md
[aws.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md
[resources.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/resources.md
[hardware.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/hardware.md
[charge.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/charge.md
[start.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/start.md
[user-guide.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/user-guide.md
[cli.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/cli.md
[horizon.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/horizon.md
[heat.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/heat.md
[baremetal.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/baremetal.md
[faq.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/chameleon/faq.md
[libcloud.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/libcloud.md
[rest.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/rest.md
[swagger.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/swagger.md
[swagger-spec.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/swagger-spec.md
[swagger-codegen.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/rest/swagger-codegen.md
[mqtt.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/msg/mqtt.md 
[graphql.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/msg/graphql.md
[go-cloud.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-cloud.md 
[go-rest.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-rest.md
[go-intro.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-intro.md
[go-cmd.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-cmd.md
[go-install.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-install.md
[go-libraries.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-libraries.md
[go-editor.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-editor.md
[go-links.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-links.md
[go-language.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/go-language.md
[opencv.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/opencv/opencv.md
[secchi.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/opencv/secchi.md
[virtualization.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/virtualization.md
[qemu.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/cloud/qemu.md
[githubprg.md]: https://github.com/cloudmesh-community/book/blob/master/chapters/prg/github.md

Students need only to do one project. The project is conducted thought the entire semester.

* Example chapters are indicated with :cloud:

* Dates may change as the semester evolves

* The project is a long term assignment (and are ideally worked on
  weekly by residential students). It is the major part of the course
  grade.

* Sections and chapters prepare you for documenting a technical aspect
  related to cloud computing. It is a preparation for a document that
  explains how to execute your project in a reproducible manner to
  others.

* Additional lectures will be added that allow easy management of the
  project.  These lectures can be taken any time when needed.

## Assessment

This course is focusing on the principal "Learning by Doing" which is
assessed by simple graded and non-graded activities. The assessment
may include comprehension of the material taught, programming
assignments, participation in online discussion forums, or the
contribution of additional material to the class showcasing your
comprehension.

The comprehension is also measured by the development of a chapter and
sections in markdown that can be distributed and replicated to other
students. This is done in preparation for the project that must
include a simple deployment and runtime instruction set.

The main deliverable of the class is a project. The project is
assessed through the following artifacts:

1. Deployment and install instructions, 
2. Project report (typically 2-3 pages per month, tutorial and
   chapters can be reused if possible), 
3. Working project code that can be installed and executed in
   reproducible manner by a third party 
4. Code developed by the project team distributed in github.com
5. Project progress notes checked into github throughout the semester. Each 
   week the project progress is reported and will be integrated
   into the final grade.
6. Discussions or progress reports with the instructors can be conducted on 
   online and residential class hours.

The grade distribution is as follows 

* 10% Comprehension Activities
* 10% Sections
* 10% Chapter
* 70% Project

As the project is the main deliverable of the course it is obvious
that those starting a week before the deadline will not succeed in
this class. The project will take a significant amount of time and
fosters the principal of "Learning by Doing" at all stages throughout
the semester.

The class will not have a regular midterm, but it is expected that you
have worked on your project and can provide a snapshot of the progress
outlining the goals of the project and how you will achieve these
goals till the end of the semester.

The final Project is due 3 weeks before the semester ends. Issues with
your project ought to have been discussed before this deadline with
the TA's The TAs will in the next 3 weeks go over the projects and
evaluate mayor and minor issues that you may be able to fix without
penalty. Larger changes will receive a grade penalty. The last fix
(upon approval) possible will be 2 weeks before semester end without
penalty. It is recommended that you are available till the last day of
class. 




## Assignments

|     | Dates  | Unit | Title  | Description |
| --- |------ | --- | ------- | --------------------- |
|   | due Week 8                | A1      | Sections           | Contribute significant sections. Do not develop redundant or duplicated content. |
|   | due Week 8                | A2      | Chapter            | Contribute a significant chapter that may use your section to the class documentation. Do not develop redundant or duplicated content. |
|  | Due Week 13               | A3      | Project Type A     | Build a cloud out of Raspberry PIs |
|  |                 |         |                    | Kubernetes, Hadoop, SLURM + OpenAPI Service,  |
|  |                 |         | Project Type B     | Build a Significant OpenAPI REST Service |
|  |                 |         | Project Type C     | Build an Edge Service Interfacing with a Cloud |
|  |                 |         | Project Type D     | Contribute to the new Cloudmesh code |
|  |                 |         | Project Type E     | Your own Project Type A, B, C, D [upon approval) |



## Calendar 

  
|  Assignment #  | Event |     | Date 
| --- | ----- | --- | --- 
|    | Full Term           | | 16 Weeks |
|   | *Begins*            | | Week 1 |
| 1, 2 | **Bio, Notebook** | assigned | Week 1 |
| 1, 2 | **Bio, Notebook** |  due | Week 2 |
| 3 | **Sections**    | assigned | Week 3 |
| 4 | **Chapter**         | assigned | Week 3 |
| 5 | **Project**         | selection or proposal  | Week 4 |
| 5 | **Project** | Draft | Week 8 |
| 3 | **Section** | due | Week 10 |
| 4 | **Chapter** | due | Week 10 |
| 5 | **Project**         | due        | Week 12 |
| 5 | **Project** (no penalty) | improvements | Week 13 |
| 5 | **Project** (with penalty) | improvements | Week 14 |
|   | **Final Deliverables due**  |  | Week 14 |
|   | *Grading*           |  | Week 15, 16 |
|   | *Ends*              |  | Week 16 |


* TA's must be available till all grades have been submitted. 
* Bio: a formal 3 paragraph Bio
* Notebook: a markdown in which you record your progress of
  this class in bullet form
* All times are in EST
* Dependent on class progress Comprehension Assignments may be added

## Incomplete

Please see the university regulations for getting an incomplete.
However, as this class uses state-of-the-art technology that changes
frequently, you must expect that an incomplete may result in
significant additional work on your behalf as your project may need
significant updates on infrastructure, technology, or even programming
models used. It is best to complete the course within one semester.

## Other classes I523, I524, B649, E516, E616 

### I524 = B649 = E516

The classes CSCI B-649 I524 are the same as E516 but are offered within
different departments:

* CSCI B-649 Cloud Computing is the same as E516 but for computer science students.
* I524 is the same as E516 but for Data Engineering Students

### What is E616?

The class E616 is a bit different as it assumes you have taken E516 as
prerequisite or know its content including REST, virtual machines,
containers, and Hadoop. In this class you are expected to focus on
advanced concepts that build upon 516.  This includes DevOps, Julia,
and any topic of 516 with enhancements. The focus will allow you to
deliver contributions based on your knowledge as part of sections, a
chapter you propose to add to the lecture notes, and a more intensive
project. It also allows PhD students to identify topics that can be
leading together with Dr.  von Laszewski as a co-author to a workshop
or conference paper.

### Can I take an Independent Study?

Dr. von Laszewski also offeres independent studies on specific
research topics.  The result of such independent studies is a high
quality report or paper.

### Can I take  E516 and E616 at the same time?

It is possible to take E516 and E616 or an independent study at the
same time.  The result will be a more intense project.

### Is I523 a prerequisite for I524?

I523 is a different class and focusses on Big Data applications and
use cases. You do not have to take I523 as prerequisite if you like to
take E516, I524, or B649.