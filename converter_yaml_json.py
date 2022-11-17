# This script transforms given yaml file to json
import yaml
import json

import glob

# All files and directories ending with .json will be matched and marked for transformation:
for jsonFile in glob.glob("./*.yaml"):
    with open(jsonFile, 'r') as file:
        configuration = yaml.safe_load(file)
    
    print("Started conversion to json for file "+jsonFile)
    with open(jsonFile+'.json', 'w') as json_file:
        json.dump(configuration, json_file)
        # output = json.dumps(json.load(open(jsonfile)), indent=2)
        # print(output)