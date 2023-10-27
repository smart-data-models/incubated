import json

def open_jsonref(fileUrl):
    import jsonref
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            output = jsonref.loads(pointer.content.decode('utf-8'), load_on_repr=True)
            return output
        except:
            return ""
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return jsonref.loads(file.read())
        except:
            return ""


source_file = "./Shipment/schema.json"
schema = open_jsonref(source_file)
print(schema)
output_file = "./Shipment/parsed_schema.json"
with open(output_file, "w") as file:
    file.write(str(json.dumps(schema, indent=4)))
