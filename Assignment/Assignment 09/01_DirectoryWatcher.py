"""
Write a program which accepts file name from user and check whether that file exists in current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not.
"""
import os

def main():
    print("\nEnter the File Name that you want to Open")
    name = input()
    
    if os.path.exists(name):
        
        print("File is Exits")

    else:
        print("There is no Such File")
    
if __name__ == "__main__":
    main()