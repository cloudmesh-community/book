How to Run Iterative MapReduce (PaaS)
=====================================

-   12 Video lectures (1 hour 37 minutes 32 seconds)

MapReduce Refresher
-------------------

A review covers cloud computing levels, MapReduce, the course structure,
etc. This is followed by a look at Google and their initial offering,
Google search engine. Amount of tasks performed on this engine increased
considerably over the course of a single decade.

-   Video: [Youtube](https://www.youtube.com/watch?v=0TRTdzgC_N0) (9:00)

Google Search Engine 1
----------------------

The Google web server relies on index and doc servers. Index servers
allow the search engine to not have to depend on manually checking every
document, reducing computing power demands. Index partitioning can be
accomplished either through subsets of documents or words. Basic
differences between index and doc servers are discussed. Cache servers
save previous query results and can bypass index/doc servers for repeat
queries.

-   Video: [Youtube](https://www.youtube.com/watch?v=S2oT7uMw5Yg) (8:04)

-   Slide: [PDF (Page
    15-20)](https://drive.google.com/open?id=0B88HKpainTSfYWZ0dDlrNThkVms)

Google Search Engine 2
----------------------

Cache servers greatly enhance the performance of search engines.
However, this duplication of queries can lead to higher latency.
Crawling in a search engine handles subsets of websites. Batch indexing
is the simplest way to create indexes, although it lacks advanced
features like checkpointing, which could lead to issues down the line.
In-memory index added to Google over a decade ago; increases throughput
and decreases latency. Image-based and video-based searches were added
in 2007, among others. Google File System, MapReduce and BigTable are
key components of Google's current search structure. A discussion of the
initial Google proposal paper follows.

-   Video: [Youtube](https://www.youtube.com/watch?v=pxos3Yt6y6I) (8:32)

-   Slide: [PDF (Page
    21-26)](https://drive.google.com/open?id=0B88HKpainTSfYWZ0dDlrNThkVms)

Hadoop PageRank
---------------

PageRank algorithm in Google ranks a webpage's popularity and relevance.
The PageRank calculation formula is examined. After this comes an
example of its performance and further mathematical formulae involved in
its application.

-   Video: [Youtube](https://www.youtube.com/watch?v=GCp5OLLOrH0) (7:58)

-   Slide: [PDF (Page
    1-9)](https://drive.google.com/open?id=0B88HKpainTSfWFpEZGxqSWRTYms)

Discussions & Parallel Thinking
-------------------------------

Four types of MapReduce: pleasingly parallel, classic, iterative, and
loosely synchronous. A diagram shows the flow of data in MapReduce.
Specific formulae for PageRank are shown with and without the damping
factor. Key-value pairs can be written in matrix form by defining the
keys as nodes. Map tasks must make sure to handle dangling nodes
(isolated from neighbors), distributed page-rank contribution, and
reducer output being the same format as map input. Reduce input is
key-value pairs. Ideas behind parallel thinking are analyzed, along with
a list of related reading. Seven important questions are asked
concerning parallel computing. 13 'Dwarves' are different methods of
parallel computing, including MapReduce.

-   Video: [Youtube](https://www.youtube.com/watch?v=ISJp7TUzo1s)
    (11:12)

-   Slide: [PDF (Page
    10-21)](https://drive.google.com/open?id=0B88HKpainTSfWFpEZGxqSWRTYms)

Hadoop Extensions
-----------------

A model of MapReduce shows its structure. Dryad is Microsoft's version
of parallel processing. Twister is an iterative map-reduce framework, as
are Hadoop, Spark and Pregel. A comparison of their features and
capabilities is included.

-   Video: [Youtube](https://www.youtube.com/watch?v=gS7TImRZZ1g) (5:37)

Iterative MapReduce Models
--------------------------

An introduction to the idea of iterative MapReduce. An overview of other
MapReduce models follows. Map Only model has parallel map tasks with no
communication between them. Classic MapReduce involves parallel map
tasks and reduce tasks which aggregate output and allow legacy code.
Loosely Synchronous is an MPI model used in computation and
communication of scientific applications.

-   Video: [Youtube](https://www.youtube.com/watch?v=CXDdWmAWIvk) (6:46)

-   Slide: [PDF (Page
    1-3)](https://drive.google.com/open?id=0B88HKpainTSfMFBaNHprbWJwQms)

Parallel Processes
------------------

CPU performance increases according to Moore's Law can no longer keep up
with the high volume of data being generated. Multi-core architecture is
a response to this issue. It requires runtime approaches supporting
parallelism, either data-centric for higher throughput (MapReduce) or
the traditional HPC approach for optimized computation performance
(MPI). MapReduce allows for moving computation to the data. A diagram
illustrates the base MapReduce process. MapReduce is designed to improve
I/O and handle intermediate data, task scheduling, and fault tolerance.
Versions of MapReduce like Hadoop, Dryad and MPI boast different
features and programming languages.

-   Video: [Youtube](https://www.youtube.com/watch?v=JAYvkIZ8TuE) (9:44)

-   Slide: [PDF (Page
    4-9)](https://drive.google.com/open?id=0B88HKpainTSfMFBaNHprbWJwQms)

Static and Variable Data
------------------------

Iterative MapReduce was introduced to support high performance systems.
It runs iterations of the map/reduce cycles. Data mining algorithms like
K-means run numerous iterations. Static data such as data points in
K-means does not change, while variable data can alter between each
iteration. A naïve iterative MapReduce model can generate huge overhead
owing to constantly referencing static data. This can be overcome with
long-running map/reduce tasks that distinguish between static and
variable data. You can also accelerate the intermediate data transfer or
combine the output of all reduce tasks. Iterative MapReduce is shown in
the Twister program, which uses the combine output method and determines
at the end of every iteration whether to stop or continue with further
iterations. The master node in Twister is the Twister Driver, and the
slave nodes are Twister Daemons. Twister stores I/O data in partition
files. Three MapReduce patterns in Twister: 1) Large input data, reduced
in the end; 2) Data size is constant; 3) Data volume increases after
MapReduce execution. Data Manipulation Tool handles data loading and
uses metadata to keep track of data in partitions. Twister employs
static scheduling. Fault tolerance is reserved for failures that
terminate running tasks. Static data can then be used to reassign the
failed iterations. A list of Twister APIs is given.

-   Video: [Youtube](https://www.youtube.com/watch?v=UJHQ3VvWOTA)
    (11:01)

-   Slide: [PDF (Page
    10-23)](https://drive.google.com/open?id=0B88HKpainTSfMFBaNHprbWJwQms)

MapReduce Model Comparison
--------------------------

This video showcases examples of work done comparing Twister results
with Hadoop, MPI and DryadLINQ. The first is Map Only with CAP3 DNA
Sequence Assembly, followed by Classic MapReduce with Pair-wise
Sequences and High-Energy Physics, Iterative with K-means clustering,
PageRank and Multi-dimensional Scaling, and finally Loosely Synchronous
with Matrix Multiplication Algorithms. In all cases, Twister outperforms
or is close to the competition.

-   Video: [Youtube](https://www.youtube.com/watch?v=n7RVGrC-wcs) (6:56)

-   Slide: [PDF (Page
    24-33)](https://drive.google.com/open?id=0B88HKpainTSfMFBaNHprbWJwQms)

Twister K-means
---------------

Twister is applied to K-means Clustering. K-means develops a set number
of clusters by creating cluster centers (centroids) that encompass the
data points after successive proximity calculations. Parallelization of
K-means is accomplished in the partitions, and the final centroids are
determined in the Reduce step. A sample of K-means Clustering code
follows, after which Twister is shown being used to determine centroids
on K-means. Several questions are posed pertaining to the features of
Twister. The results of a Twister K-means run are compared with those
from a sequential run. Shown here, as the number of data points
increases, Twister's runtimes get progressively faster. In a final set
of runs against Hadoop, DryadLINQ, and MPI, Twister outperforms all but
MPI.

-   Video: [Youtube](https://www.youtube.com/watch?v=-G5jlzABo-Y) (7:28)

-   Slide: [PDF (Page
    34-42)](https://drive.google.com/open?id=0B88HKpainTSfMFBaNHprbWJwQms)

Coding & Iterative Alternatives
-------------------------------

A more detailed look is taken at the code used to run Twister K-means.
MapReduce has many programs designed around its setup, including other
iterative versions like Hadoop, Pregel, and Spark. Twister can extend
the use of traditional MapReduce to more complex applications.

-   Video: [Youtube](https://www.youtube.com/watch?v=QTCpiwnwjvo) (5:14)

-   Slide: [PDF (Page
    43-51)](https://drive.google.com/open?id=0B88HKpainTSfMFBaNHprbWJwQms)
