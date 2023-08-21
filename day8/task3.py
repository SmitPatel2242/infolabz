import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)

userinput = input("Cricketer Name : ")
col = sheet.ncols
row = sheet.nrows
for i in range(0,col):
    if userinput == sheet.cell_value(0,i):
        crickter=i
        break
print("score of ",sheet.cell_value(0,crickter))

for i in range(1,row):

    print(sheet.cell_value(i,crickter))