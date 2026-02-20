class Task:
    name=""
    due_date=""
    completed=False
    def __init__(self,name,due_date):
        self.name=name
        self.due_date=due_date

    def __str__(self):
        return f"Task: {self.name}, Due Date: {self.due_date}, Completed: {self.completed}"


class task_manager(Task):

    def __init__(self):
        self.tasks_list=[]

# load tasks from csv
    def load_tasks(self):
        try:
            with open("tasks.csv",'r') as file:
                for line in file:
                    task=line.strip().split(',')
                    new_task=Task(task[0],task[1])
                    self.tasks_list.append(task)
        except FileNotFoundError:
            print("No existing file found. Starting with an empty list here.")
    
    #add task to list
    def add_task(self):
        task=input("Enter the task: ")
        date=input("Enter the due date (YYYY-MM-DD): ")
        obj=Task(task,date)
        self.tasks_list.append(obj)
        print("Task",task,"has been added with due date",date)
        
    
    #view all tasks
    def view_tasks(self):
        if not self.tasks_list:
            print("No task found.")
        else:
            print("Tasks: ")
            for i in self.tasks_list:
                print(i)
            print()
    
    #mark as complete and remove file from list
    def mark_task_complete(self):
        task=input("Enter the task to mark as complete: ")
        found=False
        for i in self.tasks_list:

            if i.name ==task:
                self.tasks_list.remove(i)
                print("Task",task,"has been marked as complete.")
                found=True
                break
        if not found:
                print("Task not found.")

    # searching task
    def search_task(self):
        search=input("Enter the task to search: ")
        found=False
        for task in self.tasks_list:
            if task.name==search:
                print("Task found: ",task)
                found=True
                break
            
        if not found:
            print("Task not found.")


    #saving and loading in csv file
    def save_tasks(self):
        with open("tasks.csv","a") as file:
            for i in self.tasks_list:
                if isinstance(i,Task):
                    file.write(f"{i.name},{i.due_date},{i.completed}\n")

task_manager=task_manager()
task_manager.load_tasks()
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Search Task")
    print("5. Save and Exit")
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
    else:
        print("Invalid choice. Please try again.")
