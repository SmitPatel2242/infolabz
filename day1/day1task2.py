mydata = {"category":[{"A":"FIRST","package":{"data":"21acs"}},
             {"B":"Second","data":{"new":[100]}},
             {"C":"Third","Tests":[45,75,25]}]}
print(mydata["category"][0]["package"]["data"])
print(mydata["category"][2]["Tests"][2])
print(mydata["category"][1]["data"]["new"][0])