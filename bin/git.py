from github import Github
from cloudmesh.configuration.Config import Config
from pprint import pprint
import requests
from textwrap import dedent
from pathlib import Path

config = Config()

# pprint (config.data)

g = Github(config["cloudmesh.github.user"],
           config["cloudmesh.github.password"])

org = g.get_organization("cloudmesh-community")

# repo = g.get_repo("cloudmesh-community/book")
# print (repo)

# print(g.get_user())
# print (org)

# pprint (dir(org))

# for r in org.get_repos():
#    print (r)

# request = requests.get(f'https://api.github.com/users/{username}/reposper_page=1000')
# json = request.json()

# pprint (json)

# for i in range(0,len(json)):
#  print("Project Number:",i+1)
##  print("Project Name:",json[i]['name'])
#  print("Project URL:",json[i]['svn_url'],"\n")

repos = [
    ["fa19-516-000", "Gregor von Laszewski", "laszewsk"]
]

for r in repos:
    name = r[0]
    description = r[1]
    firstname, lastname = description.split(" ", 1)
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

#    team = org.create_team("ta", name)
