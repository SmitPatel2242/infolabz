import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()
count=0
Date=0
for i in range(0,len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"])>count:
        count=int(response["cases_time_series"][i]["dailyconfirmed"])
        Date = response["cases_time_series"][i]["date"]

print(Date)