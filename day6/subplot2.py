from matplotlib import pyplot as plt

time = ["9:00","10:00","11:00","12:00","1:00"]
bob = [100,120,121,134,145]
sbi = [89,120,87,100,120]
icici = [56,79,100,76,23]

plt.subplot(2,3,1)
plt.plot(time,bob)
plt.title("BOB")