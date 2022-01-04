"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
from functools import reduce

NList = lambda Num : (Num>=70 and Num <=90)

Increment = lambda Num : Num + 10

Product = lambda a,b : a*b

def main():
    
    List = []
    size = int(input("Enter Number of Element =>"))
    
    for i in range(size):
        Ele = int(input("\nEnter List Element=>"))
        List.append(Ele)
    
    print("\nGiven List is =>",List)
    
    New_List = list(filter(NList,List))
    
    print("\nList After Filter = >",New_List)
    
    Increment_List = list(map(Increment,New_List))
    
    print("\nList After Map = >",Increment_List)
    
    Product_List = reduce(Product,Increment_List)
    
    print("\nList After Reduce =>",Product_List)

if __name__ == "__main__":
    main()