import os

def main():
    print("\nEnter the File Name that you want to Open")
    name = input()
    
    if os.path.exists(name):
        os.remove(name)
        print("File gets Deleted")

    else:
        print("There is no Such File")
    
if __name__ == "__main__":
    main()