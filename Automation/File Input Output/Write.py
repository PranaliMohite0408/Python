def main():
    print("\nEnter the File Name that you want to Open")
    name = input()
    
    fd = open(name,"w")
    #fd = open(name,"a")            //For Append data

    print("Enter the Data that you want to write in the file")
    data = input()
    
    fd.write(data)
    
    fd.close()
    
if __name__ == "__main__":
    main()