import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

# response["cases_time_series"][i]
Date = []

for i in range(0,len(response["cases_time_series"])):
    if int(response["cases_time_series"][i]["dailyconfirmed"]) > 100000:
        Date.append(response["cases_time_series"][i]["date"])

for i in Date:
    print(i)
