"""
Write a program which accept file name from user and open that file and display the contents of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.
"""

def main():
    name = input("Enter a File Name that You want to Open =>")
    
    fd =  open(name,"r")
    
    data = fd.read()
    
    print("\n",data)


if __name__ == "__main__":
    main()