"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""

from functools import reduce

Mult = lambda Num : Num *2

Max = lambda x,y : x if(x>y) else y

def Prime_Lst(Num):
    Cnt=0
    for i in range(2,Num):
        if(Num%i==0):
            Cnt = Cnt+1
                   
    if(Cnt != 0):
        return False
    else:
        return True

    
def main():
    List = []
    Ele = 0
    
    No = int(input("\nEnter Number of Elements =>"))
    
    for i in range(No):
        print("Enter List Elements =>",i+1)
        Ele = int(input())
        
        List.append(Ele)
    
    print("\nGiven List is =>",List)
    
    NList = list(filter(Prime_Lst,List))
    print("\nList After Filter is =>",NList)
    
    Multiplication = list(map(Mult,NList))
    print("\nList After Map => ",Multiplication)
    
    Max_Lst = reduce(Max,Multiplication)
    print("\nList After Reduce =>",Max_Lst)

if __name__ == "__main__":
    main()