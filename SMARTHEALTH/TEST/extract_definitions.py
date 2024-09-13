import json
with open("ActivityDefinition.json", "r") as filepointer:
    rawtxt  = filepointer.read()
# print(rawtxt)
schema = json.loads(rawtxt)["ActivityDefinition"]["properties"]
# print(schema)
definitions = set()
for element in schema:
    if "$ref" in schema[element]:
        definitions.add(schema[element]["$ref"])
        print("found one!")
        print(schema[element]["$ref"])
print(definitions)
for defin in definitions:
    print(defin)