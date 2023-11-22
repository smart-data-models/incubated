from rdflib import Graph
import json
import os

# Create a Graph
g = Graph()

# Parse the TTL file
g.parse("mandate.ttl", format="turtle")

# Iterate over the triples in the graph
header = {
    "$schema": "http://json-schema.org/schema#",
    "$schemaVersion": "0.0.1",
    "$id": "https://smart-data-models.github.io/dataModel.Mandate/XXXX/schema.json",
    "modelTags": "ERA vocabulary, railway, train",
    "license": "https://smart-data-models.github.io/dataModel.Mandate/XXXX/LICENSE.md",
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
outputDirectory = "./dataModel.Mandate"
entities = []
for subj, pred, obj in g:
    if str(obj) == "http://www.w3.org/2002/07/owl#Class":
        # print(subj, pred, obj)
        # print(type(subj),type(pred),type(obj) )
        entity = str(subj).split("#")[1]
        print(entity)
        schema_object = header
        schema_object["$id"] = schema_object["$id"].replace("XXXX", entity)
        schema_object["license"] = schema_object["license"].replace("XXXX", entity)
        schema_object["title"] = entity + " adapted to Smart Data Models"
        schema_object["derivedFrom"] = "https://github.com/everis-rpam/RPaM-Ontology"
        # schema_object["description"] = schemas[entity]["description"]
        schema_object["allOf"][2]["properties"]["type"] = {}
        schema_object["allOf"][2]["properties"]["type"] = {"type": "string", "enum": [entity], "description": "Property. NGSI data type. It has to be " + entity}
        dirname = outputDirectory + "/" + entity
        os.makedirs(dirname, exist_ok=True)
        filename = outputDirectory + "/" + entity + "/schema.json"
        with open(filename, "w") as file:
            json.dump(schema_object, file, indent=2)
        entities.append(entity)

    for subj, pred, obj in g:
        if str(pred) == "http://www.w3.org/2004/02/skos/core#definition":
            short_subj = str(subj).split("#")[1]
            if short_subj in entities:
                entity = short_subj
                print("Found description for entity" + entity)
                filename = outputDirectory + "/" + entity + "/schema.json"
                with open(filename, "r") as file:
                    schema = json.load(file)
                schema["description"] = str(obj)
                with open(filename, "w") as file:
                    json.dump(schema, file, indent=2)


