"""
Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
		 * * * *
		 * * *
		 * *
		 *
"""		 

def Pattern(Num):
    
    for i in range(Num,0,-1):
        for j in range(0,i):
            print(" * ",end=' ')
                
        print("\n")        
            
def main():
    
    print("Enter a  Number for Pattern =>")
    No = int(input())
    
    Pattern(No)

if __name__ == "__main__":
    main()




