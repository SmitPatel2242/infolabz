from matplotlib import pyplot as plt

branches = ["CE","IT","EC","CIVIL","MECH","BIOMEDICAL","PLASTIC","AUTOMOBILE","ICT"]

seats = [100,90,70,35,89,67,12,44,70]

plt.pie(seats,labels=branches,autopct="%1.2f%%",shadow=True,explode=(0.2,0,0,0,0,0,0,0,0))
plt.show()