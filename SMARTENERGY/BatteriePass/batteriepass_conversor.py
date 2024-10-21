import copy
import jsonref
import json
def open_jsonref(fileUrl):
    import jsonref
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            output = jsonref.loads(pointer.content.decode('utf-8'), load_on_repr=True)
            return output
        except:
            return ""
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return jsonref.loads(file.read())
        except:
            return ""

def extract_key(data, key_to_remove, parent_key=""):
    key = parent_key
    extracted_urn = {}
    print(data)
    print("________________________")
    if isinstance(data, dict):
        if key_to_remove in data:
            payload = {key: data[key_to_remove]}
            extracted_urn.update(payload)
            del data[key_to_remove]
        for key, value in list(data.items()):
            if isinstance(value, dict) or isinstance(value, list):
                temp = extract_key(value, key_to_remove, key)
                print(temp)
                if temp[1]:
                    extracted_urn.update(temp[1])
    elif isinstance(data, list):
        # If data is a list, iterate over its elements
        for item in data:
            if isinstance(item, dict) or isinstance(item, list):
                temp = extract_key(item, key_to_remove, key)
                if temp[1]:
                    extracted_urn.update(temp[1])
    return [data, extracted_urn]


# def remove_key(data, key_to_remove, parent_key=""):
#     results = []
#     key = parent_key
#     if isinstance(data, dict):
#         # If data is a dictionary, iterate over its keys
#         if key_to_remove in data:
#             payload = {key: data[key_to_remove]}
#             results.append(payload)
#             del data[key_to_remove]
#         for key, value in list(data.items()):
#             temp = remove_key(value, key_to_remove, key)
#             if temp:
#                 results.append(temp)
#     elif isinstance(data, list):
#         # If data is a list, iterate over its elements
#         for item in data:
#             temp = remove_key(data, key_to_remove, key)
#             if temp:
#                 results.append(temp)
#     return results

datamodel = "Circularity"
subject = "dataModel.BatteriePass"
key_to_remove = "x-samm-aspect-model-urn"
notes_context_dict = {"@context": {}}
notes_context = "SDM/" + datamodel + "/notes.context.jsonld"

base_schema = "SDM/" + datamodel + "/" + datamodel + "-schema.json"
base_schema_dict = open_jsonref(base_schema)

template_schema = "SDM/" + datamodel + "/" + "schema.json"
template_schema_dict = open_jsonref(template_schema)

# print(base_schema_dict)
# print(template_schema_dict)

schema_dict = copy.deepcopy(template_schema_dict)
schema = "SDM/" + datamodel + "/" + "schema2.json"

# conversion
# $id
schema_dict["$id"] = schema_dict["$id"].replace("dataModel.SUBJECT", "dataModel.BatteriePass").replace("DATAMODEL", datamodel)

# description
schema_dict["description"] = base_schema_dict["description"]

# title
schema_dict["title"] = schema_dict["title"].replace("SUBJECT", subject).replace("DATAMODEL", datamodel)

# modelTags
schema_dict["modelTags"] = "batteriePass"

# "derivedFrom": "",
# title

schema_dict["derivedFrom"] = "https://github.com/batterypass/BatteryPassDataModel/blob/main/BatteryPass/io.BatteryPass." + datamodel + "/1.0.0/gen/" + datamodel + "-schema.json"

# title
schema_dict["license"] = schema_dict["license"].replace("dataModel.SUBJECT", subject).replace("DATAMODEL", datamodel)

# type
schema_dict["allOf"][2]["properties"]["type"]["enum"] = [datamodel]
schema_dict["allOf"][2]["properties"]["type"]["description"] = schema_dict["allOf"][2]["properties"]["type"]["description"].replace("`ThreePhaseAcMeasurement`.", datamodel)

# remove other attributes but the type
key_to_keep = "type"
for item in list(schema_dict["allOf"][2]["properties"].keys()):
    if item != key_to_keep:
        del schema_dict["allOf"][2]["properties"][item]

# print("_______________________")
# print(base_schema_dict["properties"])
# print("_______________________")
for element in base_schema_dict["properties"]:
    print(element)
    schema_dict["allOf"][2]["properties"][element] = base_schema_dict["properties"][element]
    schema_dict["allOf"][2]["properties"][element]["description"] = "Property. " + base_schema_dict["properties"][element]["description"]
    parsed_element = extract_key(schema_dict["allOf"][2]["properties"][element], "x-samm-aspect-model-urn", "")
    schema_dict["allOf"][2]["properties"][element] = parsed_element[0]
    notes_context_dict["@context"].update(parsed_element[1])


with open(schema, "w") as file:
    json.dump(schema_dict, file, indent=2)

with open(notes_context, "w") as file:
    json.dump(notes_context_dict, file, indent=2)


