#import statements of necessary
from sys import*

#Entry point of automation script
def main():
    print("--------Marvellous Infosystem : Automation1--------")
    print("script Name :", argv[0])
    print("Number of Arguments Accepted :",len(argv)-1)
    
    
    if(len(argv)>3) or (len(argv)<2):       #validator
        print("Invalid Number of Arguments")
        exit()
    
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Script is used to Perform the addition of 2 Numbers")
        print("First_Arguments : Any Numeric Value")
        print("Second_Arguments : Any Numeric Value")
        exit()
    
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : Name_of_Script First_Arguments Second_Arguments")
        exit()
    
    
#start of automation script
if __name__ == "__main__":
    main()