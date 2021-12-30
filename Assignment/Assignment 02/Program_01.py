'''
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
'''

import Arithematic as A

def main():
    
    print("Enter First Number =>")
    No1 = int(input())
    
    print("Enter Second Number =>")
    No2 = int(input())
    
    Ret = A.Add(No1,No2)
    print("Addition of Two Number is ",Ret)
    
    Ret = A.Sub(No1,No2)
    print("Substraction of Two Number is ",Ret)
    
    Ret = A.Mult(No1,No2)
    print("Multiplication of Two Numberis ",Ret)
    
    Ret = A.Div(No1,No2)
    print("Division of Two Number is ",Ret)

if __name__ == "__main__":
    main()
    print("End Application..")
    