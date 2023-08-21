import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
df = pd.read_csv('orderdata.csv')
reg = linear_model.LinearRegression()

reg.fit(df[['users','orders','age']].values,df[['amount']])
print(reg.predict([[1700,3400,23]]))
