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
# limitations under the License.
################################################################################
# this program parses the overall definition of HL7 standard base on full json schema and
# divide it into the single entities

import copy
import pathlib
import json


def open_json(fileUrl):
    import json
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            return json.loads(pointer.content.decode('utf-8'))
        except:
            return None

    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return json.loads(file.read())
        except:
            return None


def extensor(object_dict, definitions, level):
    # create the version of the schema with limitation to the infinite recursive schema (not parseable for a jsonref package)

    # attribute that has to be avoided (it is not a proper data model)
    notExpandable = ["ResourceList"]
    import copy

    # maximum sublevels assessed of recurivity
    limitDepth = 9

    newObject = copy.deepcopy(object_dict)
    # loop to expand the $ref (till the limitiable value)
    for key, value in object_dict.items():
        print(str(key) + '->' + str(value))
        if (key == "$ref") and (level < limitDepth):
            print("_______________________")
            print("This should be replaced by")
            term = str(value).replace("#/definitions/", "")
            if term not in notExpandable:
                del newObject["$ref"]
                definition = definitions[term]
                if "description" in definition:
                    del definition["description"]
                print(definition)
                print("extended $ref =" + str(definition))
                newObject = dict(newObject, **definition)
            else:
                newObject["type"] = "string"
                del newObject["$ref"]

        # recursivity is limited
        if key == "$ref" and level >= limitDepth:
            del newObject["$ref"]
            if "type" not in newObject:
                newObject["type"] = "string"
        if isinstance(value, dict):
            print("Entering into level " + str(level + 1))
            if "properties" in value:
                value["type"] = "object"
            newObject[key] = extensor(value, definitions, level + 1)
        elif isinstance(value, list):
            for val in value:
                if isinstance(val, str):
                    pass
                elif isinstance(val, list):
                    pass
                else:
                    newObject[key][val] = extensor(newObject[key][val], definitions, level + 1)
    return newObject


schemaHeader = {
    "$schema": "http://json-schema.org/schema#",
    "$schemaVersion": "0.0.1",
    "$id": "https://smart-data-models.github.io/dataModel.HL7/XXXX/schema.json",
    "title": "Smart Data Models - HL7 / ",
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
    ]
}

filename = "overall_schema.json"
overallDict = open_json(filename)
exceptions = ["ResourceList", "base64Binary"]
definitions = overallDict["definitions"]
listToParse = overallDict["discriminator"]["mapping"].keys()
mainlimit = 1000
maincounter = 0
for item in listToParse:
    if (item not in exceptions) and (item in definitions):
        if maincounter > mainlimit:
            break
        else:
            maincounter += 1
        exportfilename = "./" + item + "/" + item + ".json"
        path = pathlib.Path(item)
        path.mkdir(parents=True, exist_ok=True)
        with open(exportfilename, "w+") as exportfile:
            json.dump({item: definitions[item]}, exportfile)
        # now load the export
        objectDict = open_json(exportfilename)
        counter = 0
        limit = 4
        while str(objectDict).find("#/definitions/") > -1:
            counter += 1
            if counter > limit:
                break
            outfilename = "./" + item + "/" + item + "_processed" + str(counter) + ".json"
            outDict = extensor(objectDict, definitions, 0)
            print(outDict)
            with open(outfilename, "w") as outfile:
                json.dump(outDict, outfile)
            objectDict = outDict
        finalfilename = "./" + item + "/" + item + "_processed" + str(limit) + ".json"
        preschema = open_json(finalfilename)
        properties = preschema[item]["properties"]
        # if there is no type we need one. mandatory
        if "type" not in properties:
            properties["type"] = {
                "type": "string",
                "description": "Property. NGSI entity type. It has to be " + item,
                "enum": [item]
            }
        # remove id to not have a conflict with actual id of NGSI. id is included in the schemaHeader
        if "id" in properties:
            del properties["id"]
        for prop in properties:
            if "description" in properties[prop]:
                properties[prop]["description"] = "Property. " + properties[prop]["description"].replace(chr(34), "").replace(chr(39), "")
            else:
                properties[prop]["description"] = "Property. Not described in HL7 original"
            if "const" in properties[prop]:
                properties[prop]["type"] = "string"
                properties[prop]["enum"] = [properties[prop]["const"]]
                del properties[prop]["const"]
        description = preschema[item]["description"]
        finalSchema = copy.deepcopy(schemaHeader)
        finalSchema["$id"] = finalSchema["$id"].replace("XXXX", item)
        finalSchema["description"] = description
        finalSchema["title"] += item + " data model based on HL7 equivalent"
        finalSchema["allOf"].append({"properties": properties})
        with open("./" + item + "/" + "schema.json", "w+") as outfile:
            rawOutput = json.dumps(finalSchema, indent=4).replace(">=", chr(39) + ">=" + chr(39))
            outfile.write(rawOutput)
