import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

filedata = pd.read_csv("diabetes.csv")

x= filedata.drop("Outcome",axis=1)
y= filedata["Outcome"]

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)
rfclassifier = RandomForestClassifier(n_estimators=100,random_state=42)
rfclassifier.fit(xtrain,ytrain)
predections = rfclassifier.predict(xtest)

accuracy = accuracy_score(ytest,predections)
print(accuracy)