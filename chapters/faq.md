# FAQ: General

In this section TA's and students can add FAQ's from the piazza. As
the material especially the programming related one is so useful that
it is shared by now in multiple classes, however they use different
piazza's sharing the information in an FAQ in the handbook allows us
to quickly disseminate the relevant information between classes. If an
FAQ is only for one class we will be especially mark it.

## Can I assume that all information is in the FAQ to do the class?

No. The class book will be our main source of information not just a
collection of FAQ's.


## Piazza

### Why are some FAQs that are on piazza not here?

Two reason:

1. some of them need not to be in this FAQ.

2. The TAs will evaluate the FAQs every day at the end of the day and
   integrate those that need to be in this list at that time. Hence it
   may take up to 24 hours for FAQs to appear here.

Once an FAQ is in the book answered (it may actually be part of
another section, TA's will mark the FAQ in piazza, so you can make sure
which FAQs are already in the book. We recommend to look in the book
as there could be information in it that you otherwise missed.


## How do I find all FAQ's in Piazza?

Two ways exist

a) Please visit your class piazza. You will find a "faq" tag in your
piazza window. Click on it and all posts marked with FAQ will show up,

b) In the search field type in FAQ. All posts with the text FAQ in it
will be listed.

## Has SOIC computers I can use remotely?

See: <https://uisapp2.iu.edu/confluence-prd/pages/viewpage.action?pageId=114491559>



## When contributing to the book my name is not listed properly or not at all

The following reasons exist:

1. if its not listed at all your contribution may be in a different
   repository, please contact Gregor

2. if it does not show up correctly and only shows your github name,
   which you can see in the contributor section or with


```bash
$ git shortlog -s -e
2  laszewsk <laszewski@gmail.com>
...
```

You need to do two things.

First, add your name to the file

* <https://github.com/cloudmesh-community/book/blob/master/.mailmap>

Second, complete the set up your git on the machine you work with in
case you use a commandline tool with git init (see our notes on this)

If you use the GUI you may need to go to the account settings and
associate a first name lastname, I however do not know ho to do that,
so if you kwon reply ti this


## How to read the technical sections of the lecture notes

We will add throughout the semester some technical lecture notes. These
notes contain information on how to install and run certain programs
on a computer. What we have seen in the past with some students is
that they do not read the text between the sections. Instead they just
execute things without reading or understanding assuming that they can
juste copy and paste. These sections include valuable information that
you **must** read before you execute any code in them.

Here is the workflow on how to read such technical sections

1. Do not execute anything yet

2. Read the entire section including the lines between the gray boxes

3. Step back and reflect on what you read

4. Reread the section, if a section needs more information google for
   it (things could be overnight updated on the internet, please
   remember we are just presenting a snapshot in time here)

5. Once you have obtained knowledge, decide if the section is relevant
   for you (e.g. windows sections may not be relevant for MacOS users)

6. Carefully execute the relevant portions for you

:warning: AS ALWAYS THERE IS NO GUARANTEE THAT WHAT THE CODE WORKS
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

Using yamllint is our preferred method.

A python script to check it is available at

* <https://github.com/cloudmesh-community/book/tree/master/examples/yaml-validation/validate_yml.py>

This python script depends on `ruamel.yaml` package. We can install it
using following command:

```bash
$ pip install ruamel.yaml
```

It accepts file path as an argument. This script will load `YAML`
file and dump its content on console. For invalid syntax it will throw
an error.

To execute python script you need to run following command after you
clone *book* repository.

```bash
$ cd examples/yaml-validation
$ chmod +x validate_yml.py
$ ./validate_yml.py <path to yaml file to validate>
```

Online checkers are available at

* <https://codebeautify.org/yaml-validator>

A ruby script can do

```bash
$ ruby-e "require 'yaml';puts YAML.load_file('./README.yml')"
```

YAML validation in visual studio can be achieved also

*  <https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml>

## Download the epub ferquently

Please be reminded that the epub is updated frequently and we
recommend that you download it before you read.


I myself have integrated an epub reader in my Web browser so that
every time I click on the View Raw in github, I get the most up to
date version.

I use ibooks on OSX, calibre is a good system on Windows and Linux, MS
also has Microsoft Edge. However on Microsoft edge you will need the
lates version which starts with 42

## Spelling of filenames in github

Most of our scripts require proper spellingg including proper capitalization.
The spelling of `notebook.md` is `notebook.md`

not

`Notebook.md` or `NOTEBOOK.md` or other spelling

Please, correct if you did not use lower case

The spelling of `README.yml` is` README.yml` and not

`README.md` (which needs to be removed) or `readme.yaml`

please correct if needed. We will not grade any assignments if your
README.yaml or notebook.md is misspelled or missing or is not
following our simple format. 

## How to open the epub from Github?

If you see thw `View Raw`, you need to click on it. It will download the
file. Than you can open that.

However, If you use edge or integrated your epub viewer in your
browser and clicking on it will automatically open your epub browser.


## Assignment Summary

:o: outdated

a) The assignment is discussed in Chapter 1 of the lecture notes

b) Examples of what other students have done are in the Example Artifacts section


Please look at both sections


In this class we addressed 3 assignment that  related to your grade


Tech summaries - they have been assigned to you
in <https://piazza.com/class/jl6rxey6w413gi?cid=89>
to show to the TAs that you work on them use the nomenclature that is discussed in the preface of the technology handbook. Put yours hid in the "headline" and a smiley when done, If you work on it put in a hand.
Project - look at examples in the example artifact sections
A paper has typically the following sections

Theory
Implementation (e.g. Python)
Benchmark


A more detailed outline is
* Paper
* Title
* Abstract
* Introductions
* Requirements
* Architecture
* Implementation
* Benchmark
* Conclusions
* Bibliography
* Work breakdown

## Auto 80 char

:o: outdated

Those that use emcas could experiment with the following. I do not
know if this works well yet.

The following will autoformat an entire file to 80 chars. The reason i
put it in test.md is that I do not know if it reliably works on all md
files, just inspect the output and decide for yourself. some md files
you may not want to manipulate with this though

```sh
cp file.md test.md
emacs -batch test.md --eval '(fill-region (point-min) (point-max))' -f save-buffer
```

## Useful FAQs for residential and online students

:o: this is outdated.

You will know if this post applies to you.

This class does not have a high volume on posts via Piazza

What we find is that some students create a high overhead on
themselves by not following our FAQs or documentation on the
technology summaries. When we observe something we just post it in an
FAQ in piazza that we expect you look at. Yet we find some students
that keep on resubmitting their technology summaries while not
integrating our tips from the FAQs that cost less then a minute to
do. Those that do not read and follow the FAQ make their work
unnecessary complicated.  We even start now noticing students that
remove bibliography entries instead of just fixing them. Also, we saw
recently students that had perfectly geat entries, other than the
authors (see FAQ) and instead of fixing the authors in case it was a
company or organization, to fix random fields such as the titles and
thus creating even more work on themselves.

We have lots of online hours during the week There are 4 hours you can
attend, Mo, We Thu, so if you do have something you do not understand,
I recommend that you use these hours. In case you are a residential
student you also have Fridays. To start, I would review our FAQs

Interestingly we see these issues more with residential students than
with online students. This may indicate that the residential students
in question forget to read the posts in piazza?

## What if i committed a wrong file to github, a.g. a private key?

The answer to this question is more complicated than you think. Thus
the best way to deal with it is to 

AVOID IT:


a) first do github adds file by fill with git add. Avoid using adds on AND DO NOT USE


```
 git add .                  # <<<<<<< DO NOT USE
```

b) only use ssh keys in ~/.ssh **NEVER** place keys in directories that are managed by git

**YOU CAN NOT EASILY DELETE FILES FROM GIT:**


c) as you may already know despite you deleting a file from git it is
still in the git history. Also there are bad characters out there so
if you checked in you ssh private key just for a second

you must assume your private key is now compromised and all machines
that use it are compromised.

d) although GIt allows you to delete the file, it is still in the
githistory, which can be mined so despite you pressing delete its
still there and can be found. This is not a bug in git but this is you
having git not used right.

e) There are ways to purge such files, but it would imply that
everyone that did a fork needs to do a new fork which is naturally a
big issue, so we do not do this during the semester.

NOW WHAT?

f) every machine on which you used the public key of this private key
is to be considered now compromised.

g) put them off from the network while plugging out the network plug

g) if the machines are not owned by you but for example, IU, notify
the people that own the machine to ask for help with mitigation.

f) if you are lucky, replace the key, this is the case for example for
services such as github. Make sure to inspect the configurations and
see if your account has not been hijacked.

h) We will immediately remove you from services such as future systems
and chameleon cloud as a precaution or deactivate your membership in
our cloud accounts.

i) if you used the keys on other services, including IU, it is up to
you to identify how to deal with this,

j) definitely create a new key and use that from now on.

k) you can call Gregors office number or use piazza to set up a call to
identify what the impact is as this is typically an emergency use 812
856 1311. Do not leave a msg, but instead send e-mail.with your phone
number so we can call you back to assess the situation.

l) if you use them on public clouds that cost money, shut down all
machines that use them. I would not start them again but instead use
new once. It may be time to drop everything and do this first. Sorry
for making you now panic.


