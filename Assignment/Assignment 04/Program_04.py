"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.

Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""

from functools import reduce

CheckEven = lambda Num : (Num % 2 == 0)

Square = lambda Num : Num**2

Addition = lambda a,b : a+b

def main():
    List = []
    Ele = 0
    
    print("Number of Element =>")
    No = int(input())
    
    for i in range(No):
        print("\nEnter List Element =>",i+1)
        Ele = int(input())
        
        List.append(Ele)
    
    print("\nGiven List is :",List)
    
    NList = list(filter(CheckEven,List))    
    print("\nList After Filter is =>",NList)
    
    Square_List = list(map(Square,NList))
    print("\nList After Map =>",Square_List)
    
    Sum = reduce(Addition,Square_List)    
    print("\nList After Reduce =>",Sum)
        
if __name__ == "__main__":
    main()