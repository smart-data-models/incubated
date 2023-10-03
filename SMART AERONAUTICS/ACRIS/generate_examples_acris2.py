from pysmartdatamodels import pysmartdatamodels as sdm

import os
import json

def github_push_from_variable(contentVariable, repoName, fileTargetPath, message, globalUser, token):
    from github import Github
    g = Github(token)
    repo = g.get_organization(globalUser).get_repo(repoName)
    try:
        file = repo.get_contents("/" + fileTargetPath)
        update = True
    except:
        update = False
    if update:
        repo.update_file(fileTargetPath, message, contentVariable, file.sha)
    else:
        repo.create_file(fileTargetPath, message, contentVariable, "master")

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


def generate_additional_example():
    # Get the current working directory
    current_directory = os.getcwd()
    print(current_directory)

    # List all directories in the current directory
    directories = [d for d in os.listdir(current_directory) if os.path.isdir(d)]

    for directory in directories:
        # Enter each directory
        # os.chdir(directory)

        # Check if a "schema.json" file exists in the current directory
        if os.path.exists("./" + directory + "/schema.json"):
            with open("./" + directory + "/schema.json", "r") as schema_file:
                # Read and parse the "schema.json" file
                schema_data = json.load(schema_file)
                if "#/components/schemas/" in str(schema_data):
                    print("next")
                else:
                    path_example = "./" + directory + "/examples/example-normalized.jsonld"
                    print(path_example)
                    path_schema = "https://raw.githubusercontent.com/smart-data-models/incubated/master/SMART%20AERONAUTICS/ACRIS/" + directory + "/schema.json"
                    normalized = sdm.ngsi_ld_example_generator(path_schema)
                    print(normalized)
                    with open(path_example, "w") as example_file:
                        example_file.write(json.dumps(normalized, indent=4))


def get_credentials(credentialsFile):
    import json

    def open_json(fileUrl):
        import json
        import requests
        if fileUrl[0:4] == "http":
            # es URL
            pointer = requests.get(fileUrl)
            return json.loads(pointer.content.decode('utf-8'))
        else:
            # es file
            file = open(fileUrl, "r")
            return json.loads(file.read())

    # credentials file is the local file where credentials are stored
    # parameters' list is the list of parameters to extract from the credentials
    try:
        with open(credentialsFile, "r") as credFile:
            credentialsText = credFile.read()
            credentialsDict = json.loads(credentialsText)
            return credentialsDict
    except:
        return False

################# TEST #################
file = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
credentials = (get_credentials(file))
globalUser = credentials["globalUser"]
token = credentials["token"]

if __name__ == "__main__":
    generate_additional_example()
