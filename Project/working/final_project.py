import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import Ridge

runs = []
id = []
total=[]
bat_team="Chennai Super Kings"
ball_team="Kolkata Knight Riders"

df = pd.read_csv("ipl_data_cleaned.csv")
df = df[df["innings"]==1]

total_score=df.groupby(["id","innings"])['total_runs'].sum().reset_index()

for index,raw in total_score.iterrows():
    runs.append(raw["total_runs"])
    id.append(raw["id"])

j=0

for index,raw in df.iterrows():
    if(id[j] != raw["id"]):
        j=j+1
    if(id[j]==raw["id"]):
        total.append(runs[j])

df["total"]=total
df.to_csv("sp.csv")

df=df[['venue', 'batting_team', 'bowling_team','overs_balls','total_runs','is_wkt_delivery','total']]
df.to_csv("sp.csv",index=False)
encode_data = pd.get_dummies(data=df,columns=['batting_team', 'bowling_team'])

# x = df.drop(['total'],axis=1).values
# y = df['total'].values
x = encode_data.drop(['venue', 'total_runs','is_wkt_delivery', 'total'],axis=1).values
y = encode_data['total'].values
xtrain, xtest, ytrain,ytest = train_test_split(x, y,test_size=0.2,random_state=42)


######### linier regrission     ##############

reg = linear_model.LinearRegression()
batt_team="batting_team_"+bat_team
balll_team="bowling_team_"+ball_team
# print(bat_team,"  ",ball_team)
# # # x = encode_data[bat_team,ball_team,'total_runs']
# # # y = encode_data['total']
# reg.fit(encode_data[[batt_team,balll_team]].values,encode_data[['total']])
# reg.predict([[batt_team,balll_team]])
reg.fit(xtrain,ytrain)
print(reg.predict(xtest))
#######Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(xtrain,ytrain)
print("ridge")
print(ridge.predict(xtest))
print("ytest")
print(ytest)