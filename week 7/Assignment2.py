#Assignment Task:
#            Task Data Analysis
#Write a Python program that uses `pandas` to:
#1. Read tasks from a CSV file into a DataFrame.
#2. Filter the tasks to show only high priority tasks.
#3. Create a bar chart to visualize the number of tasks by their status.

import pandas as pd
import matplotlib.pyplot as plt

tasks_df = pd.read_csv('tasks.csv') 
print("All Tasks:")
print(tasks_df)
print("-" * 30)

high_prio_df = tasks_df[tasks_df['Priority'] == 'High']
print("High Priority Tasks:")
print(high_prio_df)

status_counts = tasks_df['Status'].value_counts()

status_counts.plot(kind='bar', color=["red", "orange", "green"])
plt.title('Task Count by Status')
plt.xlabel('Status')
plt.ylabel('Number of Tasks')
plt.xticks(rotation=0)  


plt.tight_layout()
plt.show()
