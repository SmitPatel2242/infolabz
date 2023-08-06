import pandas as pd
import requests
# pd.options.display.max_rows = 850 # It shows the maximum no of rows
# df=pd.read_csv("Data.csv")
# print(df)


df=requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
Data=pd.DataFrame(df)
print(Data)
