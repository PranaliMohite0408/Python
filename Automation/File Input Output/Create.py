def main():
    print("\nEnter the File Name that you want to create")
    name = input()
    
    fd = open(name,"x")

    print("File Gets created with the information as :",fd)

if __name__ == "__main__":
    main()