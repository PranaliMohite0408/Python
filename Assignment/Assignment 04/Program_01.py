#Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input : 4 Output : 16
#Input : 6 Output : 64

Power = lambda No : No**2


def main():
    
    print("Enter a Number =>")
    Num = int(input())
    
    Ret = Power(Num)
    
    print("\nPower of Two Given Number is =>",Ret)

if __name__ == "__main__":
    main()