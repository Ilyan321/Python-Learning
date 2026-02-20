class task:
    name=""
    due_date=0
    completed=False
    mark_complete=False


class task_manager:
    def __init__(self):
        self.tasks_list=[]

    def add_task(self):
        task=input("Enter the task: ")
        self.tasks_list.append(task)
        print("Task",task,"has been added.")

    def view_tasks(self):
        if not self.tasks_list:
            print("No task found.")
        else:
            print("Tasks: ",self.tasks_list)
        
    def mark_task_complete(self):
        task=input("Enter the task to mark as complete: ")
        if task in self.tasks_list:
            self.tasks_list.remove(task)
            print("Task",task,"has been marked as complete.")
        else:
            print("Task not found.")


    def search_task(self):
        task=input("Enter the task to search: ")
        if task in self.tasks_list:
            print("Task",task,"found.")
        else:
            print("Task not found.")


    #saving and loading in csv file
    def save_tasks(self):
        with open("tasks.csv","a") as file:
            for i in self.tasks_list:
                file.write(i+"\n")

task_manager=task_manager()
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Search Task")
    print("5. Save and Exit")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task_manager.add_task()
    elif choice==2:
        task_manager.view_tasks()
    elif choice==3:
        task_manager.mark_task_complete()
    elif choice==4:
        task_manager.search_task()
    elif choice==5:
        task_manager.save_tasks()
        print("Tasks saved to tasks.csv. Exiting...")
        break
    elif choice==5:
        break
    else:
        print("Invalid choice. Please try again.")
