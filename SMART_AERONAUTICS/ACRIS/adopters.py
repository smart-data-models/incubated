from pysmartdatamodels import pysmartdatamodels as sdm

import os
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
        # test


def copy_adopters():
    # Get the current working directory
    current_directory = os.getcwd()
    print(current_directory)
    original_path = "../../../../data-models/dataModel.ACRIS/AirportElevation/ADOPTERS.yaml"
    with open(original_path, "r") as file:
        content = file.read()


    # List all directories in the current directory
    directories = [d for d in os.listdir(current_directory) if os.path.isdir(d)]

    for directory in directories:
        if directory == "AirportElevation":
            continue
        else:
        # Enter each directory
        # os.chdir(directory)

        # Check if a "schema.json" file exists in the current directory
            path = "./" + directory + "/ADOPTERS.yaml"
            adapted_content = content.replace("AirportElevation", directory)
            print(adapted_content)
            print(type(adapted_content))
            with open(path, "w") as file:
                file.write(adapted_content)

if __name__ == "__main__":
    copy_adopters()
