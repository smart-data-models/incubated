import json
iudxModel = "WaterDistributionNetwork"
inputFileName = iudxModel + "/raw_schema.json"
outputFileName = iudxModel + "/schema.json"
originalAttributeTypes = {'iudx:Relationship', 'rdfs:Class', 'owl:Class', 'iudx:QuantitativeProperty',
                          'iudx:TimeProperty', 'iudx:TextProperty', 'iudx:StructuredProperty', 'iudx:GeoProperty'}

schemaHeader = {
    "$schema": "http://json-schema.org/schema#",
    "modelTags": "IUDX",
    "$id": "https://smart-data-models.github.io/dataModel.WasteWater/WaterDistributionNetwork/schema.json",
    "title": "GISData",
    "$schemaVersion": "0.0.1",
    "description": "Smart Data Models - A Data Model for water supply network in a city.",
    "derivedFrom": "https://voc.iudx.org.in/WaterDistributionNetwork",
    "type": "object",
    "allOf": [
        {
            "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
        },
        {
            "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
        }]}

with open(inputFileName, "r") as inputFile:
    inputDict = json.load(inputFile)["@graph"]
# print(inputDict)
types = set()
multiTypedAttributes = []
schema = schemaHeader.copy()

properties = []
for element in inputDict:
    print(element)
    if "@type" in element:
        if isinstance(element["@type"], list) and len(element["@type"]) > 1:
            print(element["@type"])
            print("double types for " + element["@id"])
            for item in element["@type"]:
                print(item)
                types.add(item)
            multiTypedAttributes.append(element)
        else:
            simpleType = element["@type"][0]
            print(simpleType)
            types.add(simpleType)
            attributeDict = {}
            if simpleType == "iudx:Relationship":
                attributeDict = {element["rdfs:label"]: {"type": "Relationship", "description": "Relationship. " + element["rdfs:comment"]}}
                properties.append(attributeDict)
            # if simpleType == "iudx:GeoProperty":
            #     attributeDict = {element["rdfs:label"]: {"$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"}}
            #     properties.append(attributeDict)
            if simpleType == "iudx:QuantitativeProperty":
                attributeDict = {element["rdfs:label"]: {"type": "number", "description": "Property. " + element["rdfs:comment"]}}
                properties.append(attributeDict)
            if simpleType == "iudx:TextProperty":
                attributeDict = {element["rdfs:label"]: {"type": "string", "description": "Property. " + element["rdfs:comment"]}}
                properties.append(attributeDict)
            if simpleType == "iudx:TimeProperty":
                attributeDict = {element["rdfs:label"]: {"type": "string", "format": "date-time", "description": "Property. " + element["rdfs:comment"]}}
                properties.append(attributeDict)
            if simpleType == "iudx:StructuredProperty":
                attributeDict = {element["rdfs:label"]: {"type": "object", "description": "Property. " + element["rdfs:comment"], "properties": {}}}
                properties.append(attributeDict)
schema["allOf"].append({"properties": properties})
print("__________________")
print(schema)
with open(outputFileName, "w") as outputFile:
    outputFile.write(json.dumps(schema, indent=4))