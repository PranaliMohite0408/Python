#Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 Output : 7

def Digits(Num):
    
    Cnt=0
    while(Num>0):
    
        Num = Num//10
        Cnt = Cnt+1
    
    return Cnt

def main():
    
    print("Enter Number =>")
    No = int(input())
    
    Result = Digits(No)
    
    print("Count of Digits in Given Number is =>",Result)

if __name__ == "__main__":
    main()
