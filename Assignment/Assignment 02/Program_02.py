''''
Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
		 * * * * *
		 * * * * *
		 * * * * *
		 * * * * *
'''

def Pattern(Num):
    
    for i in range(0,Num):
        for j in range(0,Num):
            print(" * ", end=' ')
            
        print("\n")    

def main():
    
    print("Enter a Number to Display the Pattern =>")
    No = int(input())
    
    Pattern(No)
    

if __name__ == "__main__":
    main()
    print("End Application....")