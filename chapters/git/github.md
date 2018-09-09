# Github

In some classes the material may be openly shared in code repositories.
This includes class material, papers and project. Hence, we need some
mechanism to share content with a large number of students.

First, we like to introduce you to git and github.com (Section
[1.1](#s:github){reference-type="ref" reference="s:github"}). Next, we
provide you with the basic commands to interact with git from the
commandline (Section [1.12](#s:git-commands){reference-type="ref"
reference="s:git-commands"}). Than we will introduce you how you can
contribute to this set of documentations with pull requests.

## Overview {#s:github}

Github is a code repository that allows the development of code and
documents with many contributors in a distributed fashion. There are
many good tutorials about github. Some of them can be found on the
github Web page. An interactive tutorial is for example available at

-   <https://try.github.io/>

However, although these tutorials are helpful in many cases they do not
address some cases. For example, you have already a repository set up by
your organization and you do not have to completely initialize it. Thus
do not just replicate the commands in the tutorial, or the once we
present here before not evaluating their consequences. In general make
sure you verify if the command does what you expect **before** you
execute it.

A more extensive list of tutorials can be found at

-   <https://help.github.com/articles/what-are-other-good-resources-for-learning-git-and-github>

The github foundation has a number of excellent videos about git. If you
are unfamiliar with git and you like to watch videos in addition to
reading the documentation we recommend these videos

-   <https://www.youtube.com/user/GitHubGuides/videos>

Next, we introduce some important concepts used in github.

## Upload Key

Before you can work with a repository in an easy fashion you need to
upload a public key in order to access your repository. Naturally, you
need to generate a key first which is explained in

\TODO{lessons-ssh-generate-key}
before you upload one. Copy the contents of your `.ssh/id_rsa.pub` file
and add them to [your github keys](https://github.com/settings/keys).

More information on this topic can be found on the [github Web
page](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

## Fork

Forking is the first step to contributing to projects on GitHub. Forking
allows you to copy a repository and work on it under your own account.
Next, creating a branch, making some changes, and offering a pull
request to the original repository, rounds out your contribution to the
open source project.

[:clapper: Git 1:41 Fork](https://www.youtube.com/watch?v=5oJHRbqEofs)

## Rebase

When you start editing your project, you diverge from the original
version. During your developing, the original version may be updated, or
other developers may have some of their branches implementing good
features that you would like to include in your current work. That is
when *Rebase* becomes useful. When you *Rebase* to certain points, could
be a newer Master or other custom branch, consider you graft all your
on-going work right to that point.

Rebase may fail, because some times it is impossible to achieve what we
just described as conflicts may exist. For example, you and the
to-be-rebased copy both edited some common text section. Once this
happens, human intervention needs to take place to resolve the conflict.

[:clapper: Git 4:20 Rebase](https://www.youtube.com/watch?v=SxzjZtJwOgo)

## Remote

Collaborating with others involves managing the remote repositories and
pushing and pulling data to and from them when you need to share work.
Managing remote repositories includes knowing how to add remote
repositories, remove remotes that are no longer valid, manage various
remote branches and define them as being tracked or not, and more.

Though out this semester, you will typically work on two *remote* repos.
One is the office class repo, and another is the repo you forked from
the class repo. The class repo is used as the centralized, authority and
final version of all student submissions. The repo under your own Github
account is for your personal storage. To show progress on a weekly basis
you need to commit your changes on a weekly basis. However make sure
that things in the master branch are working. If not, just use another
branch to conduct your changes and merge at a later time. We like you to
call your development branch  dev.

-   <https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes>

## Pull Request

Pull requests are a means of starting a conversation about a proposed
change back into a project. We will be taking a look at the strength of
conversation, integration options for fuller information about a change,
and cleanup strategy for when a pull request is finished.

[:clapper: Git 4:26 Pull
Request](https://www.youtube.com/watch?v=d5wpJ5VimSU)

## Branch

Branches are an excellent way to not only work safely on features or
experiments, but they are also the key element in creating Pull Requests
on GitHub. Lets take a look at why we want branches, how to create and
delete branches, and how to switch branches in this episode.

[:clapper: Git 2:25 Branch](https://www.youtube.com/watch?v=H5GJfcp3p4Q)

## Checkout

Change where and what you are working on with the checkout command.
Whether we are switching branches, wanting to look at the working tree
at a specific commit in history, or discarding edits we want to throw
away, all of these can be done with the checkout command.

[:clapper: Git 3:11
Checkout](https://www.youtube.com/watch?v=HwrPhOp6-aM)

## Merge

Once you know branches, merging that work into master is the natural
next step. Find out how to merge branches, identify and clean up merge
conflicts or avoid conflicts until a later date. Lastly, we will look at
combining the merged feature branch into a single commit and cleaning up
your feature branch after merges.

[:clapper: Git 3:11 Merge](https://www.youtube.com/watch?v=yyLiplDQtf0)

## GUI

Using Graphical User Interfaces can supplement your use of the command
line to get the best of both worlds. GitHub for Windows and GitHub for
Mac allow for switching to command line, ease of grabbing repositories
from GitHub, and participating in a particular pull request. We will
also see the auto-updating functionality helps us stay up to date with
stable versions of Git on the command line.

[:clapper: Git 3:47 GUI](https://www.youtube.com/watch?v=BMYOs5jflGE)

There are many other git GUI tools available that directly integrate
into your operating system finders, windows, ..., or PyCharm. It is up
to you to identify such tools and see if they are useful for you. Most
of the people we work with us git from the command line, even if they
use PyCharm, eclipse, or other tools that have build in git support. You
can identify a tool that works best for you.

## Windows

This is a quick tour of GitHub for Windows. It offers GitHub newcomers a
brief overview of what this feature-loaded version control tool and an
equally powerful web application can do for developers, designers, and
managers using Windows in both the open source and commercial software
worlds. More: <http://windows.github.com>

[:clapper: Git 1:25
Windows](https://www.youtube.com/watch?v=YBbkvCrfDSo)

## Git from the Commandline {#s:git-commands}

Although github.com provides a powerful GUI and other GUI tools are
available to interface with github.com, the use of git from the
commandline can often be faster and in many cases may be simpler.

Git commandline tools can be easily installed on a variety of operating
systems including Linux, OSX, and Windows. Many great tutorials exist
that will allow you to complete this task easily. We found the following
two tutorials sufficient to get the task accomplished:

-   <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
-   <https://www.atlassian.com/git/tutorials/install-git>

Although the later is provided by an alternate repository to github. The
installation instructions are very nice and are not impacted by it. Once
you have installed git you need to configure it.

## Configuration {#config}

Once you installed Git, you can need to configure it properly. This
includes setting up your username, email address, line endings, and
color, along with the settings' associated configuration scopes.

[:clapper: Git 2:47
Configuration](https://www.youtube.com/watch?v=ZChtKFLiaNw)

It is important that make sure that use the `git config` command to
initialize git for the first time on each new computer system or virtual
machine you use. This will ensure that you use on all resources the same
name and e-mail so that git history and log will show consistently your
checkins across all devices and computers you use. If you do not do
this, your checkins in git do not show up in a consistent fashion as a
single user. Thus on each computer execute the following commands:

    $ git config --global user.name "Albert Zweistein"
    $ git config --global user.email albert.zweistein@gmail.com

where you replace the information with the information related to you.
You can set the editor to emacs with:

    $ git config --global core.editor emacs

Naturally if you happen to want to use other editors you can configure
them by specifying the command that starts them up. You will also need
to decide if you want to push branches individually or all branches at
the same time. It will be up to you to make what will work for you best.
We found that the following seems to work best:

    git config --global push.default matching

More information about a first time setup is documented at:

    * http://git-scm.com/book/en/Getting-Started-First-Time-Git-Setup

To check your setup you can say:

    $ git config --list

One problem we observed is that students often simply copy and paste
instructions, but do not read carefully the error that is reported back
and do not fix it. Overlooking the proper set of the push.default is
often overlooked. Thus we remind you: **Please read the information on
the screen when you set up**.

## Upload your public key

Please upload your public key to the repository as documented in github,
while going to your account and find it in settings. There you will find
a panel SSH key that you can click on which brings you to the window
allowing you to add a new key. If you have difficulties with this find a
video from the github foundation that explains this.

## Working with a directory that will be provided for you

In case your course provided you with a github directory, starting and
working in it is going to be real simple. Please wait till an
announcement to the class is send before you ask us questions about it.

If you are the only student
working on this you still need to make sure that papers or programs you
manage in the repository work and do not interfere with scripts that
instructors may use to check your assignments. Thus it is god to still
create a branch, work in the branch and than merge the branch into the
master once you verified things work. After you merged you can push the
content to the github repository.

Tip: Please use only **lowercase** characters in the directory names and
no special characters such as `@ ; / _` and spaces. In general we
recommend that you avoid using directory names with capital letters
spaces and \_ in them. This will simplify your documentation efforts and
make the URLs from git more readable. Also while on some OS's the
directories *MyDirectory* is different from *mydirectory* on OSX it is
considered the same and thus renaming from capital to lower case can not
be done without first renaming it to another directory.

Your homework for submission should be organized according to folders in
your clone repository. To submit a particular assignment, you must first
add it using:

    git add <name of the file you are adding>

Afterwards, commit it using:

    git commit -m "message describing your submission"

Then push it to your remote repository using:

    git push

If you want to modify your submission, you only need to:

    git commit -m "message relating to updated file"

afterwards:

    git push

If you lose any documents locally, you can retrieve them from your
remote repository using:

    git pull

## README.yml and notebook.md

In case you take classes e516 and e616 with us you will have to create a
README.yaml and notebook.md file in the top most directory of your
repository. It serves the purpose of identifying your submission for
homework and information about yourself.

It is important to follow the format precisely. As it is yaml it is an
easy homework to write a 4 line python script that validates if the
README.yaml file is valid. In addition you can use programs such as
`yamllint` which is documented at

-   <https://yamllint.readthedocs.io/en/latest/>

This file is used to integrate your assignments into a proceedings. An
example is provided at

-   <https://github.com/cloudmesh-community/hid-sample/blob/master/README.yml>

Any derivation from this format will not allow us to see your homework
as our automated scripts will use the README.yml to detect them. Make
sure the file does not contain ay TABs. Please also mind that all
filenames of all homework and the main directory must be **lowercase**
and do not include spaces. This will simplify your task of managing the
files across different operating systems.

In case you work in a team, on a submission, the document will only be
submitted in the author and hid that is listed first. All other readme files,
will have for that particular artifact a `duplicate: yes` entry to
indicate that this submission is managed elsewhere. The team will be
responsible to manage their own pull requests, but if the team desires
we can grant access for all members to a repository by a user. Please be
aware that you must make sure you coordinate with your team.

We will not accept submission of homework as pdf documents or tar files.
All assignments must be submitted as code and the reports in native
latex and in github. We have a script that will automatically create the
PDF and include it in a proceedings. There is no exception from this
rule and all reports not compilable will be returned without review and
if not submitted within the deadline receive a penalty.

Please check with your instructor on the format of the README.yaml file
as it could be different for your class.

To see an example for the notebook.md file, you can visit our sample
hid, and browse to the notebook.md file. Alternatively you can visit the
following link

-   <https://github.com/cloudmesh-community/hid-sample/blob/master/notebook.md>

The purpose of the notebook md file is to record what you did in the
class to us. We will use this file at the end of the class to make sure
you have recorded on a weekly basis what you did for the class.
Inactivity is a valid response. Not updating the notebook, is not.

The sample directory contains other useful directories and samples, that
you may want to investigate in more detail. One of the most important
samples is the github issues (see Section
[1.19](#S:git-issues){reference-type="ref" reference="S:git-issues"}).
There is even a video in that section about this and showcases you how
to organize your tasks within this class, while copying the assignments
from piazza into one or more github issues. As we are about cloud
computing, using the services offered by a prominent cloud computing
service such as github is part of the learning experience of this
course.

## Contributing to the Document

### Clone

    $ git remote add upstream \
          https://github.com/cloudmesh-community/book

### Merge

As we are allowing contribution by the community, they are best managed
through a merge with our upstream repository so you can update to the
newest status before you issue a pul request.

Make sure you have upstream repo defined:

    $ git remote add upstream \
          https://github.com/cloudmesh-community/book

Now Get latest from upstream:

    $ git rebase upstream/master

In this step, the conflicting file shows up (in my case it was
refs.bib):

    $ git status

should show the name of the conflicting file:

    $ git diff <file name>

should show the actual differences. May be in some cases, It is easy to
simply take latest version from upstream and reapply your changes.

So you can decide to checkout one version earlier of the specific file.
At this stage, the re-base should be complete. So, you need to commit
and push the changes to your fork:

    $ git commit
    $ git rebase origin/master
    $ git push

Then reapply your changes to refs.bib - simply use the backed up version
and use the editor to redo the changes.

At this stage, only refs.bib is changed:

    $ git status

should show the changes only in refs.bib. Commit this change using:

    $ git commit -a -m "new:usr: <message>"

And finally push the last committed change:

    $ git push

The changes in the file to resolve merge conflict automatically goes to
the original pull request and the pull request can be merged
automatically.

You still have to issue the pull request from the Github Web page so it
is registered with the upstream repository.

### Resources

-   [Pro Git book](https://git-scm.com/book/en/v2)
-   [Official tutorial](https://git-scm.com/docs/gittutorial)
-   [Official documentation](https://git-scm.com/doc)
-   [TutorialsPoint on git](http://www.tutorialspoint.com/git/)
-   [Try git online](https://try.github.io)
-   [GitHub resources for learning
    git](https://help.github.com/articles/good-resources-for-learning-git-and-github/)
    Note: this is for github and not for gitlab. However as it is for gt
    the only thing you have to do is replace github, for gitlab.
-   [Atlassian tutorials for
    git](https://www.atlassian.com/git/tutorials/)

In addition the tutorials from atlassian are a good source. However
remember that you may not use bitbucket as the repository, so ignore
those tutorials. We found the following useful

-   What is git: <https://www.atlassian.com/git/tutorials/what-is-git>
-   Installing git:
    <https://www.atlassian.com/git/tutorials/install-git>
-   git config:
    <https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-config>
-   git clone:
    <https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-clone>
-   saving changes:
    <https://www.atlassian.com/git/tutorials/saving-changes>
-   collaborating with git:
    <https://www.atlassian.com/git/tutorials/syncing>

## Exercises

[\[E:Github.1\]]{#E:Github.1 label="E:Github.1"} How do you set your
favorite editor as a default with github config

[\[E:Github.2\]]{#E:Github.2 label="E:Github.2"} What is the difference
between merge and rebase?

[\[E:Github.3\]]{#E:Github.3 label="E:Github.3"} Assume you have made a
change in your local fork, however other users have since committed to
the master branch, how can you make sure your commit works off from the
latest information in the master branch?

[\[E:Github.4\]]{#E:Github.4 label="E:Github.4"} Find a spelling error
in the Web page or a contribution and create a pull request for it.

[\[E:Gitlab.5\]]{#E:Gitlab.5 label="E:Gitlab.5"} Create a README.yml in
your github account directory provided for you for class.

## Github Issues {#S:git-issues}

[:clapper: Github 8:29 Issues](https://youtu.be/qozgBPQJx0A)

When we work in teams or even if we work by ourselves, it is prudent to
identify a system to coordinate your work. While conduction projects
that use a variety of cloud services, it is important to have a system
that enables us to have a cloud service that enables us to facilitate
this coordination. Github provides such a feature through its *issue*
service that is embedded in each repository.

Issues allow for the coordination of tasks, enhancements, bugs, as well
as self defined labeled activities. Issues are shared within your team
that has access to your repository. Furthermore, in an open source
project the issues are visible to the community, allowing to easily
communicate the status, as well as a roadmap to new features.

This enables the community to participate also in reporting of bugs.
Using such a system transforms the development of software from the
traditional closed shop development toa truly open source development
encouraging contributions from others. Furthermore it is also used as
bug tracker in which not only you, but the community can communicate
bugs to the project.

\TODO{Tyler: Include image of the issues on hid-sample}
A good resource for learning more about issues is provided at

-   <https://guides.github.com/features/issues/>

### Git Issue Features

A git issue has the following features:

title

:   -- a short description of what the issue is about

description

:   a more detailed description. Descriptions allow also to conveniently
    add check-boxed todo's.

label

:   a color enhanced label that can be used to easily categorize the
    issue. YOu can define your own labels.

milestone

:   a milestone so you can identify categorical groups issues as well as
    their due date. You can for example group all tasks for a week in a
    milestone, or you could for example put all tasks for a topic such
    as developing a paper in a milestone and provide a deadline for it.

assignee

:   an assignee is the person that is responsible for making sure the
    task is executed or on track if a team works on it. Often projects
    allow only one assignee, but in certain cases it is useful to assign
    a group, and the group identifies if the task can be split up and
    assigns them through check-boxed todo's.

comments

:   allow anyone with access to provide feedback via comments.

### Github Markdown

Github uses markdown which we introduce you in
Section [\[S:markdown\]](#S:markdown){reference-type="ref"
reference="S:markdown"}.

As github has its own flavor of markdown we however also point you to

as a reference. We like to mention the special enhancements fo github's
markdown that integrate well to support project management.

#### Task lists

Taks lists can be added to any description or comment in github issues
To create a task list you can add to any item `[ ]`. This includes a
task to be done. To make it as complete simple change it to `[x]`.
Whoever the great feature of tasks is that you do not even have to open
the editor but you can simply check the task on and of via a mouse
click. An example of a task list could be

    Post Bios

    * [x] Post bio on piazza
    * [ ] Post bio on google docs
    * [ ] Post bio on github
    * [ ] \(optional) integrate image in google docs bio

In case you need to use a `(`have at the beginning ot the task text, you
need to escape it with a `\`

#### Team integration

A person or team on GitHub can be mentioned by typing the username
proceeded by the `@` sign. When posting the text in the issue, it will
trigger a notification to them and allow them to react to it. It is even
possible to notify entire teams, which are described in more detail at

-   <https://help.github.com/articles/about-teams/>

#### Referencing Issues and Pull requests

Each issue has a number. If you use the `#` followed by the issue number
you can refer to it in the text which will also automatically include a
hyperlink to the task. The same is valid for pull requests.

#### Emojis

Although github supports emojis such as `:+1:` we do not use them
typically in our class.

### Notifications

Github allows you to set preferences on how you lik to receive
notifications. You can receive them either via e-mail or the Web. This
is controlled by configuring it in *your settings*, where you can set
the preferences for participating projects as well as projects you
decide to watch. To access the notifications you can simply look at them
in the *notification* screen. In this screen when you press the `?` you
will see a number of commands that allow you to control the notification
when pressing on one of them.

### cc

To carbon copy users in your issue text, simply use `/cc` followed by
the `@` sign and their github user name.

### Interacting with issues

Github has the ability to search issues with a search query and a search
language that you can find out more about it at

<https://guides.github.com/features/issues/#search>

A dashboard gives convenient overviews of the issues including a *pulse*
that lists todo's status if you use them in the issue description.
