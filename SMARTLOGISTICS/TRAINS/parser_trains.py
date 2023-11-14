import os
import json
import xml.etree.ElementTree as ET

mytree = ET.parse('ontology.rdf')
myroot = mytree.getroot()
schemas = {}

for element in myroot:
    # print(element.tag)
    # detecting the class elements (entities to be)

    if element.tag == "{http://www.w3.org/2002/07/owl#}Class":
        print(element.attrib)
        dataModel = list((element.attrib).values())[0].split("/")[-1]
        print(dataModel)
        # a = input("stop")
        print("_________________________________")
        sentence = element.attrib
        _keys = list(sentence.keys())
        uri = sentence[_keys[0]]
        derivedFrom = uri

        title = ""
        description = ""
        for item in element:
            print(item)
            title = dataModel + " + mapped from ERA ontology by Smart Data Models"
            if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}comment":
                description = item.text
        print("URI:" + uri)
        print("Datamodel:" + dataModel)
        print("Description:" + description)
        if dataModel != "":
            schemas[dataModel] = {}
            schemas[dataModel]["uri"] = uri
            schemas[dataModel]["title"] = title
            schemas[dataModel]["description"] = description
            schemas[dataModel]["derivedFrom"] = derivedFrom

print(schemas)
with open("output.json", "w") as file:
    json.dump(schemas, file)

header = {
    "$schema": "http://json-schema.org/schema#",
    "$schemaVersion": "0.0.1",
    "$id": "https://smart-data-models.github.io/dataModel.ERA/XXXX/schema.json",
    "modelTags": "ERA vocabulary, railway, train",
    "license": "https://smart-data-models.github.io/dataModel.ERA/XXXX/LICENSE.md",
    "derivedFrom": "https://data-interop.era.europa.eu/era-vocabulary/",
    "type": "object",
    "allOf": [
        {
            "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
        },
        {
            "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
        },
        {
            "properties": {}
        }
    ],
    "required": ["id", "type"]
}
print("__________________")
outputDirectory = "./dataModel.ERA"
for item in list(schemas.keys()):
    print(item)
    schema_object = header
    schema_object["$id"] = schema_object["$id"].replace("XXXX", item)
    schema_object["license"] = schema_object["license"].replace("XXXX", item)
    schema_object["title"] = schemas[item]["title"]
    schema_object["derivedFrom"] = schemas[item]["derivedFrom"]
    schema_object["description"] = schemas[item]["description"]
    schema_object["allOf"][2]["properties"]["type"] = {}
    schema_object["allOf"][2]["properties"]["type"] = {"type": "string", "enum": [item], "description": "Property. NGSI data type. It has to be " + item}
    dirname = outputDirectory + "/" + item
    os.makedirs(dirname, exist_ok=True)
    filename = outputDirectory + "/" + item + "/schema.json"
    with open(filename, "w") as file:
        json.dump(schema_object, file, indent=2)

