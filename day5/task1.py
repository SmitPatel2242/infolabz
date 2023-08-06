# import requests
# import matplotlib.pyplot as plt
#
# url= requests.get("https://data.covid19india.org/data.json")
# response = url.json()
#
#
# Cases=[]
# State=[]
# for i in range(1,len(response["statewise"])):
#     Cases.append(int(response["statewise"][i]["confirmed"]))
#     State.append(response["statewise"][i]["state"])
# plt.barh(State,Cases)
# plt.xlabel("STATE")
# plt.ylabel("CASES")
# plt.show()





                            ###################### Way 2 ########################




import requests
import matplotlib.pyplot as plt

url= requests.get("https://data.covid19india.org/data.json")
response = url.json()

Data={"State":[],"Cases":[]}
for i in range(1,len(response["statewise"])):
    Data["Cases"].append((int(response["statewise"][i]["confirmed"])))
    Data["State"].append(response["statewise"][i]["state"])

plt.barh(Data["State"],Data["Cases"])
plt.xlabel("STATE")
plt.ylabel("CASES")
plt.show()