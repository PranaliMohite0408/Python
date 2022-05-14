from sys import *

def main():
    print("Number of Command line arguments are :",len(argv))

    print("Name of Application is :",argv[0])

    print("Command line arguments are :")
    
    for data in argv:
        print(data)

if __name__ == "__main__":
    main()