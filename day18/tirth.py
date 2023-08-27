import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

file_data = pd.read_csv("titanic.csv")
file_data.dropna(inplace=True)

file_data['Fare'] = file_data['Fare'].fillna(file_data['Fare'].dropna().median())
file_data['Age'] = file_data['Age'].fillna(file_data['Age'].dropna().median())
# Change to categoric column to numeric
file_data.loc[file_data['Sex']=='male','Sex']=0
file_data.loc[file_data['Sex']=='female','Sex']=1
# instead of nan values
file_data['Embarked']=file_data['Embarked'].fillna('S')
# Change to categoric column to numeric
file_data.loc[file_data['Embarked']=='S','Embarked']=0
file_data.loc[file_data['Embarked']=='C','Embarked']=1
file_data.loc[file_data['Embarked']=='Q','Embarked']=2

X = file_data[["Pclass","SibSp","Parch","Age","Fare","Embarked","Sex"]]
# print(X)
y = file_data["Survived"]
#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
rf_classifier = RandomForestClassifier(n_estimators=100)

rf_classifier.fit(X_train, y_train)
y_pred = rf_classifier.predict(X_test)

accuracyscore = accuracy_score(y_test, y_pred)
print(accuracyscore)