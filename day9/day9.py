import pandas as pd

file1 = pd.read_excel("RESULT1.xlsx")
# print(file1)
file2 = pd.read_excel("RESULT2.xlsx")
# print(file2)

alldata = pd.concat([file1,file2])
# print(alldata)

print(alldata.head(3))
print(alldata.tail(3))
print(alldata.sort_values(["TOTAL"]))