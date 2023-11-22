import re
with open("mandate.ttl", "r") as ontology_file:
    lines = ontology_file.readlines()
cr = chr(10)
new_object = ""
objects = []
objects.append("")
extending_object = False

for line in lines:
    # print(ord(line[0]))
    if line[0] == cr:
        extending_object = False
        if len(new_object) > 1 and new_object != objects[-1]:
            objects.append(new_object)
        continue
    elif line[0] == "#":
        continue
    elif line[0] == ":":
        new_object = line
        extending_object = True
    elif extending_object:
        new_object += line

attributes = []
for index, obj in enumerate(objects):
    print(index)
    print(obj)
    # attribute = {}
    # attribute["name"] = obj.split(" ")[0][1:]
    # first_line = obj.split(cr)[1]
    # print("first line:" + first_line)
    # attribute["objectType"] = re.split("['owl:',' ']", first_line)[1]
    # attributes.append(attribute)
    # print(attribute)
    print("_____________")

