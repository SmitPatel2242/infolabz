import requests
from matplotlib import pyplot as plt
url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
populationdata = url.json()

countryinput = input("Enter the country name:")
cityinput = input("Enter the city name:")
startyear = input("Enter the starting year:")
endyear = input("Enter the end year:")
yearlist = []
valuelist = []
index1 = []
index2 = 0

found_city = False
found_country = False
found_syear = False
found_eyear = False
cityindex = 0
sum1 = 0
indexesofdate = 0

print("index 1 length",len(index1))

for i in range(len(populationdata["data"])):
    if countryinput ==populationdata["data"][i]["country"]:
        found_country = True
        if cityinput == populationdata["data"][i]["city"]:
            cityindex = i
            found_city = True

for j in range(len(populationdata["data"][cityindex]["populationCounts"])):
    if populationdata["data"][cityindex]["populationCounts"][j]["year"] == startyear:
        if (len(index1) == 0):
            index1.append(j)
        found_syear = True
        print("index 1",index1)
    if populationdata["data"][cityindex]["populationCounts"][j]["year"] == endyear:
        index2 = j
        found_eyear = True



if(found_country == False):
    print("Invalid Country")
elif(found_city == False):
    print(("Invalid City"))
elif(found_syear == False):
    print("Invalid start year")
elif(found_eyear == False):
    print("Invalid end year")
else:
    for k in range(index1[0],index2 + 1):
        if int(populationdata["data"][cityindex]["populationCounts"][k]["year"]):
            yearlist.append(int(populationdata["data"][cityindex]["populationCounts"][k]["year"]))
            valuelist.append(float(populationdata["data"][cityindex]["populationCounts"][k]["value"]))
        elif int(populationdata["data"][cityindex]["populationCounts"][k]["year"]) in yearlist:
            sum1 = float(populationdata["data"][cityindex]["populationCounts"][k]["value"])
            indexesofdate = yearlist.index(int(populationdata["data"][cityindex]["populationCounts"][k]["year"]))
            finalvalue = sum1 + valuelist[indexesofdate]
            valuelist[indexesofdate] = finalvalue

if(found_country and found_city and found_syear and found_eyear == True):
    print("value",valuelist)
    print("year",yearlist)
    plt.bar(yearlist,valuelist)
    plt.xlabel("YEARS")
    plt.ylabel("POPULATION")
    plt.title("COUNTRIES POPULATION")
    plt.show()