import copy
import json
def open_yaml(fileUrl):
    # import yaml
    import ruamel.yaml as yaml  # it avoids that on / off will be translated into True / False
    import requests
    try:
        if fileUrl[0:4] == "http":
            # es URL
            pointer = requests.get(fileUrl)
            return yaml.safe_load(pointer.content.decode('utf-8'))
    except:
        return None
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return yaml.safe_load(file.read())
        except:
            return None

def insert_property(original):
    if isinstance(original, dict):
        parsed = copy.deepcopy(original)
        if "description" in original:
            parsed["description"] = "Property. " + original["description"]
        if "properties" in original:
            for property in original["properties"]:
                parsed["properties"][property] = insert_property(original["properties"][property])
    return parsed

file = "ORIGINAL.YAML"
outputFile = "condensed2.json"
full_object = open_yaml(file)
schemas = full_object["components"]
print(schemas)
parsed_schemas = copy.deepcopy(schemas)
for schemaKey in schemas["schemas"]:
    parsed_schemas["schemas"][schemaKey] = insert_property(schemas["schemas"][schemaKey])

with open(outputFile, "w") as output:
    json.dump(parsed_schemas, output)