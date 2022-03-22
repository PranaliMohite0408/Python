"""
Write a recursive program which accept number from user and return its factorial.
Input : 5
Output : 120
"""
Fact = 1

def factorial(Num):
    global Fact
    if(Num!=0):
        Fact = Fact * Num
        Num = Num - 1
        factorial(Num)
        return Fact

def main():
    No = int(input("Enter a Number =>"))
    Ret = factorial(No)
    print("\nFactorial of Given Number is =>",Ret)


if __name__ == "__main__":
    main()