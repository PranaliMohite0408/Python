#Write a program which accept number from user and check whether that number is positive or negative or zero.

def Check_Num(Value1):
    
    if(Value1 > 0):
        print("Given Number is Positive...")
    elif(Value1 < 0):
        print("Given Number is Negative...")
    else:
        print("Given Number is Zero...")
    

def main():
    
    print("Enter Number =>")
    No = int(input())
        
    Result = Check_Num(No)
    

if __name__ == "__main__":
    main()