# Basic Import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os
from datetime import datetime
import time

# Modelling
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle
import json

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/kaggle/input/ipl-complete-dataset-2008-2022/ipl_match_ball_by_ball_data.csv',low_memory=False)
print("-------- Match Dataset --------")
print("\nData Shape is :",df.shape)
print("\nShow Top 10 Records")
df.head(10)

#4
df_info = pd.read_csv('/kaggle/input/ipl-complete-dataset-2008-2022/ipl_match_info_data.csv')
print("-------- Match info --------")
print("\nData Shape is :",df_info.shape)
print("\nShow Top 10 Records")
df_info.head(10)

#5
print("-------- Match Dataset --------\n")
print(df.isna().sum())

#6
print("-------- Match info --------\n")
print(df_info.isna().sum())

#7
print("-------- Match Dataset --------")
df.info()

#8
print("-------- Match Dataset --------")
df.nunique()

#9
print("-------- Match Dataset --------")
# Define numerical & categorical columns
numeric_columns = [column for column in df.columns if df[column].dtype != 'O']
categorical_columns = [column for column in df.columns if df[column].dtype == 'O']

# print columns
print('We have {} numerical columns(features) : {}'.format(len(numeric_columns), numeric_columns))
print('\nWe have {} categorical columns(features) : {}'.format(len(categorical_columns), categorical_columns))

#10
print("-------- Match Dataset --------")
# for feature in df.columns :
#     if df[feature].dtype == 'O':
#         print('Categories in {} variable : {}'.format(feature,df[feature].unique()))
print("Batting Team Name: {}".format(df['batting_team'].nunique()))
print(df['batting_team'].unique())
print("\nBowling Team Name: {}".format(df['bowling_team'].nunique()))
print(df['bowling_team'].unique())

#11
# define a dictionary to map the values to be replaced with their corresponding replacements
replace_dict = {'Delhi Daredevils': 'Delhi Capitals','Deccan Chargers':'Sunrisers Hyderabad','Pune Warriors':'Rising Pune Supergiants','Rising Pune Supergiant':'Rising Pune Supergiants','Gujarat Lions':'Gujarat Titans','Kings XI Punjab':'Punjab Kings'}
## Match Dataset
df['batting_team'].replace(replace_dict,inplace=True)
df['bowling_team'].replace(replace_dict,inplace=True)
## Match info
df_info['team1'].replace(replace_dict,inplace=True)
df_info['team2'].replace(replace_dict,inplace=True)
df_info['toss_winner'].replace(replace_dict,inplace=True)
df_info['winner'].replace(replace_dict,inplace=True)

#12
# Define the mapping dictionary
short_name = {'Kolkata Knight Riders': 'KKR',
              'Royal Challengers Bangalore':'RCB',
              'Chennai Super Kings':'CSK',
              'Punjab Kings':'PBKS',
              'Rajasthan Royals':'RR',
              'Delhi Capitals':'DC',
              'Sunrisers Hyderabad':'SRH',
              'Mumbai Indians':'MI',
              'Kochi Tuskers Kerala':'KTK',
              'Rising Pune Supergiants':'RPSG',
              'Gujarat Titans':'GT',
              'Lucknow Super Giants':'LSG'}
# Map the values of batting_team column to shortnames
df['batting_team_short_name'] = df['batting_team'].map(short_name)

# Map the values of bowling_team column to shortnames
df['bowling_team_short_name'] = df['bowling_team'].map(short_name)

#13
## Match Dataset
# Rename column 'venue' to 'Stadium'
df = df.rename(columns={'venue': 'stadium'})
# Rename column 'ball' to 'over'
df = df.rename(columns={'ball': 'over'})

## Match info
# Rename column 'venue' to 'Stadium'
df_info = df_info.rename(columns={'venue': 'stadium'})

#14
print("stadium: {}".format(df['stadium'].nunique()))
print(df['stadium'].unique())

#15
venue_stadium = {'M Chinnaswamy Stadium':'Bengaluru',
         'Punjab Cricket Association Stadium, Mohali':'Mohali',
         'Feroz Shah Kotla':'Delhi',
         'Eden Gardens': 'Kolkata',
         'Wankhede Stadium' : 'Mumbai',
         'Sawai Mansingh Stadium': 'Jaipur',
         'Rajiv Gandhi International Stadium, Uppal':'Hyderabad',
         'MA Chidambaram Stadium, Chepauk': 'Chennai',
         'Dr DY Patil Sports Academy' : 'Mumbai',
         'Newlands': 'Cape Town, South Africa',
         "St George's Park" : 'Gqeberha, South Africa',
        'Kingsmead' : 'Durban, KwaZulu-Natal, South Africa',
        'SuperSport Park' : 'Centurion, South Africa',
         'Buffalo Park': 'East London, Eastern Cape, South Africa',
          'New Wanderers Stadium':'Johannesburg, South Africa',
         'De Beers Diamond Oval' : 'Kimberley, South Africa',
         'OUTsurance Oval': 'Bloemfontein, South Africa',
         'Brabourne Stadium':'Mumbai',
         'Brabourne Stadium, Mumbai':'Mumbai',
         'Sardar Patel Stadium, Motera':'Ahmedabad',
         'Barabati Stadium':'Cuttack',
         'Vidarbha Cricket Association Stadium, Jamtha':'Jamtha',
         'Himachal Pradesh Cricket Association Stadium' :'Dharamshala',
         'Nehru Stadium':'Delhi',
         'Holkar Cricket Stadium': 'Indore',
         'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium' :'Visakhapatnam',
         'Subrata Roy Sahara Stadium' : 'Pune',
         'Maharashtra Cricket Association Stadium': 'Pune',
         'Maharashtra Cricket Association Stadium' : 'Pune',
         'Shaheed Veer Narayan Singh International Stadium': 'Raipur',
         'JSCA International Stadium Complex': 'Ranchi',
         'Sheikh Zayed Stadium' :'Abu Dhabi, UAE',
         'Sharjah Cricket Stadium' :'Sharjah, UAE',
         'Dubai International Cricket Stadium' : 'Dubai, UAE',
         'Punjab Cricket Association IS Bindra Stadium, Mohali' : 'Mohali',
         'Saurashtra Cricket Association Stadium': 'Rajkot',
         'Green Park' :'Kanpur',
         'M.Chinnaswamy Stadium' : 'Bengaluru',
         'MA Chidambaram Stadium': 'Chennai',
         'Arun Jaitley Stadium' : 'Delhi',
         'Rajiv Gandhi International Stadium':'Hyderabad',
         'Punjab Cricket Association IS Bindra Stadium': 'Mohali',
         'MA Chidambaram Stadium, Chepauk, Chennai': 'Chennai',
         'Wankhede Stadium, Mumbai': 'Mumbai',
         'Narendra Modi Stadium, Ahmedabad':'Ahmedabad',
         'Arun Jaitley Stadium, Delhi':'Delhi',
         'Zayed Cricket Stadium, Abu Dhabi' : 'Abu Dhabi, UAE',
         'Dr DY Patil Sports Academy, Mumbai' : 'Mumbai',
         'Maharashtra Cricket Association Stadium, Pune' : 'Pune',
         'Eden Gardens, Kolkata': 'Kolkata'
        }
## Match Datset
# Map the values of stadium column to venue_stadium
df['venue'] = df['stadium'].map(venue_stadium)

## Match info
# Map the values of stadium column to venue_stadium
df_info['venue'] = df_info['stadium'].map(venue_stadium)

#16
actual_name_stadium = {'Brabourne Stadium': 'Brabourne Stadium, Mumbai',
                'M Chinnaswamy Stadium' : 'Mangalam Chinnaswamy Stadium',
                'Punjab Cricket Association Stadium, Mohali':'Inderjit Singh Bindra Stadium',
                'Feroz Shah Kotla':'Arun Jaitley Cricket Stadium',
                'Eden Gardens' :'Eden Gardens',
                'Wankhede Stadium' : 'Sheshrao Krushnarao Wankhede Stadium',
                'Sawai Mansingh Stadium' :'Sawai Mansingh Stadium',
                'Rajiv Gandhi International Stadium, Uppal' :'Rajiv Gandhi International Stadium',
                'MA Chidambaram Stadium, Chepauk': 'M.A. Chidambaram stadium',
                'Dr DY Patil Sports Academy' : 'Dr. D.Y. Patil Sports Academy',
                'Newlands' :'Newlands',
                "St George's Park": "St George's Park",
                'Kingsmead':'Kingsmead',
                'SuperSport Park':'SuperSport Park',
                'Buffalo Park':'Buffalo Park',
                'New Wanderers Stadium':'New Wanderers Stadium',
                'De Beers Diamond Oval':'De Beers Diamond Oval',
                'Sardar Patel Stadium, Motera':'Narendra Modi Stadium',
                'Barabati Stadium':'Barabati Stadium',
                'Vidarbha Cricket Association Stadium, Jamtha': 'Vidarbha Cricket Association Jamtha Stadium',
                'Himachal Pradesh Cricket Association Stadium':'Himachal Pradesh Cricket Association Stadium',
                'Nehru Stadium':'Jawaharlal Nehru University Stadium',
                'Holkar Cricket Stadium':'Holkar Cricket Stadium',
                'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium' : 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
                'Subrata Roy Sahara Stadium' : 'Maharashtra Cricket Association Stadium',
                'Maharashtra Cricket Association Stadium' :'Maharashtra Cricket Association Stadium',
                'Maharashtra Cricket Association Stadium' :'Maharashtra Cricket Association Stadium',
                'Shaheed Veer Narayan Singh International Stadium': 'Shaheed Veer Narayan Singh International Cricket Stadium',
                'JSCA International Stadium Complex' : 'Jharkhand State Cricket Association International Cricket Stadium',
                'Sheikh Zayed Stadium':'Sheikh Zayed Cricket Stadium',
                'Sharjah Cricket Stadium' : 'Sharjah Cricket Stadium',
                'Dubai International Cricket Stadium' : 'Dubai International Cricket Stadium',
                'Punjab Cricket Association IS Bindra Stadium, Mohali': 'Inderjit Singh Bindra Stadium',
                'Saurashtra Cricket Association Stadium': 'Khandheri Cricket Stadium',
                'Green Park' : 'Green Park Cricket Stadium',
                'M.Chinnaswamy Stadium' : 'Mangalam Chinnaswamy Stadium',
                'MA Chidambaram Stadium': 'M.A. Chidambaram stadium',
                'Arun Jaitley Stadium': 'Arun Jaitley Cricket Stadium',
                'Rajiv Gandhi International Stadium':'Rajiv Gandhi International Stadium',
                'Punjab Cricket Association IS Bindra Stadium': 'Inderjit Singh Bindra Stadium',
                'MA Chidambaram Stadium, Chepauk, Chennai': 'M.A. Chidambaram stadium',
                'Wankhede Stadium, Mumbai': 'Sheshrao Krushnarao Wankhede Stadium',
                'Narendra Modi Stadium, Ahmedabad':'Narendra Modi Stadium',
                'Arun Jaitley Stadium, Delhi' : 'Arun Jaitley Cricket Stadium',
                'Zayed Cricket Stadium, Abu Dhabi' : 'Sheikh Zayed Cricket Stadium',
                'Dr DY Patil Sports Academy, Mumbai' : 'Dr. D.Y. Patil Sports Academy',
                'Maharashtra Cricket Association Stadium, Pune' :'Maharashtra Cricket Association Stadium',
                'Eden Gardens, Kolkata': 'Eden Gardens',
                'OUTsurance Oval': 'Mangaung Oval',
                'Brabourne Stadium, Mumbai':'Brabourne Stadium, Mumbai'
               }
## Match Dataset
# Map the values of stadium column to actual_name_stadium
df['actual_name_stadium'] = df['stadium'].map(actual_name_stadium)

## Match info
# Map the values of stadium column to actual_name_stadium
df_info['actual_name_stadium'] = df_info['stadium'].map(actual_name_stadium)

#17
## Match Dataset
# Converting the column 'date' from string into datetime object
df['start_date'] = df['start_date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

## Match info
# Converting the column 'date' from string into datetime object
df_info['date'] = df_info['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

#18
#calculate total_run
df['total_run'] = df['runs_off_bat'] +df['extras']

#19
#create a new column called final_total_runs
df['final_total_runs'] = 0

# group by match_id and innings, and sum the total runs
total_runs = df.groupby(['match_id', 'innings'])['total_run'].sum().reset_index()

# loop through each row in total_runs
for i, row in total_runs.iterrows():
    # find the corresponding rows in the main dataframe and update the final_total_runs column
    df.loc[(df['match_id'] == row['match_id']) & (df['innings'] == row['innings']), 'final_total_runs'] = row['total_run']

#20
# Create a new column "is_wicket" based on "wicket_type"
df['is_wicket'] = df['wicket_type'].apply(lambda x: 1 if pd.notnull(x) and x != '' else 0)

# df[['wicket_type', 'is_wicket']].head()
# df[df['wicket_type'] != 'caught'][['wicket_type', 'is_wicket']].head()
# df[df['wicket_type'].notna()][['wicket_type', 'is_wicket']].head()

#21
# Let's group the dataframe by match_id and innings
grouped = df.groupby(["match_id", "innings"])

# Let's calculate the cumulative sum of wickets, runs, and balls
df["wickets"] = grouped["is_wicket"].cumsum()
df["runs"] = grouped["total_run"].cumsum()
# df[['match_id','is_wicket','wickets','total_run', 'runs','over']].head(15)

#22
df[['match_id','stadium','venue', 'actual_name_stadium']].sample(15)

#23
print("-------- Match Dataset --------")
print("Total No. of columns:", len(df.columns))
df.columns

#24
print("-------- Match info --------")
print("Total No. of columns:", len(df_info.columns))
df_info.columns

#25
df = df[['match_id', 'season', 'start_date', 'stadium', 'actual_name_stadium', 'venue', 'innings', 'over',
         'batting_team', 'batting_team_short_name', 'bowling_team', 'bowling_team_short_name', 'striker', 'non_striker', 'bowler',
         'runs_off_bat', 'extras', 'total_run', 'final_total_runs', 'runs', 'wides', 'noballs', 'byes', 'legbyes',
         'penalty', 'wicket_type', 'is_wicket', 'wickets', 'player_dismissed', 'other_wicket_type',
         'other_player_dismissed']]
print("-------- Match Dataset --------")
print("Total No. of columns:", len(df.columns))
df.columns

#26
df_info = df_info[['match_id', 'season', 'date', 'city', 'stadium','actual_name_stadium','venue', 'team1', 'team2',
       'toss_winner', 'toss_decision', 'player_of_match', 'winner',
       'winner_wickets', 'winner_runs', 'outcome', 'result_type', 'results',
       'gender', 'event', 'match_number', 'umpire1', 'umpire2',
       'reserve_umpire', 'tv_umpire', 'match_referee', 'eliminator', 'method',
       'date_1']]
print("-------- Match info --------")
print("Total No. of columns:", len(df_info.columns))
df_info.columns

#27
df.to_csv('match_data.csv', index=False)
df_info.to_csv('match_info.csv', index=False)

#28
# Removing unwanted columns and rearranging columns
columns_to_remove = ['match_id', 'season', 'striker', 'non_striker', 'bowler',
                     'runs_off_bat', 'extras', 'wides', 'noballs', 'byes', 'legbyes',
                     'penalty', 'wicket_type', 'player_dismissed', 'other_wicket_type',
                     'other_player_dismissed', 'batting_team_short_name','start_date',
                     'bowling_team_short_name', 'total_run', 'is_wicket', 'stadium', 'actual_name_stadium']

df1 = df.drop(columns=columns_to_remove)[["batting_team", "bowling_team", "venue",
                                          "innings", "over", "runs", "wickets", "final_total_runs"]]
df1.head()


#29
encoded_teams = {k:v for v, k in enumerate(df1['batting_team'].append(df1['bowling_team']).unique(), 0)}
encoded_teams

#30
df1['batting_team'] = df1['batting_team'].map(encoded_teams)
df1['bowling_team'] = df1['bowling_team'].map(encoded_teams)
df1.sample(10)

#31
X =df1.drop(columns=['final_total_runs'],axis=1)
print("Data Shape is :",X.shape)
X.head()

#32
Y = df1['final_total_runs']
Y.head()

#33
# Get the column names of numerical and categorical features
num_features = X.select_dtypes(exclude="object").columns
cat_features = X.select_dtypes(include="object").columns

# Instantiate OneHotEncoder
encoder = OneHotEncoder()

# Use fit_transform() to encode the specified columns
encoded_features = encoder.fit_transform(X[cat_features])

# The encoded_features will be in a sparse matrix format, you can convert it to a dense array using toarray()
# If you want to append it to the original dataframe, you can convert it to a dataframe using pd.DataFrame()
encoded_features_df = pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names_out(cat_features))

# Remove the "venue_" prefix from column names in the encoded features dataframe
encoded_features_df.columns = [col.split("venue_")[1] for col in encoded_features_df.columns]

# Concatenate the encoded features dataframe with the original dataframe
X = pd.concat([X.drop(cat_features, axis=1), encoded_features_df], axis=1)

# Display the encoded dataframe
X.head()


#34
X.columns

#35
# separate dataset into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
X_train.shape, X_test.shape

#36
# Create a StandardScaler transformer for numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#37
def evaluate_model(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = np.sqrt(mean_squared_error(true, predicted))
    r2_square = r2_score(true, predicted)
    return mae,mse,rmse,r2_square

#38
algos = {
    "Linear Regression": {
        "model": LinearRegression(),
        "params": {}
    },
    "Ridge": {
        "model": Ridge(),
        "params": {
            "alpha":np.arange(0.1, 1, 0.01)
        }
    },
    "Lasso": {
        "model": Lasso(),
        "params": {
            "alpha": np.arange(0.1, 1, 0.01)
        }
    },
#     "Decision Tree": {
#         "model": DecisionTreeRegressor(),
#         "params": {
# #             "criterion": ["squared_error", "mae"],
#             "criterion": ["squared_error", "friedman_mse"],
#             "splitter": ["best", "random"],
#             "max_depth": [1, 3, 5, 7, 9, 10, 11, 12, 14, 15, 18, 20, 25, 28, 30, 33, 38, 40],
#             "min_samples_split": [2, 4, 6, 8, 10, 15, 20],
#             "min_samples_leaf": [i for i in range(1, 11)],
#             "max_leaf_nodes": [None] + [i for i in range(10, 91, 10)],
#             "max_features": ["auto", "log2", "sqrt", None]
#         }
#     },
#     "Random Forest": {
#         "model": RandomForestRegressor(),
#         "params": {
#             "n_estimators": [100, 200, 300],
# #             "criterion": ["squared_error", "mae"],
#             "criterion": ["squared_error", "friedman_mse"],
#             "max_depth": [1, 3, 5, 7, 9, 10, 11, 12, 14, 15, 18, 20, 25, 28, 30, 33, 38, 40],
#             "min_samples_split": [2, 4, 6, 8, 10, 15, 20],
#             "min_samples_leaf": [i for i in range(1, 11)],
#             "max_leaf_nodes": [None] + [i for i in range(10, 91, 10)],
#             "max_features": ["auto", "log2", "sqrt", None]
#         }
#     },
#     "Ada Boost": {
#         "model": AdaBoostRegressor(),
#         "params": {
#             "n_estimators": [100, 200, 300],
#             "learning_rate": np.arange(0.1, 1, 0.01),
#             "loss": ['linear', 'square', 'exponential']
#         }
#     },
#     "Gradient Boost": {
#         "model": GradientBoostingRegressor(),
#         "params": {
#             "learning_rate": np.arange(0.1, 1, 0.01),
#             "n_estimators": [100, 200, 300],
# #             "criterion": ["squared_error", "mae"],
#             "criterion": ["squared_error", "friedman_mse"],
#             "min_samples_split": [2, 4, 6, 8, 10, 15, 20],
#             "min_samples_leaf": [i for i in range(1, 11)],
#             "max_depth": [1, 3, 5, 7, 9, 10, 11, 12, 14, 15, 18, 20, 25, 28, 30, 33, 38, 40],
#             "max_features": ["auto", "log2", "sqrt", None],
#             "max_leaf_nodes": [None] + [i for i in range(10, 91, 10)],
#             "alpha": np.arange(0.1, 1, 0.01)
#         }
#     }
}

#39
start_time = time.time()
train_model_error = []
test_model_error = []
best_model_details = []
final_model = {}
# Train and evaluate models
for model_name, values in algos.items():
    grid_search = GridSearchCV(values["model"], values["params"], scoring='neg_mean_squared_error', cv=5)
    #     codegrid_search = RandomizedSearchCV(values["model"], values["params"], cv=5, n_iter=15, n_jobs=-1, verbose=2, random_state=4)
    grid_search.fit(X_train, Y_train)
    best_score = grid_search.best_score_
    best_params = grid_search.best_params_

    best_model_details.append({"Model Name": model_name, "Best Score": best_score, "Best Parameters": best_params})
    # Fit model with best hyperparameters
    best_model = values["model"].set_params(**best_params)
    best_model.fit(X_train, Y_train)
    final_model[model_name] = best_model
    # Make predictions
    Y_train_pred = best_model.predict(X_train)
    Y_test_pred = best_model.predict(X_test)

    # Evaluate Train and Test dataset
    model_train_mae, model_train_mse, model_train_rmse, model_train_r2 = evaluate_model(Y_train, Y_train_pred)
    model_test_mae, model_test_mse, model_test_rmse, model_test_r2 = evaluate_model(Y_test, Y_test_pred)

    train_model_error.append(
        {"Model Name": model_name, "Mean Absolute Error": model_train_mae, "Mean Squared Error": model_train_mse,
         "Root Mean Squared Error": model_train_rmse, "r2 score": model_train_r2})
    test_model_error.append(
        {"Model Name": model_name, "Mean Absolute Error": model_test_mae, "Mean Squared Error": model_test_mse,
         "Root Mean Squared Error": model_test_rmse, "r2 score": model_test_r2})
    print("Model : " + model_name)
    print('Best Model Details')
    print('Best score:', best_score)
    print('Best params:', best_params)
    print('----------------------------------')

    print('Model performance for Training set')
    print("- Root Mean Squared Error: {:.4f}".format(model_train_rmse))
    print("- Mean Absolute Error: {:.4f}".format(model_train_mae))
    print("- R2 Score: {:.4f}".format(model_train_r2))
    print('----------------------------------')

    print('Model performance for Test set')
    print("- Root Mean Squared Error: {:.4f}".format(model_test_rmse))
    print("- Mean Absolute Error: {:.4f}".format(model_test_mae))
    print("- R2 Score: {:.4f}".format(model_test_r2))

    print('=' * 35)
    print('\n')

print("--------------------------------------------------------")
print(f"it takes {(time.time() - start_time) / 60} minutes")
print("--------------------------------------------------------")


#40
pd.set_option('display.max_colwidth', None)
print("-------- Best Model Details --------")
pd.DataFrame(best_model_details)


#41
train_model_error = pd.DataFrame(train_model_error)
print("-------- Training Data Error --------")
train_model_error

#42
test_model_error = pd.DataFrame(test_model_error)
print("-------- Test Data Error --------")
test_model_error

#43
# Compare train and test data errors for each model
train_model_error = pd.DataFrame(train_model_error)
test_model_error = pd.DataFrame(test_model_error)

# print("-------- Training Data Error --------")
# print(train_model_error)
# print("\n-------- Test Data Error --------")
# print(test_model_error)

# Choose the best-performing model based on evaluation metrics
best_model = None

# Find the model with the lowest MAE
best_mae = min(test_model_error['Mean Absolute Error'])
best_models_mae = test_model_error[test_model_error['Mean Absolute Error'] == best_mae]['Model Name'].values
best_model = ', '.join(best_models_mae)

# Find the model with the lowest MSE
best_mse = min(test_model_error['Mean Squared Error'])
best_models_mse = test_model_error[test_model_error['Mean Squared Error'] == best_mse]['Model Name'].values
best_model += ', ' + ', '.join([model for model in best_models_mse if model not in best_models_mae])

# Find the model with the lowest RMSE
best_rmse = min(test_model_error['Root Mean Squared Error'])
best_models_rmse = test_model_error[test_model_error['Root Mean Squared Error'] == best_rmse]['Model Name'].values
best_model += ', ' + ', '.join([model for model in best_models_rmse if model not in best_models_mae and model not in best_models_mse])

# Find the model with the highest R2 score
best_r2 = max(test_model_error['r2 score'])
best_models_r2 = test_model_error[test_model_error['r2 score'] == best_r2]['Model Name'].values
best_model += ', ' + ', '.join([model for model in best_models_r2 if model not in best_models_mae and model not in best_models_mse and model not in best_models_rmse])

print("\nBest Performing Model(s):", best_model.split(",")[0])

#44
# let's save gradient boost model and scaler in the form of pickle file
# encoded_team and feature columns as JSON file for prediction purpose which i use in web app

save_model = best_model.split(",")[0]

with open("model.pickle", "wb") as f:
    pickle.dump(final_model[save_model], f)

with open("scaler.pickle", "wb") as f:
    pickle.dump(scaler, f)

with open("encodedteams.json", "w") as f:
    json.dump(encoded_teams, f)

with open("columns.json", "w") as f:
    json.dump({"columns": list(X.columns)}, f)


#45
# os.remove("model.pickle")
# os.remove("model1.pickle")
# os.remove("scaler.pickle")
# os.remove("encodedteams.json")
# os.remove("columns.json")

#46
scaler = None
model = None
encoded_teams = None
columns = None

with open("model.pickle", "rb") as f:
    model = pickle.load(f)

with open("scaler.pickle", "rb") as f:
    scaler = pickle.load(f)

with open("encodedteams.json", "r") as f:
    encoded_teams = json.load(f)

with open("columns.json", "r") as f:
    columns = np.array(json.load(f)["columns"])

#47

# scaler = scaler
# model = final_model[save_model
# encoded_teams = encoded_teams
# columns = list(X.columns)

# Define function for making predictions
def prediction(batting_team, bowling_team, innings, over, runs, wickets, venue):
    # Create an array to hold input features
    X_pred = np.zeros(columns.size)

    # Assign input values to corresponding array indices
    X_pred[0] = encoded_teams[batting_team]
    X_pred[1] = encoded_teams[bowling_team]
    X_pred[2] = innings
    X_pred[3] = over
    X_pred[4] = runs
    X_pred[5] = wickets

    venue_pos = np.where(venue == columns)[0][0]
    X_pred[venue_pos] = 1

    # Scale input features using the loaded scaler
    X_pred = scaler.transform([X_pred])

    # Make prediction using the loaded model
    prediction = model.predict(X_pred)

    # Return the prediction
    return prediction


# Call the prediction function with example input values
result = prediction("Kolkata Knight Riders", "Royal Challengers Bangalore", 1, 5.1, 20, 0, "Bengaluru")
print(result)




#48

from matplotlib import cm
# Create the scatter plot
fig, ax = plt.subplots()
sc = ax.scatter(Y_test, Y_test_pred, c=Y_test, cmap=cm.viridis)
fig.colorbar(sc)

# Set the axis labels
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
ax.set_title('Scatter Plot of Actual vs. Predicted')

plt.show()

#49
# Create the regression plot
sns.set_style('whitegrid')
sns.regplot(x=Y_test, y=Y_test_pred, ci=None, color='mediumorchid', line_kws={'lw':2})

# Set the axis labels and title
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Regression Plot of Actual vs. Predicted')

plt.show()

#50
import matplotlib.pyplot as plt
import seaborn as sns

# Create the regression plot for actual values in blue color
sns.set_style('whitegrid')
sns.regplot(x=Y_test, y=Y_test, ci=None, color='blue', line_kws={'lw':2})

# Set the axis labels and title for actual values plot
plt.xlabel('Actual')
plt.ylabel('Actual')
plt.title('Regression Plot of Actual vs. Actual')

plt.show()

# Create the regression plot for predicted values in light red color
sns.set_style('whitegrid')
sns.regplot(x=Y_test, y=Y_test_pred, ci=None, color='lightsalmon', line_kws={'lw':2})

# Set the axis labels and title for predicted values plot
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Regression Plot of Actual vs. Predicted')

plt.show()

#51
pred_df=pd.DataFrame({'Actual Value':Y_test,'Predicted Value':Y_test_pred,'Difference':Y_test-Y_test_pred})
pred_df

#52
