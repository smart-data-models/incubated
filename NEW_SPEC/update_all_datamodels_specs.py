import json
import time
from github import Github
import os


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


dataModelListUrl = "https://raw.githubusercontent.com/smart-data-models/data-models/master/specs/AllSubjects/official_list_data_models.json"
errorsFile = "errors.log"
errors = []
exceptions = []  # repos to be not treated
included = []  # repos to be treated
notTreatExceptions = True
onlyTreatIncluded = False
dataModelsExceptionsOn = True
dataModelsToBeTreatedOn = False
dataModelsExceptions = []
dataModelsToBeTreated = []
counter = 0
limit = 5
if onlyTreatIncluded and notTreatExceptions:
    print("not possible to parse both, choose one exceptions or included")
else:
    if counter < limit:
        counter += 1
        repos = open_json(dataModelListUrl)["officialList"]
        print(repos)
        for repo in list(reversed(repos)):
            repoName = repo["repoName"]
            if (notTreatExceptions and repoName not in exceptions) or (onlyTreatIncluded and repoName in included):
                dataModels = repo["dataModels"]
                for dataModel in dataModels:
                    if (dataModelsExceptionsOn and dataModel not in dataModelsExceptions) or (
                            dataModelsToBeTreatedOn and dataModel in dataModelsToBeTreated):
                        #############################################################
                        # edit below this comment to launch the action on the repos #
                        #############################################################
                        configFileName = "datamodels_to_publish.json"
                        configDict = open_json(configFileName)
                        configDict["dataModels"] = [dataModel]
                        configDict["subject"] = repoName
                        with open(configFileName, "w") as configFile:
                            configFile.write(json.dumps(configDict))
                        os.system("python3 20_create_spec_v10.0.py")
                        # a = input("seguir")
                        time.sleep(10)
                    counter += 1    #
                    #
                    # with open(errorsFile, "w") as file:
                    #     file.write(str(errors))



