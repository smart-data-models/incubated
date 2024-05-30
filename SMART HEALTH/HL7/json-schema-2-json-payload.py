import pandas as pd
import json
import dpath.util
import string
import random
import datetime
from datetime import datetime
import rstr

def generatestring(data):

    if 'minLength' in data.keys():
        minLength = data['minLength']
    else:
        minLength = 5

    if 'maxLength' in data.keys():
        maxLength = data['maxLength']
    else:
        maxLength = 25
    
    if 'enum' in data.keys():
        outstring = random.choice(data['enum'])
    elif 'pattern' in data.keys():
        outstring = rstr.xeger(data['pattern'])
    elif 'format' in data.keys():
        if data['format'] == 'date-time':
            outstring = now.strftime("%Y-%m-%d %H:%M:%S")
        elif data['format'] == 'date':
            outstring = now.strftime("%Y-%m-%d")
        else:
            print('Unknown format',data['format'])
    else:
        outstring = ''.join(random.choice(letters) for i in range(minLength,maxLength))
        
    return outstring

def generatenumber(data):

    if 'enum' in data.keys():
        outnumber = random.choice(data['enum'])  
    elif 'format' in data.keys():
        if data['format'] in ('float','double'):
            outnumber = random.random()
            #outdict[key] = random.uniform(10.5, 75.5)  Returns value within a range
        else:
            print('Unknown format',data['format'])
    else:
        outnumber = random.random()
        
    return outnumber

def generateinteger(data):

    if 'multipleOf' in data.keys():
        multipleOf = data['multipleOf']
    else:
        multipleOf = 1
        
    if 'minimum' in data.keys():
        int32minimum = data['minimum'] / multipleOf
        int64minimum = data['minimum'] / multipleOf
    else:
        int32minimum = 100000
        int64minimum = 10000000000
        
    if 'maximum' in data.keys():
        int32maximum = data['maximum'] / multipleOf
        int64maximum = data['maximum'] / multipleOf
    else:
        int32maximum = 9000000
        int64maximum = 500000000000

    if 'enum' in data.keys():
        outinteger = random.choice(data['enum'])    
    elif 'format' in data.keys():
        if data['format'] =='int32':
            outinteger = random.randint(int32minimum,int32maximum) * multipleOf
        elif data['format'] =='int64':
            outinteger = random.randint(int64minimum,int64maximum) * multipleOf
        else:
            print('Unknown format',data['format'])
    else:
        outinteger = random.randint(int64minimum,int64maximum) * multipleOf

    return outinteger
    
def generatevalue(data,outdict):
    outlist = []
    for key,value in data.items():
        if 'type' in data[key].keys():
            if data[key]['type'] == 'string':
                outdict[key] = generatestring(data[key])
            elif data[key]['type'] == 'boolean':
                outdict[key] = random.choice([True, False])
            elif data[key]['type'] == 'number':
                outdict[key] = generatenumber(data[key])
            elif data[key]['type'] == 'integer':
                outdict[key] = generateinteger(data[key])
            elif data[key]['type'] == 'array':
                if 'minItems' in data[key]:
                    minItems = data[key]['minItems']
                else:
                    minItems = 1
                if 'maxItems' in data[key]:
                    maxItems = data[key]['maxItems']
                else:
                    maxItems = 3
                if maxItems <= minItems:
                    maxItems = minItems + 1
                arrayItems = random.randint(minItems,maxItems)
                if 'type' in data[key]['items'].keys():
                    array = []
                    if data[key]['items']['type'] == 'string':
                        for n in range(0,arrayItems):
                            arrayproperty = generatestring(data[key]['items'])
                            array.append(arrayproperty)
                        outdict[key] = array
                    elif data[key]['items']['type'] == 'integer':
                        for n in range(0,arrayItems):
                            arrayproperty = generateinteger(data[key]['items'])
                            array.append(arrayproperty)
                        outdict[key] = array
                    elif data[key]['items']['type'] == 'number':
                        for n in range(0,arrayItems):
                            arrayproperty = generatenumber(data[key]['items'])
                            array.append(arrayproperty)
                        outdict[key] = array
                    elif data[key]['items']['type'] == 'object':
                        arraydict = {}
                        arrayproperties = data[key]['items']['properties']
                        outdict[key] = generatevalue(arrayproperties,arraydict)
                    else:
                        print('Unknown format',data[key]['format'],'for property',key) 
                elif '$ref' in data[key]['items'].keys():
                    arraypath = data[key]['items']['$ref'].split('/')
                    arraydict = {}
                    arraydictobj = {}
                    arrayproperties = jsondata['allOf'][index]['properties']
                    arraydictobj[key] = generatevalue(arrayproperties,arraydict)
                    arrayofdict.append(arraydictobj)    
                else:
                    print('Unknown array property',data[key]['type'],'for property',key)
            else:
                print('Unknown type',data[key]['type'],'for property',key)
        elif '$ref' in data[key].keys():
            refpath = data[key]['$ref'].split('/')
            refdict = {}
            refList = []
            refproperties = jsondata['definitions'][refpath[2]]['properties']
            refList = generatevalue(refproperties,refdict)
            outdict[key] = refList[0]

    outlist.append(outdict)
    return outlist

# main part:
letters = string.ascii_uppercase
now = datetime.now()

filename = './Patient/schema.json'
schemafile = open(filename)
jsondata = json.load(schemafile)
dictobj = {}
initobj = {}
arrayofdict = []
finaldict = {}

key = 'definitions'
if not jsondata.get(key,None) and jsondata.get('allOf',None):
    key = 'allOf'

index = -1
for i, elem in enumerate(jsondata[key]):
    if elem.get('properties', None):
        index = i
        break
        
if index > -1:    
    properties = jsondata[key][index]['properties']
else:
    print('no property found ')

dictobj["root"] = generatevalue(properties,initobj)
arrayofdict.append(dictobj)

for obj in arrayofdict:
    if 'root' in obj.keys():
        for key,value in obj["root"][0].items():
            finaldict[key] = value
    else:
        for key,value in obj.items():
            finaldict[key] = value

with open('Patient.json', 'w') as f:
    json.dump(finaldict, f)

