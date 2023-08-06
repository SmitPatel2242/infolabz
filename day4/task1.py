import requests

url="https://api.postalpincode.in/pincode/"
userdata = input("Enter PinCode : ")
url2=url+userdata
url3=requests.get(url2)
response = url3.json()

if(response[0]["Status"]=="Error" or response[0]["Status"]=="404" ):
    print("Enter Valid PinCode")
    exit()

for i in range(0,len(response[0]["PostOffice"])):
    print(response[0]["PostOffice"][i]["Name"])






        #######################     In My Way    #####################
# import requests
#
# url= "https://api.postalpincode.in/pincode/"
# userinput = input("Enter Pincode : ")
# url1 = url+userinput
#
# url2=requests.get(url1)
# response=url2.json()

# without validation
# for i in range (0,len(response[0]["PostOffice"])):
#     print(response[0]["PostOffice"][i]["Name"])


# With My Logic Validation
# url= "https://api.postalpincode.in/pincode/"
# userinput = input("Enter Pincode : ")
# if (len(userinput) == 0):
#     print(url[0]["Message"])
#     exit()
# if (len(userinput) != 6):
#     print("Enter Valid Length Pincode")
#     exit()
# url1 = url+userinput
#
#
# url2=requests.get(url1)
# response=url2.json()
# url=requests.get(url)
# url=url.json()
#
#
# if(response[0]["Message"]=="No records found"):
#     print(response[0]["Message"])
#     exit()
# for i in range (0,len(response[0]["PostOffice"])):
#     print(response[0]["PostOffice"][i]["Name"])
#

