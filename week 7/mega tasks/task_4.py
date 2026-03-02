#Create a horizontal bar chart that shows how close each task is to its deadline, highlighting tasks that are approaching their deadlines.
import matplotlib.pyplot as plt
tasks = ['Task A', 'Task B', 'Task C', 'Task D', 'Task E']
days_left = [5, 2, 7, 1, 3]
colors = ['green', 'orange', 'blue', 'red', 'yellow']
plt.barh(tasks,days_left,color=colors)
plt.title("Days left to complete tasks")
plt.grid()
plt.xlabel("Days left")
plt.ylabel("Tasks")
plt.legend()
plt.show()