"""
Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""

def Maximum(List):
    Max = 0
    
    for i in range(len(List)):
        if(List[i]>Max):
            Max = List[i]

    return Max
    
def main():
    List = []
    Ele = 0
    
    print("Enter Number of Elements =>")
    Num = int(input())
    
    for i in range(0,Num):
        Ele = int(input("\nEnter Elements =>"))
        List.append(Ele)
        
    print("\nGiven List is =>",List)

    ret = Maximum(List)
    
    print("\nMaximum Number From Given List is =>",ret)

if __name__ == "__main__":
    main()
