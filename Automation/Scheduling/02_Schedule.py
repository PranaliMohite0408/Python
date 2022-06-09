import time
import datetime
import schedule

cnt=0

def task():
    print("\nTask after each minute gets executated")
    print("Current time is :",datetime.datetime.now())
    global cnt
    cnt = cnt + 1

def main():
    print("Inside Main Function")
    print("Schedule Starts....")
    
    schedule.every(1).minutes.do(task)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        global cnt
        if(cnt == 5):
            print("\nScript Excution is Stop")
            exit()
            

if __name__ == "__main__":
    main()