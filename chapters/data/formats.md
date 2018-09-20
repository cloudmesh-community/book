# Data Formats :new:

## YAML

The term *YAML* stand for "YAML Ainot Markup Language". According to the
Web Page at

* <http://yaml.org/>

"YAML is a human friendly data serialization standard for all
programming languages." There are multiple versions of YAML existing and
one needs to take care of that your software supports the right version.
The current version is YAML 1.2.

YAML is often used for configuration and in many cases can also be used
as XML replacement. Important is tat YAM in contrast to XML removes the
tags while replacing them with indentation. This has naturally the
advantage that it is mor easily to read, however, the format is strict
and needs to adhere to proper indentation. Thus it is important that you
check your YAML files for correctness, either by writing for example a
python program that read your yaml file, or an online YAML checker such
as provided at

* <http://www.yamllint.com/>

An example on how to use yaml in python is provided in our next example.
Please note that YAML is a superset of JSON. Originally YAML was
designed as a markup language. However as it is not document oriented
but data oriented it has been recast and it does no longer classify
itself as markup language.

    import os
    import sys
    import yaml

    try:
        yamlFilename = os.sys.argv[1]
        yamlFile = open(yamlFilename, "r")
    except:
        print("filename does not exist")
        sys.exit()
    try:
       yaml.load(yamlFile.read())
    except:
       print("YAML file is not valid.")

Resources:

* <http://yaml.org/>
* <https://en.wikipedia.org/wiki/YAML>
* <http://www.yamllint.com/>

## JSON

The term JSON stand for *JavaScript Object Notation*. It is targeted as
an open-standard file format that emphasizes on integration of
human-readable text to transmit data objects. The data objects contain
attribute value pairs. Although it originates from JavaScript, the
format itself is language independent. It uses brackets to allow
organization of the data. PLease note that YAML is a superset of JSON
and not all YAML documents can be converted to JSON. Furthermore JSON
does not support comments. For these reasons we often prefer to us YAMl
instead of JSON. However JSON data can easily be translated to YAML as
well as XML.

Resources:

* <https://en.wikipedia.org/wiki/JSON>
* <https://www.json.org/>

## XML

XML stands for *Extensible Markup Language*. XML allows to define
documents with the help of a set of rules in order to make it machine
readable. The emphasize here is on machine readable as document in XML
can become quickly complex and difficult to understand for humans. XML is
used for documents as well as data structures.

A tutorial about XML is available at

* <https://www.w3schools.com/xml/default.asp>

Resources:

* <https://en.wikipedia.org/wiki/XML>
