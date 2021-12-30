#Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934 Output : 37

def Dig_Add(Num):
    Dig = 0 
    Add = 0
    while(Num>0):
        Dig = Num%10
        Add = Add + Dig 
        Num = Num//10
    
    return Add

def main():
    
    print("Enter a Number =>")
    No = int(input())
    
    Result = Dig_Add(No)
    
    print("Addition of Digits in that Number is =>",Result)

if __name__ == "__main__":
    main()

