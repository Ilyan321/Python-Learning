#Integrate an external API (e.g., weather or motivational quotes) into your To-Do List project. Display the fetched data every time the user views their tasks.

import requests
url = "https://zenquotes.io/api/random"
response = requests.get(url)
if response.status_code==200:
        data= response.json()
        quote= data[0]['q']
        author = data[0]['a']
def requestedquote():
    print("Quote: ",quote)
    print("- " + author)

tasks = []

def add_task(task):
    tasks.append(task)
def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
def save_tasks(filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def load_tasks(filename):
    global tasks
    with open(filename, "r") as file:
        tasks = file.read().splitlines()
if __name__ == "__main__":
    try:
        load_tasks("tasks.txt")
    except FileNotFoundError:
        print("No existing tasks found.")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
            requestedquote()

        elif choice == "3":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "4":
            save_tasks("tasks.txt")
            print("Tasks saved and exiting.")
            break
        else:
            print("Invalid choice")
