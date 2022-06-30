"""
Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt
"""
def main():
    name1 = input("Enter First File Name =>")
    name2 = input("Enter Second File Name =>")
    
    f1 = open(name1,"r")
    f2 = open(name2, "r")
    
    data1 = f1.read()
    data2 = f2.read()
    
    
    if data1 == data2:
        print("\nScuccess")
    else:
        print("\nFailure")

if __name__ == "__main__":
    main()