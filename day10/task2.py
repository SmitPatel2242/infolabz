import pandas as pd

#generate merit ( topper list ) and store it in matrix.xlsx file

file1=pd.read_excel("RESULT1.xlsx")
file2=pd.read_excel("RESULT2.xlsx")

alldata=pd.concat([file1,file2])

(alldata.sort_values("TOTAL",ascending=False)).to_excel("matrix.xlsx")