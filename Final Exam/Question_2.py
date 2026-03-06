task_list=[]
class Task_manager:
    def add_task(self,task):
        task_list.append(task)
    def view_tasks(self):
        if not task_list:
            print("No task found.")
        else:
            print("Tasks: ")
            for i in task_list:
                print(i)
            print()
    def markcompleted(self,task):
      for i in range(len(task_list)):
        if task_list[i]==task:
          task_list[i]+=" (Completed)"

Task_Manager=Task_manager()
while True:
    print("1.Add task.\n2.View task.\n3.Mark as completed.\n4.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        task=input("Enter your task: ")
        Task_Manager.add_task(task)
    elif choice==2:
        Task_Manager.view_tasks()
    elif choice==3:
        task=input("Enter the task to mark as completed.")
        Task_Manager.markcompleted(task)
    elif choice==4:
        break
    else:
        print("404 error. please select the above options.")


