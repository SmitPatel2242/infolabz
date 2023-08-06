import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")
response = url.json()

print(response.keys())

for i in response:
    print(i)

print(response["spacecrafts"][0]["name"])

userinput = int(input("Enter id : "))

for i in range(0,len(response["spacecrafts"])):
    if userinput==response["spacecrafts"][i]["id"]:
        print(response["spacecrafts"][i]["name"])
        break
else:
    print("not found")
