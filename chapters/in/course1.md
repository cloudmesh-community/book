Software Projects
=================

**Contents**

Please read the information in the overview page at

-   <http://bdaafall2016.readthedocs.io/en/latest/overview.html#software-project>

After doing so please return to this page. Identify a project suitable
for this class, propose it and work on it.

There are several categories of software projects, which are detailed in
lower sections:

1.  Deployment

2.  Analytics

You may propose a project in one of these categories, if you are doing a
software projects.

These are non-trivial project and involve substantial work. Many
students vastly underestimate the difficulty and the amount of time
required. This is the reason why the project assignment is early on in
the semester so you have ample time to propose and work on it. If you
start the project 2 weeks before December (Note the early due data) We
assume you may not finish.

Common Requirements
-------------------

All software projects must:

1.  Be submitted via gitlab (a repository will be created for you)

2.  Be reproducibly deployed

    Assume you are given a username and a set of IP addresses. From this
    starting point, you should be able to deploy everything in a single
    command line invocation.

    Do not assume that the username or IP address will be the ones you
    use during development and testing.

3.  Provide a report in the `docs/report` directory

    LaTeX or Word may be used. Include the original sources as well as a
    PDF called `report.pdf` (See overview-software-project for
    additional details on the report format. You will be using 2 column
    ACM format we have used before.)

4.  Provide a properly formatted `README.rst` or `README.md` in the root
    directory

    The README should have the following sections:

    -   Authors: list the authors

    -   Project Type: one of "Deployment", "Analytics"

    -   Problem: describe the task and/or problem

    -   Requirements: describe your assumptions and requirements for
        deployment/running. This should include any software
        requirements with a link to their webpage. Also indicate which
        versions you have developed/tested with.

    -   Running: describe the steps needed to deploy and run

    -   Acknowledgements: provide proper attribution to any websites, or
        code you may have used or adapted

    in the past we got projects that had 10 pages

    :   installation instructions. Certainly that is not good and you
        will get point deductions. The installation should be possible
        in a couple of lines. A nice example is the installation of the
        development software in the ubuntu vm. Naturally you can use
        other technologies, other than ansible. Shell scrips, makefiles,
        python scripts are all acceptable.

5.  A `LICENSE` file (this should be the `LICENSE` for Apache License
    Version 2.0)

6.  All figures should include labels with the following format:
    `label (units)`.

    For example:

    -   `distance (meters)`

    -   `volume (liters)`

    -   `cost (USD)`

7.  All figures should have a caption describing what the measurement
    is, and a summary of the conclusions drawn.

    For example:

    > This shows how A changes with regards to B, indicating that under
    > conditions X, Y, Z, Alpha is 42 times better than otherwise.

Deployment Projects
-------------------

Deployment projects focuses on automated software deployments on
multiple nodes using automation tools such as Ansible, Chef, Puppet,
Salt, or Juju. You are also allowed to use shell scripts, pdsh, vagrant,
or fabric. For example, you could work on deploying Hadoop to a cluster
of several machines. Use of Ansible is recommended and supported. Other
tools such as Chef, Puppet, etc, will not be supported.

Note that it is not sufficient to merely deploy the software on the
cluster. You must also demonstrate the use of the cluster by running
some program on it and show the utilization of your entire cluster. You
should also benchmark the deployment and running of your demonstration
on several sizes of a cluster (eg 1, 3, 6, 10 nodes) (Note that these
numbers are for example only).

We expect to see figures showing times for each (deployment, running)
pair on for each cluster size, with error bars. This means that you need
to run each benchmark multiple times (at least three times) in order to
get the error bars. You should also demonstrate cluster utilization for
each cluster size.

The program used for demonstration can be simple and straightforward.
This is not the focus of this type of project.

IaaS
----

It is allowable to use

-   virtualbox

-   chameleon cloud

-   futuresystems

-   AWS (your own cost)

-   Azure (your own cost)

for your projects. Note that on powerful desktop machines even
virtualbox can run multiple vms. Use of docker is allowed, but you must
make sure to use docker properly. In the past we had students that used
docker but did not use it in the way it was designed for. Use of docker
swarm is allowed.

### Requirements

Deployment projects must include a repeatable deployment framework that
uses cmd5 and ansible. When using ansible it should be called from a
custoom cmd5 program.

### Example projects

See also
<https://docs.google.com/document/d/1KylDsRBmVbCZSqGpRbzYwdzUGKFi92bkATwU03of5gw>

-   deploy Apache Spark on top of Hadoop

-   deploy Apache Pig on top of Hadoop

-   deploy Apache Storm

-   deploy Apache Flink

-   deploy a Tensorflow cluster

-   deploy a PostgreSQL cluster

-   deploy a MongoDB cluster

-   deploy a CouchDB cluster

-   deploy a Memcached cluster

-   deploy a MySQL cluster

-   deploy a Redis cluster

-   deploy a Mesos cluster

-   deploy a Hadoop cluster

-   deploy a docker swarm cluster

-   deploy NIST Fingerprint Matching

-   deploy NIST Human Detection and Face Detection

-   deploy NIST Live Twitter Analysis

-   deploy NIST Big Data Analytics for Healthcare Data and Health
    Informatics

-   deploy NIST Data Warehousing and Data mining

Deployment projects must have EASY installation setup just as we
demonstrated in the ubuntu image.

A command to manage the deployment must be written using python docopts
that than starts your deployment and allows management of it. You can
than from within this command call whatever other framework you use to
manage it. The docopts manual page should be designed first and
discussed in the team for completeness.

Using argparse and other python commandline interface environments is
not allowed.

Deployment project will not only deply the farmewor, but either provide
a sophisticated benchmark while doing a simple analysis using the
deployed software.

Analytics Projects
------------------

Analytics projects focus on data exploration. For this type of projects,
you should focus on analysis of a dataset (see datasets for starting
points). The key here is to take a dataset and extract some meaningful
information from in using tools such as `scikit-learn`, `mllib`, or
others. You should be able to provide graphs, descriptions for your
graphs, and argue for conclusions drawn from your analysis.

Your deployment should handle the process of downloading and installing
the required datasets and pushing the analysis code to the remote node.
You should provide instructions on how to run and interpret your
analysis code in your README.

### Requirements

An analytocs project may focus on a sophisticated and academically
correct usage of an analytics of data. It must be significant and not
just a simple replication of what others have done before.

### Example projects

-   analysis of US Census data

-   analysis of Uber ride sharing GPS data

-   analysis of Health Care data

-   analysis of images for Human Face detection

-   analysis of streaming Twitter data

-   analysis of airline prices, flights, etc

-   analysis of network graphs (social networks, disease networks,
    protein networks, etc)

-   analysis of music files for recommender engines

-   analysis of NIST Fingerprint Matching

-   analysis of NIST Human Detection and Face Detection

-   analysis of NIST Live Twitter Analysis

-   analysis of NIST Big Data Analytics for Healthcare Data and Health
    Informatics

-   analysis of NIST Data Warehousing and Data mining

-   author disambiguity problem in academic papers

-   application of a k-means algorithm

-   application of a MDS

Project Idea: World wide road kill
----------------------------------

This project can also be executed as bonus project to gather information
about the feasability of existing databases.

It would be important to identify also how to potentially merge these
databases into a single world map and derive statistics from them. This
project can be done on your local machines. Not more than 6 people can
work on this.

Identify someone that has experience with android and/or iphone
programming Design an application that preferably works on iphone and
android that allows a user while driving to

-   call a number to report roadkill via voice and submitting the gps
    coordinates

-   have a button on the phone that allows the gps coordinates to be
    collected and allow upload either live, or when the user presses
    another butten.

-   have provisions in the application that allow you to augment the
    data

-   have an html page that displays the data

-   test it out within users of this class (remember we have world wide
    audience)

Make sure the app is ready early so others can test and use it and you
can collect data.

Before starting the project identify if such an application already
exists.

If more than 6 people sign up we may build a second group doing
something similar, maybe potholes ..

Gregor would like to get this project or at least the database search
query staffed.

Project Idea: Author disambiguty problem
----------------------------------------

Given millions of publications how do we identify if an author of paper
a with the name Will Smith is the sam as the author of paper 2 with the
name Will Smith, or William Smith, or W. Smith. AUthor databases are
either provided in bibtex format, or a database that can not be shared
outside of this class. YOu may have to add additional information from
IEEE explorer, rsearch gate, ISI, or other online databases.

Identify further issues and discuss solutions to them. Example, an
author name changes, the author changes the institution.

Do a comprehensive literature review

Some ideas:

-   Develop a graph view application in JS that showcases dependencies
    between coauthors, institutions

-   Derive probabilities for the publications written by an auther given
    they are the same

-   Utilize dependency graphs as given by online databases

-   Utilize the and or topic/abstarct/full text to identify similarity

-   Utilize keywords in the title

-   Utilize refernces of the paper

-   Prepare some vizualization of your result

-   Prepare som interactive vizualization

A possible good start is a previous project published at

-   <https://github.com/scienceimpact/bibliometric>

There are also some screenshots available:

-   <https://github.com/scienceimpact/bibliometric/blob/master/Project%20Screenshots/Relationship_Authors_Publications.PNG>

-   <https://github.com/scienceimpact/bibliometric/blob/master/Project%20Screenshots/Relationship_Authors_Publications2_Clusters.PNG>
