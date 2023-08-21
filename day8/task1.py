import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)
print(sheet.cell_value(2,1))
print(sheet.cell_value(5,3))
print(sheet.cell_value(0,3))
print(sheet.cell_value(4,2))
print(sheet.cell_value(7,3))
col = sheet.ncols
for i in range(1,col):
        print(sheet.cell_value(0,i))





