"""
Design python application which creates three threads as small, capital, digits.
All the threads accepts string as parameter. aSmall thread display number of small characters, 
capital thread display number of capital characters and digits thread display number of digits. 
Display id and name of each thread.
"""
import threading
import os

def small(str):
    print("\nThread Name of small is :", threading.current_thread().name)
    print("\nPID of small is :",os.getpid())
    cnt = 0
    i = 0
    for i in range(len(str)):
        if(str[i] >="a" and str[i]<="z"):
            cnt = cnt + 1

    print("\nCount of Small Letters in Given string is =>",cnt)

def capital(str):
    print("\nThrad Name of capital is :",threading.current_thread().name)
    print("\nPID of capital is :",os.getpid())
    cnt = 0 
    for i in range(len(str)):
            if(str[i] >= "A" and str[i]<="Z"):
                cnt = cnt +1

    print("\nCount of Capital Letters in Given String is =>",cnt)            


def Digits(str):
    print("\nThread Name of Digits is :", threading.current_thread().name)
    print("\nPID of Digits is :",os.getpid())

    cnt =  0 
    for i in range(len(str)):
        if(str[i]>='0' and str[i]<='9'):
            cnt = cnt + 1

    print("\nDigits Conunt of Given string is :",cnt)       


def main():
    var = input("Enter Your Name =>")

    Small_Thread = threading.Thread(target=small,args=(var,), name='SmallThread')
    Capital_Thread = threading.Thread(target=capital, args=(var,), name='CapitalThread')
    Digits_Thread = threading.Thread(target=Digits,args=(var,), name='DigitsThread')

    Small_Thread.start()
    Capital_Thread.start()
    Digits_Thread.start()


if __name__ == "__main__":
    main()