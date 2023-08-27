import pandas as pd

result1 = pd.read_excel("C:/Users/smitp/Desktop/Infolabz/day10/RESULT1.xlsx")
result2 = pd.read_excel("C:/Users/smitp/Desktop/Infolabz/day10/RESULT2.xlsx")
full = pd.concat([result1,result2])
# print(full[["NAME"]].sort_values(["NAME"]))

######if you want to hide index
# print(full[["NAME"]].sort_values(["NAME"]).to_string(index=False))
##task2
# full.sort_values(["TOTAL"],ascending=False).to_excel("matrix.xlsx",index=False)

