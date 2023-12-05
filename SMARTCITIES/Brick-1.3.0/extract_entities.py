import re
source_file = "Brick.ttl"
pattern = r'(.*) a owl:Class.*'

with open(source_file, "r") as file:
    lines = file.readlines()

finding_tag = False
entities = set()
for line in lines:
    match = re.search(pattern, line)
    if match:
        entity = line.split(" ")[0].replace("brick:", "")
        entities.add(entity)
list_entities = list(entities)
print(sorted(list_entities))

