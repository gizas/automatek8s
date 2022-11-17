import requests
import json
import argparse
from sys import exit
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import subprocess
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('-url',
                       '-u',
                       type=str,
                       nargs="?",
                       const="https://localhost:5601",
                       default="https://localhost:5601",
                       help='The url of Kibana API')
my_parser.add_argument('-apikey',
                       '-k',
                       type=str,
                       required=True,
                       help='The APIKEY referring to token able to make API calls')
my_parser.add_argument('-k8version',
                       '-v',
                       type=str,
                       nargs="?",
                       const="1.27.1",
                       default="1.27.1",
                       help='The Version of k8s package to be installed')                       
my_parser.add_argument('-agentpolicy',
                       '-ap',
                       type=str,
                       nargs="?",
                       const="agentpolicy.yaml.json",
                       default="agentpolicy.yaml.json",
                       help='The Agent Policy file in json format')
my_parser.add_argument('-k8spolicy',
                       '-kp',
                       type=str,
                       nargs="?",
                       const="k8spolicy.yaml.json",
                       default="k8spolicy.yaml.json",
                       help='The Kubernetes Policy file in json format')
args = my_parser.parse_args()

#Parse Relevant Policies
with open(args.agentpolicy) as agentPolicy:
   agentPolicyBody = json.load(agentPolicy)

with open(args.k8spolicy) as k8sPolicy:
   k8sPolicyBody = json.load(k8sPolicy)


url=args.url+"/api/fleet/"
#print ("Starting Automation for ... ", url)

headersList = {"Authorization": "ApiKey "+args.apikey, "kbn-xsrf": "true" , "Content-Type": "application/json"}

# #Get epm packages
# x = requests.get(url+"epm/packages", headers = headersList, verify=False)
# print(x.text)

# #Get install k8s package
x = requests.post(url+"epm/packages/kubernetes/"+args.k8version, headers = headersList, verify=False)

if x.status_code != 200:
    print("Error- Installing k8s Package version %d", args.k8version)
    print(x.text)
    exit(1)
#else:
    #print("OK- Installing k8s Package version", args.k8version)


# #Create Agent Policy
x = requests.post(url+"agent_policies", headers = headersList, verify=False, json = agentPolicyBody)
if x.status_code != 200:
    print("Error- Installing Agent Policy")
    print(x.text)
    exit(1)
# else:
#     print("OK- Installing Agent Policy")


# #Create Package Policy
x = requests.post(url+"package_policies", headers = headersList, verify=False, json = k8sPolicyBody)
if x.status_code != 200:
    print("Error- Installing Package Policy")
    print(x.text)
    exit(1)
# else:
#     print("OK- Installing Package Policy")

#Retrieve the key of the new Agent Policy
x = requests.get(url+"enrollment_api_keys", headers = headersList, verify=False)
api_keys_values=x.json()
for list in api_keys_values['list']:
    if list['policy_id']=="agent-policy-id-automated":
        if list['active'] is True:
            print (list['api_key'])
