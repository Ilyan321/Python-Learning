# Assignment due date checker
from datetime import datetime

assignment="Class 4 assignment on datetime library"

due_date="2026-01-30"
due_date_1=datetime.strptime(due_date,"%Y-%m-%d").date()

today=datetime.now().date()

if(due_date_1==today):
    print("Todays the last day.")
elif(due_date_1>today):
    print("You still have time.")
else:
    print("The date's gone. You are cooked.")



