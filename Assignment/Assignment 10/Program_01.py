"""
Design automation script which accept directory name and file extension from user. Display all
files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
"""

import os
from sys import *

def DirectoryFileSearch(path):

    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)
        
    exist = os.path.isdir(path)

    if exist:
        cnt = 0
        for foldername,subfolder,filename in os.walk(path):
            for filen in filename:
                if filen.endswith(argv[2]):
                    cnt = cnt + 1
                    print(foldername+" : "+filen+"\tCount : ",cnt);
                    
    else:
        print("Invalid Path")
                    
            
       
def main():
    print("---------- Assignment 10 ----------")

    print("Application Name : "+argv[0])
    
    if(len(argv) != 3):
        print("Error :Invalid Number of Arguments ")
        print("Please Use -h for help")
        exit()
   
   
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Enter dictionary name and file extension. So that we can give you all files with that extension as an output")
        print("Syntax :python Program_01.py <FolderName>  <Extension of File> ")
        print("Example :python Program_01.py Demo .txt")
        
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : DirectoryFileSearch.py Demo .txt ")
        exit()

    try:
        DirectoryFileSearch(argv[1])

    except Exception:
        print("Error: Invalid Input")
    

if __name__ == "__main__":
    main()