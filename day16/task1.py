import pandas as pd
import matplotlib as pyplot
prices = pd.read_csv("prices.csv")
area=[]
price=[]
sum=0.0
avg=0.0
xbar = 0.0
ybar = 0.0
x_xbar=[]
y_ybar=[]
x_xbar2=[]
x_xbary_ybar=[]
x_xbary_ybarsum=0.0
x_xbar2sum=0.0
b0=0.0
b1=0.0
userinput = float(input("Enter Area :"))
output=0.0
for i in prices["area"]:
    area.append(float(i))
for i in prices["prices"]:
    price.append(float(i))
for i in area:
    sum=sum+i
    avg=avg+1

xbar=sum/avg
# print(xbar)
# print(xbar)
sum=0.0
avg=0.0

for i in price:
    sum=sum+i
    avg=avg+1

ybar=sum/avg

for i in range(len(area)):
    x_xbar.append(float(area[i]-xbar))

for i in range(len(price)):
    y_ybar.append(float(price[i]-ybar))

for i in x_xbar:
    x_xbar2.append(float(i)*float(i))

for i in range(len(x_xbar)):
    x_xbary_ybar.append(x_xbar[i]*y_ybar[i])

for i in x_xbary_ybar:
    x_xbary_ybarsum=x_xbary_ybarsum+i

for i in x_xbar:
    x_xbar2sum=x_xbar2sum+float(i*i)

b1=x_xbary_ybarsum/x_xbar2sum
print(b1)
b0=b1*xbar/ybar
print(b0)
output=b0+b1*userinput
print(output)