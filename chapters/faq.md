# FAQ: General

In this section TA's and students can add FAQ's from the piazza. As
the material especially the programming related one is so useful that
it is shared by now in multiple classes, however they use different
piazza's sharing the information in an FAQ in the handbook allows us
to quickly disseminate the relevant information between classes. If an
FAQ is only for one class we will be especially mark it.

## Where to find the FAQ as markdown?

General FAQs are in

* <https://github.com/cloudmesh-community/book/blob/master/chapters/faq.md>

For 516 we have also

* <https://github.com/cloudmesh-community/book/blob/master/chapters/faq-516.md>

For 523 we have

* <https://github.com/cloudmesh-community/book/blob/master/chapters/faq-523.md>


## Why are some FAQs that are on piazza not here?

Two reason:

1. some of them need not to be in this FAQ.

2. The TAs will evaluate the FAQs every day at the end of the day and
   integrate those that need to be in this list at that time. Hence it
   may take up to 24 hours for FAQs to appear here.

Once an FAQ is in the book answered (it may actually be part of
another section, TAs will mark the FAQ in piazza, so you can make sure
which FAQs are already in the book. We recommend to look in the book
as there could be information in it that you otherwise missed.

## Can I assume that all information is in the FAQ to do the class?

No. The class book will be our main source of information not just a
single file.

## How do I find all FAQs on Piazza?

Two ways exist

a) Please visit your class piazza. You will find a "faq" tag in your
piazza window. Click on it and all posts marked with FAQ will show up,

b) In the search field type in FAQ. All posts with the text FAQ in it
will be listed. 

## FAQ: has SOIC computers I can use remotely?

See: <https://uisapp2.iu.edu/confluence-prd/pages/viewpage.action?pageId=114491559>

##FAQ: when contributing to the book my name is not listed properly or not at all

The following reasons exist:

1. if its not listed at all your contribution may be in a different
   repository, please contact Gregor

2. if it does not show up correctly and only shows your github name,
   which you can see in the contributor section or with

 
```bash
$ git shortlog -s -e
     2  btpope <42694671+btpope@users.noreply.github.com>
     1  luoyu357 <luoyu357@gmail.com>
     1  shilpasingh21 <shilpasingh21@gmail.com>
```
 
You need to do two things.

First, add your name to the file 

* <https://github.com/cloudmesh-community/book/blob/master/.mailmap>

 

Second, complete the set up your git on the machine you work with in
case you use a commandline tool with git init (see our notes on this)

 

If you use the GUI you may need to go to the account settings and
associate a first name lastname, I however do not know ho to do that,
so if you kwon reply ti this


## FAQ: How to read the technical sections of the lecture notes

This is an important tip and I recommend that you read it.

We will add throughout the semester some technical lecture notes. These
notes contain information on how to run certain things
on a computer. What we have seen in the past with some students is
that they do not read the text between the sections that look like you
can just execute them. They also may include information that is
important and should not be overlooked.

Here is the workflow on how to read such technical sections

1. do not execute anything yet

2. read the entire section including the lines between the gray boxes

3. step back and reflect on what you read

4. reread the section, if a section needs more information google for
   it (things could be overnight updated on the internet, please
   remember we are just presenting a snapshot in time here)

5. once you have obtained knowledge, decide if the section is relevant
   for you (e.g. windows sections may not be relevant for MacOS users)

6. carefully execute the relevant portions for you

:warning: AS ALWAYS THERE IS NO GUARANTEE THAT WHAT WE DOCUMENT WORKS
OR COULD NOT DESTROY SOMETHING. MAKE SURE TO HAVE A BACKUP. IF IN
DOUBT RUN IN A VIRTUAL MACHINE IF YOU CAN.

## How to check if a yaml file is valid?

In case you need to check an open source public YAML file you can use
the following

The easiest is to use yamllint:

```bash
$ pip install yamllint
$ yamllint README.yml
```

A python script to check it is available at

* <https://github.com/cloudmesh-community/fa18-516-21/blob/master/validate_yml.py>

Online checkers are available at

* <https://codebeautify.org/yaml-validator>

A ruby script can do

```bash
$ ruby-e "require 'yaml';puts YAML.load_file('./README.yml')"
```

YAML validation in visual studio can be achieved also

  <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml>

## How do I check if a markdown file is valid?

Markdown is such a simple format that you should not have any
issue. We recommend that you do a local checkout of the epub and
compile it and look at your section contribution.

To work on a songel file yo ucan jsut use markdown editors.

A lint program is available at

* <https://github.com/remarkjs/remark-lint>

However I recommend to copy your file into a separate directory and
check it there as it installs some other programs into the directory
wher you do the checking.

Editors that students have used include

* Remarkable: <https://remarkableapp.github.io/>
* Macdown: <https://macdown.uranusjr.com/>
* Mark Down validation and preview:  <https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one>

## Do not use html smaller equal without quoting

Please note that you must not use 

`<argument>`

in markdown. It has a special meaning and likely will result in an error.

If you really need to use it you must quote it in code/verbatim mode

``<argument>``

## Has SOIC computers I can use remotely?
 
See: https://uisapp2.iu.edu/confluence-prd/pages/viewpage.action?pageId=114491559

 
## How to read the technical sections of the lecture notes
 
This is an important tip and I recommend that you read it.

We will add soon some technical lecture notes. Thes notes contain
tutorial-like information on how to run certain things on a
computer. What we have seen in the past with some students is that
they do not read the text between the sections that look like you can
just execute them. They also may include information that is important
and should not be overlooked.

 

Here is the workflow on how to read such technical sections

 

a) do not execute anything yet

b) read the entire section including the lines between the gray boxes

c) step back and reflect on what you read

d) reread the section, if a section needs more information google for it (things could be overnight updated on the internet, please remember we are just presenting a snapshot in time here)

e) once you have obtained knowledge, decide if the section is relevant for you (e.g. windows sections may not be relevant for MacOS users)

f) carefully execute the relevant portions for you

 

AS ALWAYS THERE IS NO GUARANTEE THAT WHAT WE DOCUMENT WORKS OR COULD
NOT DESTROY SOMETHING. MAKE SURE TO HAVE A BACKUP. IF IN DOUBT RUN IN
A VIRTUAL MACHINE IF YOU CAN.

## Download the epub ferquently

Please be reminded that the epub is updated frequently and we
recommend that you download it before you read.


I myself have integrated an epub reader in my Web browser so that
every time I click on the View Raw in github, I get the most up to
date version.

 

I use ibooks on OSX, calibre is a good system on Windows and Linux, MS
also has Microsoft Edge. However on Microsoft edge you will need the
lates version which starts with 42

## Spelling of notebook.md
 
The spelling of notebook.md is notebook.md

not

Notebook.md or NOTEBOOK.md or other spelling

Please, correct if you did not use lower case 

The spelling of README.yml is README.yml and not 

README.md (which needs to be removed) or readme.yaml

please correct (if needed)

## How to open the epub from Github

If you see thw View Raw, you need to click on it. It will download the
file. Than you can open that.

However, If you use edge or integrated your epub viewer in your
browser and clicking on it will automatically open your epub browser. 

 
