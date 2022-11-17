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
                       const="1.27.0",
                       default="1.27.0",
                       help='The Version of k8s package to be installed')
my_parser.add_argument('-agentId',
                       '-a',
                       type=str,
                       nargs="?",
                       help='Flag to force deletion of specific Agent') 
my_parser.add_argument('-agentPolicyId',
                       '-i',
                       type=str,
                       nargs="?",
                       const="agent-policy-id-automated",
                       help='Flag to force deletion of specific Agent policy')                         
my_parser.add_argument('-agentpolicy',
                       '-ag',
                       type=str,
                       nargs="?",
                       const="agentpolicy.yaml.json",
                       default="agentpolicy.yaml.json",
                       help='The Agent Policy file in json format')
my_parser.add_argument('-k8spolicy',
                       '-k8',
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
print ("Starting Automation for ... ", url)

headersList = {"Authorization": "ApiKey "+args.apikey, "kbn-xsrf": "true" , "Content-Type": "application/json"}


#Retrieve the key of the new Agent Policy
x = requests.get(url+"package_policies", headers = headersList, verify=False)
packagePolicies=x.json() 
for list in packagePolicies['items']:
    if list['policy_id']=="agent-policy-id-automated":
            print("Package Policy to be updated: "+list['id'])
            packagePolicyId=list['id']

# Update Package Policy
x = requests.put(url+"package_policies/"+packagePolicyId, headers = headersList, verify=False, json = k8sPolicyBody)
if x.status_code == 200:
    print("OK- Updating Package Policy")
else:
    print("Error- Updating Package Policy")
    print(x.text)
    exit(1)

