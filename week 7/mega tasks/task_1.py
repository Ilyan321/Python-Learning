#Create a line chart that shows how many tasks have been completed each day of the week. This should represent the progress made over time.
import matplotlib.pyplot as plt

days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
tasks_done=[2, 3, 5, 7, 11, 13, 17]

plt.plot(days,tasks_done,marker='o')
plt.title("Tasks completed on each day of week.")
plt.xlabel("Days")
plt.ylabel("Total tasks done")
# plt.grid()
plt.legend()
plt.show()