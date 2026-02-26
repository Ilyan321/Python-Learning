import schedule
import time

def reminder():
    print("Check your tasks.")

# schedule.every().day.at("09:00").do(reminder)
schedule.every(2).seconds.do(reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
