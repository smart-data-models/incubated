def get_contributors_repo(repoName, organization, outputFileName):
    from yaml import dump


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

    credentialsFile = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
    # credentials = "/home/fiware/credentials.json
    credentials = open_json(credentialsFile)
    token = credentials["token"]
    globalUser = credentials["globalUser"]
    # g = Github(token)

    primaryUrl = "https://" + globalUser + ":" + token + "@api.github.com/repos/" + organization + "/" + repoName + "/contributors"
    print(primaryUrl)
    primaryDict = open_json(primaryUrl)
    print("the primary dict is" + str(primaryDict))
    contributorsYaml = {"description": "This is a compilation list of all CONTRIBUTORS across different objects (data models) alphabetically ordered of the subject dataModel.GBFS. All fields are non mandatory"}
    contributorsYaml["contributors"] = []

    for contributor in primaryDict:
        print("________________________________________________")
        print(contributor)
        print("________________________________________________")
        userUrl = contributor["url"][:8] + globalUser + ":" + token + "@" + contributor["url"][8:]
        print(userUrl)
        userDict = open_json(userUrl)
        fullName = userDict["name"]
        print(fullName)
        if fullName is not None:
            if " " in fullName:
                name, surname = fullName.split(" ", 1)
            else:
                name = fullName
                surname = ""
        else:
            name = ""
            surname = ""
        if userDict["email"] is None:
            mail = ""
        if userDict["company"] is None:
            organization = ""

        contributorsYaml["contributors"].append({"name": name, "surname": surname, "mail": mail, "organization": organization, "project": "", "comments": "original contributor of GBFS standard"})
        print(contributorsYaml)
    with open(outputFileName, "w") as file:
        dump(contributorsYaml, file, default_flow_style=False)






repoName = "gbfs"
organization = "NABSA"
outputFileName = "CONTRIBUTORS.yaml"
get_contributors_repo(repoName, organization, outputFileName)