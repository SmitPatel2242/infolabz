import matplotlib.pyplot as plt
import requests

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
response = url.json()

country = input("enter country name: ")
city = input("enter city name: ")
start = float(input("enter start year: "))
end = float(input("enter end year:"))
low = 0.0
high = 0.0
dummy = {}
start_found = False

if start<end:
    low=start
    high=end
if start>end:
    low=end
    high=start
print("low ",low)
for data in range(len(response["data"])):
    for i in range(len(response["data"][data]["populationCounts"])):
        
        city_individual = response["data"][data]["city"]
        country_indi = response["data"][data]["country"]
        if city_individual == city and country_indi == country:
            if(float(response["data"][data]["populationCounts"][i]["year"]) >= low and float(response["data"][data]["populationCounts"][i]["year"]) <= high):
                if float(response["data"][data]["populationCounts"][i]["year"]) == start:
                    start_found = True
                    print(float(response["data"][data]["populationCounts"][i]["year"]))

                if start_found:
                    if float(response["data"][data]["populationCounts"][i]["year"]) in dummy:
                        dummy[float(response["data"][data]["populationCounts"][i]["year"])] += float(response["data"][data]["populationCounts"][i]["value"])
                    elif float(response["data"][data]["populationCounts"][i]["year"]) not in dummy:
                        dummy[float(response["data"][data]["populationCounts"][i]["year"])] = float(response["data"][data]["populationCounts"][i]["value"])
                    
                    else:
                        print("error")


year1 = list(dummy.keys())
population1 = list(dummy.values())


year2 = []
population2 = []

start_found1 = False
for i in year1:
    if i == start:
        start_found1 = True
    if start_found1:
        year2.append(i)
        index = year2.index(i)
        population2.append(population1[index])

print(year2)
print(population2)


plt.bar(year2, population2)
plt.title(city)
plt.show()