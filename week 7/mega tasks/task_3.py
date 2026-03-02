#Using the categories (e.g., Work, Personal, Shopping), create a bar chart to show the task completion rate for each category.
import matplotlib.pyplot as plt
catagories=["Personel","Work","Shopping"]
tasks_done=[10,20,32]
plt.bar(catagories,tasks_done,color=["blue","green",'orange'])
plt.title("Tasks done according to catagory")
plt.xlabel("catagories")
plt.ylabel("Total tasks done")
plt.grid()
plt.legend()
plt.show()