import xlrd

path = ("mydata.xlsx")
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

row = sheet.nrows
col = sheet.ncols
index=0
flag=0

m_no = int(input("Enter match no : "))
for i in range(0, row):
    for j in range(0, col):
        if m_no == sheet.cell_value(i,0):
            index = i
            flag=1
            break
if(flag==0):
    print("Match no is invalid")
    exit()

for j in range(1, col):
    print("Score of ",sheet.cell_value(0,j)," is ",sheet.cell_value(index,j))



