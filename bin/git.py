from github import Github
from cloudmesh.configuration.Config import Config
from pprint import pprint
import requests
from textwrap import dedent
from pathlib import Path
import time

repos = [
#    ["fa19-523-180", "Jonathon Grant","jongrant010"],
#    ["fa19-523-181", "Max Falkenstein","maxf7399"],
#    ["fa19-523-182", "Zak Siddiqui","zaksidd1"],
#    ["fa19-523-183", "Brent Creech","bcreech40"],
#    ["fa19-523-184", "Michael Floreak","mfloreak"],
#   ["fa19-523-185", "Die Hu","syhu"],
#    ["fa19-523-186", "Soowon Park","parksoow"],
#   ["fa19-523-187", "Chris Fang","zihfang"],
#    ["fa19-523-188", "Shivani Katukota","katukota"],
#    ["fa19-523-189", "Huizhou Wang","aiai949"],
#    ["fa19-523-190", "Skyler Konger","skonger"],
#   ["fa19-523-191", "Yiyu Tao","oliviatao22"],
#    ["fa19-523-192", "Jihoon Kim","Kim926"],
#   ["fa19-523-193", "Lin-Fei Sung","lfsung1997"],
#    ["fa19-523-194", "Ashley Minton","ashmmint"],
#   ["fa19-523-195", "Kang Jie Gan","kanggan"],
#    ["fa19-523-196", "Xinzhuo Zhang","zhanxinz"],
#    ["fa19-523-198", "Dominic Matthys","dojomatt"],
#    ["fa19-523-199", "Lakshya Gupta","lakshyagupta96"],
#    ["fa19-523-200", "Naimesh Chaudhari","nchaudh03"],
#   ["fa19-523-201", "Ross Bohlander","rbohland"],
#    ["fa19-523-202", "Limeng Liu","liulim-Liu"],
#    ["fa19-523-203", "Jisang Yoo","jisayoo"],
#    ["fa19-523-204", "Andrew Dingman","acdingman"],
#    ["fa19-523-205", "Senthil Palani","psendil"],
#    ["fa19-523-206", "Lenin Arivukadal","wowlenin"],
#    ["fa19-523-207", "Nihir Chadderwala","nihirc"],

#["fa19-523-208","Saravanan Natarajan",	"sanata"],
#["fa19-523-209","Asya Kirgiz", "AsyaJ"],
#["fa19-523-210","Matthew Han", "matthewjhan"],
#["fa19-523-211","Yu-Hsi Chiang", "chiayuhs0718"]


["fa19-523-212", "Josiah Clemons", "JLemon1"]

#["fa19-516-159", "Austin Zebrowski", "azebrowski"],
#"fa19-516-160","Shreyans Jain", "toshreyansjain"],
#["fa19-516-161","Jim Nelson", "JENelson77"],
#["fa19-516-162","Shivani Katukota, ", "katukota"],
#["fa19-516-163","John Hoerr", "jhoerr"],
#["fa19-516-164","Siddhesh Mirjankar", "smirjank"],
#["fa19-516-165","Zhi Wang", "zwang89"],
#["fa19-516-166","Brian Funk", "brianfunk3"],
#["fa19-516-167","William Screen", "william-screen"],
#["fa19-516-168","Deepak Deopura", "deepakdeopura"],
#["fa19-516-169","Harshawardhan Pandit", "hppanditims"]
#["fa19-516-170","Yanting Wan", "YantingWan"],

#["fa19-516-156", "Manikandan Nagarajan", "ManiNagarajan20"],
#["fa19-516-157", "Chenxu Wang",	"wang542"],
#["fa19-516-158", "Daivik Dayanand", "Daivik1997"]
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
          community: "523"
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
