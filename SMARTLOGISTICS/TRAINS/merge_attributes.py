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

source_attributes_file = "attributes.json"
directory_datamodels = "./dataModel.ERA"
missing_datamodels = []
missing_datamodels_file = "missing_entities.json"
missing_domain_in_attribute = []
missing_domain_in_attribute_file = "missing_domain_in_attribute.json"
attributes = open_json(source_attributes_file)
for attribute in attributes:
    print(attribute)
    if "domains" in attributes[attribute]:
        for domain in attributes[attribute]["domains"]:
            schema_location = directory_datamodels + "/" + domain + "/schema.json"
            print(schema_location)
            schema = open_json(schema_location)
            print(schema)
            if schema is None:
                missing_datamodels.append(attribute)
                continue
            schema["allOf"][2]["properties"][attribute] = {}
            schema["allOf"][2]["properties"][attribute]["type"] = attributes[attribute]["type"]
            schema["allOf"][2]["properties"][attribute]["description"] = attributes[attribute]["description"]
            with open(schema_location,"w") as file:
                json.dump(schema, file)
    else:
        missing_domain_in_attribute.append(attribute)

with open(missing_datamodels_file, "w") as file:
    file.write(str(missing_datamodels))
with open(missing_domain_in_attribute_file, "w") as file:
    file.write(str(missing_domain_in_attribute))