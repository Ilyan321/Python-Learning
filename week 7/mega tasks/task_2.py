#Create a pie chart that displays the distribution of task priorities (High, Medium, Low). Ensure that the chart includes percentages.
import matplotlib.pyplot as plt
labels = ['High', 'Medium', 'Low']
sizes = [40, 35, 25]
colors = ['red', 'yellow', 'green']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Task Priorities")
plt.axis('equal')
plt.show()