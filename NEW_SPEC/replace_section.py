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

