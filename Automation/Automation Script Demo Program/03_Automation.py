#import statements of necessary
from sys import*

def Addition(iNo1, iNo2):
    Ans = iNo1 + iNo2
    return Ans

#Entry point of automation script
def main():
    print("--------Marvellous Infosystem : Automation1--------")
    print("script Name :", argv[0])
    print("Number of Arguments Accepted :",len(argv)-1)
    
    
    if(len(argv)>3) or (len(argv)<2):       #validator
        print("Invalid Number of Arguments")
        print("Use -u flag for Usage")
        print("Use -h flag for help")
        exit()
    
    if(len(argv) == 2):
        if(argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : Script is used to Perform the addition of 2 Numbers")
            print("First_Arguments : Any Numeric Value")
            print("Second_Arguments : Any Numeric Value")
            exit()        
        elif(argv[1] == "-h") or (argv[1] == "-H"):
            print("Help : Name_of_Script First_Arguments Second_Arguments")
            exit()
        else:
            print("There is No such flag")
    
    if(len(argv) == 3):
        try:
        
            iRet = Addition(int(argv[1]), int(argv[2]))
            print("Addition is :",iRet)
        
        except Exception:
            print("Exception While executing the script")
            print("Please check the input or contact the Developer")
        
    
#start of automation script
if __name__ == "__main__":
    main()