import jsonref
from copy import deepcopy

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

def open_jsonref(fileUrl):
    import jsonref
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            output = jsonref.loads(pointer.content.decode('utf-8'), load_on_repr=True)
            return output
        except:
            return ""
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return jsonref.loads(file.read())
        except:
            return ""


full_schema_file_name = "overall_schema.json"
extendedSchema = []
with open(full_schema_file_name, "r") as file_content:
    schema_txt = file_content.read()
# print(schema_txt)
limit = 1
counter = 0
directives = ["additionalProperties"]
fullDict = jsonref.loads(schema_txt)
for key in fullDict["definitions"]:
    print(key)
    if key != "ResourceList":
        newConcept = deepcopy(fullDict["definitions"][key])
        for element in newConcept:
            print(element)
            if element not in directives:
                if "$ref" in newConcept[element]:
                    if counter > limit:
                        break
                    else:
                        counter += 1
                    term = newConcept[element]["$ref"].replace("#/definitions/","")
                    newConcept = {newConcept, fullDict["definitions"][term]}
                    del newConcept["$ref"]
        extendedSchema.append(newConcept)
print(extendedSchema)


