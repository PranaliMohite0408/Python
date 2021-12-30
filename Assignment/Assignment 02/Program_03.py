#Write a program which accept one number from user and return its factorial.

def Factorial(Num):
    Fact=1
    while(Num>0):
        Fact = Fact * Num
        Num = Num -1
    return Fact
    
def main():
    
    print("Enter a Number for Factorial =>")
    No = int(input())
    
    Result = Factorial(No)
    
    print("Factorial of Given Number is ",Result)

if __name__ == "__main__":
	main()
	print("End Application...")

