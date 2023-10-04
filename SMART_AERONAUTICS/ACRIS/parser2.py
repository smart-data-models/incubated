import copy
import json
import os
def open_json(fileUrl):
    import json
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            output = json.loads(pointer.content.decode('utf-8'), load_on_repr=True)
            return output
        except:
            return ""
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return json.loads(file.read())
        except:
            return ""

def relative(object, schemas):
    import copy
    output = copy.deepcopy(object)
    if "properties" in object:
        for elem in object["properties"]:
            if "$ref" in object["properties"][elem]:
                if "#" in object["properties"][elem]["$ref"]:
                    print("found relative")
                    term = object["properties"][elem]["$ref"].split("/")[-1]
                    print(term)
                    output["properties"][elem] = relative(schemas[term], schemas)
    return output



sourceFile = "condensed2.json"
template = open_json("template.json")
datamodels = open_json(sourceFile)
for element in datamodels["schemas"]:
    template = open_json("template.json")
    datamodels = open_json(sourceFile)
    print(element)
    os.makedirs(element)
    path = "./" + element + "/schema.json"
    template["title"] = template["title"].replace("XXX", element)
    template["$id"] = template["$id"].replace("XXX", element)
    template["allOf"][0]["properties"]["type"]["enum"][0] = element
    template["allOf"][0]["properties"]["type"]["description"] = template["allOf"][0]["properties"]["type"]["description"].replace("XXX", element)


    submodel = datamodels["schemas"][element]

    if "description" in submodel:
        description = submodel["description"]
        template["description"] = description
    parsed_submodel = relative(submodel, datamodels["schemas"])
    print(parsed_submodel)
    for elem in parsed_submodel["properties"]:
        template["allOf"][0]["properties"][elem] = parsed_submodel["properties"][elem]


    with open(path, "w") as file:
        json.dump(template, file, indent=4)
