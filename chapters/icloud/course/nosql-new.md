NoSQL
=====

RDBMS vs. NoSQL
---------------

A discussion of relational database management systems (RDBMS) compared
to NoSQL data storage systems is presented. This discussion includes an
evolution of data storage systems, limitations with RDBMS in terms of
scalability and how NoSQL fits into the picture in terms of big data.

[:clapper: RDBMS vs. NoSQL (9:22)](https://www.youtube.com/watch?v=dJunqER9lb8)

[:scroll: RDBMS vs. NoSQL (1)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: RDBMS vs. NoSQL - pptx (1)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)


NoSQL Characteristics
---------------------

Clouds have arisen as an answer to the data demands of social media.
Three major programs for NoSQL are BigTable, Dynamo, and CAP theory.
More recently mongoDB has emerged as a leader in NoSQL databases and
will also be discussed. NoSQL is not meant to replace SQL, but to tackle
the large-data problems SQL is not well equipped to handle. SQL ACID
transactions are Atomic, Consistent, Isolated, and Durable. Consistency
can be either strong (ACID) or weak (BASE). CAP theorem offers
Consistency, Availability, and Partition tolerance, only two of which
can coexist for a shared-data system. NoSQL comes in two varieties, each
with pros and cons: Key-Value or schema-less. Common advantages of NoSQL
include their being open source and fault tolerant. The number of NoSQL
databases makes it impossible to simply split them into Key-Value and
schema-less categories, instead they can generally be placed in one of
the three categories being document model, graph model and key-value and
wide column models.

[:clapper: NoSQL Characteristics (10:31)](https://www.youtube.com/watch?v=BjtTDiKhqk8)

[:scroll: NoSQL Characteristics (11)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: NoSQL Characteristics - pptx (11)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)


### Document Model

Relational databases store data in rows and columns, the class of NoSQL
databases that fall into the document model store data as documents.
Typically these documents are in JSON format and provide a straight
forward way to model data that parallels object oriented programing
where each document is an object. Each document stores one or more
fields and within the field a value is stored in the form of an array,
string date etc. In comparison to relational databases that distribute
the records across columns that are connected with keys the document
model stores records and their associated data in a single document. A
key advantage to this model is that is reduces the need for JOIN
operations that can be computationally expensive. Two examples of
document databases are MongoDB and CouchDB.

### Graph Model

As the name implies graph databases exploit the properties of graph
structures and represent data through nodes and edges. Graph databases
are useful for exploring the relationships of the components that make
up an application by representing the data as a network of
relationships. Graph databases can be useful for exploring social
network connections, topologies of networks and supply chains. Two
examples of graph databases are Neo4j and Graph.

### Key-Value and Wide Column Models

Key-value stores are the most basic type on NoSQL databases as every
item is stored as an attribute name or key paired with its value. In
this model the value is not interpretable by the system as data can only
be queried by the key. Key-value type databases do not enforce a set
schema for key-value pairs making these database useful for unstructured
and polymorphic data. In contrast to key-value stores, wide-column store
data in distributed variable-dimensional sorted map where each record is
stored as columns. These columns can be grouped into families and or
columns can be distributed to several column families. Each column
family has a primary key that can be queried in order to retrieve the
data.

* <https://www.mongodb.com/collateral/top-5-considerations-when-evaluating-nosql-databases>

BigTable
--------

Big Table is a key-value NoSQL model with data arranged in rows and
columns. It is composed of Data File System, Chubby, and SSTable. A
tablet is a range of rows in BigTable. The master node assigns tablets
to tablet servers and manages these servers. Memory is conserved by
making SSTables and memtables compact. BigTable is used in features of
Google like their search engine and Google Earth.

[:clapper: 6:55 BigTable](https://www.youtube.com/watch?v=JAlz9AI5I-M)

[:scroll: 28 BigTable](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)

[:scroll: 28 BigTable - pptx](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)


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

[:clapper: Coding HBase (4:30)](https://www.youtube.com/watch?v=KbFMpYRBTtU)

[:scroll: HBase Coding (60)](https://drive.google.com/open?id=0B88HKpainTSfaDFNbjNiMm44bnc)


[:scroll: HBase Coding - pptx (60)](https://drive.google.com/open?id=0B88HKpainTSfNnQ5SEVKTm1tRk0)


Draft: MongoDB
--------------

MongoDB belongs to the document model described above. Within a typical
MongoDB server there are often multiple databases. Each database is a
physical container of collections with its own set of files within the
file system. A collection is a set of MongoDB documents similar to a
typical relational database table. In MongoDB databases the collections
are not required to follow a schema allowing documents in the same
collection to have different fields. Some of the main advantages of
MongoDB are its ease of scalability, lack of complex joins, schema-less,
use of internal memory and the support for dynamic queriers.

* <https://www.tutorialspoint.com/mongodb/mongodb_quick_guide.htm>

Indexing Applications
---------------------

The setup of a search engine is briefly discussed using a diagram that
contains the core components of a search engine. Google's search engine
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

