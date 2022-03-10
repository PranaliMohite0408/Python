class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside destructor")

def main():
    print("Inside main")
    obj = Demo()
    print("End of main")

if __name__ == "__main__":
    main()
    print("End of application")