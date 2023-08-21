import pandas as pd

#print all students name in alphabatical order

file1=pd.read_excel("RESULT1.xlsx")
file2=pd.read_excel("RESULT2.xlsx")

alldata=pd.concat([file1,file2])
srno=alldata["SRNO"].tolist()
alldata=alldata["NAME"].tolist()
print("SRNO   NAME")
for i in range(0,len(alldata)):
    print(srno[i],"    ",alldata[i])