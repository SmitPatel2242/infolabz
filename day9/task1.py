import xlrd

path = ("day9/mydata.xlsx")
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

row = sheet.nrows
col = sheet.ncols
flag=0

score = input("Enter Score : ")
for i in range(1,row):
    for j in range(1,col):
        if float(score)==sheet.cell_value(i,j):
            print("match no : ",sheet.cell_value(i,0))
            print("Name : ",sheet.cell_value(0,j))
            flag=1

if flag==0:
    print("Score not found")