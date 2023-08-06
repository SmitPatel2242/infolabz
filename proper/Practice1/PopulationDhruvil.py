from matplotlib import pyplot as plt
import requests

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")

response = url.json()
country = "Australia"
city = "Newcastle-Maitland"
startYear = 2011
endYear = 2012
if startYear>endYear:
    startYear,endYear = endYear,startYear
# country = input("Country : ")
# city = input("City : ")
# startYear = int(input("Enter Start Year : "))
# endYear = int(input("Enter End Year : "))
startIndex = 0
endIndex = 0
year = 0
population = 0
no=0
for i in range(0,len(response["data"])):
    if country == response["data"][i]["country"] and city == response["data"][i]["city"]:
        no=i
        for j in range(0,len(response["data"][i]["populationCounts"])):
            if startYear == int(response["data"][i]["populationCounts"][j]["year"]):
                startIndex = j
                print("Start Year ",startIndex)
            if endYear == int(response["data"][i]["populationCounts"][j]["year"]):
                endIndex = j
                print("End Year ",endIndex)

if startYear < endYear:
    for j in range(startIndex,endIndex+1):
        print(response["data"][no]["populationCounts"][j]["year"])

if startYear > endYear:
    for j in range(endIndex,startIndex+1,-1):
        print(response["data"][no]["populationCounts"][j]["year"])