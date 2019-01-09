# Data Management {#sec:python-data}

Obviously when dealing with big data we may not only be dealing with
data in one format but in many different formats. It is important that
you will be able to master such formats and seamlessly integrate in your
analysis. Thus we provide some simple examples on which different data
formats exist and how to use them.

## Formats

### Pickle

Python pickle allows you to save data in a python native format into a
file that can later be read in by other programs. However, the data
format may not be portable among different python versions thus the
format is often not suitable to store information. Instead we recommend
for standard data to use either json or yaml.

```python
import pickle

flavor = {
    "small": 100, 
    "medium": 1000,
    "large": 10000
    }

pickle.dump( flavor, open( "data.p", "wb" ) )
```

To read it back in use

```python
flavor = pickle.load( open( "data.p", "rb" ) )
```

### Text Files

To read text files into a variable called content you can use

```python
content = open('filename.txt', 'r').read() 
```

You can also use the following code while using the convenient `with`
statement

```python
with open('filename.txt','r') as file:
    content = file.read()
```

To split up the lines of the file into an array you can do

```python
with open('filename.txt','r') as file:
    lines = file.read().splitlines()
```

This cam also be done with the build in `readlines` function

```python
lines = open('filename.txt','r').readlines()
```

In case the file is too big you will want to read the file line by line:

```python
with open('filename.txt','r') as file:
    line = file.readline()
    print (line)
```

### CSV Files

Often data is contained in comma separated values (CSV) within a file.
To read such files you can use the csv package.

```python
import csv
with open('data.csv', 'rb') as f:
   contents = csv.reader(f)
for row in content:
    print row
```

Using pandas you can read them as follows.

```python
import pandas as pd
df = pd.read_csv("example.csv") 
```

There are many other modules and libraries that include CSV read
functions. IN case you need to split a single line by comma, you may
also use the `split` function. However, remember it swill split at every
comma, including those contained in quotes. SO this method although
looking originally convenient has limitations.

### Excel spread sheets

Pandas contains a method to read Excel files

```python
import pandas as pd
filename = 'data.xlsx'
data = pd.ExcelFile(file)
df = data.parse('Sheet1')
```

### YAML

YAML is a very important format as it allows you easily to structure
data in hierarchical fields It is frequently used to coordinate programs
while using yaml as the specification for configuration files, but also
data files. To read in a yaml file the following code can be used

```python
import yaml
with open('data.yaml', 'r') as f:
    content = yaml.load(f)
```

The nice part is that this code can also be used to verify if a file is
valid yaml. To write data out we can use

```python
with open('data.yml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
```

The flow style set to false formats the data in a nice readable fashion
with indentations.

### JSON

```python
import json
with open('strings.json') as f:
    content = json.load(f)
```

### XML :o:

Please contribute a XML python section

### RDF

To read RDF files you will need to install RDFlib with

``` {.bash}
$ pip install rdflib
```

This will than allow you to read RDF files

```python
from rdflib.graph import Graph
g = Graph()
g.parse("filename.rdf", format="format")
for entry in g:
   print(entry)
```

Good examples on using RDF are provided on the RDFlib Web page
at <https://github.com/RDFLib/rdflib>

From the Web page we showcase also how to directly process RDF data from
the Web

```python
import rdflib
g=rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')

for s,p,o in g:
    print s,p,o
```

### PDF

The Portable Document Format (PDF) has been made available by Adobe
Inc. royalty free. This has enabled PDF to become a world wide adopted
format that also has been standardized in 2008 (ISO/IEC 32000-1:2008,
<https://www.iso.org/standard/51502.html>). A lot of research is
published in papers making PDF one of the de-facto standards for
publishing. However, PDF is difficult to parse and is focused on high
quality output instead of data representation. Nevertheless, tools to
manipulate PDF exist:

PDFMiner

:   <https://pypi.python.org/pypi/pdfminer/> allows the simple
    translation of PDF into text that than can be further mined. The
    manual page helps to demonstrate some examples
    <http://euske.github.io/pdfminer/index.html>.

pdf-parser.py

:   <https://blog.didierstevens.com/programs/pdf-tools/> parses pdf
    documents and identifies some structural elements that can than be
    further processed.

If you know about other tools, let us know.

### HTML

A very powerful library to parse HTML Web pages is provided
with <https://www.crummy.com/software/BeautifulSoup/>

More details about it are provided in the documentation page
<https://www.crummy.com/software/BeautifulSoup/bs4/doc/>

:o: TODO: Students can contribute a section

### ConfigParser

:o: TODO: Students can contribute a section

* <https://pymotw.com/2/ConfigParser/>

### ConfigDict

* <https://github.com/cloudmesh/cloudmesh.common/blob/master/cloudmesh/common/ConfigDict.py>

## Encryption

Often we need to protect the information stored in a file. This is
achieved with encryption. There are many methods of supporting
encryption and even if a file is encrypted it may be target to attacks.
Thus it is not only important to encrypt data that you do not want
others to se but also to make sure that the system on which the data is
hosted is secure. This is especially important if we talk about big data
having a potential large effect if it gets into the wrong hands.

To illustrate one type of encryption that is non trivial we have chosen
to demonstrate how to encrypt a file with an ssh key. In case you have
openssl installed on your system, this can be achieved as follows.

```bash
    #! /bin/sh

    # Step 1. Creating a file with data
    echo "Big Data is the future." > file.txt

    # Step 2. Create the pem 
    openssl rsa -in ~/.ssh/id_rsa -pubout  > ~/.ssh/id_rsa.pub.pem

    # Step 3. look at the pem file to illustrate how it looks like (optional)
    cat ~/.ssh/id_rsa.pub.pem

    # Step 4. encrypt the file into secret.txt
    openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pub.pem -in file.txt -out secret.txt

    # Step 5. decrypt the file and print the contents to stdout
    openssl rsautl -decrypt -inkey ~/.ssh/id_rsa -in secret.txt
```

Most important here are Step 4 that encrypts the file and Step 5 that
decrypts the file. Using the Python os module it is straight forward to
implement this. However, we are providing in cloudmesh a convenient
class that makes the use in python very simple.

```python
from cloudmesh.common.ssh.encrypt import EncryptFile

e = EncryptFile('file.txt', 'secret.txt')
e.encrypt()
e.decrypt()
```

In our class we initialize it with the locations of the file that is to
be encrypted and decrypted. To initiate that action just call the
methods `encrypt` and `decrypt`.

## Database Access

:o: TODO: Students: define conventional database access section

see: <https://www.tutorialspoint.com/python/python_database_access.htm>

## SQLite

;o: TODO: Students can contribute to this section

<https://www.sqlite.org/index.html>

<https://docs.python.org/3/library/sqlite3.html>

### Exercises :o:

E:Encryption.1:

> Test the shell script to replicate how this example works

E:Encryption.2:

Test the cloudmesh encryption class

E:Encryption.3:

What other encryption methods exist. Can you provide an example and
contribute to the section?

E:Encryption.4:

> What is the issue of encryption that make it challenging for Big
> Data

E:Encryption.5:

> Given a test dataset with many files text files, how long will it
> take to encrypt and decrypt them on various machines. Write a
> benchmark that you test. Develop this benchmark as a group, test out
> the time it takes to execute it on a variety of platforms.
