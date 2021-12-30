"""
Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)
"""
import MarvellousNum as M

def ListPrime(List):
    Prime_Lst = []
    Num =0
    for i in List:
        Num = M.ChkPrime(i)
        if (Num == "Number is Prime"):
            Prime_Lst.append(i)
     
    return Prime_Lst

def Add_Prime_Lst(List):    
    Add =0
    for i in range(len(List)):
        Add = Add + List[i]
        
    return Add

def main():
    
    List = []
    Ele=0
    
    print("\nEnter Number of Elements =>")
    No = int(input())
    
    for i in range(0,No):
        Ele = int(input("\nEnter Elements =>"))
        List.append(Ele)
        
    print("\nGiven List is :",List)
    
    ret = ListPrime(List)
    
    print("\nPrime List is :",ret)
    
    Addition = Add_Prime_Lst(ret)
    
    print("\nAddition of Prime List is =>",Addition)
  
if __name__ == "__main__":
    main()
