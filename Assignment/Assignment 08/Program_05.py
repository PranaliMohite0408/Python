"""
Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
"""
import threading
import time

def Digits():
    for i in range(1,50+1):
        print(i,end=' ')

def Number():
    i = 50
    while(i>=1):
        print(i,end=' ')
        i = i-1

def main():
    
    Thread1 =  threading.Thread(target=Digits)
    Thread2 = threading.Thread(target=Number)
    
    Thread1.start()
    time.sleep(1)
    print("\n")
    Thread2.start()

if __name__ == "__main__":
    main()