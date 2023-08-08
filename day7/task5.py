import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)

userinput = input("Cricketer Name : ")
col = sheet.ncols
row = sheet.nrows
max=0
for i in range(0,col):
    if userinput == sheet.cell_value(0,i):
        crickter=i
        break
print("score of ",sheet.cell_value(0,crickter))

for i in range(1,row):

    if max<sheet.cell_value(i,crickter):
        max=sheet.cell_value(i,crickter)

print(max)