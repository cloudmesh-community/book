# AWS RedShift
---
## Learning Objectives
* Introduction to AWS RedShift
* AWS RedShift Architecture
* Query Processing in AWS RedShift
* Creating an AWS RedShift cluster using Terraform
* Interacting with AWS RedShift using DB Tools
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
To allow for optimal data retrieval, and data collocation, RedShift provides for 3 table optimization mechanisms. These mechanisms are important especially for larger tables (typically those with > 100M rows)
* Sort Keys : AWS RedShift does not support Indexes, but has sort keys instead. Data on the disk is stored in the sorted order of the sort-keys. Examples of sort-keys could be zip codes, or dates, or join columns. These can be decided based on the kinds of queries.
* Distribution Keys : To decide which rows go into which node slices of the cluster, AWS RedShift uses distribution keys. Designing the distribution keys should target collocation of rows from joining tables, and also target even data distribution among slices of the cluster (to allow for parallel query execution).
* Compression Encodings : Column encoding and compression is dependent on the data types of the columns, and how much values differ in one row from the next, or the others. Delta encoding, raw encoding (i.e. no encoding), byte encoding are the forms of encoding and compression. Compression affects storage and performance, but not to the extent of sort keys or distribution keys.

## Query Processing in AWS RedShift
The query syntax is very similar to PostgreSQL. So much, that you can use a PostgreSQL JDBC driver to interact with RedShift, but for production usage, better to use the Amazon JDBC driver. Amazon says in the documentation that RedShift is based on PostgreSQL 8.x. 

The leader node processes queries, creates the parse tree and execution plan. The query is send to the compute node, only when the data required by the query is present on that compute node. Each compute node execute the query fragments, and send the result back to the leader node, that does the final aggregation.
When a query gets fired again, the leader node may retrieve results from the results cache instead of re-executing the query.

Join processing is distributed between nodes. For an join involving an outer table (typically larger), and an inner table (typically smaller), depending on the distribution key, the leader node may decide to broadcast the entire inner table to all the nodes (an example could be the expansion of state codes to the full names). In the ideal condition, a copy of such tables should exist on each of the nodes. Redistribution of data across nodes of the cluster of both the larger and smaller tables may also be required to evaluate the results. This would be a costly operation. The database designer should look for such bad execution plans, and tune the storage of the tables.

## Here is how to create an AWS RedShift cluster using Terraform
Terraform is a IaC (Infrastructure as Code) tool used to interact with cloud resources, across various clouds and providers. It is a simple download, and a single executable that helps creation and destruction of dependencies and resources, in the right order.


Here is a set of commands for creating the AWS RedShift cluster. Note: I ran terraform from my Windows laptop, so please make adjustments for paths and OS commands depending on your workstation OS.

````
#Modified from https://github.com/terraform-aws-modules/terraform-aws-redshift/blob/master/examples/complete/main.tf
#and : https://medium.com/@aoc/kinesis-firehose-to-redshift-pipeline-with-terraform-2261b5afd29d

cmd> mkdir proj2
cmd> cd proj2
cmd> cat redshift.tf
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  name = "demo-vpc"
  cidr = "10.10.0.0/16"
  azs              = ["us-east-1a", "us-east-1b", "us-east-1c"]
  public_subnets = ["10.10.90.0/24", "10.10.91.0/24", "10.10.92.0/24"]
}

resource "aws_redshift_subnet_group" "redshift" {
  name        = "demo-redshift-subnet"
  description = "Redshift subnet group"
  subnet_ids  = ["${module.vpc.public_subnets}"]
}

module "sg" {
  source = "terraform-aws-modules/security-group/aws//modules/redshift"

  name   = "demo-redshift"
  ingress_cidr_blocks = ["0.0.0.0/0"]
  vpc_id = "${module.vpc.vpc_id}"
  ingress_rules = ["postgresql-tcp"]
  egress_rules = ["all-all"]
}



resource "aws_redshift_cluster" "my-redshift-cluster" {
  cluster_identifier = "my-redshift-cluster"
  database_name      = "mydb"
  master_username    = "DB_USER_HERE"
  master_password    = "DB_PASSWORD_HERE"
  node_type          = "dc2.large"
  cluster_type       = "single-node"
  cluster_subnet_group_name = "${aws_redshift_subnet_group.redshift.name}"
  vpc_security_group_ids = ["${module.sg.this_security_group_id}"]
  skip_final_snapshot = true
  publicly_accessible = true
}

cmd>
cmd> <path_to_terraform>\terraform init
cmd> <path_to_terraform>\terraform plan -out CREATmyredshiftcluster.tfplan
cmd> <path_to_terraform>\terraform apply CREATmyredshiftcluster.tfplan

### Perform all your connections, queries and tests with RedShift here.
### Destroy environment when done.

cmd> <path_to_terraform>\terraform plan -destroy -out DESTmyredshiftcluster.tfplan
cmd> <path_to_terraform>\terraform apply DESTmyredshiftcluster.tfplan
````

## Interacting with AWS RedShift using DB Tools
DB Tools like SQL-Workbench (https://www.sql-workbench.eu/), and Squirrel SQL (http://squirrel-sql.sourceforge.net/) can used to interact with RedShift (and most other databases), by downloading the RedShift JDBC driver, and configuring it in the tool.

The AWS Console page for the RedShift cluster displays the JDBC connection string that can be used. 

Here is a sample schema creation script that can be used to create tables and populate them in AWS RedShift. (This is modified from Oracle's demo EMP/DEPT script).

````

--DROP TABLE EMP;
--DROP TABLE DEPT;

CREATE TABLE EMP
       (EMPNO DECIMAL(4) NOT NULL,
        ENAME VARCHAR(10),
        JOB VARCHAR(9),
        MGR DECIMAL(4),
        HIREDATE DATE,
        SAL DECIMAL(7, 2),
        COMM DECIMAL(7, 2),
        DEPTNO DECIMAL(4));

INSERT INTO EMP VALUES
        (7369, 'SMITH',  'CLERK',     7902,
        TO_DATE('17-DEC-1980', 'DD-MON-YYYY'),  800, NULL, 20);
INSERT INTO EMP VALUES
        (7499, 'ALLEN',  'SALESMAN',  7698,
        TO_DATE('20-FEB-1981', 'DD-MON-YYYY'), 1600,  300, 30);
INSERT INTO EMP VALUES
        (7521, 'WARD',   'SALESMAN',  7698,
        TO_DATE('22-FEB-1981', 'DD-MON-YYYY'), 1250,  500, 30);
INSERT INTO EMP VALUES
        (7566, 'JONES',  'MANAGER',   7839,
        TO_DATE('2-APR-1981', 'DD-MON-YYYY'),  2975, NULL, 20);
INSERT INTO EMP VALUES
        (7654, 'MARTIN', 'SALESMAN',  7698,
        TO_DATE('28-SEP-1981', 'DD-MON-YYYY'), 1250, 1400, 30);
INSERT INTO EMP VALUES
        (7698, 'BLAKE',  'MANAGER',   7839,
        TO_DATE('1-MAY-1981', 'DD-MON-YYYY'),  2850, NULL, 30);
INSERT INTO EMP VALUES
        (7782, 'CLARK',  'MANAGER',   7839,
        TO_DATE('9-JUN-1981', 'DD-MON-YYYY'),  2450, NULL, 10);
INSERT INTO EMP VALUES
        (7788, 'SCOTT',  'ANALYST',   7566,
        TO_DATE('09-DEC-1982', 'DD-MON-YYYY'), 3000, NULL, 20);
INSERT INTO EMP VALUES
        (7839, 'KING',   'PRESIDENT', NULL,
        TO_DATE('17-NOV-1981', 'DD-MON-YYYY'), 5000, NULL, 10);
INSERT INTO EMP VALUES
        (7844, 'TURNER', 'SALESMAN',  7698,
        TO_DATE('8-SEP-1981', 'DD-MON-YYYY'),  1500,    0, 30);
INSERT INTO EMP VALUES
        (7876, 'ADAMS',  'CLERK',     7788,
        TO_DATE('12-JAN-1983', 'DD-MON-YYYY'), 1100, NULL, 20);
INSERT INTO EMP VALUES
        (7900, 'JAMES',  'CLERK',     7698,
        TO_DATE('3-DEC-1981', 'DD-MON-YYYY'),   950, NULL, 30);
INSERT INTO EMP VALUES
        (7902, 'FORD',   'ANALYST',   7566,
        TO_DATE('3-DEC-1981', 'DD-MON-YYYY'),  3000, NULL, 20);
INSERT INTO EMP VALUES
        (7934, 'MILLER', 'CLERK',     7782,
        TO_DATE('23-JAN-1982', 'DD-MON-YYYY'), 1300, NULL, 10);

CREATE TABLE DEPT
       (DEPTNO DECIMAL(2),
        DNAME VARCHAR(14),
        LOC VARCHAR(13) );

INSERT INTO DEPT VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO DEPT VALUES (20, 'RESEARCH',   'DALLAS');
INSERT INTO DEPT VALUES (30, 'SALES',      'CHICAGO');
INSERT INTO DEPT VALUES (40, 'OPERATIONS', 'BOSTON');
````
