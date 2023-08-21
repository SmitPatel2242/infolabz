import requests
from matplotlib import pyplot as plt

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
response = url.json()


country = input("Enter Country Name : ")
city = input("Enter City Name : ")
StartYear = int(input("Enter Start Year : "))
EndYear = int(input("Enter End Year : "))

if(StartYear > EndYear):
    StartYear,EndYear=EndYear,StartYear

CCValadation = 0
SYearValidation = 0
EYearValidation = 0
total = 0.00
YearForTotal = 0
used = 0
Year = []
population = []
cityflag=0
countryflag=0

#########   Only For Validation     ###########

for i in range(0, len(response["data"])):
    if (response["data"][i]["country"] == country):
        countryflag = 1
    if (response["data"][i]["city"] == city):
        cityflag = 1
    if (response["data"][i]["city"] == city and response["data"][i]["country"] == country):
        for j in range(0, len(response["data"][i]["populationCounts"])):
            if int(response["data"][i]["populationCounts"][j]["year"]) == StartYear:
                SYearValidation = 1
            if int(response["data"][i]["populationCounts"][j]["year"]) == EndYear:
                EYearValidation = 1
if (countryflag != 1):
    print("Enter Valid Country")
    exit()
if (cityflag != 1):
    print("Enter Valid City")
    exit()
if (SYearValidation != 1):
    print("Enter Valid StartYear")
    exit()
if (EYearValidation != 1):
    print("Enter Valid EndYear")
    exit()

#########  Validation Over   ################


for i in range(0,len(response["data"])):
    if(response["data"][i]["city"]==city and response["data"][i]["country"]==country):
        for j in range(StartYear,EndYear+1):
            for k in range(0, len(response["data"][i]["populationCounts"])):
                if(int(response["data"][i]["populationCounts"][k]["year"])) == j:
                    total=total+float(response["data"][i]["populationCounts"][k]["value"])
                    YearForTotal = int(response["data"][i]["populationCounts"][k]["year"])
                    used=1

            if used == 1:
                Year.append(YearForTotal)
                population.append(total)
                total=0
                used=0

print(Year)
print(population)
plt.bar(Year,population)
plt.xlabel("YEAR")
plt.ylabel("POPULATION")
plt.title("POPULATION")
plt.show()
