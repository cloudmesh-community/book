## Mongoengine

### Introduction

MongoEngine is a document mapper for working with mongoldb with python. To be able to use mongo engine MongodD should be already installed and running. 

### Install and connect

Mongoengine can be installed by running:     

    pip install mongo engine

This will install six, pymongo and mongoengine.
To connect to mongoldb use connect () function by specifying mongoldb instance name. You don’t need to go to mongo shell but this can be done from unix shell or cmd line. In this case we are connecting to a database named student_db.  

    from mongo engine import *
    connect (‘student_db’)

If mongodb is running on a port different from default port , port number and host need to be specified.
If mongoldb needs authentication username and password need to be specified.

###  Basics

Mongodb does not enforce schemas. Comparing to RDBMS, Row in mongoldb is called a “document” and table can be compared to *Collection*. 
Defining a schema is helpful as it minimizes coding error’s. To define a schema we create a class that inherits from document.


    from mongoengine import *

    class Student(Document): 
       first_name = StringField(max_length=50)
       last_name = StringField(max_length=50)
       
\TODO{Can you fix the code sections and look at the examples we provided}       

Fields are not mandatory but if needed, set the required keyword argument to True. There are multiple values available for field types. Each field can be customized by by keyword argument.  
If each student is sending text messages to Universities central database , these can be stored using Mongodb. Each text can have different data types, some might have images or some might have url's.
So we can create a class text and link it to student by using Reference field (similar to foreign key in RDBMS).  

```
class Text(Document):
    title = StringField(max_length=120, required=True)  
    author = ReferenceField(Student)  
    meta = {'allow_inheritance': True} 

class OnlyText(Text):.  
    content = StringField()

class ImagePost(Text):.  
    image_path = StringField()

class LinkPost(Text):  
    link_url = StringField()
```  
   
MongoDb supports adding tags to individual texts rather then storing them separately and then having them referenced.Similarly Comments can also be stored directly in a Text. 

```
class Text(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
```

For accessing data: if we need to get titles.  

```
for text in OnlyText.objects:  
    print(text.title)  
```
    
Searching texts with tags.

```
for text in Text.objects(tags='mongodb'): 
    print(text.title)
```