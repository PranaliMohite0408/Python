'''
Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
'''

def Check_Num(Num):
    if(Num%5 == 0):
        print("True")
    else:
        print("False")
    


def main():
    
    print("Enter Number =>")
    No = int(input())
    
    Result = Check_Num(No)

if __name__ == "__main__":
    main()