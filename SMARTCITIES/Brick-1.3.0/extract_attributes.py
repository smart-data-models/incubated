import re
source_file = "Brick.ttl"
pattern = r'\s*rdfs:label \"(.*)\"'

with open(source_file, "r") as file:
    lines = file.readlines()

finding_tag = False
attributes = set()
for line in lines:
    if line[0:4] == "tag:":
        finding_tag = True
        key = line.split(" ")[0].replace("tag:", "")
    if finding_tag:
        match = re.search(pattern, line)
        if match:
            attributes.add(key)
            key =""
            finding_tag = False
list_attributes = list(attributes)
print(sorted(list_attributes))

