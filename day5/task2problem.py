# import requests
# from matplotlib import pyplot as plt
#
# url=requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
# response = url.json()
# country = input("Enter Country Name : ")
# city = input("Enter City Name : ")
# StartYear = int(input("Enter Start Year : "))
# EndYear = int(input("Enter End Year : "))
# lable=0
# Access=0
# Year = []
# Population = []
# for i in range(0,len(response["data"])):
#     # print(response["data"][i]["city"])
#     if(response["data"][i]["city"]==city and response["data"][i]["country"]==country):
#         for j in range(0,len(response["data"][i]["populationCounts"])):
#             if(int(response["data"][i]["populationCounts"][j]["year"])==StartYear or Access==1):
#                 Access = 1
#                 Year.append(response["data"][i]["populationCounts"][j]["year"])
#                 Population.append(int(response["data"][i]["populationCounts"][j]["value"]))
#
#             if (int(response["data"][i]["populationCounts"][j]["year"]) == EndYear):
#                 lable=1;
#                 break
#     if(lable==1):
#         break
#
# plt.bar(Year,Population)
# plt.xlabel("YEAR")
# plt.ylabel("POPULATION")
# plt.show()





####################### Modification #############################


import requests
from matplotlib import pyplot as plt

url=requests.get("https://countriesnow.space/api/v0.1/countries/population/cities")
response = url.json()
country = input("Enter Country Name : ")
city = input("Enter City Name : ")
StartYear = int(input("Enter Start Year : "))
EndYear = int(input("Enter End Year : "))
Index=0
lable=0
AccessStart=0
AccessEnd=0
StartIndex=0
EndIndex=0
Year = []
Population = []
for i in range(0,len(response["data"])):
    # print(response["data"][i]["city"])
    Index = Index + 1
    if(response["data"][i]["city"]==city and response["data"][i]["country"]==country):

        for j in range(0, len(response["data"][Index]["populationCounts"])):

            if (int(response["data"][Index]["populationCounts"][j]["year"]) == StartYear and AccessStart==0):
                StartIndex=j
                AccessStart =1
            if (int(response["data"][Index]["populationCounts"][j]["year"]) == EndYear and AccessEnd==0):
                EndIndex=j;
                AccessEnd =1
        if(EndIndex > StartIndex):
            for i in range(StartIndex,EndIndex+1):
                Year.append(response["data"][Index]["populationCounts"][i]["year"])
                Population.append(int(response["data"][Index]["populationCounts"][j]["value"]))
        if (EndIndex < StartIndex):
            for i in range(EndIndex, StartIndex-1,-1):
                Year.append(response["data"][Index]["populationCounts"][i]["year"])
                Population.append(int(response["data"][Index]["populationCounts"][j]["value"]))



plt.bar(Year,Population)
plt.xlabel("YEAR")
plt.ylabel("POPULATION")
plt.show()

