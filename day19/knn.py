import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

filedata = pd.read_csv("moviedataset.csv")

x = filedata.drop("genre",axis=1)
y = filedata["genre"]

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=30)

scalar = StandardScaler()
xtrain_scaled = scalar.fit_transform(xtrain)
xtest_scaled = scalar.transform(xtest)

kclassifier = KNeighborsClassifier(n_neighbors=3)
kclassifier.fit(xtrain_scaled,ytrain)

prediction = kclassifier.predict(xtest_scaled)

accuracy = accuracy_score(ytest,prediction)
print("accuracy : ",accuracy)

newdata = np.array([[75,8.3]])

newscaleddata = scalar.transform(newdata)

newpredection = kclassifier.predict(newscaleddata)
print(newpredection)
