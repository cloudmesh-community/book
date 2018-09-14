# Python Apache Avro :o:

Although Apache Avro is not directly a messaging system, it uses
messaging to comunicate between components while serializing and
deserializing object defined with a schema. In addition it provides
data structures, remote procedure call (RPC), a container file to
store persistent data and simple integration with dynamic languages
[@hid-sp18-405-tutorial-avro-doc]. Avro depends on schemas, which
are defined with JSON. This facilitates implementation in other
languages that have the JSON libraries. The key advantages of Avro are
schema evolution - Avro will handle the missing/extra/modified fields,
dynamic typing - serialization and deserialization without code
generation, untagged data - data encoding and faster data processing
by allowing data to be written without overhead.

The following steps illustrate using Avro to serialize and deserialize
data with example modified from Apache Avro 1.8.2 Getting Started
(Python) [@hid-sp18-405-tutorial-avro-python].

## Download, Unzip and Install

The zipped installation file *avro-1.8.2.tar.gz* could be downloaded
from
[here](<http://mirrors.ocf.berkeley.edu/apache/avro/avro-1.8.2/py/>)

To unzip, using linux:
    
    tar xvf avro-1.8.2.tar.gz

using MacOS:

    gunzip -c avro-1.8.2.tar.gz | tar xopf -

cd into the directory and install using the following:

    cd avro-1.8.2
    python setup.py install

To check successful installation, import avro in python without error
message:
    
    python
    >>> import avro

This instruction is for Python2. The Python3 counterpart,
*avro-python3-1.8.2.tar.gz* could be downloaded from
[here](<http://mirrors.sonic.net/apache/avro/avro-1.8.2/py3/>) and the unzip and install procedure is the same.

## Defining a schema

Use a simple schema for students contributed in cloudmesh as an
example: paste the following lines into an empty text file with the
name it *student.avsc*

    {"namespace": "cloudmesh.avro",
     "type": "record",
     "name": "Student",
     "fields": [
        {"name": "name", "type": "string"},
        {"name": "hid",  "type": "string"},
        {"name": "age", "type": ["int", "null"]},
        {"name": "project_name", "type": ["string", "null"]}
        ]
    }

This schema defines a record representing a hypothetical student,
which is defined to be a record with the name *Student* and 4 fields,
namely name, hid, age and project name. The type of each of the field
needs to be provided. If any field is optional, one could use the list
including *null* to define the type as shown in age and project name
in the example schema. Further, a namespace *cloudmesh.avro* is also
defined, which together with the name attribute defines the full name
of the schema (cloudmesh.avro.Student in this case).


## Serializing 

The following piece of python code illustrates serialization of some
data

    import avro.schema
    from avro.datafile import DataFileWriter
    from avro.io import DatumWriter

    schema = avro.schema.parse(open("student.avsc", "rb").read())

    writer = DataFileWriter(open("students.avro", "wb"), DatumWriter(), schema)
    writer.append({"name": "Albert Zweistein",
                   "hid": "hid-sp18-405",
                   "age": 99,
                   "project_name": "hadoop with docker"})
    writer.append({"name": "Ben Smith",
                   "hid": "hid-sp18-309",
                   "project_name": "spark with docker"})
    writer.append({"name": "Alice Johnson",
                   "hid": "hid-sp18-208",
                   "age": 27})
    writer.close()

The code does the following:

* Imports required modules
* Reads the schema *student.avsc* (make sure that the schema file is
  placed in the same directory as the python code)
* Create a *DataFileWriter* called writer, for writing serialized
  items to a data file on disk
* Use *DataFileWriter.append()* to add data points to the data
  file. Avro records are represented as Python dicts.
* The resulting data file saved on the disk is named *students.avro*
* This above instruction is for Python2. If one is using Python3,
  change

  ```
  schema = avro.schema.parse(open("student.avsc", "rb").read())
  ```
  
  to:

  ```
  schema = avro.schema.Parse(open("student.avsc", "rb").read())
  ```
  
  since the method name has a different case in Python3.

## Deserializing

The following python code illustrates deserialization 

    from avro.datafile import DataFileReader
    from avro.io import DatumReader

    reader = DataFileReader(
        open("students.avro", "rb"), DatumReader())
    for student in reader:
    print (student)
    reader.close()

The code does the following:

* Imports required modules
* Use *DatafileReader* to read the serilaized data file
  *students.avro*, it is an iterator
* Returns the data in a python dict

The output should look like:

```
{'name': 'Albert Zweistein',
 'hid': 'hid-sp18-405', 
 'age': 29,
 'project_name': 'hadoop with docker'
}
{'name': 'Ben Smith',
 'hid': 'hid-sp18-309',
 'age': None,
 'project_name': 'spark with docker'
}
{'name': 'Alice Johnson',
 'hid': 'hid-sp18-208',
 'age': 27,
 'project_name': None
}
```

## Resources

* The steps and instructions are modified from
  [Apache Avro 1.8.2 Getting Started (Python)](<http://avro.apache.org/docs/1.8.2/gettingstartedpython.html>)
  [@hid-sp18-405-tutorial-avro-python].
* The Avro Python library does not support code generation, while Avro
  used with Java supports code generation, see
  [Apache Avro 1.8.2 Getting Started (Java)](<http://avro.apache.org/docs/1.8.2/gettingstartedjava.html>)
  [@hid-sp18-405-tutorial-avro-java].
* Avro provides a convenient way to represent complex data structures
  within a Hadoop MapReduce job. Details about Avro are documented in
  [Apache Avro 1.8.2 Hadoop MapReduce guide](<http://avro.apache.org/docs/1.8.2/mr.html>)
  [@hid-sp18-405-tutorial-avro-mapreduce].
* For more information on schema files and how to specify name and
  type of a record can be found at
  [record specification](<http://avro.apache.org/docs/1.8.2/spec.html#schema_record>)
  [@hid-sp18-405-tutorial-avro-record].






