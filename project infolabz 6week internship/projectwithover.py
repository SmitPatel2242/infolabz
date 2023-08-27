
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

bat_team=input("Enter Batting Team : ")
ball_team=input("Enter Balling Team : ")
venue = input("Enter Venue : ")
overs = float(input("Enter Over : "))
runs_last5 = int(input("Enter last 5 over run : "))
wickets_last5 = int(input("Enter last 5 over wicket : "))

# bat_team='Kings XI Punjab'
# ball_team='Chennai Super Kings'
# venue = 'Punjab Cricket Association Stadium, Mohali'
# overs = 9.4
# runs_last5 = 63
# wickets_last5 = 0

actual_value=0
data = pd.read_csv("match_data.csv")

data = data.drop(['mid','innings','batsman','bowler','runs_per_ball','wickets','date'],axis=1)
encode_data = pd.get_dummies(data=data,columns=['bat_team','bowl_team','venue'])

bat_team='bat_team_'+bat_team
ball_team='bowl_team_'+ball_team
venue='venue_'+venue
encode_data = encode_data[['overs',venue,bat_team,ball_team,'totalrun_last_5', 'wickets_last_5','total']]

xtrain, xtest, ytrain, ytest = train_test_split(encode_data.drop(['total'],axis=1).values,encode_data['total'].values,test_size=0.1,random_state=22,shuffle=True)

ridge = Ridge(alpha=1.0,random_state=22)
ridge.fit(xtrain,ytrain)
pridect=ridge.predict([[overs,1,1,1,runs_last5,wickets_last5]])
print("Pridected Score is",int(pridect[0]),"to",int(pridect[0])+30)
for index,raw in encode_data.iterrows():
    if(raw[bat_team]==1 and raw[ball_team] and raw[venue]):
        actual_value=raw['total']
        break

print("Actual Score is : ",actual_value)



