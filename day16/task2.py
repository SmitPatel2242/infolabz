import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
df = pd.read_csv('car.csv')
reg = linear_model.LinearRegression()

reg.fit(df[['carage']].values,df[['price']])
print(reg.predict([[14]]))
