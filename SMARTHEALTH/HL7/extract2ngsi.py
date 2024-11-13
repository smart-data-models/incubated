################################################################################
#  Licensed to the FIWARE Foundation (FF) under one
#  or more contributor license agreements. The FF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#  Author: alain.galdemas@mail.com
################################################################################

# This program will create json schemas files for HL7/FHIR mapping in NGSI-LD
# it extract all needed information from the global json schema file "overall_schema.json"
# it produce a global schema file containing all base definitions : "common-hl7-definitions.json"
# it produce a directory for each type of HL7/FHIR resource, and a json schema file for it
# conforming NGSI-LD and smartdatamodels rules, see https://github.com/smart-data-models or https://smartdatamodels.org/

# contact alain.galdemas@mail.com

import json
import os
import copy
import pathlib
import sys
import jsonschema
import shutil as sh
from jsonschema import validate, RefResolver, Draft202012Validator
import requests
import jsonref
import pysmartdatamodels as sdm

###############################################################################
# global variables
global_schema_file = "overall_schema_4.3.json"  #'fhir.schema.5.0.json' # # HL7/FHIR origin schema file name
definition_file = (
    "hl7-schema.json"  # common base definitions for HL7/FHIR mapping
)
schema_url = "https://json-schema.org/schema#"

# define the base url for "$id" don't forget a "/" at the end !
base_repo_url = (
    "https://raw.githubusercontent.com/agaldemas/incubated/master/SMARTHEALTH/HL7/"
)
# by AA:
extra_repo = 'https://smartdatamodels.org/extra/'
# need absolutely point 'raw.githubusercontent.com' this does not work
# 'https://github.com/agaldemas/incubated/blob/master/SMARTHEALTH/HL7/ 

# this following should be the final one
# "https://github.com/smart-data-models/dataModel.SMARTHEALTH.Hl7/"

# path to FHIR release for a specific directory
fhir_release_path='FHIR-R4/'

###############################################################################
# Functions
def open_jsonref(fileUrl: str):
    """
    Opens a JSON file given its URL or path and returns the loaded content as a JSON object.
    Capable of parsing JSON file with $ref
    Parameters:
    - file_url (str): The URL or path of the JSON file.
    Returns:
    - dict: The loaded JSON content if successful, none otherwise.
    Example:
    open_jsonref("https://example.com/data.json")
    {...}
    open_jsonref("local_file.json")
    {...}
    open_jsonref("invalid-url")
    None
    """
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            output = jsonref.loads(pointer.content.decode('utf-8'), load_on_repr=True, merge_props=True)
            return output
        except:
            return None
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return jsonref.loads(file.read(), load_on_repr=True, merge_props=True)
        except:
            return None


# infer content of property based on the definition got from definitions dictionary
def infer_type(hl7_type: str, definition_dict: dict):
    """
    Attempt to infer the type of a property from an HL7 definition dictionary.

    This function looks up the hl7_type definition and returns it if found; otherwise,
    it returns None.

    Args:
        hl7_type (str): The name or code of the HL7 type whose type needs to be inferred.
        definition_dict (dict): A dictionary containing definitions for various HL7 types.
                                The 'definitions' key is expected to map to another
                                dictionary containing hl7_type keys and their definitions.

    Returns:
        dict or None: If the hl7_type definition is found, it returns a dictionary
                      containing the definition; otherwise, it returns None.
    """
    # print("infer type for hl7 <{}> definition".format(hl7_type))
    def_dict = definition_dict.get("definitions", {}).get(hl7_type)
    # if it contains "properties" keep the "$ref" to definition,
    # and set "type" to "object"
    if def_dict.get("properties"):
        # get original description
        description = def_dict.get("description", "no description available")
        return {
            "description": description,
            #"type": "object", # may be not needed with "$ref"
            "$ref": "#/definitions/" + hl7_type,
        }
    # take care with 'ResourceList'
    if hl7_type == 'ResourceList':
        return {'$ref': '#/definitions/ResourceList'}
    return def_dict if def_dict else None

#################################################################
# function to prepare example json data to be used in examples.
def prepare_example_json(json_data, schema):
    """
    Prepare example json data to be used in examples.

    This function takes an example json and returns it with some modifications.
    It keeps all the properties that are in the example, but add all missing properties from schema with random values corresponding to the type of the property.

    Args:
        json_data (dict): A dictionary containing a json example.
        schema (dict): A dictionary containing the schema definition.
    Returns:
        dict or None: If the example is found, it returns a dictionary
                      containing the modified example; otherwise, it returns None.
     """
    # first get "properties" elements from the schema "allOf" array elements.
    # Initialize an empty list to store property names
    schema_properties = {}

    # Check if schema is a dictionary and contains "allOf" which is a list
    if isinstance(schema, dict) and "allOf" in schema:
        # Iterate through each item in the "allOf" array
        for item in schema["allOf"]:
            # Ensure the item is a dictionary before proceeding
            if isinstance(item, dict):
                # Check if this specific item has properties defined
                if "properties" in item:
                    # Extend the list with keys of each property within this item's properties
                    schema_properties =item["properties"]

    # Now you can use schema_properties as needed, for example to iterate over it:
    for prop in schema_properties:
        print(f"Property found: {prop}")    # iterate through the list of properties in schema
        output_json = {}
        for prop in schema_properties.keys():
            if prop in json_data:
                output_json[prop] = json_data[prop]
            else:
                if "type" in schema_properties[prop]:
                    type_ = schema_properties[prop]["type"]
                    if type_ == "array":
                        # Handle array property
                        if "items" in schema_properties[prop]:
                            if "type" in schema_properties[prop]["items"]:
                                item_type = schema_properties[prop]["items"]["type"]
                                if item_type == "string":
                                    output_json[prop] = [(prop + " text")]
                                elif item_type == "number":
                                    output_json[prop] = [12345]  # random number
                                elif item_type == "boolean":
                                    output_json[prop] = [True if prop.startswith("is") else False]  # random boolean value based on property name prefix
                                elif item_type == "object":
                                    output_json[prop] = [{}]
                        # Add more types as needed for array items
                    elif type_ == "string":
                        output_json[prop] = prop + " text"
                    elif type_ == "number":
                        output_json[prop] = 12345  # random number
                    elif type_ == "boolean":
                        output_json[prop] = True if prop.startswith("is") else False  # random boolean value based on property name prefix
                    elif type_ == "object":
                        output_json[prop] = {}
                    # Add more types as needed
                else:
                    output_json[prop] = "unknown_type"  # or handle unknown types appropriately
    return output_json
    ##-----------------------
###############################################################################
# MAIN
# now the main loop that do the job
# Load the JSON schema file into a Python dictionary
with open(global_schema_file) as f:
    schema = json.load(f)
# Extract the list of resource types from the global schema dictionary
hl7_resource_types = list(schema["discriminator"]["mapping"].keys())
# print(hl7_resource_types)

# Extract the "definitions" key from the loaded dictionary
condition = True
hl7_definitions = {k: v for k, v in schema["definitions"].items() if condition}
# Create a new dictionary by filtering out any elements whose keys are present in hl7_resource_types
base_definitions = {
    k: v for k, v in hl7_definitions.items() if k not in hl7_resource_types
}

# now replace "extension" properties content of each definition with this dict :
# @TODO: check in NGSI-LD, or schem if possible to constrain the type of entity/object in schema ?
# for the moment I added "@type": "Extension" to achieve this, check if it's licit in schema ?
extension_dict = {
    "@type": "Extension",
    "anyOf": [
        {
            "type": "string",
            "minLength": 1,
            "maxLength": 256,
            "pattern": "^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$",
            "description": "Property. Identifier format of any NGSI entity",
        },
        {
            "type": "string",
            "format": "uri",
            "description": "Property. Identifier format of any NGSI entity",
        },
    ],
}

# loop on all definitions to replace "extension" property in the right place
for def_name, definition in base_definitions.items():
    # iterate on element of the definition
    for key, element in definition.items():
        if key == 'properties':
            for prop, content in element.items():
                if prop == 'extension' or prop == 'modifierExtension':
                    # replace with the new dict
                    if content.get('items', None):
                        content["items"].update(extension_dict)
                        del content["items"]["$ref"]
                    else:
                        print('TTTTTTTTTT definiton of {} => found Extension dependance on property {} without "items" : ', def_name, prop )


# loop on all definitions to radd 'type': 'object' to definition
for def_name, definition in base_definitions.items():
    if 'properties' in definition:
        # add 'type': 'object' to definition
        definition.update({'type':'object'})
            
                
 


# add header to definitions schema
# to build global common definitions
definition_schema = {
    "$schema": schema_url,
    "description": "Base definitions for HL7 FHIR resources mapping to NGSI-LD",
    #"$id": base_repo_url + fhir_release_path + definition_file,
    "title": "Common HL7/FHIR definitions for NGSI-LD Harmonized Data Models",
    "definitions": {
        # "hl7-commons": {
        #     "description": "common properties for HL7",
        #     "type": "object",
        #     "properties": {}
        # },
    }
}
print("definition_schema: ", definition_schema)


# merge with base_definitions dict
definition_schema["definitions"].update(base_definitions)


# create directory for the entity resource type
path = pathlib.Path(fhir_release_path)
path.mkdir(parents=True, exist_ok=True)


# ==============================
# define the schema header to include in each schema file
# note it contains $ref to global base definitions file definition_file "common-hl7-definitions.json"
schema_header = {
    "$schema": schema_url,
    "$schemaVersion": "0.0.1",
    "$id": base_repo_url + fhir_release_path + "XXXX/schema.json",
    "title": "Smart Data Models - HL7/FHIR",
    "description": "Smart Data Models for HL7/FHIR mapping",
    "modelTags": "HL7",
    "derivedFrom": "https://hl7.org/fhir/R4B/",
    "license": "https://www.hl7.org/implement/standards/fhir/license.html",
    "type": "object",
    "required": ["id", "type"],
    "allOf": [
        {
            "$ref": "https://smart-data-models.github.io/dataModel.Hl7/hl7-schema.json#/definitions/GSMA-Commons"
        },
        {
            "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
        },
    # ],
    # "anyOf": [
        {
            "$ref": base_repo_url + fhir_release_path + definition_file + "#/definitions/Element"
            #"$ref": extra_repo + definition_file + "#/definitions/Element"
        },
    ],
}

# add "Extension" to hl7_resource_types to create an entity schema for it
hl7_resource_types.append('Extension')

# now prepare dict of definitions which are not in "ResourceList"
resources_definitions = {
    k: v for k, v in hl7_definitions.items() if k in hl7_resource_types
}
# loop on HL7/FHIR resource types to create an NGSI-LD entity schema for each,
# the type of the entity match the name of the resourceType

for entity_type, entity_def in resources_definitions.items():
    print(">>>>>>>>> process hl7 resource for entity_type: <" + entity_type + ">")
    #print('>>>>>>>>> process hl7 resource for entity_def: ', entity_def)
    
    hl7_type_content = None
    # loop on entity properties to prepare it for destination schema
    for prop, content in entity_def["properties"].items():
        print('Process <' + prop + '> property')
        # add necessary "Property. Model:’https://schema.org/<type of property value>"
        # in description of the property to match NGSI-LD rules
        #
        hl7_type = ''
        type_dict = None
        item_type = "string"
        if "$ref" in content:
            hl7_type = content["$ref"].replace("#/definitions/", "")
            # we don't need "$ref" inside property definition, but "properties" block must be inside "allOf" block !
            # content['$ref'] = content['$ref'].replace('#/definitions/', base_id_url + definition_file + '/')
            # then remove it
            del content["$ref"]
            # infer item type from hl7 type (is it a number, an array, an object) ?
            # we should infer "type" and add it, but it can't be the hl7 original type

            type_dict = infer_type(hl7_type, definition_schema)
            # print('TTTTTTTTTTTT type_dict: ', type_dict)
            content.update(type_dict)

        elif (
            content.get("type",None) == "array"
            and "items" in content
        ):
            if content['items'].get('$ref'):
                hl7_type = content['items']['$ref'].replace('#/definitions/', '')
            elif entity_type == 'Extension':
                hl7_type = 'Extension'
                # normally we already changed the content....
            else:
                # in theory it doesn't occur !
                print('EEEEEEE entity type <{}> has no $ref for property <{}>', entity_type, prop)
                print ('content: ', content)

            # we don't need "$ref" inside property definition, but "properties" block must be inside "allOf" block !
            # content['items']['$ref'] = content['items']['$ref'].replace('#/definitions/', base_id_url + definition_file + '#/definitions/')
            # then remove it
            if content['items'].get('$ref'):
                del content["items"]["$ref"]
            # property "type" exist it's an array, but the type of "items"
            # can be hl7 original type or a "$ref" (it seems it's always a $ref, since no exception occur)
            type_dict = infer_type(hl7_type, definition_schema)
            # print('TTTTTTTTTTTT in items type_dict: ', type_dict)
            content['items'].update(type_dict)


        origDesc = content["description"]
        # compute new description
        # #TODO: see if we need to change 'https://schema.org/' with something else
        # like the base_id_url ?
        # because the model is coming from the "$ref" content definition,
        # which are in 'SMART HEALTH/HL7/common-hl7-schema.json' file
        base_url = base_repo_url + fhir_release_path  # "https://hl7.org/fhir/" # take care to '/'
        description = "Property. Model:'" + base_url + fhir_release_path + hl7_type + "' " + origDesc
        content["description"] = content["description"].replace(origDesc, description)

        # manage 'extension' and 'modifierExtension' properties with a special treatment:
        # to prevent infinite loop with recursion of Extension, which can contains an Extension...
        # so Extension will be an entity in itself, created and in relation through this property
        if prop == "extension" or prop == "modifierExtension":
            # keep only "description" element from original
            # del content['items']['$ref']
            # adjust description to conform NGSI-LD SMD rules ! => it's a relationship
            content["description"] = content["description"].replace(
                "Property.", "Relationship."
            )
            content["items"].update(extension_dict)
            content["type"] = "array"

        # manage id
        # if prop == "id":
        #     # change "id" property content to match NGSI-LD rules
        #     # or change name for "fhirHL7Id" and add NGSI "id"
        #     print("id content:", content)

        # type exist in some hl7/FHIR resource objects
        #
        if prop == "type":
            # change "type" to "hl7Type"
            # print('TTTTTTTTTT resource <{}> contains a "type" property"', entity_type)
            hl7_type_content = {"hl7Type": content}
            print ('TTTTTTTTT hl7_type dict:', hl7_type_content)
            # entity_def['properties'].update(hl7_type)
        # else:

        # update "$ref" with url SMART HEALTH/HL7/common-hl7-schema.json
        # if "$ref" in content:
        #     content["$ref"] = content["$ref"].replace(
        #         "#/definitions/", base_repo_url + fhir_release_path + definition_file + "#/definitions/"
        #     )
        # if 'items' in content and content.get("items",None).get("$ref",None):
        #     content["items"]["$ref"] = content["items"]["$ref"].replace(
        #         "#/definitions/", base_repo_url + fhir_release_path + definition_file + "#/definitions/"
        #     )

        if "$ref" in content:
            content["$ref"] = content["$ref"].replace(
                "#/definitions/", base_repo_url + fhir_release_path + definition_file + "#/definitions/"
            )
        if 'items' in content and content.get("items",None).get("$ref",None):
            content["items"]["$ref"] = content["items"]["$ref"].replace(
                "#/definitions/", base_repo_url + fhir_release_path + definition_file + "#/definitions/"
            )

    # end loop on properties

    # prepare entity schema and set things in header
    entity_schema = schema_header
    entity_schema["$id"] = base_repo_url + fhir_release_path + entity_type + "/schema.json"
    entity_schema["title"] = entity_type + " data model based on HL7 equivalent resource"
    entity_schema["description"] = "Smart Data Models for " + entity_type + " HL7/FHIR resource type"

    # remove "properties" in "allOff" array !
    index = -1
    for i, elem in enumerate(entity_schema["allOf"]):
        if elem.get('properties', None):
            index = i
            break
           
    if index > -1:    
        del entity_schema["allOf"][index]
    # del entity_schema["allOf"].key("properties")


    # now we are on global entity schema (entity_def)
    # add "type" as a global entity property
    type_prop = {
        "type": {
            "type": "string",
            "enum": [entity_type],
            "description": "Property. NGSI Entity type. It has to be '" + entity_type + "'",
        }
    }
    if hl7_type_content:
        #del entity_def['properties']['type']
        entity_def['properties'].update(hl7_type_content)

    entity_def["properties"].update(type_prop)
    # remove "id"
    if entity_def["properties"].get('id',None):
        del entity_def["properties"]["id"]
    # print('TTTTTTTTTTTTTTT entity_def: ', entity_def['properties'])
    # prepare dict with the header and the entity def
    entity_schema['allOf'].append({'properties': entity_def['properties']})

    # remove "$id" to be able to valid locally !
    # del entity_schema["$id"]

    

    # validate the entity schema itself
    try:
        resolver = RefResolver(base_uri= base_repo_url + fhir_release_path, referrer=entity_schema)
    except Exception as e:
        print("RefResolver Error:", e)
    else:
        print(
            "resolver for: " + entity_type + " is !",
            resolver
        )

    try:
        validator = Draft202012Validator(entity_schema, resolver=resolver)
    except Exception as e:
        print("Draft202012Validator Error:", e)
    else:
        print(
            "Entity schema for " + entity_type + " is valid against Draft202012Validator !"
        )

    # create directory for the entity resource type
    path = pathlib.Path(fhir_release_path + entity_type)
    path.mkdir(parents=True, exist_ok=True)
    # create dir for example
    path1 = pathlib.Path(fhir_release_path + entity_type + "/examples")
    path1.mkdir(parents=True, exist_ok=True)
    
    # delete already present json files

    # delete already present json files in entity directory
    files = os.listdir(path)
    print('files: ', files)
    for file in files:
        if file.endswith('.json'):
            try:
                os.remove('./' + fhir_release_path + entity_type + '/' + file)
            except FileNotFoundError:
                print('file not found !')

    # write schema file in the directory
    exportfilename = "./" + fhir_release_path + entity_type + "/schema.json"
    with open(exportfilename, "w+") as exportfile:
        json.dump(entity_schema, exportfile, indent=4, separators=(", ", ": "))
    print(">>>>>> wrote schema file for entity type " + entity_type)
    print("=============================================")
    
    # add ADOPTERS.yaml file (copy from HL7 directory)
    # copy HL7 ADOPTERS.yaml file to entity directory
    sh.copy(
        "./ADOPTERS.yaml",
        "./" + fhir_release_path  + entity_type  + "/ADOPTERS.yaml"
    )
    # add notes.yaml file
    sh.copy(
        "./notes.yaml",
        "./" + fhir_release_path  + entity_type  + "/notes.yaml"
    )
    # add LiCENSE.md file (copy from HL7 directory)
    sh.copy(
        "./LiCENSE.md",
        "./" + fhir_release_path  + entity_type  + "/LiCENSE.md"
    )
    
    #========================== validation loop and example generation
    # this loop try to validate examples toward entity schema, which is somehow a bit stupid,
    # because the objects should be adapted to NGSI-LD before, even the schema remains almost the same except for Extension
    if 1:
        print("start validation loop on examples files:")
        directory_path = "./_examples/hl7.fhir.r4b.examples/package"
        for filename in os.listdir(directory_path):
            if filename.startswith(entity_type) and filename.endswith(".json") and '-example' in filename:
                print('>>>>>>>>>>> try to validate json file: ' + filename)
                try:
                    file_path = os.path.join(directory_path, filename)

                    with open(file_path, 'r') as f:
                        json_data = json.load(f)
                except Exception as e:
                    print("!!!!!!!!!! Error opening file {}: {} {}".format(filename, e.__class__, str(e)))
                
                #======================= adapt json data to NGSI-LD format
                json_data = prepare_example_json(json_data, entity_schema)
                if 0: # no validation for now
                    try:
                        # validator = Draft7Validator(json_data)
                        # print('++++++++++ file {} is valid against Draft7Validator'.format(filename))

                        validate(instance=json_data, schema=entity_schema, resolver=resolver)

                    except jsonschema.exceptions.ValidationError as e:
                        print('!!!!!!!!!! Error validating file ', filename)
                        print('ValidationError occured: ', e)
                    except Exception as e:
                        print('!!!!!!!!!! Error validating file ', filename)
                        print('Exception occured: ', e)
                        # os._exit(1)
                    else:
                        print("++++++++++ file {}: validate against schema".format(filename))

                # copy file to example directory copyfile(file_path, os.path.join(path1, 'example.json'))
                exportfilename = "./" + fhir_release_path + entity_type + "/examples/example.json"
                with open(exportfilename, "w+") as exportfile:
                    json.dump(json_data, exportfile, indent=4, separators=(", ", ": "))

                # exit from for loop when a file has been validated and copied to example directory
                break
        print("======end validation loop=======================================")

    # end validation loop
# end for loop on resources definitions

# remove Extension from base_definitions
if 'Extension' in definition_schema["definitions"]:
    print('>>>>>> delete Extension definition')
    del definition_schema["definitions"]['Extension']

# Save the extracted base definitions to a new JSON file
with open(fhir_release_path + definition_file, "w") as f:
    json.dump(definition_schema, f, indent=4, separators=(", ", ": "))

print('job finished !!!!')
