import argparse
import sys
import os
import json
from ruamel.yaml import YAML

parser = argparse.ArgumentParser(
    description='For updating json string on yaml file!!')
parser.add_argument(
    '-j',
    '--jsonfile',
    type=str,
    help="full path to json file",
    required=True)
parser.add_argument(
    '-y',
    '--yamlfile',
    type=str,
    help="full path to yaml file",
    required=True)
args = parser.parse_args()
jsonfile = args.jsonfile
yamlfile = args.yamlfile
try:
    isJsonFileExist = os.path.exists(jsonfile)
    isYamlFileExist = os.path.exists(yamlfile)
    if isJsonFileExist != True:
        raise Exception('Input json file does not exist!!.')
    if isYamlFileExist != True:
        raise Exception('Input yaml file does not exist!!.')

    jsonstring = json.loads(open(jsonfile).read())
    yamlstring = open(yamlfile).read()
    yaml = YAML()
    code = yaml.load(yamlstring)
    code['data']['mcc_config.json'] = json.dumps(jsonstring)
    with open("deployment-configmap.yaml", 'w') as fp:
        yaml.dump(code, fp)

except AssertionError as error:
    print(error)
    print('Failed to update json into yaml file.')
