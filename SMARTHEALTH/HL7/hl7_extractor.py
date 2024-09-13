import jsonref
import copy

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
limit = 0
counter = 0
directives = ["additionalProperties", "required"]
fullDict = jsonref.loads(schema_txt)
definitions = fullDict["definitions"]
# looping across the elements of the definitions, only
for key in definitions:
    print(key)
    if key != "ResourceList":
        # a copy of each element is made, supposedly a dict
        if "properties" in definitions[key]:
            if counter > limit:
                break
            else:
                counter += 1
            newObject = copy.deepcopy(definitions[key]["properties"])
            print("NewObject")
            print(newObject)
            print(type(newObject))
            for element in newObject:
                print(key + ": has a subelement " + element)
                if "$ref" in newObject[element]:

                    # if found it is replaced
                    # Adding the new reference
                    term = newObject[element]["$ref"].replace("#/definitions/", "")
                    newObject = {newObject, definitions[term]}
                    print("replacing $ref=" + newObject[element]["$ref"] + " with " + str(definitions[term]))
                    # extending with the relative link
                    # removing the old one
                    del newObject["$ref"]
        extendedSchema.append(newObject)
print(extendedSchema)


