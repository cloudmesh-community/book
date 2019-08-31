from github import Github
from cloudmesh.configuration.Config import Config
from pprint import pprint
import requests
from textwrap import dedent
from pathlib import Path
import time

repos = [
["fa19-516-156", "Manikandan Nagarajan", "ManiNagarajan20"],
["fa19-516-157", "Chenxu Wang",	"wang542"],
["fa19-516-158", "Daivik Dayanand", "Daivik1997"]
#    ["fa19-516-000", "Gregor von Laszewski", "laszewsk"]
]

config = Config()

g = Github(config["cloudmesh.github.user"],
           config["cloudmesh.github.password"])

org = g.get_organization("cloudmesh-community")

# repo = g.get_repo("cloudmesh-community/book")
# print (repo)

# print(g.get_user())
# print (org)

# pprint (dir(org))


# for t in org.get_teams():
#    pprint (t)


ta_team = org.get_team(2631498)

# pprint (team)

# sys.exit()
# for r in org.get_repos():
#    print (r)

# request = requests.get(f'https://api.github.com/users/{username}/reposper_page=1000')
# json = request.json()

# pprint (json)

# for i in range(0,len(json)):
#  print("Project Number:",i+1)
##  print("Project Name:",json[i]['name'])
#  print("Project URL:",json[i]['svn_url'],"\n")


for r in repos:
    name = r[0]
    description = r[1]
    firstname, lastname = description.split(" ", 1)
    username = r[2]
    print("creating", name, description)
    repo = org.create_repo(name,
                           description=description,
                           license_template="apache-2.0")
    readme = dedent(f"""
        ---
        owner:
          firstname: "{firstname}"
          lastname: "{lastname}"
          hid: "{name}"
          community: "e516"
          semester: "fa19"
        """).strip()
    print(readme)
    print("Add README.yaml")
    repo.create_file("README.yml", "create the Readme.yaml", readme,
                     branch="master")

    print("Add .gitignore")

    with open(Path("../.gitignore").resolve()) as file:
        gitignore = file.read()

    repo.create_file(".gitignore", "create the .gitignore", gitignore,
                     branch="master")

    try:
        repo.add_to_collaborators(username, permission="write")
    except Exception as e:
        pass
    ta_team.add_to_repos(repo)
    ta_team.set_repo_permission(repo, "write")
