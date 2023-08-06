import matplotlib.pyplot as plt
# from matplotlib import plplot as plt

cities = ["Ahmedabad","Surat","Rajkot"]
cases = [333,111,444]

mydata = {"cities":["Ahmedabad","Surat","Rajkot"], "cases":[200,200,400]}

plt.bar(mydata["cities"],mydata["cases"])
plt.xlabel("CITIES")
plt.ylabel("CASES")
plt.title("COVID CASES OF GUJARAT")
plt.show()