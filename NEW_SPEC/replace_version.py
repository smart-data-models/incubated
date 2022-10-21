from github import Github


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

def replace_section(repository, spec_path, section, content, token, globalUser):
    import requests

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
    specUrl = "https://smart-data-models.github.io/" + repository + "/" + spec_path
    specPointer = requests.get(specUrl)
    if specPointer.status_code == 200:

        contentSpec = specPointer.text
        start = "<!-- " + section + " -->"
        end = "<!-- \\" + section + " -->"
        sectionStartFound = contentSpec.find(start)
        sectionEndFound = contentSpec.find(end)
        if (sectionStartFound == -1) or (sectionEndFound == -1):
            return [False, "not found section " + section + " inside spec at " + specUrl]
        else:
            newSectionContent = content[:sectionStartFound] + content + contentSpec[sectionEndFound:]
            message = "updated section " + section
            github_push_from_variable(newSectionContent, repository, spec_path, message, globalUser, token)
            return [True, "updated this section " + section + " of the file " + spec_path + " with this content " + content]
    else:
        return [False, "not found spec at " + specUrl]


credentialsFile = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
# credentials = "/home/fiware/credentials.json
credentials = open_json(credentialsFile)
token = credentials["token"]
globalUser = credentials["globalUser"]
g = Github(token)

repository = "incubated"
spec_path = "Person/doc/spec.md"
section = "20-Description"
content = """
Global description: **A person (alive, dead, undead, or fictional) mapped from schema.org**  

version: 0.0.2  

"""

output = replace_section(repository, spec_path, section, content, token, globalUser)
if output[0]:
    print("successfully replace")
else:
    print(output[1])