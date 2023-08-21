# import pandas as pd
#
# #print all data with total greater than 2000
#
# file1=pd.read_excel("RESULT1.xlsx")
# file2=pd.read_excel("RESULT2.xlsx")
#
# alldata=pd.concat([file1,file2])
# total=[]
# for i in alldata["TOTAL"]:
#     if i>200:
#        total.append(i)
#
# print(total)

import pandas as pd

#print all data with total greater than 2000

file1=pd.read_excel("RESULT1.xlsx")
file2=pd.read_excel("RESULT2.xlsx")

alldata=pd.concat([file1,file2])
name=[]
total=[]
s_total=[]
s_name=[]
for i in alldata["NAME"]:
    name.append(i)

for i in alldata["TOTAL"]:
    total.append(i)

for i in range(0,len(total)):
    if total[i]>200:
        s_total.append(total[i])
        s_name.append(name[i])

for i in range(0,len(s_total)):
    print(s_name[i]," : ",s_total[i])