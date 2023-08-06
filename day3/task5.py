import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

Date = []
userinput = input("Enter Date : ")
for i in range(0,len(response["cases_time_series"])):
    if response["cases_time_series"][i]["date"] == userinput:
        if int(response["cases_time_series"][i]["dailyconfirmed"]) > 100000:
            print("yes")
        else:
            print("no")
else:
    print("enter valid date")
