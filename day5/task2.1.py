import requests
from matplotlib import pyplot as plt

url = requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
response = url.json()
country = input("Enter Country Name : ")
city = input("Enter City Name : ")
StartYear = int(input("Enter Start Year : "))
EndYear = int(input("Enter End Year : "))
total=0.00
YearForTotal = 0
used=0
Year=[]
population=[]
for i in range(0,len(response["data"])):
    if(response["data"][i]["city"]==city and response["data"][i]["country"]==country):
        for j in range(StartYear,EndYear+1):

            for k in range(0, len(response["data"][i]["populationCounts"])):
                if(int(response["data"][i]["populationCounts"][k]["year"])) == j:
                    total=total+float(response["data"][i]["populationCounts"][k]["value"])
                    YearForTotal = int(response["data"][i]["populationCounts"][k]["year"])
                    used=1
            # else:
            #     print("Enter Valid Year")

            if used == 1:
                Year.append(YearForTotal)
                total=0
                population.append(total)
                used=0

plt.bar(Year,population)
plt.xlabel("YEAR")
plt.ylabel("POPULATION")
plt.title("POPULATION")
plt.show()


