import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)


col = sheet.ncols
row = sheet.nrows
matches=[]
run=0
max=0

for i in range(1,row):
    for j in range(1,col):
        if max<sheet.cell_value(i,j):
            max=sheet.cell_value(i,j)
            run=1
    if run == 1:
        matches.append(max)
        max = 0

print(matches)
for i in range(0,len(matches)):
    print("Match ",i+1," Max Score is ",matches[i])