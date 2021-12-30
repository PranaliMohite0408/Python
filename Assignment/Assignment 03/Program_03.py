"""
Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
"""

def Minimum(List):
    Min = 0
    
    for i in range(len(List)):
        
        if(i == 0):
            Min = List[i]
            continue
       
        if(List[i]<Min):
            Min = List[i]

    return Min
    
def main():
    List = []
    Ele = 0
    
    print("Enter Number of Elements =>")
    Num = int(input())
    
    for i in range(0,Num):
        Ele = int(input("\nEnter Elements =>"))
        List.append(Ele)
        
    print("\nGiven List is =>",List)

    ret = Minimum(List)
    
    print("\nMinimun Number From Given List is =>",ret)

if __name__ == "__main__":
    main()




















