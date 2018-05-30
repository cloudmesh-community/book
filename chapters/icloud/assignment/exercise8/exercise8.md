Harp MiniBatch Kmeans
=====================

 

\TODO{Hyungro: check hyperlinks}
The goal for this exercise is to implement Harp Mini-batch Kmeans from
scratch (See [Useful Links](#link_exercise8)).

Deliverables
------------

Zip your source code and report as username\_mbkmeans.zip. Please submit
this file to the Canvas Assignments page.

Evaluation
----------

The point total for this exercise is 6, where the distribution is as
follows:

-   Completeness of your code (5 points)

-   In the report, describe your implementation and the output. (1
    points)

You can get up to 4 bonus points based on your extra efforts.

Bonus credits
=============

Some options you may consider to get extra credits:

-   Perform experiments on various (small, medium, large, etc) datasets

-   Test your algorithm on at least 2 nodes on FutureSystem.

-   Implement mini-batch kmeans using other tools/platforms (Spark,
    Flink, etc) and compare the performance between different
    tools/platforms (See [Useful Links](#link_exercise8)).

You are encouraged to explore other options to get extra credits.
Remember to present all of your extra work in the report.

Dataset
-------

You can implement a script to generate data randomly as your input
datasets. You are also free to use public datasets such as RCV1-v2
(See [Useful Links](#link_exercise8)).

Mini-batch Kmeans
-----------------

You can refer to the paper for sequential mini-batch kmeans algorithm.
You will need to design how to parallelize the algorithm so that it can
run with large scale datasets on distributed computing environment.

![Mini-batch
Kmeans.](section/icloud/assignment/exercise8/mbkmeans){width="8cm"}

Useful Links
------------

-   [RCV1: A New Benchmark Collection for Text Categorization
    Research](http://jmlr.csail.mit.edu/papers/volume5/lewis04a/lewis04a.pdf)

-   [Harp](https://dsc-spidal.github.io/harp)

-   [Spark](http://spark.apache.org)

-   [Flink](https://flink.apache.org)

-   [Web-scale k-means clustering - D.
    Sculley](https://dl.acm.org/citation.cfm?id=1772862)
