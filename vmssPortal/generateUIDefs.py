import json
import copy
from pprint import pprint

with open('imageList.json') as imageListFile:
    imageList = json.load(imageListFile)

with open('CreateUiDefinition.json') as baseFile:
    base = json.load(baseFile)

for environment in imageList:
    path = 'output/' + environment
    data = copy.copy(base)
    data["parameters"]["steps"][0]["elements"][0]["constraints"]["allowedValues"] = imageList[environment]["windows"]
    data["parameters"]["steps"][0]["elements"][0]["defaultValue"] = imageList[environment]["windowsDefault"]
    data["parameters"]["steps"][0]["elements"][1]["constraints"]["allowedValues"] = imageList[environment]["linux"]
    #pprint(data)

    with open(path, 'w') as outFile:
        outFile.write(json.dumps(data))
