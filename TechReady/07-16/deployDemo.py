import json
import argparse
import sys
import subprocess

sys.path.insert(0, "/home/negat/credentials/aad")
from aadcredentials import *

defaultNameBase = "nsgtr"
defaultRegion = "westus"

parser = argparse.ArgumentParser(description='Create Service Bus Queue.')
parser.add_argument('--nameBase', metavar='NAME_BASE', type=str, default=defaultNameBase,
                    help='string used to name resources; lowercase letters and numbers only')
parser.add_argument('--region', metavar='REGION', type=str, default=defaultRegion,
                    help='Azure region to deploy to')
args = parser.parse_args()

print("deploying to region " + args.region)

sbParams = {
    "serviceBusNamespaceName": {"value": args.nameBase + "namespace"},
    "serviceBusQueueName": {"value": args.nameBase + "queue"}
}

deploySbCommand = ["azure", "group", "create", "-n", args.nameBase + "rg", "-d", args.nameBase + "dep", "-l", args.region, "-f", "sbQueue.json", "-p", json.dumps(sbParams), "--json"]

print(" ".join(deploySbCommand))

print(subprocess.check_output(deploySbCommand))
