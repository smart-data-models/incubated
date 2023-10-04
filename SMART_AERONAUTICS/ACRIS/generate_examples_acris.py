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


def list_directories_and_read_schema():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all directories in the current directory
    directories = [d for d in os.listdir(current_directory) if os.path.isdir(d)]

    for directory in directories:
        # Enter each directory
        os.chdir(directory)

        # Check if a "schema.json" file exists in the current directory
        if os.path.exists("schema.json"):
            with open("schema.json", "r") as schema_file:
                # Read and parse the "schema.json" file
                schema_data = json.load(schema_file)
                if "#/components/schemas/" in str(schema_data):
                    print("next")
                else:
                    pathSchema = "https://raw.githubusercontent.com/smart-data-models/incubated/master/SMART%20AERONAUTICS/ACRIS/" + directory + "/schema.json"
                    print(pathSchema)
                    keyvalues = sdm.ngsi_ld_keyvalue_example_generator(pathSchema)
                    # github_push_from_variable(json.dumps(keyvalues, indent=4), "incubated", "SMART AERONAUTICS/ACRIS/" + directory + "/examples/example.json", "Example created", globalUser, token)
                    normalized = sdm.ngsi_ld_example_generator(pathSchema)
                    github_push_from_variable(json.dumps(keyvalues, indent=4), "incubated", "SMART AERONAUTICS/ACRIS/" + directory + "/examples/example-normalized.jsonld", "Example created", globalUser, token)
                    print(normalized)





        # Return to the parent directory
        os.chdir(current_directory)

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
    list_directories_and_read_schema()
