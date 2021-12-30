#Write a program which accept one number form user and return addition of its factors.
#Input : 12 Output : 16 (1+2+3+4+6)


def Add_Fact(Num):
    Fact=0
    for i in range(1,Num):
        if(Num%i == 0):
            Fact = Fact + i
            
    return Fact
    



def main():
    
    print("Enter a Number for Addition Factor =>")
    No = int(input())
    
    Result = Add_Fact(No)
    
    print("Additon Factor of Given Number is",Result)


if __name__ == "__main__":
    main()

