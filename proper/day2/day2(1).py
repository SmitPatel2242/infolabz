import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()
print(response)
print(type(response))

print(response["cases_time_series"][0]["date"])

for i in response:
    print(i)

print(response.keys())
print(len(response["cases_time_series"]))

for i in range(0,len(response["cases_time_series"])):
    print(i+1,"Dates:",response["cases_time_series"][i]["date"],"cases:",response["cases_time_series"][i]["dailyconfirmed"])

userdate = input("Enter date:")

for i in range(0,len(response["cases_time_series"])):
    if userdate == response["cases_time_series"][i]["date"]:
        print("Cases ",response["cases_time_series"][i]["dailyconfirmed"])
        break
else:
    print("data not found")