import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)

col = sheet.ncols
row = sheet.nrows

userinput = input("Cricketer Name : ")

for i in range(0,col):
    if userinput == sheet.cell_value(0,i):
        print("found")
        break
else:
    print("not found")