How to Run MapReduce (PaaS)
===========================

-   15 Video lectures (1 hour 58 minutes 4 seconds)

Apache Data Analysis Open Stack
-------------------------------

The buildup of Big Data has seen the development of new data storage
systems like MapReduce and Hadoop. Apache's Big Data Stack houses a host
of programs designed around Google's offerings like MapReduce. The
architecture of Hadoop 1.0 and 2.0 are compared, along with an
examination of the MapReduce concept. A demo video of Twister-MDS
includes a 3-dimensional representation of data cluster sorting through
the PlotViz program. Data analysis tool Twister boasts features like
in-memory support of tasks, data flow separation, and portability.

-   Video: [Youtube](https://www.youtube.com/watch?v=6vkgvGtyv4Q)
    (12:01)

-   Slide:
    [PDF](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

MapReduce
---------

MapReduce was designed by Google to address the problem of large-scale
data processing. A breakdown of basic MapReduce terms and functions
follows. Use of MapReduce has flourished since its premier, as
illustrated by an in-depth example of its use in WordCount. Finally the
basic process of MapReduce is shown.

-   Video: [Youtube](https://www.youtube.com/watch?v=sSIGaDaulvA) (9:07)

-   Slide: [PDF (Page
    6-14)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

Hadoop Framework
----------------

Hadoop is an open source version of MapReduce designed for broad
application in terms of code and settings. Storage is done in the Hadoop
Distributed File System through master and slave nodes. Compute is
handled by JobTracker and TaskTracker; the duties of these two
intertwined programs are then explored more fully.

-   Video: [Youtube](https://www.youtube.com/watch?v=Vuroqly6FTE) (8:32)

-   Slide: [PDF (Page
    15-23)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

Hadoop Tasks
------------

The Map stage of MapReduce is shown in greater detail. This process
starts with Hadoop Distributed File System, which handles the input
data. Key value pairs are assigned to the data blocks. Combiner reduces
data size and Partitioner determines distribution of keys among
reducers. Intermediate data is stored in a circular buffer before being
sent to reduce tasks. Shuffle and Merge are used to order and reduce
size of intermediate data. Reduce tasks take over then to determine the
output data format. A final chart illustrates the concept of parallelism
in MapReduce.

-   Video: [Youtube](https://www.youtube.com/watch?v=UN4t3tvdjms)
    (11:01)

-   Slide: [PDF (Page
    24-35)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

Fault Tolerance
---------------

Fault tolerance is a natural benefit of MapReduce. The master node pings
worker nodes regularly to verify they are working, and acts accordingly
if they do not respond. A diagram illustrates the files which are in
charge of things like number of map and reduce tasks, and what to do
when the limit is reached on the buffer. The lecture ends with a
discussion of class assignments.

-   Video: [Youtube](https://www.youtube.com/watch?v=a3AlOTmD42k) (2:45)

-   Slide: [PDF (Page
    36-41)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

Programming on a Computer Cluster
---------------------------------

Hadoop is now a large part of Yahoo!'s system setup, as well as handling
a tremendous variety of data in other areas like medicine and business.
A list of time spans for actions in system requirements is given. The
original MapReduce was designed to resolve problems like load balancing
and machine failures.

-   Video: [Youtube](https://www.youtube.com/watch?v=rRR2ALa5CUA) (6:01)

-   Slide: [PDF (Page
    1-7)](https://drive.google.com/open?id=0B88HKpainTSfd3hkTG4yY2FYUVE)

How Hadoop Runs on a MapReduce Job
----------------------------------

A detailed diagram of the MapReduce job framework is given. This
includes task status updates, shuffling, and writing data to nodes.
MapReduce is a C++ framework, while Hadoop is written in Java. Shuffling
and sorting occurs in the map phase. Reduce reads and writes files to
HDFS, and the merger generates the final result. The second Quiz is
given at the end.

-   Video: [Youtube](https://www.youtube.com/watch?v=KWLY_maNEPA) (9:25)


-   Slide: [PDF (Page
    8-15)](https://drive.google.com/open?id=0B88HKpainTSfd3hkTG4yY2FYUVE)

Literature Review
-----------------

This video deals primarily with scientific papers written on the topic
of MapReduce and related programs. There is a certain criteria for
judging scientific submissions. The first paper highlights Google File
System, covering topics like data chunks, metadata, and replicas. This
is followed by MapReduce and BigTable.

-   Video: [Youtube](https://www.youtube.com/watch?v=5YmjrhEFQsk) (9:43)

-   Slide: [PDF (Page
    16-27)](https://drive.google.com/open?id=0B88HKpainTSfd3hkTG4yY2FYUVE)

Introduction to BLAST
---------------------

There are four types of programming model communication patterns:
embarrassingly parallel (only map), classic map/reduce, iterative
map/reduce, and loosely synchronous. The basic bioinformatics BLAST
(Basic Local Alignment Sequence Tool) program data flow is illustrated.
An example of database creation comes from the Seattle Children's
Hospital. BLAST uses scores to find similar sequences in databases.

-   Video: [Youtube](https://www.youtube.com/watch?v=i3H9HmUYfq8) (8:27)

-   Slide: [PDF (Page
    1-12)](https://drive.google.com/open?id=0B88HKpainTSfdnFvY1V3dlFTRlE)

BLAST Parallelization
---------------------

The role of master and worker nodes in BLAST multi-thread usage is
discussed. BLAST can be parallelized in several ways: multi-thread,
query segmentation, and database segmentation. BLAST is pleasingly
parallel in application, but many programs are not. Further information
about articles featuring BLAST is provided at the end.

-   Video: [Youtube](https://www.youtube.com/watch?v=isc0MjkwTlk) (4:44)

-   Slide: [PDF (Page
    13-19)](https://drive.google.com/open?id=0B88HKpainTSfdnFvY1V3dlFTRlE)

SIMD vs MIMD;SPMD vs MPMD
-------------------------

Four types of parallel models: SISD (traditional PCs), SIMD (GPUs), MISD
(shuttle flight control computer), MIMD (distributed systems).
Point-to-point (P2P) communication in MPI is used as an example of
parallelization. Each successive process adds its own stamp to the data
before passing it on to the next. Matrix multiplication for scientific
applications differs from the norm in that data is sent in a matrix, not
a string. WordCount functions in a map/reduce pattern. These are all
types of SIMD. SPMD and MPMD are two other types of model.

\* Video: [Youtube](https://www.youtube.com/watch?v=zHQiR56Zmtc) (9:42)
.. todo: slide is missing

Data Locality
-------------

A brief review is given of previous topics. As opposed to MPI and HPC,
MapReduce brings the computation to the data, rather than vice-versa.
This is done to limit energy usage and network congestion. Several
factors such as number of nodes and tasks can impact data locality. An
equation to improve data locality is tested in an experiment, whose
results are given. By default, Hadoop determines scheduling of tasks to
available slots in terms of best local composition, not global.

-   Video: [Youtube](https://www.youtube.com/watch?v=RqLA7_asK50) (8:36)

-   Slide: [PDF (Page
    10-16)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

Optimal Data Locality
---------------------

Global data optimization can be achieved through a proposed algorithm
given here. Task, slot, and cost are factors in this algorithm. Network
bandwidth must also be taken into consideration when assigning tasks to
slots. Linear Sum Assignment Problems require greater time to finish
when matrix size is increased. Two different scheduling algorithms were
designed to improve the original one in Hadoop. An experiment was run
comparing all three, with the network topology-aware algorithm clearly
outperforming the others.

-   Video: [Youtube](https://www.youtube.com/watch?v=Ok8vdrFXo5w) (4:17)

-   Slide: [PDF (Page
    17-28)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

Task Granularity
----------------

Size of data blocks affects load balancing and overhead. Using Bag of
Divisible Tasks method, tasks can be split into sub-tasks and
distributed amongst slots to maximize efficiency. When splitting tasks,
one must take into account when and which tasks to split, as well as how
and how many. In our current proposed algorithm, tasks are split until
each slot is occupied. It also uses ASPK (Aggressive Scheduling with
Prior Knowledge) to split larger tasks first and when the performance
gain is deemed optimal. Optimal and Expected Remaining Job Execution
Time can help determine task splitting. Several examples are offered
with either single or multiple jobs.

-   Video: [Youtube](https://www.youtube.com/watch?v=u9UpgTnOZz4) (9:51)

-   Slide: [PDF (Page
    29-44)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

Resource Utilization and Speculative Execution
----------------------------------------------

Resource stealing involves appropriating cores that are kept in reserve
on separate nodes and returning them when the computation is over.
Speculative execution addresses fault tolerance; when the master node
notices a task is running slowly, it will start a speculative task which
can take over if it is determined the original task will not finish in
time. Overuse of speculative tasks can lead to poor data locality and
higher energy demands.

-   Video: [Youtube](https://www.youtube.com/watch?v=wWyFiqDIYus) (3:52)


-   Slide: [PDF (Page
    46-53)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)
