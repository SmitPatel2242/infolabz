import xlrd

path = ("mydata.xlsx")
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

row = sheet.nrows
col = sheet.ncols
flag=0
flag1=0

name = input("Enter name : ")
index1=0
index2=0
m_no = int(input("Enter match no : "))
for i in range(0,row):
    for j in range(0,col):
        if name==sheet.cell_value(0,j):
            index1=j
            flag=1
            break
for i in range(0, row):
    for j in range(0, col):
        if m_no == sheet.cell_value(i,0):
            index2 = i
            flag1=1
            break
if(flag==0 or flag1==0):
    print("not found")
    exit()

print("score : ",sheet.cell_value(index2,index1))


