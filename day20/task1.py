import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import numpy as np

filedata = pd.read_csv("houseprice.csv")
x = filedata.drop(["Location","Price"], axis=1)
y = filedata["Price"]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
ridgemodel = Ridge (alpha=1.0)
ridgemodel.fit(xtrain, ytrain)
prediction = ridgemodel.predict(xtest)
print (prediction)

i = np.array([[1520,3,1998]])
print(ridgemodel.predict(i))