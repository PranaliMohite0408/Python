"""
Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
"""
def Addition(List):
    
    Add =0
    for i in range(len(List)):
        Add = Add + List[i]
        
    return Add

def main():
    List = []
    Ele=0
    
    print("Enter a Number of Elements =>")
    Num = int(input())   
    
    for i in range(0,Num):
        Ele = int(input("\nEnter List Element =>"))
        List.append(Ele)
    
    print("\nGiven List is =>",List)
    
    ret = Addition(List)
    
    print("\nAddition of List Element is  =>",ret)
    
if __name__ == "__main__":
    main()
