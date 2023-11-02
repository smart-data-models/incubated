import os
import json
import xml.etree.ElementTree as ET

mytree = ET.parse('ontology.rdf')
myroot = mytree.getroot()

datatypes = set()
for element in myroot:
    if element.tag == "{http://www.w3.org/2002/07/owl#}ObjectProperty":
        print(element.attrib)
        print("______________________________")
        for item in element:
            print(item)
            print(item.tag)
            print(item.attrib)
            if item.tag == "{http://www.w3.org/2000/01/rdf-schema#}range":
                datatypes.add(list((item.attrib).values())[0])
print("______________________________")
print(datatypes)