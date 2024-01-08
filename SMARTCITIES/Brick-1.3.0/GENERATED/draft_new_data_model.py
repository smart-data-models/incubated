import re
import os
import json
def draft_new_datamodel(dataModel, description="", localPath="."):
    import json
    def create_directory_if_not_exists(directory_path):
        import os
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    schema = {
        "$schema": "http://json-schema.org/schema#", "$schemaVersion": "0.0.1",
        "$id": "https://smart-data-models.github.io/dataModel.BRICK/XXXX/schema.json",
        "title": "Smart Data Models - XXXX", 
        "description": "Adaptation of the BRICK ontology to Smart Data Models for the entity XXXX",
        "modelTags": "BRICK, Building",
        "derivedFrom": "",
        "license": "https://smart-data-models.github.io/dataModel.BRICK/XXXX/LICENSE.md",
        "type": "object", "allOf": [
            {
                "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
            },
            {
                "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
            },
            {
                "properties": {}
            }
        ]
    }
    schema["$id"] = schema["$id"].replace("XXXX", dataModel)
    schema["title"] = schema["title"].replace("XXXX", dataModel)
    schema["description"] = description
    schema["license"] = schema["license"].replace("XXXX", dataModel)
    schema["description"] = schema["description"].replace("XXXX", dataModel)
    create_directory_if_not_exists(localPath + "/" + dataModel)

    path = localPath + "/" + dataModel + "/schema.json"
    print(path)
    with open(path, "w") as file:
        json.dump(schema, file, indent=2)

def add_attribute_to_datamodel(dataModel, attribute, localPath=".", attributeschema={}):
    import json
    path = localPath + "/" + dataModel + "/schema.json"
    with open(path, "r") as file:
        schema = json.load(file)
    print(schema)
    schema["allOf"][2]["properties"][attribute] = attributeschema
    with open(path, "w") as file:
        json.dump(schema, file, indent=2)

# draft_new_datamodel("test", description="test description", localPath=".")
# add_attribute_to_datamodel("test", "attribute1", localPath=".", attributeschema={"type": "string", "description": "Property. Test description"})

def list_files_with_extension(directory, extension):
    files = []
    for root, _, file_list in os.walk(directory):
        files += [os.path.join(root, file) for file in file_list if file.endswith(extension)]
    return files

def extract_entities(payload_url):

    with open(payload_url, "r") as file:
        lines = file.readlines()
    pattern = "^.*\sa\s(.*)\s;$"
    occurrences = []
    for line in lines:
        if line[0] !="#":
            match = re.search(pattern, line)
            if match:
                occurrences.append(match.group(1))
    print(occurrences)
    print(len(occurrences))
    return list(set(occurrences))

def load_prefixes(ttl_file_path):
    import re
    term_uris = []
    pattern = "<(.*)>.*"
    with open(ttl_file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        if line[0:7] == "@prefix":
            prefix = line.split()[1].replace(":", "")
            match = re.search(pattern, line.split()[2])
            if match:
                url = match.group(1)
                term_uris.append([prefix, url])
            else:
                print("warning, not found uri")
                break
    return term_uris





    return list(prefixes)

def extract_attribute(attribute_lines):
    attributes = []
    for line in attribute_lines:
        pieces = line.split()
        attributes.append(pieces[0].split(":")[1])
    return attributes

def extract_attributes_entity(ttl_file_path, entities_to_look_for):
    # This function will extract the attributes from the file matching the entities in the array of entities
    # it returns an array of [[entity1, attribute1], [entity2, attribute2],..]
    output_array = []
    with open(ttl_file_path, "r") as file:
        lines = file.readlines()
    ontologies = load_prefixes(ttl_file_path)
    terms = [term[0] for term in ontologies]
    for entity_to_look_for in entities_to_look_for:
        # this is the pattern to lok for. with any of the prefixes ontologies
        pattern = "[" + "|".join(terms) + "]:"+ entity_to_look_for
        print(pattern)
        # variable to start th retrieval of lines with the attributes
        adding_lines = False
        attributes_lines = []
        attributes_entity = set()
        # looking for the entity across the lines
        for line in lines:
            if adding_lines:
                if len(line) > 1:
                    attributes_lines.append(line)
                else:
                    adding_lines = False
                    attributes_entity.add(set(extract_attribute(attributes_lines)))
                    attributes_lines = []
            if line[0] != "#":
                match = re.search(pattern, line)
                if match:
                    adding_lines = True
        for attribute in attributes_entity:
            output_array.append([entity_to_look_for, attribute])

    return output_array


# identify the ttl files in teh examples folder
file_list = list_files_with_extension("./../examples", ".ttl")
print(file_list)

# to gather all different data models
dataModels = set()

for example in file_list:
    print("__________________________________________")
    print("Starting example " + example)
    print("__________________________________________")

    # we extract the entities in the files
    raw_entities  = extract_entities(example)
    ontologies = load_prefixes(example)
    print(raw_entities)
    entities = []

    new_references  = []
    for item in raw_entities:
        split_entity = item.split(":")
        url = split_entity[0]
        # removes extra spaces, colons, commas and dots
        entity = split_entity[1].replace(" ", "").replace(";", "").replace(",", "").replace(".", "")
        dataModels.add(entity)
        with open("notes_context.jsonld", "r") as file:
            schema = json.load(file)
        print(url)
        if entity not in schema["@context"]:
            schema[entity] = ontologies[entity]
    with open("notes_context.jsonld", "w") as file:
            json.dump(schema, file)
    print(new_references)
print(dataModels)
print(len(dataModels))
for datamodel in dataModels:
    draft_new_datamodel(datamodel, description="", localPath=".")

for example in file_list:
    print("__________________________________________")
    print("Starting example " + example)
    print("__________________________________________")
    raw_entities  = extract_entities(example)


## I need to  include the attributes in the schemas and the notes_context.jsonld in the same directory, but maybe this file is in the wrong place and it should be in the root of BRICk folcder