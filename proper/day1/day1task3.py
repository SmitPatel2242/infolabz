import requests

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
mydata = url.json();
print(mydata["bpi"]["USD"]["rate"])