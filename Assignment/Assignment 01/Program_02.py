"""
Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.

"""

def ChkNum(Value1):
    
    if(Value1%2 == 0):
        print("Number is Even...")
    else:
        print("Number is Odd...")
        
def main():
    
    print("Enter Number =>")
    No = int(input())
    
    Ret = ChkNum(No)

if __name__ == "__main__":
    main()
