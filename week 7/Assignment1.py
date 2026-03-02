import matplotlib.pyplot as plt

categories = ['Completed', 'In Progress', 'Pending']
task_counts = [45, 20, 15] 

priorities = ['High', 'Medium', 'Low']
priority_counts = [25, 40, 15]
colors = ["red","orange","blue"]


days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
tasks_completed_per_day = [5, 12, 8, 15, 5]

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5)) 


ax1.bar(categories, task_counts, color=['green', 'orange', 'red'])
ax1.set_title("1. Task Completion Rate")
ax1.set_xlabel("Status")
ax1.set_ylabel("Number of Tasks")

ax2.pie(priority_counts, labels=priorities, colors=colors, autopct='%1.1f%%', startangle=90)
ax2.set_title("2. Task Priorities")

ax3.plot(days_of_week, tasks_completed_per_day, marker='o', linestyle='-', color='blue', linewidth=2)
ax3.set_title("3. Task Completion Over Time")
ax3.set_xlabel("Day of the Week")
ax3.set_ylabel("Tasks Completed")
ax3.grid(True, linestyle='--', alpha=0.6) 

plt.tight_layout() 
plt.show()
