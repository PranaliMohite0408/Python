#Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18

Mult = lambda a,b : a*b

def main():
    
    print("\nEnter a Two Number for Multiplication =>")
    
    No1 = int(input("\nEnter First Number =>"))
    No2 = int(input("\nEnter Second Number =>"))
    
    Ret = Mult(No1,No2)
    
    print("\nMultiplication of Given Two Number is =>",Ret)
    
if __name__ == "__main__":
    main()