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

def create_examples_payloads(repoName, dataModel, globalUser, token, *options):
    # options[0] could be schema (default) or in a future from example
    import requests
    if len(options) == 0 or options == None:
        mode = "schema"
    else:
        mode = options[0]

    serviceNGSIKeyvaluesExample = "https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues_v0.92.php"
    serviceNGSINormalizedExample = "https://smartdatamodels.org/extra/ngsi-ld_generator_v0.92.php"
    g = Github(token)
    repo = g.get_organization(globalUser).get_repo(repoName)
    if mode == "schema":
        try:
            path = dataModel + "/schema.json"
            print(path)
            file = repo.get_contents(path)
        except:
            return "cannot get repo schema. Wrong path / repo?"
        urlSchema = "https://raw.githubusercontent.com/smart-data-models/" + repoName + "/master/" + dataModel + "/schema.json"
        urlToRequestNormalized = serviceNGSINormalizedExample + "?schemaUrl=" + urlSchema + "&email=alberto.abella@fiware.org"
        urlToRequestKeyvalues = serviceNGSIKeyvaluesExample + "?schemaUrl=" + urlSchema + "&email=alberto.abella@fiware.org"
        try:
            print(urlToRequestKeyvalues)
            pointer = requests.get(urlToRequestKeyvalues)
            keyvaluesLDPayload = dict(pointer.content.decode('utf-8'))
        except:
            return "Problem with keyvalues example"
        try:
            print(urlToRequestNormalized)
            pointer = requests.get(urlToRequestNormalized)
            normalizedLDPayload = dict(pointer.content.decode('utf-8'))
        except:
            return "Problem with normalized example"
        keyvaluesV2Payload = keyvaluesLDPayload
        contextUrl = keyvaluesV2Payload.pop("@context", None)
        normalizedV2Payload = keyvalues2normalized(keyvaluesV2Payload)
        # write the examples in the directory
        message = "Key values V2 Example generated automatically"
        print(keyvaluesV2Payload)
        github_push_from_variable(keyvaluesV2Payload, repoName, dataModel + "/examples/example.json", message, globalUser, token)

        message = "Key values LD Example generated automatically"
        print(keyvaluesLDPayload)
        github_push_from_variable(keyvaluesLDPayload, repoName, dataModel + "/examples/example.jsonld", message, globalUser, token)

        message = "Normalized LD Example generated automatically"
        print(normalizedLDPayload)
        github_push_from_variable(normalizedLDPayload, repoName, dataModel + "/examples/example-normalized.jsonld", message, globalUser, token)

        message = "Normalized V2 Example generated automatically"
        print(normalizedV2Payload)
        github_push_from_variable(normalizedV2Payload, repoName, dataModel + "/examples/example-normalized.json", message, globalUser, token)
    else:
        print("this is the mode:" + mode)



credentialsFile = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
# credentials = "/home/fiware/credentials.json
credentials = open_json(credentialsFile)
token = credentials["token"]
globalUser = credentials["globalUser"]

repoName = "incubated"
dataModel = "SMARTCITIES/GTBS/original_sources/free_bike_status"
output = "don't know"
output = create_examples_payloads(repoName, dataModel, globalUser, token, "schema")
print(output)
