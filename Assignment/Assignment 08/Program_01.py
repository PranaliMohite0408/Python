"""
Design python application which creates two thread named as even and odd. 
Even  thread will display first 10 even numbers and odd thread will display first 10 odd numbers.
"""
import os
import threading
import time

def even():
    print("PID of Even :",os.getpid())
    print("First 10 Even Numbers are => ")
    for i in range(2,22,2):
        print(i,end='  ')
       
def odd():
    print("\nPID of ODD :",os.getpid())    
    print("First 10 Odd Numbers are =>")
    for i in range(1,20):
        if(i%2!=0):
            print(i,end='  ')

def main():
    print("PID of Main :",os.getpid())   
    Thread1 = threading.Thread(target = even)
    Thread2 = threading.Thread(target = odd)
    
    Thread1.start()
    time.sleep(1)
    Thread2.start()
    
    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()