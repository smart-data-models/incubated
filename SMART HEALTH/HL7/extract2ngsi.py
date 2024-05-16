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
# it produce a directory for each type of HL7/FHIR resource, and a json schema file for it in NGSI-LD

# contact alain.galdemas@mail.com

import json
import copy
import pathlib
import jsonschema

global_schema_file = 'overall_schema.json' # HL7/FHIR origin schema file name
definition_file = 'common-hl7-schema.json' # common base definitions for HL7/FHIR mapping

base_id_url = "https://github.com/smart-data-models/dataModel.Hl7/"

# Load the JSON schema file into a Python dictionary
with open(global_schema_file) as f:
    schema = json.load(f)
# Extract the list of resource types from the dictionary
hl7_resource_types = list(schema["discriminator"]["mapping"].keys())
#print(hl7_resource_types)

# Extract the "definitions" key except 'ResourceList' from the loaded dictionary
hl7_definitions = {k: v for k, v in schema["definitions"].items() if k != "ResourceList"}
# Create a new dictionary by filtering out any elements whose keys are present in hl7_resource_types
base_definitions = {k: v for k, v in hl7_definitions.items() if k not in hl7_resource_types}

# now replace "extension" properties content of each definition with this dict :
# @TODO: check in NGSI-LD, or schem if possible to constrain the type of entity/object in schema ?
extension_dict = {
    "@type": "Extension",
    "anyOf": [
        {
            "type": "string",
            "minLength": 1,
            "maxLength": 256,
            "pattern": "^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$",
            "description": "Property. Identifier format of any NGSI entity"
        },
        {
            "type": "string",
            "format": "uri",
            "description": "Property. Identifier format of any NGSI entity"
        }
    ],
}

# loop to replace in the right place 
for root, definitions in base_definitions.items():
     for key, property in definitions.items():
        if key == 'properties':
            for prop, content in property.items():
                if prop == 'extension':
                    # replace with the new dict
                    del content['items']['$ref']
                    content['items'].update(extension_dict)

# add header SMART HEALTH/HL7/common-hl7-definitions.json
definition_header = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$id": "https://github.com/smart-data-models/dataModel.Hl7/" + definition_file,
    "title": "Common HL7/FHIR definitions for NGSI-LD Harmonized Data Models",
    "definitions": {}
}
print ('definition_header: ', definition_header)
# merge with base_definitions dict
definition_header['definitions'].update(base_definitions)
# Save the extracted base definitions to a new JSON file
with open(definition_file, 'w') as f:
    json.dump(definition_header, f, indent=4, separators=(", ", ": "))

# define the schema header to include in each file
# note it contains $ref to global base definitions file "common-hl7-definitions.json"
schemaHeader = {
    "$schema": "http://json-schema.org/schema#",
    "$schemaVersion": "0.0.1",
    "$id": "https://smart-data-models.github.io/dataModel.HL7/XXXX/schema.json",
    "title": "Smart Data Models - ",
    "description": "",
    "modelTags": "HL7",
    "derivedFrom": "http://hl7.org/fhir/R4B/",
    "license": "http://www.hl7.org/implement/standards/fhir/license.html",
    "type": "object",
    "required": ["id", "type"],
    "allOf": [
        {
            "$ref": "https://smart-data-models.github.io/dataModel.Hl7/hl7-schema.json#/definitions/GSMA-Commons"
        },
        {
            "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
        }
    ],
    "anyOf": [
        {
            "$ref": "https://github.com/smart-data-models/dataModel.Hl7/common-hl7-definitions.json"
        }
    ]
}

# now prepare dict of definitions which are not in "ResourceList"
resources_definitions = {k: v for k, v in hl7_definitions.items() if k in hl7_resource_types}

for entity_type, entity_def in resources_definitions.items():
    # print('entity_type: ' + entity_type)

    # replace extension property content with "extension_dict"
    for prop, content in entity_def['properties'].items():
        # if entity_type == 'Account':
        #     print('entity_def', entity_def)
        #     print('prop: ', prop)
        if prop == 'extension' or prop == 'modifierExtension':
            # keep only "description" element from original
            del content['items']['$ref']
            content['items'].update(extension_dict)

    # prepare dict with the header and the entity def
    entity_dict = schemaHeader
    entity_dict.update(entity_def)
    # set things in header
    entity_dict["$id"] = entity_dict["$id"].replace("XXXX", entity_type)
    entity_dict["title"] += entity_type + " data model based on HL7 equivalent resource"

    try:
        validator = jsonschema.Draft7Validator(entity_dict)
    except Exception as e:
        print("Error:", e)
    else:
        print("Entity schema for " + entity_type + " is valid !")

    # create directory for the entity resource type
    path = pathlib.Path(entity_type)
    path.mkdir(parents=True, exist_ok=True)
    # write schema file in the directory
    exportfilename = './' + entity_type  + '/schema.json'
    with open(exportfilename, "w+") as exportfile:
        json.dump(entity_dict, exportfile, indent=4, separators=(", ", ": "))



