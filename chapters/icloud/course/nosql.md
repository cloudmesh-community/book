Outdated: NoSQL
===============

RDBMS vs. NoSQL
---------------

[:clapper: RDBMS vs. NoSQL (9:22)](https://www.youtube.com/watch?v=dJunqER9lb8)

[:scroll: RDBMS vs. NoSQL (1)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: RDBMS vs. NoSQL - pptx (1)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)

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

[:clapper: NoSQL Characteristics (10:31)](https://www.youtube.com/watch?v=BjtTDiKhqk8)

[:scroll: NoSQL Characteristics (11)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: NoSQL Characteristics - pptx (11)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)

BigTable
--------

Big Table is a key-value NoSQL model with data arranged in rows and
columns. It is composed of Data File System, Chubby, and SSTable. A
tablet is a range of rows in BigTable. The master node assigns tablets
to tablet servers and manages these servers. Memory is conserved by
making SSTables and memtables compact. BigTable is used in features of
Google like their search engine and Google Earth.

[:clapper: BigTable (6:55)](https://www.youtube.com/watch?v=JAlz9AI5I-M)

[:scroll: BigTable (28)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: BigTable - pptx (28)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)


HBase
-----

HBase is a NoSQL core component of the Hadoop Distributed File System.
It is a scalable distributed data store. A timeline of HBase and Hadoop
is shown. BigTable still has its uses but does not scale well to large
amounts of analytic processing. HBase has a row-column structure similar
to BigTable as well as master and slave nodes. Its place in the
architecture of HDFS is shown in a diagram.

[:clapper: HBase (7:37)](https://www.youtube.com/watch?v=i-ibhuVs-ck)

[:scroll: HBase (44)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: HBase - pptx (44)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)

HBase Coding
------------

This video gives an overview of the code used in the installation of
HBase and connecting to it.

[:clapper: HBase Coding (4:30)](https://www.youtube.com/watch?v=KbFMpYRBTtU)

[:scroll: HBase Coding (60)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: HBase Coding - pptx (60)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)

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

[:clapper: Indexing Applications (9:33)](https://www.youtube.com/watch?v=MxgabfoGH-M)

[:scroll: Indexing Applications (1)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

[:scroll: Indexing Applications - pptx (1)](https://drive.google.com/open?id=0B88HKpainTSfZkJpLTNIbDJ1dVU)

Related Work
------------

Indexing improves efficiency in querying data subsets and analysis.
Indices can be single (B+, Hash) or multi-dimensional (R, Quad). Four
databases which utilize indexing are HBase, Cassandra, Riak, and
MongoDB. Current indexing strategies have limits; for instance, they
cannot support range queries or only retrieve Top 'n' most relevant
topics. Customizability of indexing among NoSQL databases is desirable.

[:clapper: Related Work (5:56)](https://www.youtube.com/watch?v=NDjAdFSVzxo)

[:scroll: Related Work (11)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

[:scroll: Related Work - pptx (11)](https://drive.google.com/open?id=0B88HKpainTSfZkJpLTNIbDJ1dVU)


Indexamples
-----------

Mapping between metadata and raw index data is the essential issue with
indexing. Examples are shown for HBase, Riak, and MongoDB. An abstract
index structure contains index keys, entry IDs among multiple entries,
and additional fields. Index configuration allows for customizability
through choice of fields, which can be anything from timestamps, text,
or retweet status.

[:clapper: Indexamples (8:35)](https://www.youtube.com/watch?v=Ec3VFeTGuo8)

[:scroll: Indexamples (15)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

[:scroll: Indexamples - pptx (15)](https://drive.google.com/open?id=0B88HKpainTSfZkJpLTNIbDJ1dVU)


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

[:clapper: Indexing 101 (9:53)](https://www.youtube.com/watch?v=eKQaLkw-HBU)

[:scroll: Indexing 101 (20)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

[:scroll: Indexing 101 - pptx (20)](https://drive.google.com/open?id=0B88HKpainTSfZkJpLTNIbDJ1dVU)

Social Media Searches
---------------------

The Truthy Project archives social media data by way of metadata memes.
Some problems faced in analyzing this data include its large volume,
sparsity of information in tweets, and attempting to arrange streaming
tweets. Apache Open Stack upgrades Hadoop 2.0 with YARN and a new HDFS.
A diagram displays an indexing setup for social media data with YARN.

[:clapper: Social Media Searches (6:19)](https://www.youtube.com/watch?v=a3tcL-Qw9to)

[:scroll: Social Media Searches (28)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

[:scroll: Social Media Searches - pptx (28)](https://drive.google.com/open?id=0B88HKpainTSfZkJpLTNIbDJ1dVU)

Analysis Algorithms
-------------------

Another method of use for inverted indices is in analysis algorithms.
The mathematics involved in this is explored, as well as how it relates
to index data, mapping, and reducing. Rather than scanning all raw data
present, indices allow for searching only the relevant data. An example
is given illustrating how this decreases the time needed to search
hashtags in Twitter.

[:clapper: Analysis Algorithms (6:57)](https://www.youtube.com/watch?v=MxoMd4mdshE)

[:scroll: Analysis Algorithms (35)](https://drive.google.com/open?id=0B88HKpainTSfWUh6dVNHcXloSnc)

[:scroll: Analysis Algorithms - pptx (35)](https://drive.google.com/open?id=0B88HKpainTSfZkJpLTNIbDJ1dVU)

