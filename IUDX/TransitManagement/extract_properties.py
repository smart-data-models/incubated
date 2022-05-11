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
locationSchema = "https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/Dataset/schema.json"
schema = open_json(locationSchema)
for element in schema["allOf"][1]["properties"]:
    print(element)
    if "description" in schema["allOf"][1]["properties"][element]:
        # print(schema["allOf"][1]["properties"][element]["description"])
        nada = 0
    else:
        print("missing description")
    # print()

