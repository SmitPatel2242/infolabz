import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()
# Way 1
Day=0

for i in range(0,len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) > 100000:
        Day=Day+1

print(Day)

# Way 2
Date = [];
for i in range(0,len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) > 100000:
        Date.append(response["cases_time_series"][i]["dailyconfirmed"])

print(len(Date))