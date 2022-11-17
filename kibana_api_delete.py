import requests
import json
import argparse
from sys import exit
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time

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
                       default="1.2.1",
                       help='The Version of k8s package to be installed')                       
my_parser.add_argument('-delete',
                       '-d',
                       nargs="?",
                       type=bool,
                       default=False,
                       const=True,
                       help='Flag to force deletion of specific Agent policy')
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

# with open(args.k8spolicy) as k8sPolicy:
#    k8sPolicyBody = json.load(k8sPolicy)


url=args.url+"/api/fleet/"
print ("Starting Automation for ... ", url)

headersList = {"Authorization": "ApiKey "+args.apikey, "kbn-xsrf": "true" , "Content-Type": "application/json"}

# Delete Agent
if args.delete is True and args.agentId:
    x = requests.delete(url+"agents/"+args.agentId, headers = headersList, verify=False)
    if x.status_code == 200:
        print("OK- Deleting Agent", args.agentId)
        #Give some time the agent to be deleted:
        time.sleep(10)
    else:
        print("Error- Deleting Agent", args.agentId, "Error:", x.text)
        exit(1)


# Delete Agent Policy
if args.delete is True:
    x = requests.post(url+"agent_policies/delete", headers = headersList, verify=False, json = {"agentPolicyId": args.agentPolicyId})
    if x.status_code == 200:
        print("OK- Deleting Agent Policy", args.agentPolicyId)
    else:
        print("Error- Deleting Agent Policy",args.agentPolicyId, "Error:", x.text)
        exit(1)

