# AWS RedShift
---
## Learning Objectives
* Introduction to AWS RedShift
* AWS RedShift Architecture
* Query Processing in AWS RedShift
* Application interfaces with AWS RedShift
* Examples of Python interaction
---
## Introduction to AWS RedShift
(ref: https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html)
AWS RedShift is a managed cloud data warehouse, with per-hour billing. AWS RedShift provides a cloud alternative to on-premise data warehouse databases like Oracle, Teradata, SQL Server, HPE Vertica. In typical cloud parlance, we can describe RedShift as DBaaS (DB as a service), where the management of the DB (including patching and upgrades) is handled by AWS.
Queries are processed during an MPP (massively parallel processor) architecture. Data storage is columnar. RedShift is a clustered database.

## AWS RedShift Architecture

Client applications interact with the leader node of the RedShift cluster, which in turn talks to the compute nodes. Fast interconnect network exists between nodes of the cluster. The cluster can be scaled up or down, changing the number of nodes.
A compute node is paritioned into slices (memory + disk, of each node). A portion of the workload is executed by the slice. Data is stored on the compute nodes. There is no separation of compute and storage.
(ref: https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html)

Nodes can consist of 2 node types Dense Storage (DS) that consist of HDDs (hard disks) for high data volumes, or Dense Compute (DC) that consist of SSDs (solid state disks) for medium to low data volumes, but higher performance. Storage is locally attached to the machines. 

RedShift stores data in the form of Tables, and supports SQL Queries against the data. It has foreign keys and constraints like other relational databases. Columnar storage allows for repeated values (for example country or state identifiers) to be stored using column compression (and stored only once). Such an arrangement works best with Star Schemas or Fact and Dimension data models. 
RedShift supports very efficient import from S3 to allow for the loading part of the ETL processes. 
To allow for optimal data retrieval, and data collocation, RedShift provides for 3 table optimization mechanisms.
* Sort Keys : AWS RedShift does not support Indexes, but has sort keys instead. Data on the disk is stored in the sorted order of the sort-keys. Examples of sort-keys could be zip codes, or dates, or join columns. These can be decided based on the kinds of queries.
* Distribution Keys : To decide which rows go into which node slices of the cluster, AWS RedShift uses distribution keys. Designing the distribution keys should target collocation of rows from joining tables, and also target even data distribution among slices of the cluster (to allow for parallel query execution).
* Compression Encodings : Column encoding and compression is dependent on the data types of the columns, and how much values differ in one row from the next, or the others. Delta encoding, raw encoding (i.e. no encoding), byte encoding are the forms of encoding and compression. Compression affects storage and performance, but not to the extent of sort keys or distribution keys.

## Query Processing in AWS RedShift
The query syntax is very similar to PostgreSQL. So much, that you can use a PostgreSQL JDBC driver to interact with RedShift. Amazon says in the documentation that RedShift is based on PostgreSQL 8.x. 

The leader node processes queries, creates the parse tree and execution plan. The query is send to the compute node, only when the data required by the query is present on that compute node. Each compute node execute the query fragments, and send the result back to the leader node, that does the final aggregation.
When a query gets fired again, the leader node may retrieve results from the results cache instead of re-executing the query.

Join processing is distributed between nodes. For an join involving an outer table (typically larger), and an inner table (typically smaller), depending on the distribution key, the leader node may decide to broadcast the entire inner table to all the nodes (an example could be the expansion of state codes to the full names). In the ideal condition, a copy of such tables should exist on each of the nodes. Redistribution of data across nodes of the cluster of both the larger and smaller tables may also be required to evaluate the results. This would be a costly operation. The database designer should look for such bad execution plans, and tune the storage of the tables.

