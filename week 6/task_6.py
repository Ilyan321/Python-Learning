#Assignment Task: Schedule Task Reminders for Your To-Do List Write a Python program that:

#Schedules a reminder to check the To-Do List every day at 9:00 AM.
#Tracks task deadlines and notifies when a deadline is within the next 2 days.
#Saves the scheduled reminders to a file for future use.

import schedule
import time
import threading
from datetime import datetime
import requests

# --- Motivational Quote ---
def get_quote():
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            print(f'\nQuote: "{quote}"')
            print(f"- {author}")
    except:
        print("\nCould not fetch quote.")

tasks = []

def add_task(name, deadline):
    task = {"name": name, "deadline": deadline}
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} (Deadline: {task['deadline']})")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Deleted: {removed['name']}")
    else:
        print("Invalid task number.")

def check_deadlines():
    now = datetime.now().date()
    found = False
    for task in tasks:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        days_left = (deadline - now).days
        if 0 <= days_left <= 2:
            print(f" Task '{task['name']}' is coming up in {days_left} day(s)!")
            found = True
    if not found:
        print("No upcoming deadlines within 2 days.")

def schedule_reminder():
    schedule.every().day.at("09:00").do(check_deadlines)
    while True:
        schedule.run_pending()
        time.sleep(60)

def save_tasks(filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task["name"] + "," + task["deadline"] + "\n")

def load_tasks(filename):
    global tasks
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                add_task(parts[0], parts[1])

if __name__ == "__main__":
    try:
        load_tasks("reminders.txt")
        print(f"Loaded {len(tasks)} task(s) from file.")
    except FileNotFoundError:
        print("No existing reminders found.")

    reminder_thread = threading.Thread(target=schedule_reminder, daemon=True)
    reminder_thread.start()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Check Deadlines")
        print("5. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter task name: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            add_task(name, deadline)
            print("Task added!")
            get_quote()
        elif choice == "2":
            view_tasks()
            get_quote()
        elif choice == "3":
            view_tasks()
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
            get_quote()
        elif choice == "4":
            check_deadlines()
            get_quote()
        elif choice == "5":
            save_tasks("reminders.txt")
            print("Tasks saved. Exiting.")
            get_quote()
            break
        else:
            print("Invalid choice.")
            get_quote()
