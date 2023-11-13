import os
import json
import xml.etree.ElementTree as ET

mytree = ET.parse('ontology.rdf')
myroot = mytree.getroot()

attributes_object = {}
for element in myroot:
    if element.tag == "{http://www.w3.org/2002/07/owl#}ObjectProperty":
        print()
        source_attribute = element.attrib
        key = list(source_attribute.keys())[0]
        attributeName = source_attribute[key].split("/")[-1]
        print(source_attribute)
        print(attributeName)

        attributes_object[attributeName] = {}
        print("_________________________________")
        print(element.tag)
        datatype = ""
        description = ""
        string_format = ""
        entities = []

        for item in element:
            print(item)
            print(item.tag)
            # gets the description
            if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}label":
                description = item.text
            # gets the data type
            if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}range":
                complex_range = False
                for subitem in item:
                    print("detected complex")
                    complex_range = True
                    attributes_object[attributeName]["type"] = []
                    for subsubitem in subitem:
                        for sub3item in subsubitem:
                            source_range = sub3item.attrib
                            detected_type = list(source_range.values())[0].split("/")[-1]
                            attributes_object[attributeName]["type"].append(detected_type)
                if not complex_range:
                    attributes_object[attributeName]["type"] = ""
                    source_range = item.attrib
                    print("source_range:" + str(source_range))
                    detected_type = list(source_range.values())[0].split("/")[-1]
                    print("list")
                    print(list(source_range.values())[0])
                    print("detected_type: " + str(detected_type))
                    attributes_object[attributeName]["type"] = "string"
                    attributes_object[attributeName]["format"] = "uri"
##############problem because there are some objects properties that can have different types. WTF!

            # gets the entities where the attribute belongs to
            if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}domain":
                print(item)
                complex_domain = False
                for subitem in item:
                    complex_domain = True
                    attributes_object[attributeName]["domains"] = []
                    for subsubitem in subitem:
                        for sub3item in subsubitem:
                            source_domain = sub3item.attrib
                            domain = list(source_domain.values())[0].split("/")[-1]
                            print(domain)
                            attributes_object[attributeName]["domains"].append(domain)
                if not complex_domain:
                    attributes_object[attributeName]["domains"] = []
                    source_domain = item.attrib
                    print(source_domain)
                    domain = list(source_domain.values())[0].split("/")[-1]
                    attributes_object[attributeName]["domains"].append(domain)



                # a = input("stop")


        if attributeName == "":
            continue
        else:
            attributes_object[attributeName]["description"] = "Relationship. " + description
            if string_format != "":
                attributes_object[attributeName]["format"] = string_format


print("_______________***____________________")
print(attributes_object)
with open("relations.json", "w") as file:
    json.dump(attributes_object, file, indent=4)


