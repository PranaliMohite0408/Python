#multiprocessing
import os
import multiprocessing

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
    print("PID of Parent Process :",os.getpid())
    
    Process1 =  multiprocessing.Process(target = Fun, args = (No,))
    Process2 =  multiprocessing.Process(target = Gun, args = (No,))
    
    Process1.start()
    Process2.start()
    
    Process1.join()
    Process2.join()
        
    print("End of Main")
    
if __name__ == "__main__":
    main()