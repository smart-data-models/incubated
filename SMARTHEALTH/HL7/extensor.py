# to debug
# error prompt
# unsure the replacement is recursive enough

import json
def open_json(fileUrl):
    import json
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            return json.loads(pointer.content.decode('utf-8'))
        except:
            return None

    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return json.loads(file.read())
        except:
            return None


def replacer(payload, definitions):
    # it will be an object with their properties
    import copy
    newPayload = copy.deepcopy(payload)
    keys = list(payload.keys())
    key0 = keys[0]
    print(key0)
    print(payload)
    directives = ["additionalProperties", "required", "description"]
    for element in payload[key0]:
        if element not in directives:
            if element == "properties":
                for item in payload[key0]["properties"]:
                    subObject = {item: payload[key0]["properties"][item]}
                    newPayload[key0]["properties"][item] = replacer(subObject, definitions)[item]
                    del newPayload[key0]["properties"][item]["$ref"]
                    print("the returned schema is " + str(newPayload[key0]["properties"][item]))
            elif "$ref" in payload[key0][element]:
                print("found $ref in " + str(payload[key0][element]))
                term = payload[key0][element]["$ref"].replace("#/definitions/", "")
                termDefinition = replacer(definitions[term], definitions)
                newPayload[key0][element] = dict(newPayload[key0][element], **termDefinition)
                del newPayload[key0][element]["$ref"]
                print("the returned schema is " + str(newPayload[key0][element]))
            elif "items" in payload[key0][element]:
                subObject = {"items": payload[key0][element]}
                print("got into items" + str(subObject))
                newPayload[key0][element]["items"] = replacer(subObject, definitions)["items"]
                print("the returned schema is " + str(newPayload[key0][element]["items"]))
    a = input("seguir")
    return newPayload


full_schema_file_name = "overall_schema.json"
extendedSchema = []
with open(full_schema_file_name, "r") as file_content:
    schema_txt = file_content.read()
fullDict = json.loads(schema_txt)
definitions = fullDict["definitions"]
entity = "Element"
filename = entity + ".json"
outfilename = entity +"_processed.json"
objectDict = open_json(filename)
print(objectDict)
with open(filename, "r") as txtFile:
    textObject = txtFile.read()

extendedSchema = replacer(objectDict, definitions)
with open(outfilename, "w") as outfile:
    json.dump(extendedSchema, outfile)
print(extendedSchema)