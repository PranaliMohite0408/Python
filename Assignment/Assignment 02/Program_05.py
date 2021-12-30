#Write a program which accept one number for user and check whether number is prime or not.
#Input : 5 Output : It is Prime Number


def Prime(Num):
    
    Cnt=0
    for i in range(2,Num):
        if(Num%i==0):
            Cnt = Cnt+1
                   
    if(Cnt != 0):
        print("Given Number is Not Prime")
    else:
        print("Given Number is Prime")
    
def main():
    
    print("Enter a Number =>")
    No = int(input())
    
    if(No>1):
        Prime(No)
    else:
        print("Please Enter Valid Number")
        return -1

if __name__ == "__main__":
    main()
