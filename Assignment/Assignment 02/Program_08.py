"""
8. Write a program which accept one number and display below pattern.
Input : 5
Output : 1
		 1 2
		 1 2 3
		 1 2 3 4
		 1 2 3 4 5
"""

def Pattern(Num):
    for i in range(1,Num+1):
        for j in range(1,Num+1):
            if(i>=j):
                print(j,end=' ')

        print("\n")

def main():
    
    print("Enter Number For Pattern =>")
    No = int(input())
    
    Pattern(No)

if __name__ == "__main__":
    main()