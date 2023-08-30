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
datamodels = open_json(sourceFile)
object = {
      "type": "object",
      "description": "Property. The height of an Airport, above sea level.",
      "properties": {
        "Name": {
          "type": "string",
          "description": "Property. The name of an Airport elevation above sea level."
        },
        "Value": {
          "type": "number",
          "description": "Property. The value of an Airport elevation above sea level."
        },
        "AirportElevationUnitOfMeasurement": {
          "$ref": "#/components/schemas/AirportElevationUnitOfMeasurement"
        }
      }
    }
print(relative(object, datamodels["schemas"]))