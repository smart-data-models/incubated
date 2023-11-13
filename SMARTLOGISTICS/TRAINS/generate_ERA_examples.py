import os
from pysmartdatamodels import pysmartdatamodels as sdm

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

path = "./dataModel.ERA"

directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
url_path = "https://raw.githubusercontent.com/smart-data-models/incubated/master/SMARTLOGISTICS/TRAINS/dataModel.ERA/"
for directory in directories:
    schema_url = url_path + directory + "/schema.json"
    print(schema_url)
    example_normalized = sdm.ngsi_ld_example_generator(schema_url)
    example_keyvalues = sdm.ngsi_ld_keyvalue_example_generator(schema_url)
    print(example_normalized)
    print(example_keyvalues)
    a = input("go on")


