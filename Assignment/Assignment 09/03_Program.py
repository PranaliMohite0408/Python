"""
Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
"""
def main():
    f1 = open("Demo.txt", "w")
    
    name = input("\nEnter a File name that you want to Open =>")
    fd = open(name, "r")
    
    for line in fd:
        f1.write(line)
if __name__ == "__main__":
    main()