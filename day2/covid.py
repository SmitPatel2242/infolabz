import requests

url = requests.get("https://data.covid19india.org/data.json")
response = url.json()

print(response.keys())


for i in response:
    print(i)

