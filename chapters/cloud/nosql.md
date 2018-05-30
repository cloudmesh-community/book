How to Store Data (NoSQL)
=========================

\TODO{Tyler: use our video and slide macro}
-   11 Video lectures (1 hour 26 minutes 8 seconds)

RDBMS vs. NoSQL
---------------

-   Video: [Youtube](https://www.youtube.com/watch?v=dJunqER9lb8) (9:22)

-   Slide: [PDF (Page
    1-10)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

NoSQL Characteristics
---------------------

Clouds have arisen as an answer to the data demands of social media.
Three major programs for NoSQL are BigTable, Dynamo, and CAP theory.
NoSQL is not meant to replace SQL, but to tackle the large-data problems
SQL is not well equipped to handle. SQL ACID transactions are Atomic,
Consistent, Isolated, and Durable. Consistency can be either strong
(ACID) or weak (BASE). CAP theorem offers Consistency, Availability, and
Partition tolerance, only two of which can coexist for a shared-data
system. NoSQL comes in two varieties, each with pros and cons: Key-Value
or schema-less. Common advantages of NoSQL include their being open
source and fault tolerant.

-   Video: [Youtube](https://www.youtube.com/watch?v=BjtTDiKhqk8)
    (10:31)

-   Slide: [PDF (Page
    11-26)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

BigTable
--------

Big Table is a key-value NoSQL model with data arranged in rows and
columns. It is composed of Data File System, Chubby, and SSTable. A
tablet is a range of rows in BigTable. The master node assigns tablets
to tablet servers and manages these servers. Memory is conserved by
making SSTables and memtables compact. BigTable is used in features of
Google like their search engine and Google Earth.

-   Video: [Youtube](https://www.youtube.com/watch?v=JAlz9AI5I-M) (6:55)

-   Slide: [PDF (Page
    28-42)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

HBase
-----

HBase is a NoSQL core component of the Hadoop Distributed File System.
It is a scalable distributed data store. A timeline of HBase and Hadoop
is shown. BigTable still has its uses but does not scale well to large
amounts of analytic processing. HBase has a row-column structure similar
to BigTable as well as master and slave nodes. Its place in the
architecture of HDFS is shown in a diagram.

-   Video: [Youtube](https://www.youtube.com/watch?v=i-ibhuVs-ck) (7:37)

-   Slide: [PDF (Page
    44-59)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

HBase Coding
------------

This video gives an overview of the code used in the installation of
HBase and connecting to it.

-   Video: [Youtube](https://www.youtube.com/watch?v=KbFMpYRBTtU) (4:30)

-   Slide: [PDF (Page
    60-66)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

MongoDB
-------

\TODO{Add MongoDB overview. This was completed as a tech abstract so
  some material should be leveraged from that}
Indexing Applications
---------------------

A brief summary of the course up to this point is given, followed by a
diagram showing the setup of a search engine. Google's search engine
contains three key technologies: Google File System, BigTable, and
MapReduce. However, research into big data remains difficult owing to
the scope of its size. Social media data in particular is a huge source
of data with numerous subsets, all of which demands specific approaches
in terms of search queries. There are three stages to this approach:
query, analysis, and visualization.

-   Video: [Youtube](https://www.youtube.com/watch?v=MxgabfoGH-M) (9:33)

-   Slide: [PDF (Page
    1-10)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

Related Work
------------

Indexing improves efficiency in querying data subsets and analysis.
Indices can be single (B+, Hash) or multi-dimensional (R, Quad). Four
databases which utilize indexing are HBase, Cassandra, Riak, and
MongoDB. Current indexing strategies have limits; for instance, they
cannot support range queries or only retrieve Top 'n' most relevant
topics. Customizability of indexing among NoSQL databases is desirable.

-   Video: [Youtube](https://www.youtube.com/watch?v=NDjAdFSVzxo) (5:56)

-   Slide: [PDF (Page
    11-14)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

Indexamples
-----------

Mapping between metadata and raw index data is the essential issue with
indexing. Examples are shown for HBase, Riak, and MongoDB. An abstract
index structure contains index keys, entry IDs among multiple entries,
and additional fields. Index configuration allows for customizability
through choice of fields, which can be anything from timestamps, text,
or retweet status.

-   Video: [Youtube](https://www.youtube.com/watch?v=Ec3VFeTGuo8) (8:35)

-   Slide: [PDF (Page
    15-19)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

Indexing 101
------------

User-defined index allows a user to select the fields used in their
search. Data records are indexed or un-indexed. Index structure is made
up of key, entry ID, and entry fields. A walk-through customized index
creation is shown on HBase, called IndexedHBase. HBase is suited to
accommodate the creation of index tables. A performance test of
IndexedHBase is done on the Truthy Twitter repository, displaying the
various tables that can be created with different criteria. Loading time
for large-scale historical data can be reduced by adding nodes.
Streaming data can be handled by increasing loaders. A comparison of
query evaluation is made between IndexedHBase and Riak, with Riak being
more efficient with small data loads but IndexedHBase proving superior
for large-scale data.

-   Video: [Youtube](https://www.youtube.com/watch?v=eKQaLkw-HBU) (9:53)

-   Slide: [PDF (Page
    20-27)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

Social Media Searches
---------------------

The Truthy Project archives social media data by way of metadata memes.
Some problems faced in analyzing this data include its large volume,
sparsity of information in tweets, and attempting to arrange streaming
tweets. Apache Open Stack upgrades Hadoop 2.0 with YARN and a new HDFS.
A diagram displays an indexing setup for social media data with YARN.

-   Video: [Youtube](https://www.youtube.com/watch?v=a3tcL-Qw9to) (6:19)

-   Slide: [PDF (Page
    28-34)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

Analysis Algorithms
-------------------

Another method of use for inverted indices is in analysis algorithms.
The mathematics involved in this is explored, as well as how it relates
to index data, mapping, and reducing. Rather than scanning all raw data
present, indices allow for searching only the relevant data. An example
is given illustrating how this decreases the time needed to search
hashtags in Twitter.

-   Video: [Youtube](https://www.youtube.com/watch?v=MxoMd4mdshE) (6:57)

-   Slide: [PDF (Page
    35-40)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)
