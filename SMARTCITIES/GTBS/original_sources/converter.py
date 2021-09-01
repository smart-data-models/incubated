from os import listdir, mkdir
from os.path import isfile, join
import json

def open_json(fileUrl):
    import json
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        pointer = requests.get(fileUrl)
        return json.loads(pointer.content.decode('utf-8'))
    else:
        # es file
        file = open(fileUrl, "r")
        return json.loads(file.read())

localDirectory = "."
onlyFiles = [f for f in listdir(localDirectory) if isfile(join(localDirectory, f)) if f[-5:] == ".json"]
print(onlyFiles)
for file in onlyFiles:
    dataModelName = file.replace(".json", "")
    schemaDict = open_json(file)
    schemaDict["$schemaVersion"] = "0.0.1"
    schemaDict["title"] = "Smart Data Models adaptation of GBFS standard data model " + dataModelName
    schemaDict["description"] = schemaDict["description"] + " According to the Standard GBFS 2.2"
    schemaDict["$id"] = "https://smart-data-models.github.io/dataModel.GBFS/" + dataModelName + "/schema.json"
    for prop in schemaDict["properties"]:
        print(prop)
        print(dataModelName)
        print(schemaDict["properties"][prop])
        schemaDict["properties"][prop]["description"] = "Property. " + schemaDict["properties"][prop]["description"]
    schemaDict["properties"]["id"] = {"$ref": "https://github.com/smart-data-models/data-models/raw/master/common-schema.json#/definitions/EntityIdentifierType"}
    schemaDict["properties"]["type"] = {"type": "string", "description": "Property. NGSI entity type. It has to be " + dataModelName}
    try:
        directoryName = localDirectory + "/" + dataModelName
        mkdir(directoryName)
    except OSError:
        print("Creation of the directory %s failed" % directoryName)
    else:
        print("Successfully created the directory %s " % directoryName)
    schemaDict["required"].append("id")
    schemaDict["required"].append("type")
    with open(directoryName + "/schema.json", "a") as file:
        json.dump(schemaDict, file)
        print("stored the data model " + dataModelName)

