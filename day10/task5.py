import pandas as pd
path1=pd.read_excel("RESULT1.xlsx")
path2=pd.read_excel("RESULT2.xlsx")
alldata=pd.concat([path1,path2])
Name=[]
Category=[]
Percentage=[]
s_name=[]
s_percentage=[]
for i in alldata["PERCENTAGE"]:
    Percentage.append(i)
for i in alldata["NAME"]:
    Name.append(i)

for i in range(len(Percentage)):
    if (Percentage[i]>=80 and Percentage[i]<=100):
        s_name.append(Name[i])
        Category.append("SCHOLER")
        s_percentage.append(Percentage[i])
    if (Percentage[i]>=50 and Percentage[i]<=79):
        s_name.append(alldata["NAME"])
        Category.append("AVERAGE")
        s_percentage.append(Percentage[i])

    if (Percentage[i]>=0 and Percentage[i]<=49):
        s_name.append(alldata["NAME"])
        Category.append("WEAK")
        s_percentage.append(Percentage[i])

data={
    "NAME":Name,
    "PERCENTAGE":Percentage,
    "CATEGORY":Category
}

pd.DataFrame(data).to_excel("result.xlsx")