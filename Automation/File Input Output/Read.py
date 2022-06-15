import os


def main():
    print("\nEnter the File Name that you want to Open")
    name = input()
    
    if os.path.exists(name):
    
        fd = open(name,"r")
        print(type(fd))
        data = fd.read(5)
           
        print("Data from File is :",data)
        
        fd.close()

    else:
        print("There is no Such File")
    
if __name__ == "__main__":
    main()