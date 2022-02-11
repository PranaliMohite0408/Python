def Maximum(value1,value2):
    if(value1 > value2):
        return value1
    else:
        return value2
    

def main():
    print("Enter First Number :")
    No1 = int(input())
    
    print("Enter Second Number :")
    No2 = int(input())
    
    ret = Maximum(No1,No2)
    
    print("Maximum Number is :",ret)

if __name__ == "__main__":
    main()