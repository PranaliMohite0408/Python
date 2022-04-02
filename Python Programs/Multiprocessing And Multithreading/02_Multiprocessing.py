#serial Programming
import os

def Fun():
    print("Inside Fun")
    print("PID is :",os.getpid())
    for i in range(5):
        print("Fun :",i)
    
def Gun():
    print("Inside Gun")
    print("PID is :",os.getpid())
    for i in range(5):
        print("Gun :",i)

def main():
    print("Inside main")
    print("PID is :",os.getpid())
    Fun()
    Gun()

if __name__ == "__main__":
    main()