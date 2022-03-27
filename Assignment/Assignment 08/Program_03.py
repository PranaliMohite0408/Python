"""
Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
"""
import threading

def evenlist(Data):
    Add = 0
    for i in range(len(Data)):
        if(Data[i]%2 == 0):
           Add = Add + Data[i]
    print("Addition of Evenlist is =>",Add)       

def oddlist(Data):
    Add = 0
    for i in range(len(Data)):
        if(Data[i]%2 != 0):
           Add = Add + Data[i]
    print("Addition of Odd list is =>",Add) 

def main():
    Data = []
    Ele = 0
    
    No = int(input("Enter the Number of Elements =>"))

    for i in range(No):
        Ele = int(input("Enter the list Parameters =>"))
        Data.append(Ele)

    print("Parameter of Given list are =>",Data)

    Evenlist_Thread = threading.Thread(target=evenlist, args =(Data,))
    Oddlist_Thread = threading.Thread(target=oddlist, args =(Data,))

    Evenlist_Thread.start()
    Oddlist_Thread.start()

    Evenlist_Thread.join()
    Oddlist_Thread.join()

if __name__ == "__main__":
    main()