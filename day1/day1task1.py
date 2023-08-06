mydata= {
    "maharastra":{"mumbai":{"city":"metro city","metro":"yes"},
    "population":"20 cr"},
    "gujarat":["AHMEDABAD","SURAT","RAJKOT"],
    "rajastan":["AJMER","JAISALMER",{"capital":"jaipur"},["MEWAD","RJ","INR"]]
}

"""
Question 1 : print metro city
Question 2 : print jaipur
Question 3 : print Rajkot
Question 4 : print RJ
"""

print(mydata["maharastra"]["mumbai"]["city"])
print(mydata["rajastan"][2]["capital"])
print(mydata["gujarat"][2])
print(mydata["rajastan"][3][1])