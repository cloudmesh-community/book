# MongoDB in Python


---

**:mortar_board: Learning Objectives**

* Introduction to basic MongoDB knowledge
* Use of MOngoDB via PyMongo
* Use of MongoEngine MongoEngine and Object-Document mapper,
* Use of Flask-Mongo

---

In today's era, NoSQL databases have developed an enormous potential 
to process the unstructured data efficiently. Modern information is 
complex, extensive, and may not have pre-existing relationships. With 
the advent of the advanced search engines, machine learning, and 
Artificial Intelligence, technology expectations to process, store, and 
analyze such data have grown tremendously [@www-upwork]. The NoSQL 
database engines such as MongoDB, Redis, and Cassandra have successfully 
overcome the traditional relational database challenges such as 
scalability, performance, unstructured data growth, agile sprint cycles, 
and growing needs of processing data in real-time with minimal hardware 
processing power [@www-guru99]. The NoSQL databases are a new generation 
of engines that do not necessarily require SQL language and are sometimes 
also called *Not Only SQL* databases. However, most of them support 
various third-party open connectivity drivers that can map NoSQL queries 
to SQL's. It would be safe to say that although NoSQL databases are 
still far from replacing the relational databases, they are adding an 
immense value when used in hybrid IT environments in conjunction with 
relational databases, based on the application specific needs 
[@www-guru99]. In this paper, we will be covering the MongoDB technology, 
its driver PyMongo, its object-document mapper MongoEngine, and the 
Flask-PyMongo micro-web framework that make MongoDB more attractive
and user-friendly.

## MongoDB

Today MongoDB is one of leading NoSQL database which is fully capable 
of handling dynamic changes, processing large volumes of complex and 
unstructured data, easily using object-oriented programming features; 
as well as distributed system challenges [@www-mongodb]. At its core, 
MongoDB is an open source, cross-platform, document database mainly 
written in C++ language. 

### Installation

MongoDB can be installed on various Unix Platforms, including Linux, 
Ubuntu, Amazon Linux, etc [@www-digitaloceaninst]. This section focuses 
on installing MongoDB on Ubuntu 18.04 Bionic Beaver used as a standard 
OS for a virtual machine used as a part of Big Data Application Class 
during the 2018 Fall semester.                              

#### Installation procedure

Before installing, it is recommended to configure the non-root user and 
provide the administrative privileges to it, in order to be able to 
perform general MongoDB admin tasks. This can be accomplished by login 
as the root user in the following manner [@www-digitaloceanprep].           

```bash
$ adduser mongoadmin
$ usermod -aG sudo sammy
```

When logged in as a regular user, one can perform actions with superuser
privileges by typing *sudo* before each command [@www-digitaloceanprep]. 

Once the user set up is completed, one can login as a regular user (mongoadmin)
and use the following instructions to install MongoDB.

To update the Ubuntu packages to the most recent versions, use below command:

```bash
$ sudo apt update
```

To install the MongoDB package:

```bash
$ sudo apt install -y mongodb
```

To check the service and database status:

```bash
$ sudo systemctl status mongodb
```

Verifying the status of a successful MongoDB installation can be confirmed 
with an output similar to this:

```bash
$ mongodb.service - An object/document-oriented database
    Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset: enabled)
    Active: **active** (running) since Sat 2018-11-15 07:48:04 UTC; 2min 17s ago
      Docs: man:mongod(1)
  Main PID: 2312 (mongod)
     Tasks: 23 (limit: 1153)
    CGroup: /system.slice/mongodb.service
           └─2312 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc/mongodb.conf
```

To verify the configuration, more specifically the installed version, server, 
and port, use the following command:

```bash
$ mongo --eval 'db.runCommand({ connectionStatus: 1 })'
```

Similarly, to restart MongoDB, use the following:

```bash
$ sudo systemctl restart mongodb
```

To allow access to MongoDB from an outside hosted server one can use the 
following command which opens the fire-wall connections [@www-digitaloceaninst].

```bash
$ sudo ufw allow from your_other_server_ip/32 to any port 27017
```

Status can be verified by using:

```bash
$ sudo ufw status
```

Other MongoDB configurations can be edited through the */etc/mongodb.conf* 
files such as port and hostnames, file paths.

```bash
$ sudo nano /etc/mongodb.conf
```

Also, to complete this step, a server's IP address must be added to the 
bindIP value [@www-digitaloceaninst].                                    

```bash
$ logappend=true

  bind_ip = 127.0.0.1,your_server_ip
  *port = 27017*
```

MongoDB is now listening for a remote connection that can be accessed 
by anyone with appropriate credentials [@www-digitaloceaninst].  

### Collections and Documents

Each database within Mongo environment contains collections which in turn 
contain documents. Collections and documents are analogous to tables and 
rows respectively to the relational databases. The document structure is 
in a key-value form which allows storing of complex data types composed 
out of field and value pairs. Documents are objects which correspond to 
native data types in many programming languages, hence a well defined, 
embedded document can help reduce expensive joins and improve query 
performance. The `_id` field  helps to identify each document uniquly
[@www-guru99]. 

MongoDB offers flexibility to write records that are not restricted by 
column types. The data storage approach is flexible as it allows one 
to store data as it grows and to fulfill varying needs of applications 
and/or users. It supports JSON like binary points known as BSON where 
data can be stored without specifying the type of data. Moreover, it 
can be distributed to multiple machines at high speed. It includes a 
sharding feature that partitions and spreads the data out across various 
servers. This makes MongoDB an excellent choice for cloud data processing. 
Its utilities can load high volumes of data at high speed which ultimately 
provides greater flexibility and availability in a cloud-based environment 
[@www-upwork].

The dynamic schema structure within MongoDB allows easy testing of the 
small sprints in the Agile project management life cycles and research 
projects that require frequent changes to the data structure with minimal 
downtime. Contrary to this flexible process, modifying the data structure 
of relational databases can be a very tedious process [@www-upwork]. 


#### Collection example: 

The following collection example for a person named *Corey* includes
additional information such as age, status, and group [@www-mongocollection].

```json
{
 name: "Corey"
 age: "21"
 status: "Open"
 group: ["AI" , "Machine Learning"]
}
```

#### Document structure:

```json
{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

#### Collection Operations 

If collection does not exists, MongoDB database will create a collection 
by default.

```bash
> db.myNewCollection1.insertOne( { x: 1 } )
> db.myNewCollection2.createIndex( { y: 1 } )
```

### MongoDB Querying

The data retrieval patterns, the frequency of data manipulation 
statements such as insert, updates, and deletes may demand for 
the use of indexes or incorporating the sharding feature to improve 
query performance and efficiency of MongoDB environment [@www-guru99]. 
One of the significant difference between relational databases and NoSQL 
databases are joins. In the relational database, one can combine results 
from two or more tables using a common column, often called as *key*. The 
native table contains the *primary key* column while the referenced table 
contains a *foreign key*. This mechanism allows one to make changes in a 
single row instead of changing all rows in the referenced table. This 
action is referred to as *normalization*. MongoDB is a document database 
and mainly contains denormalized data which means the data is repeated 
instead of indexed over a specific key. If the same data is required in 
more than one table, it needs to be repeated. This constraint has been 
eliminated in MongoDB's new version 3.2. The new release introduced a 
*$lookup* feature which more likely works as a left-outer-join. Lookups 
are restricted to aggregated functions which means that data usually 
need some type of filtering and grouping operations to be conducted 
beforehand. For this reason, joins in MongoDB require more complicated 
querying compared to the traditional relational database joins. Although 
at this time, *lookups* are still very far from replacing *joins*, this 
is a prominent feature that can resolve some of the relational data 
challenges for MongoDB [@www-sitepoint]. MongoDB queries support regular 
expressions as well as range asks for specific fields that eliminate the 
need of returning entire documents [@www-guru99]. MongoDB collections do 
not enforce document structure like SQL databases which is a compelling 
feature. However, it is essential to keep in mind the needs of the 
applications[@www-upwork].

#### Mongo Queries examples:

The queries can be executed from Mongo shell as well as through scripts. 

To query the data from a MongoDB collection, one would use MongoDB's *find()*
method.

```bash
> db.COLLECTION_NAME.find()
```

The output can be formatted by using the *pretty()* command.

```bash
> db.mycol.find().pretty()
```

The MongoDB insert statements can be performed in the following manner:

```bash
> db.COLLECTION_NAME.insert(document)
```

> "The *$lookup* command performs a left-outer-join to an unsharded 
> collection in the same database to filter in documents from the 
> *joined* collection for processing" [@www-mongodblookup]. 

```json
$ {
    $lookup:
      {
        from: <collection to join>,
        localField: <field from the input documents>,
        foreignField: <field from the documents of the "from" collection>,
        as: <output array field>
      }
  }
```

This operation is equivalent to the following SQL operation:

```
 $ SELECT *, <output array field>
   FROM collection
   WHERE <output array field> IN (SELECT *
                               FROM <collection to join>
                               WHERE <foreignField> = <collection.localField>);`
``` 

To perform a Like Match (Regex), one would use the following command:

```bash
> db.products.find( { sku: { $regex: /789$/ } } )
```

### MongoDB Basic Functions

When it comes to the technical elements of MongoDB, it posses a 
rich interface for importing and storage of external data in various 
formats. By using the Mongo *Import/Export* tool, one can easily 
transfer contents from JSON, CSV, or TSV files into a database. MongoDB 
supports CRUD (create, read, update, delete) operations efficiently 
and has detailed documentation available on the product website. 
It can also query the geospatial data, and it is capable of storing 
geospatial data in GeoJSON objects. The *aggregation* operation of 
the MongoDB process data records and returns computed results. MongoDB 
aggregation framework is modeled on the concept of data pipelines 
[@www-mongoexportimport].

#### Import/Export functions examples:

To import JSON documents, one would use the following command:
 
```bash
$ mongoimport --db users --collection contacts --file contacts.json
```

The CSV import uses the input file name to import a collection, hence, 
the collection name is optional [@www-mongoexportimport].

```bash
$ mongoimport --db users --type csv --headerline --file /opt/backups/contacts.csv
```

> "*Mongoexport* is a utility that produces a JSON or CSV export of data stored 
> in a MongoDB instance" [@www-mongoexportimport].

```bash
$ mongoexport --db test --collection traffic --out traffic.json
```

### Security Features

Data security is a crucial aspect of the enterprise infrastructure management 
and is the reason why MongoDB provides various security features such as 
ole based access control, numerous authentication options, and encryption. 
It supports mechanisms such as SCRAM, LDAP, and Kerberos authentication. 
The administrator can create role/collection-based access control; also 
roles can be predefined or custom. MongoDB can audit activities such 
as DDL, CRUD statements, authentication and authorization operations 
[@www-mongosecurity]. 

#### Collection based access control example:

A user defined role can contain the following privileges [@www-mongosecurity].

```bash
$ privileges: [
   { resource: { db: "products", collection: "inventory" }, actions: [ "find", "update"] },
   { resource: { db: "products", collection: "orders" },  actions: [ "find" ] }
 ]
```

### MongoDB Cloud Service

In regards to the cloud technologies, MongoDB also offers fully automated 
cloud service called *Atlas* with competitive pricing options. Mongo Atlas 
Cloud interface offers interactive GUI for managing cloud resources and 
deploying applications quickly. The service is equipped with geographically 
distributed instances to ensure no single point failure. Also, a well-rounded 
performance monitoring interface allows users to promptly detect anomalies and 
generate index suggestions to optimize the performance and reliability of the 
database. Global technology leaders such as Google, Facebook, eBay, and Nokia 
are leveraging MongoDB and *Atlas* cloud services making MongoDB one of the most 
popular choices among the NoSQL databases [@www-mongoatlas]. 

## PyMongo

PyMongo is the official Python driver or distribution that allows work 
with a NoSQL type database called *MongoDB* [@api-mongodb-com-api]. The 
first version of the driver was developed in 2009 [@www-pymongo-blog], 
only two years after the development of MongoDB was started. This driver 
allows developers to combine both Python's versatility and MongoDB's 
flexible schema nature into successful applications. Currently, this 
driver supports MongoDB versions 2.6, 3.0, 3.2, 3.4, 3.6, and 4.0 
[@www-github]. MongoDB and Python represent a compatible fit considering 
that BSON (binary JSON) used in this NoSQL database is very similar 
to Python dictionaries, which makes the collaboration between the two 
even more appealing [@www-slideshare]. For this reason, dictionaries 
are the recommended tools to be used in PyMongo when representing 
documents [@www-gearheart]. 

### Installation

Prior to being able to exploit the benefits of Python and MongoDB 
simultaneously, the PyMongo distribution must be installed using 
*pip*. To install it on all platforms, the following command should 
be used [@www-api-mongodb-installation]:

`$ python -m pip install pymongo`

Specific versions of PyMongo can be installed with command lines 
such as in our example where the 3.5.1 version is installed 
[@www-api-mongodb-installation].

```bash
$ python -m pip install pymongo==3.5.1
```

A single line of code can be used to upgrade the driver as well 
[@www-api-mongodb-installation].

```bash
$ python -m pip install --upgrade pymongo
```

Furthermore, the installation process can be completed with
the help of the *easy_install* tool, which requires users to use 
the following command [@www-api-mongodb-installation].

```bash
$ python -m easy_install pymongo
```

To do an upgrade of the driver using this tool, the following 
command is recommended [@www-api-mongodb-installation]:

```bash
$ python -m easy_install -U pymongo
```

There are many other ways of installing PyMongo directly from 
the source, however, they require for C extension dependencies 
to be installed prior to the driver installation step, as they 
are the ones that skim through the sources on GitHub and use 
the most up-to-date links to install the driver 
[@www-api-mongodb-installation].

To check if the installation was completed accurately, the 
following command is used in the Python console 
[@www-realpython].

```bash
import pymongo
```

If the command returns zero exceptions within the Python 
shell, one can consider for the PyMongo installation to 
have been completed successfully.

### Dependencies

The PyMongo driver has a few dependencies that should 
be taken into consideration prior to its usage. Currently, 
it supports CPython 2.7, 3.4+, PyPy, and PyPy 3.5+ 
interpreters [@www-github]. An optional dependency that 
requires some additional components to be installed is 
the GSSAPI authentication [@www-github]. For the Unix based 
machines, it requires *pykerberos*, while for the Windows 
machines *WinKerberos* is needed to fullfill this requirement 
[@www-github]. The automatic installation of this dependency 
can be done simultaneously with the driver installation, in 
the following manner:

```bash
$ python -m pip install pymongo[gssapi]
```

Other third-party dependencies such as *ipaddress*, *certifi*, 
or *wincerstore* are necessary for connections with help of 
TLS/SSL and can also be simultaneously installed along with the 
driver installation [@www-github].

### Running PyMongo with Mongo Deamon

Once PyMongo is installed, the Mongo deamon can be run with a 
very simple command in a new terminal window [@www-realpython].

```bash
$ mongod
```

### Connecting to a database using MongoClient

In order to be able to establish a connection with a database, 
a MongoClient class needs to be imported, which sub-sequentially 
allows the MongoClient object to communicate with the database 
[@www-realpython]. 

```python
from pymongo import MongoClient
client = MongoClient()
```

This command allows a connection with a default, local host 
through port 27017, however, depending on the programming 
requirements, one can also specify those by listing them in the 
client instance or use the same information via the Mongo URI 
format [@www-realpython].

### Accessing Databases

Since MongoClient plays a server role, it can be used to access 
any desired databases in an easy way. To do that, one can use two 
different approaches. The first approach would be doing this via 
the *attribute* method where the name of the desired database is 
listed as an attribute, and the second approach, which would 
include a dictionary-style access [@www-realpython]. For example, 
to access a database called *cloudmesh_community*, one would use 
the following commands for the attribute and for the dictionary 
method, respectively.

```python
db = client.cloudmesh_community
db = client['cloudmesh_community']
```

### Creating a Database

Creating a database is a straight forward process. First, one must
create a MongoClient object and specify the connection (IP address)
as well as the name of the database they are trying to create 
[@www-w3schools]. The example of this command is presented in the
followng section:

```python
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['cloudmesh']
```

### Inserting and Retrieving Documents (Querying)

Creating documents and storing data using PyMongo is equally easy 
as accessing and creating databases. In order to add new data, a 
collection must be specified first. In this example, a decision is 
made to use the *cloudmesh* group of documents.

```python
cloudmesh = db.cloudmesh
```

Once this step is completed, data may be inserted using the 
*insert_one()* method, which means that only one document is 
being created. Of course, insertion of multiple documents at 
the same time is possible as well with use of the *insert_many()*
method [@www-realpython]. An example of this method is as follows: 

```python
course_info = {
     'course': 'Big Data Applications and Analytics',
     'instructor': ' Gregor von Laszewski',
     'chapter': 'technologies'
}
result = cloudmesh.insert_one(course_info)`
```

Another example of this method would be to create a collection.
If we wanted to create a collection of students in the 
*cloudmesh_community*, we would do it in the following manner:

```python
student = [ {'name': 'John', 'st_id': 52642},
    {'name': 'Mercedes', 'st_id': 5717},
    {'name': 'Anna', 'st_id': 5654},
    {'name': 'Greg', 'st_id': 5423},
    {'name': 'Amaya', 'st_id': 3540},
    {'name': 'Cameron', 'st_id': 2343},
    {'name': 'Bozer', 'st_id': 4143},
    {'name': 'Cody', 'price': 2165} ]

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.cloudmesh
    db.students.insert_many(student)
```

Retrieving documents is equally simple as creating them. The 
*find_one()* method can be used to retrieve one document 
[@www-realpython]. An implementation of this method is given 
in the following example.

```python
gregors_course = cloudmesh.find_one({'instructor':'Gregor von Laszewski'})
```

Similarly, to retieve multiple documents, one would use the 
*find()* method instead of the *find_one()*. For example, to 
find all courses thought by professor von Laszewski, one would 
use the following command:

```python
gregors_course = cloudmesh.find({'instructor':'Gregor von Laszewski'})
```

One thing that users should be cognizant of when using the *find()*
method is that it does not return results in an array format but 
as a *cursor* object, which is a combination of methods that work 
together to help with data querying [@www-realpython]. In order to 
return individual documents, iteration over the result must be 
completed [@www-realpython].

### Limiting Results

When it comes to working with large databases it is always useful to
limit the number of query results. PyMongo supports this option 
with its *limit()* method [@www-w3schools]. This method takes in one
parameter which specifies the number of documents to be returned
[@www-w3schools]. For example, if we had a collection with a large 
number of cloud technologies as individual documents, one could 
modify the query results to return only the top 10 technologies. 
To do this, the following example could be utilized:

```python
client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['cloudmesh']
    col = db['technologies']
    topten = col.find().limit(10)
```

### Updating Collection

Updating documents is very similar to inserting and retrieving 
the same. Depending on the number of documents to be updated,
one would use the *update_one()* or *update_many()* method
[@www-w3schools]. Two parameters need to be passed in the 
*update_one()* method for it to successfully execute. The 
first argument is the query object that specifies the document 
to be changed, and the second argument is the object that 
specifies the new value in the document. An example of 
the *update_one()* method in action is the following:

```python
myquery = { 'course': 'Big Data Applications and Analytics' }
newvalues = { '$set': { 'course': 'Cloud Computing' } }
```

Updating all documents that fall under the same criteria can be
done with the *update_many* method [@www-w3schools]. For example, 
to update all documents in which course title starts with letter 
*B* with a different instructor information, we would do the
following:

```python
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['cloudmesh']
col = db['courses']
query = { 'course': { '$regex': '^B' } }
newvalues = { '$set': { 'instructor': 'Gregor von Laszewski' } }
   
edited = col.update_many(query, newvalues)
```

### Counting Documents

Counting documents can be done with one simple operation called
*count_documents()* instead of using a full query 
[@www-pymongo-tutorial]. For example, we can count the documents 
in the *cloudmesh_commpunity* by using the following command:

```python
cloudmesh = count_documents({})
```

To create a more specific count, one would use a command similar 
to this:

```python
cloudmesh = count_documents({'author': 'von Laszewski'})
```

This technology supports some more advanced querying options as 
well. Those advanced queries allow one to add certain contraints 
and narrow down the results even more. For example, to get the 
courses thought by professor von Laszewski after a certain date, 
one would use the following command:

```python
d = datetime.datetime(2017, 11, 12, 12)
for course in cloudmesh.find({'date': {'$lt': d}}).sort('author'):
    pprint.pprint(course)
```

### Indexing

Indexing is a very important part of querying. It can greately 
improve query performance but also add functionality and aide in 
storing documents [@www-pymongo-tutorial]. 

> "To create a unique index on a key that rejects documents whose 
> value for that key already exists in the index" 
> [@www-pymongo-tutorial].

We need to firstly create the index in the following manner:

```python
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
unique=True)
sorted(list(db.profiles.index_information()))
```

This command acutally creates two different indexes. The first 
one is the *_id* , created by MongoDB automatically, and the 
second one is the *user_id*, created by the user.

The purpose of those indexes is to cleverly prevent future 
additions of invalid *user_ids* into a collection.

### Sorting

Sorting on the server-side is also avaialable via MongoDB. 
The PyMongo *sort()* method is equivalent to the SQL 
*order by*  statement and it can be performed as *pymongo.ascending* 
and *pymongo.descending* [@book-ohiggins]. This method is much 
more efficient as it is being completed on the server-side, 
compared to the sorting completed on the client side. For example, 
to return all users with first name *Gregor* sorted in descending 
order by birthdate we would use a command such as this:

```python
users = cloudmesh.users.find({'firstname':'Gregor'}).sort(('dateofbirth', pymongo.DESCENDING))
for user in users:
   print user.get('email')
```

### Aggregation

Aggregation operations are used to process given data and produce 
summarized results. Aggregation operations collect data from a number 
of documents and provide collective results by grouping data. PyMongo 
in its documentation offers a separate framework that supports data 
aggregation. This aggregation framework can be used to 

> "provide projection capabilities to reshape the returned data"
> [@www-mongo-aggregation].

In the aggregation pipeline, documents pass through multiple pipeline 
stages which convert documents into result data. The basic pipeline 
stages include filters. Those filters act like document transformation 
by helping change the document output form. Other pipelines help group 
or sort documents with specific fields. By using native operations from 
MongoDB, the pipeline operators are efficient in aggregating results.

The *addFields* stage is used to add new fields into documents. It 
reshapes each document in stream, similarly to the *project* stage. 
The output document will contain existing fields from input documents 
and the newly added fields @www-docs-mongodb]. The following example 
shows how to add *student details* into a document.

```
  db.cloudmesh_community.aggregate([
 {
        $addFields: {
        "document.StudentDetails": {
        $concat:['$document.student.FirstName', '$document.student.LastName']
            }
        }
    } ])
```

The *bucket* stage is used to categorize incoming documents 
into groups based on specified expressions. Those groups are 
called *buckets* [@www-docs-mongodb]. The following example shows 
the *bucket* stage in action.

```python
db.user.aggregate([
{ "$group": {
  "_id": {
    "city": "$city",
    "age": {
      "$let": {
        "vars": { 
 "age": { "$subtract" :[{ "$year": new Date() },{ "$year": "$birthDay" }] }},
        "in": {
          "$switch": {
            "branches": [
              { "case": { "$lt": [ "$$age", 20 ] }, "then": 0 },
              { "case": { "$lt": [ "$$age", 30 ] }, "then": 20 },
              { "case": { "$lt": [ "$$age", 40 ] }, "then": 30 },
              { "case": { "$lt": [ "$$age", 50 ] }, "then": 40 },
              { "case": { "$lt": [ "$$age", 200 ] }, "then": 50 }
            ] }  }  } } },
  "count": { "$sum": 1 }}})
```

In the *bucketAuto* stage, the boundaries are automatically 
determined in an attempt to evenly distribute documents into
a specified number of buckets. In the following operation, 
input documents are grouped into four buckets according to 
the values in the price field [@www-docs-mongodb].

```python
db.artwork.aggregate( [
  {
    $bucketAuto: {
        groupBy: "$price",
        buckets: 4
    }
  }
 ] )
```

The *collStats* stage returns statistics regarding a collection 
or view [@www-docs-mongodb].

```python
db.matrices.aggregate( [ { $collStats: { latencyStats: { histograms: true } }
 } ] )
 ```
The *count* stage passes a document to the next stage that 
contains the number documents that were input to the stage 
[@www-docs-mongodb].

 ```python
 db.scores.aggregate(  [    {
    $match: {        score: {          $gt: 80    } }  },
  {      $count: "passing_scores"  } ])
```

The *facet* stage helps process multiple aggregation pipelines 
in a single stage [@www-docs-mongodb].

```python
db.artwork.aggregate( [ {
   $facet: {  "categorizedByTags": [   { $unwind: "$tags" },
       { $sortByCount: "$tags" }  ],  "categorizedByPrice": [
       // Filter out documents without a price e.g., _id: 7
       { $match: { price: { $exists: 1 } } },
      { $bucket: { groupBy: "$price",
          boundaries: [  0, 150, 200, 300, 400 ],
          default: "Other",
          output: { "count": { $sum: 1 },
            "titles": { $push: "$title" }
          } }        }], "categorizedByYears(Auto)": [
      { $bucketAuto: { groupBy: "$year",buckets: 4 }
      } ]}}])
```

The *geoNear* stage returns an ordered stream of documents 
based on the proximity to a geospatial point. The output documents 
include an additional distance field and can include a location 
identifier field [@www-docs-mongodb].

```python
db.places.aggregate([
 {    $geoNear: {
      near: { type: "Point", coordinates: [ -73.99279 , 40.719296 ] },
      distanceField: "dist.calculated",
      maxDistance: 2,
      query: { type: "public" },
      includeLocs: "dist.location",
      num: 5,
      spherical: true
   }  }])
```

The *graphLookup* stage performs a recursive search on a 
collection. To each output document, it adds a new array field 
that contains the traversal results of the recursive search 
for that document [@www-docs-mongodb].

```python
db.travelers.aggregate( [
 {
    $graphLookup: {
       from: "airports",
       startWith: "$nearestAirport",
       connectFromField: "connects",
       connectToField: "airport",
       maxDepth: 2,
       depthField: "numConnections",
       as: "destinations"
    }
 }
] )
```

The *group* stage consumes the document data per each 
distinct group. It has a RAM limit of 100 MB. If the 
stage exceeds this limit, the *group* produces an 
error [@www-docs-mongodb].

```python
db.sales.aggregate(
 [
    {
      $group : {
         _id : { month: { $month: "$date" }, day: { $dayOfMonth: "$date" }, 
         year: { $year: "$date" } },
         totalPrice: { $sum: { $multiply: [ "$price", "$quantity" ] } },
         averageQuantity: { $avg: "$quantity" },
         count: { $sum: 1 }
       }
    }
 ]
)
```

The *indexStats* stage returns statistics regarding 
the use of each index for a collection [@www-docs-mongodb].
 
```python
db.orders.aggregate( [ { $indexStats: { } } ] )
```
 
The *limit* stage is used for controlling the number of 
documents passed to the next stage in the pipeline 
[@www-docs-mongodb].

```python
db.article.aggregate(
  { $limit : 5 }
)
```

The *listLocalSessions* stage gives the session information 
currently connected to mongos or mongod instance 
[@www-docs-mongodb].

```python
db.aggregate( [  { $listLocalSessions: { allUsers: true } } ] )
```
 
The *listSessions* stage lists out all session that have 
been active long enough to propagate to the *system.sessions* 
collection [@www-docs-mongodb].

```python
 use config
 db.system.sessions.aggregate( [  { $listSessions: { allUsers: true } } ] )
```

The *lookup* stage is useful for performing outer joins to 
other collections in the same database [@www-docs-mongodb].

```python
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       as: <output array field>
     }
}
```

The *match* stage is used to filter the document stream. 
Only matching documents pass to next stage [@www-docs-mongodb].

```python
db.articles.aggregate(
    [ { $match : { author : "dave" } } ]
)
```

The *project* stage is used to reshape the documents by 
adding or deleting the fields.

```python
db.books.aggregate( [ { $project : { title : 1 , author : 1 } } ] )
```

The *redact* stage reshapes stream documents by restricting 
information using information stored in documents themselves 
[@www-docs-mongodb].

```python
  db.accounts.aggregate(
  [
    { $match: { status: "A" } },
    {
      $redact: {
        $cond: {
          if: { $eq: [ "$level", 5 ] },
          then: "$$PRUNE",
          else: "$$DESCEND"
        }      }    }  ]);
```

The *replaceRoot* stage is used to replace a document with 
a specified embedded document [@www-docs-mongodb].

```python
  db.produce.aggregate( [
   {
     $replaceRoot: { newRoot: "$in_stock" }
   }
] )
```

The *sample* stage is used to sample out data by randomly 
selecting number of documents form input [@www-docs-mongodb].

```python
  db.users.aggregate(
   [ { $sample: { size: 3 } } ]
)
```

The *skip* stage skips specified initial number of documents 
and passes remaining documents to the pipeline [@www-docs-mongodb].

 ```python
 db.article.aggregate(
    { $skip : 5 }
 );
 ```
 
The *sort* stage is useful while reordering document stream 
by a specified sort key [@www-docs-mongodb].

```python
 db.users.aggregate(
    [
      { $sort : { age : -1, posts: 1 } }
    ]
 )
```

The *sortByCounts* stage groups the incoming documents 
based on a specified expression value and counts documents 
in each distinct group [@www-docs-mongodb].

```python
db.exhibits.aggregate(
[ { $unwind: "$tags" },  { $sortByCount: "$tags" } ] )
```

The *unwind* stage deconstructs an array field from the 
input documents to output a document for each element [@www-docs-mongodb].

```python
db.inventory.aggregate( [ { $unwind: "$sizes" } ] )
db.inventory.aggregate( [ { $unwind: { path: "$sizes" } } ] )
```

The *out* stage is used to write aggregation pipeline results 
into a collection. This stage should be the last stage of a 
pipeline [@www-docs-mongodb].

```python
db.books.aggregate( [
                  { $group : { _id : "$author", books: { $push: "$title" } } },
                      { $out : "authors" }
                  ] )
```

Another option from the *aggregation operations* is the Map/Reduce 
framework, which essentially includes two different functions,
*map* and *reduce*. The first one provides the key value pair for 
each tag in the array, while the latter one

> "sums over all of the emitted values for a given key"
> [@www-mongo-aggregation].

The last step in the Map/Reduce process it to call the 
*map_reduce()* function and iterate over the results 
[@www-mongo-aggregation]. The Map/Reduce operation provides 
result data in a collection or returns results in-line. One 
can perform subsequent operations with the same input collection 
if the output of the same is written to a collection 
[@www-docs-map-reduce]. An operation that produces results 
in a in-line form must provide results with in the BSON 
document size limit. The current limit for a BSON document is 
16 MB. These types of operations are not supported by views 
[@www-docs-map-reduce]. The PyMongo's API supports all 
features of the MongoDB's Map/Reduce engine [@www-api-map-reduce]. 
Moreover, Map/Reduce has the ability to get more detailed results 
by passing *full_response=True* argument to the *map_reduce()* 
function [@www-api-map-reduce].

### Deleting Documents from a Collection

The deletion of documents with PyMongo is fairly straight 
forward. To do so, one would use the *remove()* method of 
the PyMongo Collection object [@book-ohiggins]. Similarly 
to the reads and updates, specification of documents to be 
removed is a must. For example, removal of the entire 
document collection with a score of 1, would required one 
to use the following command:

```python
cloudmesh.users.remove({"score":1, safe=True})
```

The *safe* parameter set to *True* ensures the operation was 
completed [@book-ohiggins]. 

### Copying a Database

Copying databases within the same mongod instance or between
different mongod servers is made possible with the *command()*
method after connecting to the desired mongod instance 
[@www-pymongo-documentation-copydb]. For example, to copy the 
*cloudmesh* database and name the new database *cloudmesh_copy*, 
one would use the *command()* method in the following manner:

```python
client.admin.command('copydb',
                         fromdb='cloudmesh',
                         todb='cloudmesh_copy')
```

There are two ways to copy a database between servers. If a
server is not password-prodected, one would not need to 
pass in the credentials nor to authenticate to the admin 
database [@www-pymongo-documentation-copydb]. In that case, 
to copy a database one would use the following command:

```python
client.admin.command('copydb',
                         fromdb='cloudmesh',
                         todb='cloudmesh_copy',
                         fromhost='source.example.com')
```

On the other hand, if the server where we are copying the 
database to is protected, one would use this command instead:

```python
client = MongoClient('target.example.com',
                     username='administrator',
                     password='pwd')
client.admin.command('copydb',
                     fromdb='cloudmesh',
                     todb='cloudmesh_copy',
                     fromhost='source.example.com')
```

### PyMongo Strengths

One of PyMongo strengths is that allows document creation and 
querying natively

> "through the use of existing language features such as nested 
> dictionaries and lists" [@book-ohiggins]. 

For moderately experienced Python developers, it is very easy to 
learn it and quickly feel comfortable with it.

> "For these reasons, MongoDB and Python make a powerful 
> combination for rapid, iterative development of horizontally 
> scalable backend applications" [@book-ohiggins].

According to [@book-ohiggins], MongoDB is very applicable 
to modern applications, which makes PyMongo equally valuable 
[@book-ohiggins].

## MongoEngine

> "MongoEngine is an Object-Document Mapper, written in Python 
> for working with MongoDB" [@www-docs-mongoengine]. 

It is actually a library that allows a more advanced communication 
with MongoDB compared to PyMongo. As MongoEngine is technically 
considered to be an object-document mapper(ODM), it can also be 
considered to be 

> "equivalent to a SQL-based object relational mapper(ORM)" 
> [@www-realpython].

The primary technique why one would use an ODM includes 
*data conversion* between computer systems that are not 
compatible with each other [@www-wikiodm]. For the purpose of 
converting data to the appropriate form, a *virtual object 
database* must be created within the utilized programming 
language [@www-wikiodm]. This library is also used to define 
schemata for documents within MongoDB, which ultimately helps
with minimizing coding errors as well defining methods 
on existing fields [@www-mongoengine-schema]. It is also           
very beneficial to the overall workflow as it tracks changes 
made to the documents and aids in the document saving process 
[@www-mongoengine-instances].

### Installation

The installation process for this technology is fairly simple 
as it is considered to be a library. To install it, one would 
use the following command [@www-installing]:

```bash
$ pip install mongoengine
```

A *bleeding-edge* version of MongoEngine can be installed directly 
from GitHub by first cloning the repository on the local machine, 
virtual machine, or cloud.

### Connecting to a database using MongoEngine

Once installed, MongoEngine needs to be connected to an 
instance of the mongod, similarly to PyMongo [@www-connecting]. 
The *connect()* function must be used to successfully 
complete this step and the argument that must be used in 
this function is the name of the desired database [@www-connecting]. 
Prior to using this function, the function name needs 
to be imported from the MongoEngine library.

```python
from mongoengine import connect
connect('cloudmesh_community')
```

Similarly to the MongoClient, MongoEngine uses the local 
host and port 27017 by default, however, the *connect()* 
function also allows specifying other hosts and port 
arguments as well [@www-connecting].

```bash
connect('cloudmesh_community', host='196.185.1.62', port=16758)
```

Other types of connections are also supported (i.e. URI) 
and they can be completed by providing the URI in the 
*connect()* function [@www-connecting]. 

### Querying using MongoEngine

To query MongoDB using MongoEngine an *objects attribute* 
is used, which is, technically, a part of the document 
class [@www-querying]. This attribute is called the 
*QuerySetManager* which in return 

>"creates a new *QuerySet* object on access" [@www-querying].

To be able to access individual documents from a database, 
this object needs to be iterated over. For example, to 
return/print all students in the *cloudmesh_community* object 
(database), the following command would be used.

```python
for user in cloudmesh_community.objects:
   print cloudmesh_community.student
```

MongoEngine also has a capability of query filtering 
which means that a keyword can be used within the called 
*QuerySet* object to retrieve specific information 
[@www-querying]. Let's say one would like to iterate over 
*cloudmesh_community* students that are natives of Indiana. 
To achieve this, one would use the following command:

```python
indy_students = cloudmesh_community.objects(state='IN')
```

This library also allows the use of all operators except 
for the equality operator in its queries, and moreover, 
has the capability of handling *string queries*, *geo queries*, 
*list querying*, and querying of the raw PyMongo queries 
[@www-querying]. 

The string queries are useful in performing text operations 
in the conditional queries. A query to find a document exactly
matching and with state *ACTIVE* can be performed in the 
following manner:

```python
db.cloudmesh_community.find( State.exact("ACTIVE") )
```

The query to retrieve document data for names that start with 
a case sensitive *AL* can be written as:

```python
db.cloudmesh_community.find( Name.startswith("AL") )
```

To perform an exact same query for the non-key-sensitive *AL* one 
would use the following command:

```python
db.cloudmesh_community.find( Name.istartswith("AL") )
```

The MongoEngine allows data extraction of geographical locations 
by using Geo queries. The *geo_within* operator checks if a 
geometry is within a polygon.

```python
  cloudmesh_community.objects(
            point__geo_within=[[[40, 5], [40, 6], [41, 6], [40, 5]]])
  cloudmesh_community.objects(
            point__geo_within={"type": "Polygon",
                 "coordinates": [[[40, 5], [40, 6], [41, 6], [40, 5]]]})
```

The list query looks up the documents where the specified fields 
matches exactly to the given value. To match all pages that have 
the word  *coding* as an item in the *tags* list one would use 
the following query:

```python
  class Page(Document):
     tags = ListField(StringField())

  Page.objects(tags='coding')
```

Overall, it would be safe to say that MongoEngine has good 
compatibility with Python. It provides different functions 
to utilize Python easily with MongoDBand which makes this 
pair even more attractive to application developers.

## Flask-PyMongo

> "Flask is a micro-web framework written in Python" 
> [@www-flask-framework].                                                       

It was developed after Django, and it is very pythonic 
in nature which implies that it is explicitly the targeting 
the Python user community. It is lightweight as it does not 
require additional tools or libraries and hence is classified 
as a Micro-Web framework. It is often used with MongoDB using 
PyMongo connector, and it treats data within MongoDB as searchable 
Python dictionaries. The applications such as Pinterest, LinkedIn, 
and the community web page for Flask are using the Flask framework. 
Moreover, it supports various features such as the RESTful request 
dispatching, secure cookies, Google app engine compatibility, and 
integrated support for unit testing, etc [@www-flask-framework]. 
When it comes to connecting to a database, the connection details 
for MongoDB can be passed as a variable or configured in PyMongo 
constructor with additional arguments such as username and password, 
if required. It is important that versions of both Flask and MongoDB 
are compatible with each other to avoid functionality breaks 
[@www-flask-pymongo]. 

### Installation

Flask-PyMongo can be installed with an easy command such as this:

```bash
$ pip install Flask-PyMongo
```

PyMongo can be added in the following manner:

```python
  from flask import Flask
  from flask_pymongo import PyMongo
  app = Flask(__name__)
  app.config["MONGO_URI"] = "mongodb://localhost:27017/cloudmesh_community"
  mongo = PyMongo(app)
```

### Configuration

There are two ways to configure Flask-PyMongo. The first way 
would be to pass a MongoDB URI to the PyMongo constructor, 
while the second way would be to

> "assign it to the MONGO_URI Flask confiuration variable" 
> [@www-flask-pymongo].

### Connection to multiple databases/servers

Multiple PyMongo instances can be used to connect to multiple 
databases or database servers. To achieve this, once would 
use a command similar to the following:

```python
  app = Flask(__name__)
  mongo1 = PyMongo(app, uri="mongodb://localhost:27017/cloudmesh_community_one")
  mongo2 = PyMongo(app, uri="mongodb://localhost:27017/cloudmesh_community_two")
  mongo3 = PyMongo(app, uri=
        "mongodb://another.host:27017/cloudmesh_community_Three")
```

### Flask-PyMongo Methods

Flask-PyMongo provides helpers for some common tasks. 
One of them is the *Collection.find_one_or_404* method 
shown in the following example: 

```python
  @app.route("/user/<username>")
  def user_profile(username):
      user = mongo.db.cloudmesh_community.find_one_or_404({"_id": username})
      return render_template("user.html", user=user)
```

This method is very similar to the MongoDB's *find_one()* 
method, however, instead of returning *None* it causes 
a *404 Not Found HTTP* status [@www-flask-pymongo]. 

Similarly, the *PyMongo.send_file* and *PyMongo.save_file* 
methods work on the file-like objects and save them to GridFS 
using the given file name [@www-flask-pymongo].

### Additional Libraries

Flask-MongoAlchemy and Flask-MongoEngine are the additional 
libraries that can be used to connect to a MongoDB database 
while using enhanced features with the Flask app. The 
Flask-MongoAlchemy is used as a proxy between Python and 
MongoDB to connect. It provides an option such as server or 
database based authentication to connect to MongoDB. While the 
default is set server based, to use a database-based authentication, 
the config value *MONGOALCHEMY_SERVER_AUTH* parameter must be 
set to *False* [@www-pythonhosted-MongoAlchemy]. 

Flask-MongoEngine is the Flask extension that provides 
integration with the MongoEngine. It handles connection 
management for the apps. It can be installed through *pip* and 
set up very easily as well. The default configuration 
is set to the local host and port 27017. For the custom port 
and in cases where MongoDB is running on another server, the host 
and port must be explicitly specified in connect strings within 
the *MONGODB_SETTINGS* dictionary with *app.config*, along with 
the database username and password, in cases where a database 
authentication is enabled. The URI style connections are also 
supported and supply the URI as the host in the *MONGODB_SETTINGS* 
dictionary with *app.config*. There are various custom query sets 
that are available within Flask-Mongoengine that are attached to 
Mongoengine's default queryset [@www-flask-mongoengine]. 

### Classes and Wrappers

Attributes such as *cx* and *db* in the PyMongo objects are 
the ones that help provide access to the MongoDB server 
[@www-flask-pymongo]. To achieve this, one must pass the 
Flask app to the constructor or call *init_app()* [@www-flask-pymongo]. 

> "Flask-PyMongo wraps PyMongo's MongoClient, Database, and 
> Collection classes, and overrides their attribute and item 
> accessors" [@www-flask-pymongo]. 

This type of wrapping allows Flask-PyMongo to add methods to 
*Collection* while at the same time allowing a MongoDB-style 
dotted expressions in the code [@www-flask-pymongo]. 

```python
type(mongo.cx)
type(mongo.db)
type(mongo.db.cloudmesh_community)
```

Flask-PyMongo creates connectivity between Python and Flask 
using a MongoDB database and supports 

> "extensions that can add application features as if they were 
> implemented in Flask itself" [@www-wiki-flask],

hence, it can be used as an additional Flask functionality in 
Python code. The extensions are there for the purpose of 
supporting form validations, authentication technologies, 
object-relational mappers and framework related tools which 
ultimately adds a lot of strength to this micro-web framework 
[@www-wiki-flask]. One of the main reasons and benefits why it is 
frequently used with MongoDB is its capability of adding more 
control over databases and history [@www-wiki-flask].

