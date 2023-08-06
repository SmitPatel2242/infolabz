mydata = {"Ahmedabad:400"}
print(mydata)
print(type(mydata))

mydata1= {"Ahmedabad":"Gujarat","Jaipur":"Rajasthan","bhopal":"MP"}
print(mydata1)
print(mydata1["Ahmedabad"])

mydata2 = {"Ahmedabad":200,"Surat":400,"Rajkot":300}
print(mydata2["Surat"])

mydata3 = {"Ahmedabad":200,"Surat":[300,80,20],"Rajkot":300}
print("Active cases of surat ",mydata3["Surat"][1])

mydata4 = {
    "Ahmadabad":[
        {"date":"25 July 2023","cases":400},
        {"date":"26 July 2023","cases":200},
        {"date": "27 July 2023","cases":300}
    ]
}
print("Active cases in ahmedabad at ",mydata4["Ahmadabad"][1]["date"])
