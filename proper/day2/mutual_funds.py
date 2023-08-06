import requests

url = requests.get("https://api.mfapi.in/mf")
response = url.json()

print(response[0].keys())

for i in response[0]:
    print(i)

print(response[2]["schemeCode"])
userinput = int(input("enter id: "))
for i in range(0,len(response)):
    if userinput==response[i]["schemeCode"]:
        print(response[i]["schemeName"])
        break
else:
    print("Not Found")
