import os
for root, dirs, files in os.walk("."):
    for file in files:
        filename = "notes_context.jsonld"
        if file.endswith(filename):
            file_path = os.path.join(root, file)
            print("found " + filename + " in:" + file_path)
            os.remove(os.path.join(root, file))