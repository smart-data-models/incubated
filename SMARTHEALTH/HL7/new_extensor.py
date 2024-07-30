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


def extensor(object_dict, definitions, level):
    notExpandable = ["ResourceList"]
    import copy
    limitDepth = 6
    newObject = copy.deepcopy(object_dict)
    for key, value in object_dict.items():
        print(str(key)+'->'+str(value))
        if (key == "$ref") and (level < limitDepth):
            print("_______________________")
            print("This should be replaced by")
            term = str(value).replace("#/definitions/", "")
            if term not in notExpandable:
                del newObject["$ref"]
                definition = definitions[term]
                if "description" in definition:
                    del definition["description"]
                print(definition)
                print("extended $ref =" + str(definition))
                newObject = dict(newObject, **definition)
            else:
                newObject["type"] = "string"
                del newObject["$ref"]

        # recursivity is limited
        if key == "$ref" and level >= limitDepth:
            del newObject["$ref"]
            if "type" not in newObject:
                newObject["type"] = "string"
        if isinstance(value, dict):
            print("Entering into level " + str(level + 1))
            newObject[key] = extensor(value, definitions, level + 1)
        elif isinstance(value, list):
            for val in value:
                if isinstance(val, str):
                    pass
                elif isinstance(val, list):
                    pass
                else:
                    newObject[key][val] = extensor(newObject[key][val], definitions)
    return newObject


full_schema_file_name = "overall_schema.json"
extendedSchema = []
with open(full_schema_file_name, "r") as file_content:
    schema_txt = file_content.read()
fullDict = json.loads(schema_txt)
definitions = fullDict["definitions"]

entity = "Patient"
filename = entity + ".json"
outfilename = entity +"_processed.json"
objectDict = open_json(filename)
print("**********************************")
counter = 0
limit = 9
while str(objectDict).find("#/definitions/") > -1:
    counter += 1
    if counter > limit:
        break
    outfilename = entity + "_processed" + str(counter) + ".json"
    outDict = extensor(objectDict, definitions, 0)
    print(outDict)
    with open(outfilename, "w") as outfile:
        json.dump(outDict, outfile)
    objectDict = outDict