# Technology Training - kNN and Clustering :o:

This section is meant to provide a discussion on the kth Nearest
Neighbor (kNN) algorithm and clustering using K-means. Python version
for kNN is discussed in the video and instructions for both Java and
Python are mentioned in the slides. Plotviz is used for generating 3D
visualizations.

## Recommender Systems - K-Neighbors

We discuss simple Python k Nearest Neighbor code and its application to
an artificial data set in 3 dimensions. Results are visualized in
Matplotlib in 2D and with Plotviz in 3D. The concept of training and
testing sets are introduced with training set pre-labelled.

Files:

- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/kNN.py>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/kNN_Driver.py>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/dating_test_set2.txt>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/clusterFinal-M3-C3Dating-ReClustered.pviz>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/dating_rating_original_labels.pviz>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/clusterFinal-M30-C28.pviz>

## Python k'th Nearest Neighbor Algorithms

This lesson considers the Python k Nearest Neighbor code found on the
web associated with a book by Harrington on Machine Learning. There are
two data sets. First we consider a set of 4 2D vectors divided into two
categories (clusters) and use k=3 Nearest Neighbor algorithm to classify
3 test points. Second we consider a 3D dataset that has already been
classified and show how to normalize. In this lesson we just use
Matplotlib to give 2D plots.

## 3D Visualization

The lesson modifies the online code to allow it to produce files
readable by PlotViz. We visualize already classified 3D set and rotate
in 3D.

## Testing k'th Nearest Neighbor Algorithms

The lesson goes through an example of using k NN classification
algorithm by dividing dataset into 2 subsets. One is training set with
initial classification; the other is test point to be classified by k=3
NN using training set. The code records fraction of points with a
different classification from that input. One can experiment with
different sizes of the two subsets. The Python implementation of
algorithm is analyzed in detail.

## Clustering and methods

We use example of recommender system to discuss clustering. The details
of methods are not discussed but k-means based clustering methods are
used and their results examined in Plotviz. The original labelling is
compared to clustering results and extension to 28 clusters given.
General issues in clustering are discussed including local optima, the
use of annealing to avoid this and value of heuristic algorithms.

Files:

-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/plotviz/fungi_lsu_3_15_to_3_26_zeroidx.pviz>
-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/plotviz/datingrating_originallabels.pviz>
-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/plotviz/clusterFinal-M30-C28.pviz>
-   <https://github.com/cloudmesh-community/book/blob/master/examples/python/plotviz/clusterfinal_m3_c3dating_reclustered.pviz>

## Kmeans Clustering

We introduce the k means algorithm in a gentle fashion and describes its
key features including dangers of local minima. A simple example from
Wikipedia is examined.

## Clustering of Recommender System Example

Plotviz is used to examine and compare the original classification with
an *optimal* clustering into 3 clusters using a fancy deterministic
annealing method that is similar to k means. The new clustering has
centers marked.

## Clustering of Recommender Example into more than 3 Clusters

The previous division into 3 clusters is compared into a clustering into
28 separate clusters that are naturally smaller in size and divide 3D
space covered by 1000 points into compact geometrically local regions.

## Local Optima in Clustering

This lesson introduces some general principles. First many important
processes are *just* optimization problems. Most such problems are rife
with local optima. The key idea behind annealing to avoid local optima
is described. The pervasive greedy optimization method is described.

## Clustering in General

The two different applications of clustering are described. First find
geometrically distinct regions and secondly divide spaces into
geometrically compact regions that may have no *thin air* between them.
Generalizations such as mixture models and latent factor methods are
just mentioned. The important distinction between applications in vector
spaces and those where only inter-point distances are defined is
described. Examples are then given using PlotViz from 2D clustering of a
mass spectrometry example and the results of clustering genomic data
mapped into 3D with Multi Dimensional Scaling MDS.

## Heuristics

Some remarks are given on heuristics; why are they so important why
getting exact answers is often not so important?

\TODO{These resources have not all been checked to see if they still
  exist this is curretnly in progress}

## Resources

-   <https://en.wikipedia.org/wiki/Kmeans>
-   <http://grids.ucs.indiana.edu/ptliupages/publications/DACIDR_camera_ready_v0.3.pdf>
-   <http://salsahpc.indiana.edu/millionseq/>
-   <http://salsafungiphy.blogspot.com/>
-   <https://en.wikipedia.org/wiki/Heuristic>
