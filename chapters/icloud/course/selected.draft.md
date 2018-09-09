Selected Cloud Computing Lectures
=================================

Cloud and MapReduce
-------------------

This lecture gives a brief introduction of Infrastructure as a Service
(IaaS), Platform as a Service (PaaS), and Software as a Service (PaaS)
and MapReduce on clusters. Google systems are also described regarding
to parallel processing and MapReduce communication patterns are explained
like Embarrassingly Parallel, Classical MapReduce, Iterative Reductions
and Loosely Synchronous e.g. MPI.

[:clapper: Cloud and MapReduce (10:17)](https://www.youtube.com/watch?v=_irz3v1gT-A)

[:scroll: IaaS, PaaS and SaaS (25)](https://drive.google.com/open?id=1eXWtNlQ_jgeq_nVS_9B7MTaiDjzddXjC)

Hadoop Framework
----------------

Hadoop components are explained i.e. JobTracker, TaskTracker, MapTask,
ReduceTask including HDFS.

[:clapper: Hadoop Components including HDFS (8:32)](https://www.youtube.com/watch?v=Vuroqly6FTE)

[:scroll: Hadoop Components including HDFS (15)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

[:scroll: Hadoop Components including HDFS - pptx (15)](https://drive.google.com/open?id=0B88HKpainTSfTVlNRzRMemNaZEU)

Hadoop Framework II
-------------------

A detailed diagram of the MapReduce job framework is given. This
includes task status updates, shuffling, and writing data to nodes.
MapReduce is a C++ framework, while Hadoop is written in Java. Shuffling
and sorting occurs in the map phase. Reduce reads and writes files to
HDFS, and the merger generates the final result. The second Quiz is
given at the end.

[:clapper: Hadoop Framework II (9:25)](https://www.youtube.com/watch?v=KWLY_maNEPA)

[:scroll: Hadoop Framework II (8)](https://drive.google.com/open?id=0B88HKpainTSfd3hkTG4yY2FYUVE)

[:scroll: Hadoop Framework II - pptx (8)](https://drive.google.com/open?id=0B88HKpainTSfcUkwN0l1VHBEdlU)

Walk Through MapReduce: Hadoop Tasks
-------------------------------------------------

This lecture gives a walk through explanation of map and reduce task
under Hadoop and HDFS framework. Map stage starts with Hadoop Distributed
File System (HDFS) where stores key value pairs assigned to the data
blocks. In the next stage, the combiner reduces data size and the
partitioner determines distribution of keys among reducers. Intermediate
data is stored in a circular buffer before being sent to reduce tasks.
In detail, Shuffle and Merge are used to order and reduce size of
intermediate data. The last stage, Reduce, handles each group of output
data, per key, in parallel.

[:clapper: 11:01 Hadoop Tasks (Step-by-Step)](https://www.youtube.com/watch?v=UN4t3tvdjms)

[:scroll: Hadoop Tasks (24)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

[:scroll: Hadoop Tasks - pptx (24)](https://drive.google.com/open?id=0B88HKpainTSfTVlNRzRMemNaZEU)

Google File System and BigTable
-------------------------------

THis lecture reviews papers in MapReduce developments such as Google
File System (GFS), and BigTable and introduces other research projects
e.g. Microsoft Dryad, a distributed execution engine for data parallel
applications. In Google File System, data chunks, metadata, and replicas
are briefly discussed.

[:clapper: GFS and BigTable (9:43)](https://www.youtube.com/watch?v=5YmjrhEFQsk)

[:scroll: GFS and BigTable (16)](https://drive.google.com/open?id=0B88HKpainTSfd3hkTG4yY2FYUVE)

[:scroll: GFS and BigTable - pptx (16)](https://drive.google.com/open?id=0B88HKpainTSfcUkwN0l1VHBEdlU)

MapReduce Example - WordCount
-----------------------------

MapReduce is revisited with the WordCount example to demonstrate how it
actually works in the map and reduce phase.

[:clapper: MapReduce WordCount (9:07)](https://www.youtube.com/watch?v=sSIGaDaulvA)

[:scroll: MapReduce WordCount (6)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

[:scroll: MapReduce WordCount - pptx (6)](https://drive.google.com/open?id=0B88HKpainTSfTVlNRzRMemNaZEU)

MapReduce Example - Twister
---------------------------

At 5:26 of the video, Twister, in-memory iterative MapReduce framework,
is introduced with MDS (Multidimensional Scaling) example to process 30K
metagenomics dataset. This is part of published work by Zhang, Bingjing,
et al. \"Applying twister to scientific applications.\" Cloud Computing
Technology and Science (CloudCom), 2010 IEEE Second International
Conference on. IEEE, 2010. In addition, there is an additional
walk-through tutorial recorded on Youtube,

<https://www.youtube.com/watch?v=jTUD_yLrW1s>

which includes a 3-dimensional representation of data cluster sorting by
the PlotViz program developed by Indiana University. The architecture
between Hadoop 1 and 2 are explained in the beginning along with
MapReduce.

[:clapper: Twister Introduction (12:01)](https://www.youtube.com/watch?v=6vkgvGtyv4Q)

[:scroll: MapReduce and Twister (1)](https://drive.google.com/open?id=0B88HKpainTSfMnpCelpNQUpNdVE)

[:scroll: MapReduce and Twister (1)](https://drive.google.com/open?id=0B88HKpainTSfTVlNRzRMemNaZEU)

Embarrassingly Parallel Example, Basic Local Alignment Search Tool (BLAST)
--------------------------------------------------------------------------

The bioinformatics tool, BLAST (Basic Local Alignment Sequence Tool) is
a good example of embarrassingly parallel. This lecture shows an use case
with data collected from the Seattle Children's Hospital to find similar
sequences in databases in parallel. Blast introduction starts at 2:12.
BLAST can be parallelized in several ways: query
segmentation, and database segmentation.

[:clapper: 8:27 Introduction to BLAST (multi-thread,)](https://www.youtube.com/watch?v=i3H9HmUYfq8)

[:scroll: Introduction to BLAST (1)](https://drive.google.com/open?id=0B88HKpainTSfdnFvY1V3dlFTRlE)

[:scroll: Introduction to BLAST - pptx (1)](https://drive.google.com/open?id=0B88HKpainTSfMDAwZm5uQlZWckU)

[:clapper: BLAST Parallelization (4:44)](https://www.youtube.com/watch?v=isc0MjkwTlk)

[:scroll: BLAST Parallelization (13)](https://drive.google.com/open?id=0B88HKpainTSfdnFvY1V3dlFTRlE)

[:scroll: BLAST Parallelization - pptx (13)](https://drive.google.com/open?id=0B88HKpainTSfcUkwN0l1VHBEdlU)

MapReduce Optimization - Data Locality
--------------------------------------

A brief review is given of previous topics. As opposed to MPI and HPC,
MapReduce brings the computation to the data, rather than vice-versa.
This is done to limit energy usage and network congestion. Several
factors such as number of nodes and tasks can impact data locality. An
equation to improve data locality is tested in an experiment, whose
results are given. By default, Hadoop determines scheduling of tasks to
available slots in terms of best local composition, not global.

[:clapper: Data Locality (8:36)](https://www.youtube.com/watch?v=RqLA7_asK50)

[:scroll: Data Locality (10)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

[:scroll: Data Locality - pptx (10)](https://drive.google.com/open?id=0B88HKpainTSfVGdyVzNjTzdfb3c)

MapReduce Optimization - Optimal Data Locality
----------------------------------------------

Global data optimization can be achieved through a proposed algorithm
given here. Task, slot, and cost are factors in this algorithm. Network
bandwidth must also be taken into consideration when assigning tasks to
slots. Linear Sum Assignment Problems require greater time to finish
when matrix size is increased. Two different scheduling algorithms were
designed to improve the original one in Hadoop. An experiment was run
comparing all three, with the network topology-aware algorithm clearly
outperforming the others.

[:clapper: Optimal Data Locality (4:17)](https://www.youtube.com/watch?v=Ok8vdrFXo5w)

[:scroll: Optimal Data Locality (17)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

[:scroll: Optimal Data Locality - pptx (17)](https://drive.google.com/open?id=0B88HKpainTSfVGdyVzNjTzdfb3c)

MapReduce Optimization - Task Granularity
-----------------------------------------

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

[:clapper: Task Granularity (9:51)](https://www.youtube.com/watch?v=u9UpgTnOZz4)

[:scroll: Task Granularity (29)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

[:scroll: Task Granularity - pptx (29)](https://drive.google.com/open?id=0B88HKpainTSfVGdyVzNjTzdfb3c)

MapReduce Optimization - Resource Utilization and Speculative Execution
-----------------------------------------------------------------------

Resource stealing involves appropriating cores that are kept in reserve
on separate nodes and returning them when the computation is over.
Speculative execution addresses fault tolerance; when the master node
notices a task is running slowly, it will start a speculative task which
can take over if it is determined the original task will not finish in
time. Overuse of speculative tasks can lead to poor data locality and
higher energy demands.

[:clapper: Resource Utilization and Speculative Execution (3:52)](https://www.youtube.com/watch?v=wWyFiqDIYus)

[:scroll: Resource Utilization and Speculative Execution (46)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

[:scroll: Resource Utilization and Speculative Execution - pptx (46)](https://drive.google.com/open?id=0B88HKpainTSfVGdyVzNjTzdfb3c)

Appendix; SIMD vs MIMD;SPMD vs MPMD
-----------------------------------

Four types of parallel models: (traditional PCs), SIMD (GPUs), MISD
(shuttle flight control computer), MIMD (distributed systems).
Point-to-point (P2P) communication in MPI is used as an example of
parallelization. Each successive process adds its own stamp to the data
before passing it on to the next. Matrix multiplication for scientific
applications differs from the norm in that data is sent in a matrix, not
a string. WordCount functions in a map/reduce pattern. These are all
types of SIMD. SPMD and MPMD are two other types of model.

[:clapper: SIMD vs MIMD;SPMD vs MPMD (SISD) (9:42)](https://www.youtube.com/watch?v=zHQiR56Zmtc)

[:scroll: SIMD vs MIMD;SPMD vs MPMD (1)](https://drive.google.com/open?id=0B88HKpainTSfT28zLTdKYWhGdGM)

[:scroll: SIMD vs MIMD;SPMD vs MPMD - pptx (1)](https://drive.google.com/open?id=0B88HKpainTSfVGdyVzNjTzdfb3c)

