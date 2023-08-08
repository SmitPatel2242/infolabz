import xlrd

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)
max =0

row = sheet.nrows
col = sheet.ncols
for i in range(1,row):
    print("Match ",i)
    for j in range(1,col):
        print("score of ",sheet.cell_value(0,j)," ",sheet.cell_value(i,j))
