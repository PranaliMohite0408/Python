#multithreading
import os
import threading

def Fun(x):
    print("Inside Fun")
    print("PID of Fun :",os.getpid())
    print("PPID of Fun",os.getppid())
    for i in range(x):
        print("Fun :",i)
    
def Gun(x):
    print("Inside Gun")
    print("PID of Gun :",os.getpid())
    print("PPID of Gun",os.getppid())
    for i in range(x):
        print("Gun :",i)

def main():
    No = 5
    print("Inside main")
    print("PID of Parent Thread :",os.getpid())
    
    thread1 =  threading.Thread(target = Fun, args = (No,))
    thread2 =  threading.Thread(target = Gun, args = (No,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
        
    print("End of Main")
    
if __name__ == "__main__":
    main()