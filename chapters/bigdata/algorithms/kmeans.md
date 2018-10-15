# Practical K-Means, Map Reduce, and Page Rank for Big Data Applications and Analytics :o:

We use the K-means Python code in SciPy package to show real code for
clustering. After a simple example we generate 4 clusters of distinct
centers and various choice for sizes using Matplotlib tor visualization.
We show results can sometimes be incorrect and sometimes make different
choices among comparable solutions. We discuss the *hill* between
different solutions and rationale for running K-means many times and
choosing best answer. Then we introduce MapReduce with the basic
architecture and a homely example. The discussion of advanced topics
includes an extension to Iterative MapReduce from Indiana University
called Twister and a generalized Map Collective model. Some measurements
of parallel performance are given. The SciPy K-means code is modified to
support a MapReduce execution style. This illustrates the key ideas of
mappers and reducers. With appropriate runtime this code would run in
parallel but here the *parallel* maps run sequentially. This simple 2
map version can be generalized to scalable parallelism. Python is used
to Calculate PageRank from Web Linkage Matrix showing several different
formulations of the basic matrix equations to finding leading
eigenvector. The unit is concluded by a calculation of PageRank for
general web pages by extracting the secret from Google.

## K-means in Practice

We introduce the k means algorithm in a gentle fashion and describes its
key features including dangers of local minima. A simple example from
Wikipedia is examined.

We use the K-means Python code in SciPy package to show real code for
clustering. After a simple example we generate 4 clusters of distinct
centers and various choice for sizes using Matplotlib tor visualization.
We show results can sometimes be incorrect and sometimes make different
choices among comparable solutions. We discuss the *hill* between
different solutions and rationale for running K-means many times and
choosing best answer.

Files:

-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/kmeans/xmean.py>
-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/kmeans/sample.csv>
-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/kmeans/parallel-kmeans.py>
-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/kmeans/kmeans-extra.py>

### K-means in Python

We use the K-means Python code in SciPy package to show real code for
clustering and applies it a set of 85 two dimensional vectors --
officially sets of weights and heights to be clustered to find T-shirt
sizes. We run through Python code with Matplotlib displays to divide
into 2-5 clusters. Then we discuss Python to generate 4 clusters of
varying sizes and centered at corners of a square in two dimensions. We
formally give the K means algorithm better than before and make
definition consistent with code in SciPy.

### Analysis of 4 Artificial Clusters

We present clustering results on the artificial set of 1000 2D points
described in previous lesson for 3 choices of cluster sizes *small*
*large* and *very large*. We emphasize the SciPy always does 20
independent K means and takes the best result -- an approach to avoiding
local minima. We allow this number of independent runs to be changed and
in particular set to 1 to generate more interesting erratic results. We
define changes in our new K means code that also has two measures of
quality allowed. The slides give many results of clustering into 2 4 6
and 8 clusters (there were only 4 real clusters). We show that the *very
small* case has two very different solutions when clustered into two
clusters and use this to discuss functions with multiple minima and a
hill between them. The lesson has both discussion of already produced
results in slides and interactive use of Python for new runs.

## Parallel K-means :o:

We modify the SciPy K-means code to support a MapReduce execution style
and runs it in this short unit. This illustrates the key ideas of
mappers and reducers. With appropriate runtime this code would run in
parallel but here the *parallel* maps run sequentially. We stress that
this simple 2 map version can be generalized to scalable parallelism.

Files:

- <https://github.com/cloudmesh-community/book/blob/master/examples/python/kmeans/parallel-kmeans.py>

## PageRank in Practice :o:

We use Python to Calculate PageRank from Web Linkage Matrix showing
several different formulations of the basic matrix equations to finding
leading eigenvector. The unit is concluded by a calculation of PageRank
for general web pages by extracting the secret from Google.

Files:

- <https://github.com/cloudmesh-community/book/blob/master/examples/python/page-rank/pagerank1.py>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/page-rank/pagerank2.py>


## Resources

-   <https://en.wikipedia.org/wiki/Kmeans>
-   <http://grids.ucs.indiana.edu/ptliupages/publications/DACIDR_camera_ready_v0.3.pdf>
-   <http://salsahpc.indiana.edu/millionseq/>
-   <http://salsafungiphy.blogspot.com/>
-   <https://en.wikipedia.org/wiki/Heuristic>
