"""
Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.
"""
import os
import threading
import time

def evenfactor(Num):
    for i in range(1,Num+1):
        if(Num%i==0):
            if(i%2==0):
                print("Even Factors of Givne Number is =>",i)

def oddfactor(Num):
    for i in range(1,Num):
        if(Num%i==0):
            if(i%2!=0):
                print("Odd Factors of Given Number is =>",i)


def main():
    No = int(input("Enter a Integer Value =>"))

    Thread1 = threading.Thread(target=evenfactor,args=(No,))
    Thread2 = threading.Thread(target=oddfactor, args=(No,))
    
    Thread1.start()
    time.sleep(1)
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()
    print("\nExit from main")