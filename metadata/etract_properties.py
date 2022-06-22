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
locationSchema = "https://raw.githubusercontent.com/smart-data-models/incubated/master/metadata/schema.json"
schema = open_json(locationSchema)
# print(schema)
properties = schema["allOf"][1]
for element in properties["properties"]:

    if "description" in properties["properties"][element]:
        print(element + ": " + properties["properties"][element]["description"])
    else:
        print("missing description")
    # print()