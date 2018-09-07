Goal
====

The goal of this project is to familiarize yourself with the concept of
map-collective applications. Harp is similar to MapReduce in programming
with the exception that it provides collective communication support
across map tasks.

Deliverables
============

Zip your source code and output as username_harp-kmeans.zip. Please
submit this file to the Canvas Assignments page.

Evaluation
==========

The point total for this project is 20, where the distribution is as
follows:

-   Completeness of your code (16 points)

-   Correct output (4 points)

Prerequisites
=============

-   Before working on Harp K-Means, make sure you can successfully run
    Harp WordCount following the instructions of Lab 10 (the
    presentation is in Canvas).

-   Download **simplekmeans** folder from Canvas assignments under
    **B649_Project7** folder.

-   Copy that folder to **harp2-project-master/harp2-app/src/edu/iu**

-   Open **harp2-project-master/harp2-app/build.xml** and add the
    following line next to where you find other **include** tags. Note:
    this is within the **javac** tag of the **build.xml**\
    **\<include name="edu/iu/simplekmeans/\*\*" /\>**

K-Means Clustering Algorithm
============================

K-Means is a clustering algorithm to partition $n$ observations
$(x_1,x_2,..., x_n)$ into $k$ $(\leq n)$ sets $S=\{S_1,S_2,...,S_k\}$
clusters in which each observation belongs to the cluster with the
nearest mean of Euclidean distance. The objection function is to
minimize the sum of distance functions for each point to centroids,
where $\mu_i$ is the mean of points in $S_i$. $$\begin{aligned}
\arg\min\limits_S\sum\limits_{i=1}^k\sum\limits_{x\in S_i}{||x-\mu_i||}^2\end{aligned}$$
The input is data points (data) and the model is cluster centers
(centroids). The problem is computationally difficult (NP-hard);
however, there are efficient algorithms via an iterative refinement
approach.

![Image source:
https://en.wikipedia.org/wiki/K-means_clustering](p7-1){width="8cm"
height="2cm"}

![K-Means Clustering for MapReduce](p7-2){width="8cm" height="6cm"}

Harp Data Structure
===================

The main data structure used for this assignment is
ArrTable\<DoubleArray\>. You can think of this as a collection of double
array objects. Each double array represents a center. For example, if
the centers for your program are 3D, then each array will have $3+1$ (4)
elements. The first 3 will be the $x, y, z$ coordinates. The last
element is used to store the number of points assigned to this center.

To retrieve all the centers you can invoke the **getPartitions()**
method on ArrTable object, which will return a collection of
ArrPartition objects. To retrieve the underlying double array from these
ArrPartition objects, you can invoke the **getArray()** method on
ArrPartition object. To figure out the index (ID) of this center you can
invoke **getPartitionID()** method on the same ArrPartition object.

![Parallelization of K-means Clustering](p7-3){width="8cm" height="5cm"}

Harp Implementation
===================

Most of the code is completed for you; your task will be to perform the
nearest center finding computation and updating new centers. The code to
implement this is in the **simplekmeans/KmeansMapper.java**

The two functions are listed below.

**Finding Nearest Center**

FindingNearestCenter.java

**Updating Centers**

INPUT UpdatingCenters.java

Compilation and Running
=======================

-   To compile the code, simply go into
    **harp2-project-master/harp2-app** and type **ant**

-   Then copy the
    **harp2-project-master/harp2-app/build/harp2-app-hadoop-2.6.0.jar**
    to\
    **\$HADOOP_HOME**

-   To run the file, use the following command within
    **\$HADOOP_HOME**. This will produce 100 data points and cluster
    them into 12 clusters. We use 3D points. The program will run 2
    parallel map tasks for 20 iterations. Note: you may want to give
    unique directory names for the last two parameters each time that
    you test. Otherwise, you may run into issues because of existing
    directories. Alternatively, you can delete old directories and reuse
    the same names.

    The folder **harpkmeans** will be in HDFS. The
    **/tmp/simplekmeansdata** will be in your local disk.

    ``` {.bash language="bash"}
    $ hadoop jar harp2-app-hadoop-2.6.0.jar edu.iu.simplekmeans.KmeansMapCollective 100 12 3 2 20 harpkmeans /tmp/simplekmeansdata
    ```

-   To get the output do the following and look at the part- files as
    usual.

    ``` {.bash language="bash"}
    $ hdfs dfs -get harpkmeans/out .
    ```

\bibliographystyle{unsrt}
