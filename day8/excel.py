import xlrd

#if error will occur
# xlrd.xlsx.ensure_elementtree_imported(False.None)
# xlrd.xlsx.Element_has_iter = True

filelocation = ("mydata.xlsx")
openbook = xlrd.open_workbook(filelocation)
sheet = openbook.sheet_by_index(0)

print(sheet)
print(sheet.cell_value(1,3))
print("Total rows : ",sheet.nrows)
print("Total cols : ",sheet.ncols)