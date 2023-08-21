import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
df = pd.read_csv('prices.csv')
reg = linear_model.LinearRegression()

reg.fit(df[['area']].values,df[['prices']])
print(reg.predict([[3300]]))
