# e-Commerce and LifeStyle

Recommender systems operate under the hood of such widely recognized
sites as Amazon, eBay, Monster and Netflix where everything is a
recommendation. This involves a symbiotic relationship between vendor
and buyer whereby the buyer provides the vendor with information about
their preferences, while the vendor then offers recommendations tailored
to match their needs. Kaggle competitions h improve the success of the
Netflix and other recommender systems. Attention is paid to models that
are used to compare how changes to the systems affect their overall
performance. It is interesting that the humble ranking has become such a
dominant driver of the world's economy. More examples of recommender
systems are given from Google News, Retail stores and in depth Yahoo!
covering the multi-faceted criteria used in deciding recommendations on
web sites.

The formulation of recommendations in terms of points in a space or bag
is given where bags of item properties, user properties, rankings and
users are useful. Detail is given on basic principles behind recommender
systems: user-based collaborative filtering, which uses similarities in
user rankings to predict their interests, and the Pearson correlation,
used to statistically quantify correlations between users viewed as
points in a space of items. Items are viewed as points in a space of
users in item-based collaborative filtering. The Cosine Similarity is
introduced, the difference between implicit and explicit ratings and the
k Nearest Neighbors algorithm. General features like the curse of
dimensionality in high dimensions are discussed. A simple Python k
Nearest Neighbor code and its application to an artificial data set in 3
dimensions is given. Results are visualized in Matplotlib in 2D and with
Plotviz in 3D. The concept of a training and a testing set are
introduced with training set pre labeled. Recommender system are used to
discuss clustering with k-means based clustering methods used and their
results examined in Plotviz. The original labelling is compared to
clustering results and extension to 28 clusters given. General issues in
clustering are discussed including local optima, the use of annealing to
avoid this and value of heuristic algorithms.

## Recommender Systems {#s-recommender}

We introduce Recommender systems as an optimization technology used in a
variety of applications and contexts online. They operate in the
background of such widely recognized sites as Amazon, eBay, Monster and
Netflix where everything is a recommendation. This involves a symbiotic
relationship between vendor and buyer whereby the buyer provides the
vendor with information about their preferences, while the vendor then
offers recommendations tailored to match their needs, to the benefit of
both.

There follows an exploration of the Kaggle competition site, other
recommender systems and Netflix, as well as competitions held to improve
the success of the Netflix recommender system. Finally attention is paid
to models that are used to compare how changes to the systems affect
their overall performance. It is interesting how the humble ranking has
become such a dominant driver of the world's economy.

[:scroll: Lifestyle Recommender
(45)](https://drive.google.com/open?id=0B6wqDMIyK2P7YkIwczVfQlJqVG8)

### Recommender Systems as an Optimization Problem

We define a set of general recommender systems as matching of items to
people or perhaps collections of items to collections of people where
items can be other people, products in a store, movies, jobs, events,
web pages etc. We present this as "yet another optimization problem".

[:clapper: Recommender Systems I
(8:06)](https://www.youtube.com/watch?v=kO023BIW2dw)

### Recommender Systems Introduction

We give a general discussion of recommender systems and point out that
they are particularly valuable in long tail of tems (to be recommended)
that are not commonly known. We pose them as a rating system and relate
them to information retrieval rating systems. We can contrast
recommender systems based on user profile and context; the most familiar
collaborative filtering of others ranking; item properties; knowledge
and hybrid cases mixing some or all of these.

[:clapper: Recommender Systems Introduction
(12:56)](https://youtu.be/KbjBKrzFYKg)

### Kaggle Competitions

We look at Kaggle competitions with examples from web site. In
particular we discuss an Irvine class project involving ranking jokes.

[:clapper: Kaggle Competitions: (3:36)](https://youtu.be/DFH7GPrbsJA)

:warning: Please not that we typically do not accept any projects
using kaggle data for this classes. This class is not about winning a
kaggle competition and if done wrong it does not fullfill the minimum
requiremnt for this class. Please consult with the instructor.

### Examples of Recommender Systems

We go through a list of 9 recommender systems from the same Irvine
class.

[:clapper: Examples of Recommender Systems
(1:00)](https://youtu.be/1Eh1epQj-EQ)

### Netflix on Recommender Systems

We summarize some interesting points from a tutorial from Netflix for
whom *everything is a recommendation*. Rankings are given in multiple
categories and categories that reflect user interests are especially
important. Criteria used include explicit user preferences, implicit
based on ratings and hybrid methods as well as freshness and diversity.
Netflix tries to explain the rationale of its recommendations. We give
some data on Netflix operations and some methods used in its recommender
systems. We describe the famous Netflix Kaggle competition to improve
its rating system. The analogy to maximizing click through rate is given
and the objectives of optimization are given.

[:clapper: Netflix on Recommender Systems
(14:20)](https://www.youtube.com/watch?v=ModhdIT9D24)

Next we go through Netflix's methodology in letting data speak for
itself in optimizing the recommender engine. An example iis given on
choosing self produced movies. A/B testing is discussed with examples
showing how testing does allow optimizing of sophisticated criteria.
This lesson is concluded by comments on Netflix technology and the full
spectrum of issues that are involved including user interface, data, AB
testing, systems and architectures. We comment on optimizing for a
household rather than optimizing for individuals in household.

[:clapper: Consumer Data Science (13:04)](https://youtu.be/B8cjaOQ57LI)

### Other Examples of Recommender Systems

We continue the discussion of recommender systems and their use in
e-commerce. More examples are given from Google News, Retail stores and
in depth Yahoo! covering the multi-faceted criteria used in deciding
recommendations on web sites. Then the formulation of recommendations in
terms of points in a space or bag is given.

Here bags of item properties, user properties, rankings and users are
useful. Then we go into detail on basic principles behind recommender
systems: user-based collaborative filtering, which uses similarities in
user rankings to predict their interests, and the Pearson correlation,
used to statistically quantify correlations between users viewed as
points in a space of items.

[:scroll: Lifestyle Recommender
(49)](https://drive.google.com/open?id=0B6wqDMIyK2P7UVloVElaZ2FXcTg)

We start with a quick recap of recommender systems from previous unit;
what they are with brief examples.

[:clapper: Recap and Examples of Recommender Systems
(5:48)](https://www.youtube.com/watch?v=PwS8UE4TDS4)

#### Examples of Recommender Systems

We give 2 examples in more detail: namely Google News and Markdown in
Retail.

[:clapper: Examples of Recommender Systems
(8:34)](https://youtu.be/og07mH9fU0M)

#### Recommender Systems in Yahoo Use Case Example

We describe in greatest detail the methods used to optimize Yahoo web
sites. There are two lessons discussing general approach and a third
lesson examines a particular personalized Yahoo page with its different
components. We point out the different criteria that must be blended in
making decisions; these criteria include analysis of what user does
after a particular page is clicked; is the user satisfied and cannot
that we quantified by purchase decisions etc. We need to choose
Articles, ads, modules, movies, users, updates, etc to optimize metrics
such as relevance score, CTR, revenue, engagement.These lesson stress
that if though we have big data, the recommender data is sparse. We
discuss the approach that involves both batch (offline) and on-line
(real time) components.

[:clapper: Recap of Recommender Systems II
(8:46)](https://youtu.be/FBn7HpGFNvg)

[:clapper: Recap of Recommender Systems III
(10:48)](https://youtu.be/VS2Y4lAiP5A)

[:clapper: Case Study of Recommender systems
(3:21)](https://youtu.be/HrRJWEF8EfU)

#### User-based nearest-neighbor collaborative filtering

Collaborative filtering is a core approach to recommender systems. There
is user-based and item-based collaborative filtering and here we discuss
the user-based case. Here similarities in user rankings allow one to
predict their interests, and typically this quantified by the Pearson
correlation, used to statistically quantify correlations between users.

[:clapper: User-based nearest-neighbor collaborative filtering I
(7:20)](https://youtu.be/lsf_AE-8dSk)

[:clapper: User-based nearest-neighbor collaborative filtering II
(7:29)](https://youtu.be/U7-qeX2ItPk)

#### Vector Space Formulation of Recommender Systems

We go through recommender systems thinking of them as formulated in a
funny vector space. This suggests using clustering to make
recommendations.

[:clapper: Vector Space Formulation of Recommender Systems new
(9:06)](https://youtu.be/IlQUZOXlaSU)

### Resources

-   <http://pages.cs.wisc.edu/~beechung/icml11-tutorial/>

## Item-based Collaborative Filtering and its Technologies

We move on to item-based collaborative filtering where items are viewed
as points in a space of users. The Cosine Similarity is introduced, the
difference between implicit and explicit ratings and the k Nearest
Neighbors algorithm. General features like the curse of dimensionality
in high dimensions are discussed.

[:scroll: Lifestyle Filtering
(18)](https://drive.google.com/open?id=0B6wqDMIyK2P7UExxVFc5YlpOZ28)

### Item-based Collaborative Filtering

We covered user-based collaborative filtering in the previous unit. Here
we start by discussing memory-based real time and model based offline
(batch) approaches. Now we look at item-based collaborative filtering
where items are viewed in the space of users and the cosine measure is
used to quantify distances. WE discuss optimizations and how batch
processing can help. We discuss different Likert ranking scales and
issues with new items that do not have a significant number of rankings.

[:clapper: Item Based Filtering
(11:18)](https://www.youtube.com/watch?v=HTdYGaOTlFI)

[:clapper: k Nearest Neighbors and High Dimensional Spaces
(7:16)](https://youtu.be/SM8EJdAa4mw)

### k-Nearest Neighbors and High Dimensional Spaces {#s-knn}

We define the k Nearest Neighbor algorithms and present the Python
software but do not use it. We give examples from Wikipedia and describe
performance issues. This algorithm illustrates the curse of
dimensionality. If items were a real vectors in a low dimension space,
there would be faster solution methods.

[:clapper: k Nearest Neighbors and High Dimensional Spaces
(10:03)](https://youtu.be/2NqUsDGQDy8)


#### Recommender Systems - K-Neighbors

Next we provide some sample Python code for the k Nearest Neighbor and its application to
an artificial data set in 3 dimensions. Results are visualized in
Matplotlib in 2D and with Plotviz in 3D. The concept of training and
testing sets are introduced with training set pre-labelled.
This lesson is adapted from the Python k Nearest Neighbor code found on the
web associated with a book by Harrington on Machine Learning [??]. There are
two data sets. First we consider a set of 4 2D vectors divided into two
categories (clusters) and use k=3 Nearest Neighbor algorithm to classify
3 test points. Second we consider a 3D dataset that has already been
classified and show how to normalize. In this lesson we just use
Matplotlib to give 2D plots.


The lesson goes through an example of using k NN classification
algorithm by dividing dataset into 2 subsets. One is training set with
initial classification; the other is test point to be classified by k=3
NN using training set. The code records fraction of points with a
different classification from that input. One can experiment with
different sizes of the two subsets. The Python implementation of
algorithm is analyzed in detail.

#### Plotviz

The clustering methods are used and their results examined in
Plotviz. The original labelling is compared to clustering results and
extension to 28 clusters given.  General issues in clustering are
discussed including local optima, the use of annealing to avoid this
and value of heuristic algorithms.


#### Files

- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/kNN.py>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/kNN_Driver.py>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/dating_test_set2.txt>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/clusterFinal-M3-C3Dating-ReClustered.pviz>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/dating_rating_original_labels.pviz>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/knn/clusterFinal-M30-C28.pviz>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/plotviz/clusterfinal_m3_c3dating_reclustered.pviz>
- <https://github.com/cloudmesh-community/book/blob/master/examples/python/plotviz/fungi_lsu_3_15_to_3_26_zeroidx.pviz>

### k-Means


### Resources

-   <http://www.slideshare.net/xamat/building-largescale-realworld-recommender-systems-recsys2012-tutorial> [@www-slideshare-building]
-   <http://www.ifi.uzh.ch/ce/teaching/spring2012/16-Recommender-Systems_Slides.pdf> [@www-ifi-teaching]
-   <https://www.kaggle.com/> [@www-kaggle]
-   <http://www.ics.uci.edu/~welling/teaching/CS77Bwinter12/CS77B_w12.html> [www-ics-uci-welling]
-   [Jeff
    Hammerbacher](https://berkeleydatascience.files.wordpress.com/2012/01/20120117berkeley1.pdf)[@20120117berkeley1]
-   <http://www.techworld.com/news/apps/netflix-foretells-house-of-cards-success-with-cassandra-big-data-engine-3437514/> [@www-techworld-netflix]
-   <https://en.wikipedia.org/wiki/A/B_testing> [@wikipedia-ABtesting]
-   <http://www.infoq.com/presentations/Netflix-Architecture> [@www-infoq-architec]
