import xlrd

workbook = xlrd.open_workbook("mydata.xlsx")
sheet = workbook.sheet_by_index(0)