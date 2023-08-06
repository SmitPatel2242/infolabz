import requests

from matplotlib import pyplot as plt

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")

response = url.json()

usercountry = input("Enter country:")
usercity = input("Enter city:")
#
# userstyear = int(input("Enter year:"))
# userendyear = int(input("Enter year:"))

list1 = []
list2 = []

for i in range(len(response["data"])):
    if usercountry == response["data"][i]["country"] and usercity == response["data"][i]["city"]:
       for j in range(len(response["data"][i]["populationCounts"])):
           list1.append(response["data"][i]["populationCounts"][j]["year"])
           list2.append(response["data"][i]["populationCounts"][j]["value"])

print(list1)
print(list2)

plt.bar(list2,list1)
plt.show()