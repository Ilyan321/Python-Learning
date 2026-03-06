import matplotlib.pyplot as plt

days=["Mon","tue","wed","thu","fri"]
hours=[3,4,5,6,8]
plt.plot(days,hours)
plt.xlabel("Days")
plt.ylabel("Hours of Study")
plt.grid()
plt.title("Weekly Study Tracker")
plt.show()
plt.savefig("Study_report.png")