def fun():
    print("Inside fun")

def gun(func_Name):
    print("Inside gun")
    func_Name()
    
def main():
    gun(fun)

if __name__ == "__main__":
    main()