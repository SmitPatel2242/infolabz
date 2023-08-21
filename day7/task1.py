import matplotlib.pyplot as plt
import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

date = []
dailyconfirmed = []
dailydeceased = []
dailyrecovered = []

for i in range(0,len(response["cases_time_series"])):
    dailyconfirmed.append(int(response["cases_time_series"][i]["dailyconfirmed"]))
    dailydeceased.append(int(response["cases_time_series"][i]["dailydeceased"]))
    dailyrecovered.append(int(response["cases_time_series"][i]["dailyrecovered"]))
    date.append(i+1)
plt.subplot(2,3,1)
plt.plot(date,dailyconfirmed)
plt.title("dailyconfirmed")

plt.subplot(2,3,2)
plt.plot(date,dailyrecovered)
plt.title("dailyrecovered")

# dailyDeased
plt.subplot(2,3,3)
plt.plot(date,dailydeceased)
plt.title("dailydeceased")

plt.show()