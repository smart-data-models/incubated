import os
import shutil

mypath = './dataModel.ERA'  # Replace with the path of your current directory
onlydirectories = []
# Iterate through the directory and its subdirectories
# for root, directories, files in os.walk(mypath):
#     if root == mypath:
#         for directory in directories:
#             onlydirectories.append(os.path.join(root, directory))
entries = os.listdir(mypath)
onlydirectories = [entry for entry in entries if os.path.isdir(os.path.join(mypath, entry))]
print(onlydirectories)
# copy the license
with open ("./ADOPTERS.yaml", "r") as file:
    content = file.read()

for directory in onlydirectories:
    datamodel = directory
    adopter_content = content.replace("[Data model]", datamodel).replace("[Subject]", "dataModel.ERA").replace(" More info at https://smart-data-models.github.io/data-models/templates/dataModel/CURRENT_ADOPTERS.yaml", "")
    print(adopter_content)
    shutil.copy("./LICENSE.md", "./dataModel.ERA/" + directory + "/LICENSE.md")
    shutil.copy("./notes.yaml", "./dataModel.ERA/" + directory + "/notes.yaml")
    with open("./dataModel.ERA/" + directory + "/ADOPTERS.yaml", "w") as file:
        file.write(adopter_content)




