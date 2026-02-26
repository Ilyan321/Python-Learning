#Use the datetime library to notify the user when a task deadline is approaching (e.g., within the next 2 days).
from datetime import datetime
tasks=[]
def add_task(name,deadline):
    task={"name":name,"deadline":deadline}
    tasks.append(task)

def check_deadlines():
    now=datetime.now().date()
    for task in tasks:
        deadline=datetime.strptime(task["deadline"],"%Y-%m-%d").date()
        days_left=(deadline-now).days
        if 0 <= days_left <= 2:
            print("Task",task["name"],"is coming up in ",days_left,"days")
        else:
            print("Task",task["name"],"is not coming up soon")

while True:
    print("1. Add Task")
    print("2. Check Deadlines")
    print("3. Exit")
    choice=input("Enter your choice (1-3): ")
    if choice=="1":
        name=input("Enter task name (exit to stop): ")
        if name.lower()=="exit":
            break
        deadline=input("Enter deadline (YYYY-MM-DD): ")
        add_task(name,deadline)
    elif choice=="2":
        check_deadlines()
    elif choice=="3":
        break
    