import pandas as pd
import json
import requests
#import dpath.util
import string
import random
import datetime
from datetime import datetime
import rstr

json_data = {}
properties = {}
depth= 0
entity_type = 'Patient'
entity_property = ''
letters = string.ascii_uppercase
now = datetime.now()

def open_json(fileUrl):
    '''Opens a JSON file or an HTTP link that contains JSON data and parses it into a Python dictionary.
    
    Parameters:
        fileUrl (str): A string that contains the URL of a JSON file or an HTTP link that returns JSON data. If the string starts with "http", it is assumed to be an HTTP URL and the requests library is used to retrieve the contents of the URL as a string. Otherwise, it is assumed to be a local file path and the open() function is used to open the file in read mode ("r").
    
    Returns:
        A Python dictionary that contains the JSON data parsed from the specified file or URL. If an error occurs while opening or reading the file, such as a file not found error or a permission denied error, the function returns None.
    '''

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

def generatestring(data):
    '''Generates a random string based on the input data.
    
    Parameters:
        data (dict): A dictionary containing information about the desired output string. The dictionary can have the following keys:
            * 'minLength' (int): The minimum length of the generated string.
            * 'maxLength' (int): The maximum length of the generated string.
            * 'enum' (list): A list of strings that the function should pick from as its output. If this key is present, the function will return a random element from the list instead of generating a string.
            * 'pattern' (str): A regular expression pattern that the function should use to generate the string. The function will use the re module to match the pattern against a random string.
            * 'format' (str): The format of the output string. Currently supported formats are 'date-time' and 'date'. If this key is present, the function will generate a string in the specified format instead of generating a random string.
    
    Returns:
        A random string based on the input data.
    '''
    print('get in generatestring data:', data)
    if 'minLength' in data.keys():
        minLength = data['minLength']
    else:
        minLength = 5

    maxLength = 16
    if 'maxLength' in data.keys():
        if data['maxLength'] < 16:
            maxLength = data['maxLength'] 
    
    if 'enum' in data.keys():
        outstring = random.choice(data['enum'])
    elif 'pattern' in data.keys():
        outstring = entity_type + ' ' + entity_property + ' value'  #+ rstr.xeger(data['pattern'])
    elif 'format' in data.keys():
        if data['format'] == 'date-time':
            outstring = now.strftime("%Y-%m-%d %H:%M:%S")
        elif data['format'] == 'date':
            outstring = now.strftime("%Y-%m-%d")
        elif data['format'] == 'uri':
            outstring = now.strftime("%Y-%m-%d")
        else:
            print('Unknown format',data['format'])
    else:
        outstring = entity_type + ' ' + entity_property + ''.join(random.choice(letters) for i in range(minLength,maxLength))
    print('out generatestring: ', outstring)    
    return outstring

def generatenumber(data):
    '''Generates a random number based on the input data.
    
    Parameters:
        data (dict): A dictionary containing information about the desired output number. The dictionary can have the following keys:
            * 'enum' (list): A list of numbers that the function should pick from as its output. If this key is present, the function will return a random element from the list instead of generating a number.
            * 'format' (str): The format of the output number. Currently supported formats are 'float', 'double', and 'int'. If this key is present, the function will generate a number in the specified format instead of generating a random number.
    
    Returns:
        A random number based on the input data.
    '''
    print('generatenumber data:', data)
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

    depth = 0
    print('out generatestring: ', outnumber)  
    return outnumber

def generateinteger(data):
    '''Generates a random integer based on the input data.
    
    Parameters:
        data (dict): The input data that determines the range of the generated integer.
            It should contain the following keys:
                - multipleOf (int, optional): The multiple of the generated integer.
                    Defaults to 1.
                - minimum (int, optional): The minimum value of the generated integer.
                    Defaults to 100000 if not specified.
                - maximum (int, optional): The maximum value of the generated integer.
                    Defaults to 9000000 if not specified.
                - format (str, optional): The format of the generated integer. It should be either 'int32' or 'int64'.
                    Defaults to 'int64' if not specified.
                - enum (list of ints, optional): A list of allowed values for the generated integer.
                    If this key is present, the generated integer will be one of the values in the list.
                    Defaults to None if not specified.
            
    Returns:
        The generated random integer.
    '''
    print('generateinteger data:', data)
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
    
    depth = 0
    print('out generateinteger: ', outinteger)
    return outinteger
    
def generatevalue(data,outdict,depth):
    '''Generates a random value based on the input data.
    
    Parameters:
        data (dict): The input data that determines the structure and range of the generated value.
            It should contain the following keys:
                - type (str, optional): The type of the generated value. It should be either 'string', 'boolean', 'number', 'integer', or 'object'.
                    Defaults to 'object' if not specified.
                - properties (dict, optional): A dictionary containing the structure and range of the generated object.
                    If this key is present, the generated value will be an object with the specified properties.
                    Defaults to None if not specified.
                - items (dict, optional): A dictionary containing the structure and range of the generated array.
                    If this key is present, the generated value will be an array with the specified items.
                    Defaults to None if not specified.
            
        outdict (dict): The output dictionary where the generated value will be stored.

    Returns:
        A list of dictionaries containing the generated values.

    Raises:
        ValueError: If the input data is invalid or contains unknown keys.
        TypeError: If the input data is not a dictionary.

    '''

    outlist = []
    for key,value in data.items():
        print('>>>>>>>>>>process property with key: <', key,'>')
        if depth == 0:
            entity_property = key
        # print('>>>>>>>>>> value: ', value)
        # print('>>>>>>>>>> data[key]: ', data[key])
        if 'type' in data[key].keys() and data[key]['type'] != 'object':
            if data[key]['type'] == 'string':
                outdict[key] = generatestring(data[key])
            elif data[key]['type'] == 'boolean':
                outdict[key] = random.choice([True, False])
            elif data[key]['type'] == 'number':
                outdict[key] = generatenumber(data[key])
            elif data[key]['type'] == 'integer':
                outdict[key] = generateinteger(data[key])
            # elif data[key]['type'] == 'object':
            #     arraydict = {}
            #     arrayproperties = data[key]['properties']
            #     outdict[key] = generatevalue(arrayproperties,arraydict)
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
                        outdict[key] = generatevalue(arrayproperties,arraydict,depth)
                    else:
                        print('Unknown format',data[key]['format'],'for property',key) 
                elif '$ref' in data[key]['items'].keys():
                    arraypath = data[key]['items']['$ref'].split('/')
                    arraydict = {}
                    arraydictobj = {}
                    print('>>>>>>>>>>[] find $ref definition for item ', arraypath[len(arraypath)-1])
                    if 'properties' in base_defs[arraypath[len(arraypath)-1]].keys():
                        ref_properties = {key: base_defs[arraypath[len(arraypath)-1]]['properties']}
                    else:
                        ref_properties = {key: base_defs[arraypath[len(arraypath)-1]]}

                    arraydictobj[key] = generatevalue(ref_properties,arraydict, depth)
                    arrayofdict.append(arraydictobj)    
                else:
                    print('Unknown array property !: ',data[key]['type'],' for property ',key)
            else:
                print('Unknown type ',data[key]['type'],' for property ',key)
        elif '$ref' in data[key].keys():
            refpath = data[key]['$ref'].split('/')
            refdict = {}
            refList = []
            print('>>>>>>>>>> find $ref definition for ', refpath[len(refpath)-1])
            if 'properties' in base_defs[refpath[len(refpath)-1]].keys():
                ref_properties = {key: base_defs[refpath[len(refpath)-1]]['properties']}
            else:
                ref_properties = {key: base_defs[refpath[len(refpath)-1]]}

            print ('ref_properties: ', ref_properties)
            depth += 1
            print('DDDDDDDDDDDDDD depth: ', depth)

            refList = generatevalue(ref_properties,refdict,depth)
            outdict[key] = refList[0]

    outlist.append(outdict)
    return outlist

# main part:

filename = './Patient/schema.json'
schemafile = open(filename)
jsondata = json.load(schemafile)
dictobj = {}
initobj = {}
arrayofdict = []
finaldict = {}
depth = 0

key = 'definitions'
if not jsondata.get(key,None) and jsondata.get('allOf',None):
    key = 'allOf'

index = -1
def_urls = []
for i, elem in enumerate(jsondata[key]):
    if elem.get('properties', None):
        index = i
        #break
    if elem.get('$ref'):
        def_urls.append(elem['$ref'])

if index > -1:    
    properties = jsondata[key][index]['properties']
else:
    print('no property found ')

# we need to get definitions from referenced files in "$ref"
base_defs={}
for url in def_urls:
    print('get file for url: ' + url)
    definitions_properties = open_json(url)
    print('definitions_properties is: ', type(definitions_properties))
    # print(definitions_properties)

    if definitions_properties.get('definitions', None):
        base_defs.update(definitions_properties['definitions'])
        print('base_defs is updated !!!')



dictobj["root"] = generatevalue(properties,initobj,depth)
arrayofdict.append(dictobj)

for obj in arrayofdict:
    if 'root' in obj.keys():
        for key,value in obj["root"][0].items():
            finaldict[key] = value
    else:
        for key,value in obj.items():
            finaldict[key] = value
# write output json file
with open('Patient.json', 'w') as f:
    json.dump(finaldict, f, indent=4, separators=(", ", ": "))

