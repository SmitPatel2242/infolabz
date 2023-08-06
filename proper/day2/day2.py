for i in range(1,101):
    print(i)

for i in range(30,10,-2):
    print(i)

for i in range(10,30,2):
    print(i)


userinput = int(input("Enter number : "))

for i in range(1,101):
    if userinput == i:
        print("Number Found")

else:
    print("Number Not Found")

