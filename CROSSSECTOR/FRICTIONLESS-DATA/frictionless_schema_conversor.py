import json
def removeLastPoint(text):
    outputText = text
    if len(text) < 1:
        return text
    if text[-1] not in [".", " "]:
        return outputText
    else:
        return removeLastPoint(text[:-1])

def open_jsonref(fileUrl):
    import jsonref
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        pointer = requests.get(fileUrl)
        return jsonref.loads(pointer.content.decode('utf-8'))
    else:
        # es file
        file = open(fileUrl, "r")
        return jsonref.loads(file.read())

fileToConvert = "./CSVDialect/original_schema.json"
dataModelName = "CSVDialectFrictionlessData"
outputFile = "./CSVDialect/schema.json"

originalSchema = open_jsonref(fileToConvert)
convertedSchema = {}
convertedSchema["title"] = "Smart Data Models - " + originalSchema["title"]
convertedSchema["description"] = originalSchema["description"] + "Converted for Smart Data Models initiative from original frictionless data"
convertedSchema["$schemaVersion"] = "0.0.1"
convertedSchema["$schema"] = "http://json-schema.org/schema"
convertedSchema["id"] = "https://smart-data-models.github.io/dataModel.FrictionlessData/" + dataModelName + "/schema.json"
convertedSchema["type"] = "object"
convertedSchema["required"] = originalSchema["required"]
props = originalSchema["properties"]
convertedSchema["properties"] = {}
# print(props)
for prop in props:
    print(prop)
    title = props[prop].get("title", "")
    description = props[prop].get("description", "")
    context = props[prop].get("context", "")
    propType = props[prop].get("type", "")
    convertedSchema["properties"][prop] = {}
    convertedSchema["properties"][prop]["type"] = propType
    convertedSchema["properties"][prop]["description"] = "Property. " + removeLastPoint(title) + ". " + removeLastPoint(context) + ". " + removeLastPoint(description)
print(convertedSchema)
with open(outputFile, "w") as file:
    file.write(json.dumps(convertedSchema))