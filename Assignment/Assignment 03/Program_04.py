"""
Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""

def Frequency(List):
    
    Cnt=0
    
    print("\nEnter Element to Search in Given List =>")
    Src_Ele = int(input())
    
    for i in range(len(List)):
        
        if(List[i] == Src_Ele):
            Cnt = Cnt+1
    
    return Cnt

def main():
    List = []
    Ele=0
    
    print("Enter Number of Elements =>")
    No = int(input())
    
    for i in range(0,No):
        Ele = int(input("\nEnter Elements =>"))
        List.append(Ele)
        
    print("\nGiven List is ",List)

    ret = Frequency(List)
    
    print("\nFrequency Count of Search Element is =>",ret)
    

if __name__ == "__main__":
    main()
