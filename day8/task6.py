import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)


col = sheet.ncols
row = sheet.nrows
matches=[]
run=0
maximum=0

for i in range(1,col):
    for j in range(1,row):
        if maximum<sheet.cell_value(j,i):
            maximum=sheet.cell_value(j,i)
            run=1
    if run == 1:
        matches.append(maximum)
        maximum = 0

for i in range(0,len(matches)):
    print("Maximum Score of",sheet.cell_value(0,i+1),"is",matches[i])

print("Overall Max : ",max(matches))
