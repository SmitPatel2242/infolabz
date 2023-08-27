import pandas as pd
from sklearn import linear_model

df = pd.read_csv("modified_ipl.csv")
reg = linear_model.LinearRegression()

reg.fit(df[["total_runs"]],df[["overs_balls"]])
print(reg.predict([[50]]))
