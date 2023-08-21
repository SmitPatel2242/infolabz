
# import pandas as pd
#
# #print all data with total less than 100
#
# file1=pd.read_excel("RESULT1.xlsx")
# file2=pd.read_excel("RESULT2.xlsx")
#
# alldata=pd.concat([file1,file2])
# name=[]
# total=[]
# totally={
# "s_total":[],
# "s_name":[]
# }
# for i in alldata["NAME"]:
#     name.append(i)
#
# for i in alldata["TOTAL"]:
#     total.append(i)
#
# for i in range(0,len(total)):
#     if total[i]<100:
#         totally["s_total"].append(total[i])
#         totally["s_name"].append(name[i])
#
# totally.to_excel("matrix.xlsx")
#
#



#
import pandas as pd

#print all data with total greater than 2000

file1=pd.read_excel("RESULT1.xlsx")
file2=pd.read_excel("RESULT2.xlsx")

alldata=pd.concat([file1,file2])
name=[]
s_name=[]
total=[]
s_total=[]
srno=[]
s_srno=[]
branch=[]
s_branch=[]
percentage=[]
s_percentage=[]
passfail=[]
s_passfail=[]
for i in alldata["SRNO"]:
    srno.append(i)

# for i in alldata["BRANCH"]:
#     branch.append(i)

for i in alldata["NAME"]:
    name.append(i)

for i in alldata["TOTAL"]:
    total.append(i)

for i in alldata["PERCENTAGE"]:
    percentage.append(i)

for i in alldata["PASSFAIL"]:
    passfail.append(i)

for i in range(0,len(total)):
    if total[i]<100:
        s_srno.append(srno[i])
        # s_branch.append(branch[i])
        s_name.append(name[i])
        s_total.append(total[i])
        s_percentage.append(percentage[i])
        s_passfail.append(passfail[i])
data = {
    "srno":s_srno,
    # "Branch":s_branch,
    "Name":s_name,
    "Total":s_total,
    "Percentage":s_percentage,
    "PassFail":s_passfail
}
pd.DataFrame(data).to_excel("weakstudents.xlsx")



