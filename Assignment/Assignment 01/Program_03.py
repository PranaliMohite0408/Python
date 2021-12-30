"""
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.

"""

def Add(Value1,Value2):
    
    Ret = 0
    
    Ret = Value1 + Value2
    
    return Ret

def main():
    
    print("Enter First Number =>")
    No1 = int(input())
    
    print("Enter Second Number =>")
    No2 = int(input())
    
    Result = Add(No1,No2)
    
    print("Addition of Two Numbers is ",Result)


if __name__ == "__main__":
	main()
	