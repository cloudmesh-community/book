#!/usr/bin/env python3
# validate_yml.py : Validate YAML file
# Mihir Shanishchara, 2018
# Open README.yml and dump

import sys
from ruamel.yaml import YAML

file = sys.argv[1]

input_readme = open(file).read()

yaml = YAML()
yaml.dump(yaml.load(input_readme), sys.stdout)