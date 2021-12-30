#Write a program which accept number from user and print that number of “*” on screen.


def Pattern(Num):
    for i in range(Num):
        print(" * ", end=' ')


def main():
    
    print("Enter a Number =>")
    No = int(input())    
    
    Pattern(No)



if __name__ == "__main__":
    main()