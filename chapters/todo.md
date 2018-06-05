## To Do

Todos are integrated in the text marked with `TODO`. A TODO should have
the form

TODO Assignee, Summary

where Assignee is the person that this to do is assigned to and Summary
is a one line text that summarizes the issue. More details can be
provided in text, but the summary is mean as a describe the issue in one
sentence. Please be brief.

Additional items we like to work on are listed here

-   OpenFaaS
    <https://blog.alexellis.io/your-serverless-raspberry-pi-cluster/>
-   Git: integrate <https://git-scm.com/book/en/v2>

    -   [[PDF](https://github.com/progit/progit2/releases/download/2.1.61/progit.pdf)]
        [[epub](https://github.com/progit/progit2/releases/download/2.1.61/progit.epub)]
        [[mobi](https://github.com/progit/progit2/releases/download/2.1.61/progit.mobi)]


Please add TODOs or better, pick some and do them. Additional todos
are files as github issues.



### Integrate old class links

If you observe something missing let us know.

-   <https://github.com/bigdata-i523>
-   <https://raw.githubusercontent.com/bigdata-i523/sample-hid000/master/README.md>


### Integrate student contributions

Evaluate and potentially integrate the following contributions

* Python 2 vs 3: <https://docs.google.com/document/d/1WGK6Bhdp4ErwvNr-bk5dlZmHKDjdzTn1emHtbijTqjo/edit>
* Data formats <https://github.com/bigdata-i523/hid233/blob/master/experiment/dataformats/group_assignment.md>
* Raspberry Pi <https://github.com/bigdata-i523/hid201/blob/master/python_stuff/raspberry_pi.md>
* open: cloudmesh.cmd5 on Windows Native and with docker
    <https://piazza.com/class/j5wll7vzylg25j?cid=337>
* MQTT
  <https://github.com/bigdata-i523/hid104/tree/master/experiment>
  word document is here
  <https://github.com/bigdata-i523/hid224/tree/master/experiment>
- Experimenting with MQTT <https://piazza.com/class/j5wll7vzylg25j?cid=238>

*  Cloudmesh.cmd5 <https://piazza.com/class/j5wll7vzylg25j?cid=335>
-   Description            <https://piazza.com/class/j5wll7vzylg25j?cid=240>
-   Experimenting with gitbash on windows            <https://piazza.com/class/j5wll7vzylg25j?cid=236>
-   Experimenting Windows Subsystem for Linux Documentation            <https://piazza.com/class/j5wll7vzylg25j?cid=237>
-   Experimenting with Graphs            <https://piazza.com/class/j5wll7vzylg25j?cid=239>
-   Experimenting with IoT sculptures            <https://piazza.com/class/j5wll7vzylg25j?cid=241>
-   Build a camera enhanced Raspberry Pi robot car            <https://piazza.com/class/j5wll7vzylg25j?cid=242>
-   Build a Raspberry PI docker swarm cluster            <https://piazza.com/class/j5wll7vzylg25j?cid=243>

Others see:

<https://piazza.com/class/j5wll7vzylg25j?cid=722>




### Others Volumes need to be integrated into the assignments:


1. (This document) Handbook of Clouds and Big Data, Gregor von Laszewski, Geoffrey C. Fox, and Judy Qiu, Fall 2017, <http://cyberaide.org/papers/vonLaszewski-bigdata.pdf>

Technology papers

1. [Use Cases in Big Data Software and Analytics Vol. 2, Gregor von Laszewski, Fall 2017](https://github.com/laszewski/laszewski.github.io/raw/master/papers/vonLaszewski-i523-v2.pdf) (195 pages)
2. [Use Cases in Big Data Software and Analytics Vol. 1, Gregor von
Laszewski, Fall 2017](https://github.com/laszewski/laszewski.github.io/raw/master/papers/vonLaszewski-i523-v1.pdf) (205 pages)
3. (Draft) Big Data Software Vol 1., Gregor von Laszewski, Spring 2017, <https://github.com/cloudmesh/sp17-i524/blob/master/paper1/proceedings.pdf>
4. (Draft) Big Data Software Vol 2., Gregor von Laszewski, Spring 2017, <https://github.com/cloudmesh/sp17-i524/blob/master/paper2/proceedings.pdf>
5. [Vol 7, Gregor von Laszewski, Spring 2018](http://cyberaide.org/papers/vonLaszewski-cloud-vol-7.pdf)
6. [Cloud and Big Data Technologies Vol 8, Gregor von Laszewski, Spring 2018]
(http://cyberaide.org/papers/vonLaszewski-cloud-vol-8.pdf)

### Tutorial about spark and kubernetes

-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-1/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-2/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-3/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-4/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-5/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-6/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-7/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-8/>
-   <http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-9/>
    This could naturally be the basis of your project. However you can
    not just paste and copy, you need to write it as a section and not
    use the word tutorial. You need to make meaningful modifications or
    enhancements to it. Such as creating a Dockerfile doing all of this
    in an elegant fashion without any human input other than starting
    the process. We know this is possible and can be done. Then you need
    a dataset and test your deployment on a variety of machines.

3 committed people can work on this.

### Docker Cluster on PI Video

The following video is pretty interesting as it shows many of the steps
that are needed to create a docker cluster. This is regardless if you
use a cluster based on zeros, 3 B, 3B+.

-   <https://www.youtube.com/watch?v=qSpfWP-Fgjc> Naturally, the video
    shows how to do things by hand. To bring this to the next level, One
    could, for example, provide a host file with the static addresses
    (or create them) and use it as part of a script to modify Vanilla SD
    cars that contain the vanilla OS on it.

E.g. the tutorial contains many steps that ask to manipulate things by
hand. This is unnecessary as all the steps can be provided by a script.

The reason we want everything scripted is that we like to replicate this
many many times as we want to replicate a swarm cluster for example on
100 Pi's doing this on 1-4 by hand may be reasonable, but doing this on
100, we have to further automate this.

Using just 4 zeros is a good way to test this automated setup.

This could become a project. Then you just develop some swagger rest
services and try to place them on the swarm. Similar things can be done
with kubernetes.
