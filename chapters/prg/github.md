# Github REST Services {#sec:Github-REST}

In this section we want to explore a more features of REST
services and how to access them. Naturally many cloud services
provide such REST sinterfaces. This is valid for IaaS, PaaS, and SaaS.

Instead of using a REST service for IaaS, let us here inspect a REST
service for the Github.com platform.

Its interfaces are documented nicely at 

* <https://developer.github.com/v3/>

We see that Github offers many resources that can be accessed by the users which includes

* Activities
* Checks
* Gists
* Git Data
* GitHub Apps
* Issues
* Migrations
* Miscellaneous
* Organizations
* Projects
* Pull Requests
* Reactions
* Repositories
* Searches
* Teams
* Users

Most likely we forgot the one or the other Resource that we can access
via REST. It will be out of scope for us to explore all of these
issues, so let us focus on how we for example access Github Issues. In
fact we will use the script that we use to create issue tables for
this book to showcase how easy the interaction is and to retrieve
the information.

## Issues

The REST service for issues is described in the following Web page as
specification

* <https://developer.github.com/v3/issues/>

We see the following functionality:

* [List issues](https://developer.github.com/v3/issues/#list-issues)
* [List issues for a repository](https://developer.github.com/v3/issues/#list-issues-for-a-repository)
* [Get a single issue](https://developer.github.com/v3/issues/#get-a-single-issue)
* [Create an issue](https://developer.github.com/v3/issues/#edit-an-issue)
* [Edit an issue](https://developer.github.com/v3/issues/#edit-an-issue)
* [Lock an issue](https://developer.github.com/v3/issues/#lock-an-issue)
* [Unlock an issue](https://developer.github.com/v3/issues/#unlock-an-issue)
* [Custom media types](https://developer.github.com/v3/issues/#custom-media-types)

As we have learned in our REST section we need to issue GET requests
to obtain information about the issues. Such as

```bash
GET /issues
GET /user/issues
```

As response we obtain a json object with the information we need to
further process it. Unfortunately, the free tier of github has
limitations in regards to the frequency we can issue such requests to
the service, as well as in the volume in regards to number of pages
returned to us.

Let us now explore how to easily query some information. In our
example we like to retrive the list of issues for a repository as LaTeX
table but also as markdown. This way we can conveniently integrate it
in documents of either format. As LaTeX has a more sophisticated table
management, let us first create a LaTeX table document and than use a
program to convert LaTeX to markdown. For the later we can reuse a
program called `pandoc` that can convert the table for LaTeX to
markdown.

Let us assume we have a program called `issues.py` that prints the
table in markdown format

```bash
$ python issues.py 
```


An example for such a program is listes at. 

* <https://github.com/cloudmesh-community/book/blob/master/bin/issues.py>

Although python provides the very nice module `requests` which we
typically use for such issues. we have here just wrapped the
commandline call to `curl` into a system command and redirect its
output to a file. However, as we only get limited information back in
pages, we need to continue such a request multiple times. To keep
things simple we identified that for the project at this time not
more that n pages need to be fetched, so we append the output from
each page to the file.

Your task is it to improve this script and automatize this activity so
that no maximum fetches have to be entered.

The reason why this program is so short is that we leverage the build
in function for `json` data structure manipulation, hear a read and a
dump. When we look in the `issue.json` file that is created as
intermediary file we see a list of items such as

```json
[
...
 {
        "url": "https://api.github.com/repos/cloudmesh-community/book/issues/46",
        "repository_url": "https://api.github.com/repos/cloudmesh-community/book",
        "labels_url": "https://api.github.com/repos/cloudmesh-community/book/issues/46/labels{/name}",
        "comments_url": "https://api.github.com/repos/cloudmesh-community/book/issues/46/comments",
        "events_url": "https://api.github.com/repos/cloudmesh-community/book/issues/46/events",
        "html_url": "https://github.com/cloudmesh-community/book/issues/46",
        "id": 360613438,
        "node_id": "MDU6SXNzdWUzNjA2MTM0Mzg=",
        "number": 46,
        "title": "Taken: Virtualization",
        "user": {
            "login": "laszewsk",
            "id": 425045,
            "node_id": "MDQ6VXNlcjQyNTA0NQ==",
            "avatar_url": "https://avatars1.githubusercontent.com/u/425045?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/laszewsk",
            "html_url": "https://github.com/laszewsk",
            "followers_url": "https://api.github.com/users/laszewsk/followers",
            "following_url": "https://api.github.com/users/laszewsk/following{/other_user}",
            "gists_url": "https://api.github.com/users/laszewsk/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/laszewsk/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/laszewsk/subscriptions",
            "organizations_url": "https://api.github.com/users/laszewsk/orgs",
            "repos_url": "https://api.github.com/users/laszewsk/repos",
            "events_url": "https://api.github.com/users/laszewsk/events{/privacy}",
            "received_events_url": "https://api.github.com/users/laszewsk/received_events",
            "type": "User",
            "site_admin": false
        },
        "labels": [],
        "state": "open",
        "locked": false,
        "assignee": {
            "login": "laszewsk",
            "id": 425045,
            "node_id": "MDQ6VXNlcjQyNTA0NQ==",
            "avatar_url": "https://avatars1.githubusercontent.com/u/425045?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/laszewsk",
            "html_url": "https://github.com/laszewsk",
            "followers_url": "https://api.github.com/users/laszewsk/followers",
            "following_url": "https://api.github.com/users/laszewsk/following{/other_user}",
            "gists_url": "https://api.github.com/users/laszewsk/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/laszewsk/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/laszewsk/subscriptions",
            "organizations_url": "https://api.github.com/users/laszewsk/orgs",
            "repos_url": "https://api.github.com/users/laszewsk/repos",
            "events_url": "https://api.github.com/users/laszewsk/events{/privacy}",
            "received_events_url": "https://api.github.com/users/laszewsk/received_events",
            "type": "User",
            "site_admin": false
        },
        "assignees": [
            {
                "login": "laszewsk",
                "id": 425045,
                "node_id": "MDQ6VXNlcjQyNTA0NQ==",
                "avatar_url": "https://avatars1.githubusercontent.com/u/425045?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/laszewsk",
                "html_url": "https://github.com/laszewsk",
                "followers_url": "https://api.github.com/users/laszewsk/followers",
                "following_url": "https://api.github.com/users/laszewsk/following{/other_user}",
                "gists_url": "https://api.github.com/users/laszewsk/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/laszewsk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/laszewsk/subscriptions",
                "organizations_url": "https://api.github.com/users/laszewsk/orgs",
                "repos_url": "https://api.github.com/users/laszewsk/repos",
                "events_url": "https://api.github.com/users/laszewsk/events{/privacy}",
                "received_events_url": "https://api.github.com/users/laszewsk/received_events",
                "type": "User",
                "site_admin": false
            }
        ],
        "milestone": null,
        "comments": 0,
        "created_at": "2018-09-16T07:35:35Z",
        "updated_at": "2018-09-16T07:35:35Z",
        "closed_at": null,
        "author_association": "CONTRIBUTOR",
        "body": "Develop a section about Virtualization"
    },
    
...
]
```

As we can see from this entry there is a lot of information associated
that for our purposes we do not need, but certainly could be used to
mine github in general.

We like to point out that github is actively mined for exploits where
passwords are posted in clear text for AWS, Azure and other
clouds. This is a common mistake as many sample programs ask the
student to place the password directly into their programs instead of
using a configuration file that is never part of the code repository.

## Exercise

E.github.issues.1:

> Develop a new code like the one in this section, but use python requests
> instead of the `os.system` call.

E.github.issues.2:

> In the simple program we hardcoded the number of page requests. 
> How can we find out exactly how many pages we need to retrieve?
> Implement your solution

E.github.issues.3:

> Be inspired by the many REST interfaces. How can they be used 
> to mine interesting things.

E.github.issues.4:

> Can you create a project, author, or technology map based on 
> information that is available in github. For example python 
> projects may include a requirements file, or developers may 
> work on some projects together, but others do other 
> projects with others can you create a network?

E.github.issues.5:

> Use github to develop some cool python programs that show some
> statistics about github. An example would be: Given a github
> repository, show the checkins by data and visualize them graphically
> for one committer and all committers. Use bokeah or matplotlib.

E.github.issues.6:

> Develop a python program that retrieves a file. Deevlop a python
> program that uploads a file. Develop a class that does this and use
> it in your proggram. Use docopt to create a manual page. Please
> remember this prepares you for your project so this is very useful
> to do.
