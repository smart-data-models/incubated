import csv
import xlrd
from xlrd.sheet import ctype_text


fileNameEDI = "All_EDI_EPCIS_CVP_and_Shared_Code_Lists_June2019.xlsx"
fileNameGDSN = "GDSN_and_Shared_Code_Lists_3p1p11_1_Dec_11_2019(1).xlsx"

# Give the location of the file

# To open Workbook
wb = xlrd.open_workbook(fileNameEDI)
sheet = wb.sheet_by_index(0)
row = sheet.row(0)
# For row 0 and column 0
# print(sheet.cell_value(0, 0))
maxRows = 2
for index in range(0, maxRows):
    row = sheet.row(index)
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        print('(%s) %s %s' % (idx, cell_type_str, cell_obj.value))
