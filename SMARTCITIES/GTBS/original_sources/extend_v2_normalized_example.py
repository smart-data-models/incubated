from os import listdir, mkdir
from os.path import isfile, join
import json
from github import Github

def github_push_from_variable(contentVariable, repoName, fileTargetPath, message, globalUser, token):
    from github import Github
    g = Github(token)
    repo = g.get_organization(globalUser).get_repo(repoName)
    try:
        file = repo.get_contents("/" + fileTargetPath)
        update = True
    except:
        update = False
    if update:
        repo.update_file(fileTargetPath, message, contentVariable, file.sha)
    else:
        repo.create_file(fileTargetPath, message, contentVariable, "master")


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


def keyvalues2normalized(keyvaluesPayload):
    import json

    keyvaluesDict = json.loads(keyvaluesPayload)
    output = {}
    # print(normalizedDict)
    for element in keyvaluesDict:
        item = {}
        print(keyvaluesDict[element])
        if isinstance(keyvaluesDict[element], list):
            # it is an array
            item["type"] = "array"
            item["value"] = keyvaluesDict[element]
        elif isinstance(keyvaluesDict[element], dict):
            # it is an object
            item["type"] = "object"
            item["value"] = keyvaluesDict[element]
        elif isinstance(keyvaluesDict[element], str):
            # it is an string
            item["type"] = "string"
            item["value"] = keyvaluesDict[element]
        elif keyvaluesDict[element] == True:
            # it is an boolean
            item["type"] = "boolean"
            item["value"] = True
        elif keyvaluesDict[element] == False:
            # it is an boolean
            item["type"] = "boolean"
            item["value"] = False
        elif isinstance(keyvaluesDict[element], int) or isinstance(keyvaluesDict[element], float):
            # it is an number
            item["type"] = "number"
            item["value"] = keyvaluesDict[element]
        else:
            print("*** other type ***")
            print("I do now know what is it")
            print(keyvaluesDict[element])
            print("--- other type ---")
        output[element] = item
    if "id" in output:
        output["id"] = output["id"]["value"]
    if "type" in output:
        output["type"] = output["type"]["value"]

    print(output)
    return output


def normalized2keyvalues(normalizedPayload):
    # input has to be a string
    normalizedDict = json.loads(normalizedPayload)
    output = {}
    # print(normalizedDict)
    for element in normalizedDict:
        print(normalizedDict[element])
        try:
            value = normalizedDict[element]["value"]
            output[element] = value
        except:
            output[element] = normalizedDict[element]

    print(json.dumps(output, indent=4, sort_keys=True))
    return output

def extend_v2_normalized_example(repoName, dataModel, globalUser, token):
    # gather the example
    g = Github(token)
    repo = g.get_organization(globalUser).get_repo(repoName)
    exampleV2NormalizedStr = repo.get_contents(dataModel + "/examples/example-normalized.json").decoded_content.decode()
    print("original normalized V2")
    print(exampleV2NormalizedStr)
    exampleV2NormalizedDict = json.loads(exampleV2NormalizedStr)


    # create the key values format V2
    exampleV2KeyvaluesDict = normalized2keyvalues(exampleV2NormalizedStr)
    exampleV2KeyvaluesStr = json.dumps(exampleV2KeyvaluesDict, indent=4)
    print("derivative key values V2")
    print(exampleV2KeyvaluesStr)

    # create the key values format LD
    exampleLDKeyvaluesDict = exampleV2KeyvaluesDict.copy()
    exampleLDKeyvaluesDict["@context"] = ["https://smartdatamodels.org/context.jsonld"]
    exampleLDKeyvaluesStr = json.dumps(exampleLDKeyvaluesDict, indent=4)
    print("derivative key values LD")
    print(exampleLDKeyvaluesStr)

    # create the Ld normalized version
    payload = exampleV2NormalizedDict.copy()
    for prop in payload:
        if prop in ["id", "type"]:
            continue
        elif payload[prop]["type"] == "geo:json":
            payload[prop]["type"] = "Geoproperty"
        elif payload[prop]["type"] == "Relationship":
            payload[prop]["object"] == payload[prop]["value"]
            del payload[prop]["value"]
        elif payload[prop]["type"] == "DateTime":
            payload[prop]["type"] = "Property"
            payload[prop]["value"] = {"@type": "DateTime", "@value": payload[prop]["value"]}
        else:
            payload[prop]["type"] = "Property"

    payload["@context"] = ["https://smartdatamodels.org/context.jsonld"]
    exampleLDNormalizedStr = json.dumps(payload, indent=4)
    print("derivative normalized LD")
    print(exampleLDNormalizedStr)

    print("_____________________________________-")
    message = "Key values V2 Example generated from normalized v2 example automatically"
    print(exampleV2KeyvaluesStr)
    github_push_from_variable(exampleV2KeyvaluesStr, repoName, dataModel + "/examples/example.json", message, globalUser, token)

    message = "Key values LD Example generated from normalized v2 example automatically"
    print(exampleLDKeyvaluesStr)
    github_push_from_variable(exampleLDKeyvaluesStr, repoName, dataModel + "/examples/example.jsold", message, globalUser, token)

    message = "Normalized LD Example generated from normalized v2 example automatically"
    print(exampleLDNormalizedStr)
    github_push_from_variable(exampleLDNormalizedStr, repoName, dataModel + "/examples/example-normalized.jsonld", message, globalUser, token)

    return True


credentialsFile = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
# credentials = "/home/fiware/credentials.json
credentials = open_json(credentialsFile)
token = credentials["token"]
globalUser = credentials["globalUser"]

repoName = "incubated"
dataModel = "SMARTCITIES/GTBS/original_sources/free_bike_status"
output = extend_v2_normalized_example(repoName, dataModel, globalUser, token)

print(output)
