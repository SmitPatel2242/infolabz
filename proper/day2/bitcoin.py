import requests

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response = url.json()
print(response.keys())
print(response["bpi"]["USD"]["rate"])
print(len(response["bpi"]))
userinput = input("Enter Currancy : ")

for i in response["bpi"]:
    if userinput == i:
        print(response["bpi"][userinput]["rate"])
        break
else:
    print("Enter valid currancy")
