# program for conversion of codes
import xlrd
from xlrd.sheet import ctype_text
import json

fileNameEDI = "All_EDI_EPCIS_CVP_and_Shared_Code_Lists_June2019.xlsx"
fileNameGDSN = "GDSN_and_Shared_Code_Lists_3p1p11_1_Dec_11_2019(1).xlsx"
outputFile = "GDSNCodes.json"

# To open Workbook
workBook = xlrd.open_workbook(fileNameGDSN)
sheet = workBook.sheet_by_index(1)
numRows = sheet.nrows
terms = []

keys = []
listStart = True
for index in range(numRows):
    row = sheet.row(index)
    if index == 0:
        # print("keys")
        # print(type(row))
        # print(row)
        for idx, cell_obj in enumerate(row):
            keys.append(cell_obj.value)
        # print(keys)
        # a = input("para")
    else:
        payload = []
        print("payload")
        print(row)
        # print(type(row))
        for idx, cell_obj in enumerate(row):
            payload.append(cell_obj.value)
        print(payload)
        element = dict(zip(keys, payload))
        print(element)
        if element["resourceSubTypeCode"] == "CODELIST":
            if listStart == True:
                nada = 0
            else:
                terms.append(listElement)
            listElement = {}
            listElement["listName"] = element["Code List"]
            listElement["items"] = []
            listStart = True
        elif element["resourceSubTypeCode"] == "CODEVALUE":
            listStart = False
            listElement["items"].append(element)
        else:
            print("weird element")

print("*** terms ***")
print(terms)
print("--- terms ---")

with open(outputFile, 'w') as file:
    file.write(json.dumps(terms))
