import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

# startdate = input("Enter strat date : ")
# enddate = input("Enter end date : ")
# start=0
# end=0
# totalcases = 0
# count=0
# Date=" "
# valid=1
# for i in range(0, len(response["cases_time_series"])):
#     if(response["cases_time_series"][i]["date"]==startdate):
#         start=i;
#     else:
#         print("Enter Valid Start Date")
#         valid=0
#         break
#     if (response["cases_time_series"][i]["date"] == enddate):
#         end = i;
#     else:
#         print("Enter Valid End Date")
#         valid=0
#         break
#
# for i in range(start,end):
#
#     totalcases=totalcases+int(response["cases_time_series"][i]["dailyconfirmed"])
#     if int(response["cases_time_series"][i]["dailyconfirmed"]) > count:
#         count = int(response["cases_time_series"][i]["dailyconfirmed"])
#         Date = response["cases_time_series"][i]["date"]
#
# if valid==1:
#     print("Total number Of Cases : ",totalcases)
#     print("highest Cases : ", count)
#     print("highest Cases Date: ", Date)



#####   Way 2


import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

startDate = input("Start Date :")
endDate = input("End Date :")
total = 0
label = 0
count=0
Date=" "
for i in range(0, len(response["cases_time_series"])):

    if endDate == response["cases_time_series"][i]["date"]:
        break

    if startDate == response["cases_time_series"][i]["date"] or label == 1:
        label = 1
        total = total + int(response["cases_time_series"][i]["dailyconfirmed"])

        if int(response["cases_time_series"][i]["dailyconfirmed"]) > count:
            count = int(response["cases_time_series"][i]["dailyconfirmed"])
            Date = response["cases_time_series"][i]["date"]
    else:
        print("Enter Valid Start Date")
        break

print("Total number Of Cases : ", total)
print("highest Cases Date: ", Date)
print("highest Cases : ", count)
