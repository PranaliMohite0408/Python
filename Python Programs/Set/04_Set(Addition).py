from functools import reduce

def Addition(a,b):
    return a+b
           
def main():
    Size = int(input("Enter Number of Elements =>"))
    
    data = set()
    
    for i in range(Size):
        no = int(input("\nEnter Set Elements=>"))
        data.add(no)
    
    print(data)
    
    print(type(data))
    
    ret = reduce(Addition,data)
    
    print("\nAddition is =>",ret)


if __name__ == "__main__":
    main()
    