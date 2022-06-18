def main():
    print("\nEnter the File Name that you want to Open")
    name = input()
    
    fd = open(name,"rb")
    #fd = open(name,"r")
    
    data = fd.read(5)
    
    fd.seek(3,1)
    
    data = fd.read()
    
    print(data)
    
if __name__ == "__main__":
    main()
    
    
    #1 - Beginning
    #2 - current
    #3 - End 
    
     