from rdflib import Graph
from pprint import pprint
import json
import os

# Create a Graph
g = Graph()

# Parse the TTL file
g.parse("mandate.ttl", format="turtle")
attributes_object = {}
# pprint(g)
for element in g:
    print(element)


outputDirectory = "./dataModel.Mandate"
attributes = []
for subj, pred, obj in g:
    if str(obj) == "http://www.w3.org/2002/07/owl#DatatypeProperty":
        attribute = str(subj).split("#")[1]
        attributes.append(attribute)
        print(attribute)










# for element in myroot:
#     if element.tag == "{http://www.w3.org/2002/07/owl#}DatatypeProperty":
#         print()
#         source_attribute = element.attrib
#         key = list(source_attribute.keys())[0]
#         attributeName = source_attribute[key].split("/")[-1]
#         print(source_attribute)
#         print(attributeName)
#
#         attributes_object[attributeName] = {}
#         print("_________________________________")
#         print(element.tag)
#         datatype = ""
#         description = ""
#         string_format = ""
#         entities = []
#
#         for item in element:
#             print(item)
#             print(item.tag)
#             # gets the description
#             if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}label":
#                 description = item.text
#             # gets the data type
#             if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}range":
#                 sourcetype = list(item.attrib.values())[0]
#                 print(sourcetype)
#                 # a = input ("stop")
#                 if sourcetype in ["http://www.w3.org/2001/XMLSchema#string", "http://www.opengis.net/ont/geosparql#wktLiteral"]:
#                     datatype = "string"
#                 elif sourcetype == "http://www.w3.org/2001/XMLSchema#anyURI":
#                     datatype = "string"
#                     string_format = "uri"
#                     print("detected URI")
#                 elif sourcetype in ["http://www.w3.org/2001/XMLSchema#integer", "http://www.w3.org/2001/XMLSchema#int"]:
#                     datatype = "integer"
#                 elif sourcetype == "http://www.w3.org/2001/XMLSchema#boolean":
#                     datatype = "boolean"
#                 elif sourcetype == "http://www.w3.org/2001/XMLSchema#double":
#                     datatype = "number"
#                 elif sourcetype == "http://www.w3.org/2001/XMLSchema#date":
#                     datatype = "string"
#                     string_format = "date-time"
#                 else:
#                     datatype = "string"
#             # gets the entities where the attribute belongs to
#             if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}domain":
#                 print(item)
#                 complex_domain = False
#                 for subitem in item:
#                     complex_domain = True
#                     attributes_object[attributeName]["domains"] = []
#                     for subsubitem in subitem:
#                         for sub3item in subsubitem:
#                             source_domain = sub3item.attrib
#                             domain = list(source_domain.values())[0].split("/")[-1]
#                             print(domain)
#                             attributes_object[attributeName]["domains"].append(domain)
#                 if not complex_domain:
#                     attributes_object[attributeName]["domains"] = []
#                     source_domain = item.attrib
#                     print(source_domain)
#                     domain = list(source_domain.values())[0].split("/")[-1]
#                     attributes_object[attributeName]["domains"].append(domain)
#
#

                # a = input("stop")
#
#
#         if attributeName == "":
#             continue
#         else:
#             attributes_object[attributeName]["type"] = datatype
#             attributes_object[attributeName]["description"] = "Property. " + description
#             if string_format != "":
#                 attributes_object[attributeName]["format"] = string_format
#
#
# print("_______________***____________________")
# print(attributes_object)
# with open("attributes.json", "w") as file:
#     json.dump(attributes_object, file)
#
#
