def Addition(No1,No2):
    Ans = 0;
    
    Ans = No1 + No2;
    
    return Ans;


def main():
    print("Enter First Number :");
    value1 = int(input());
    
    print("Enter Second Number :");
    value2 = int(input());
    
    
    #Keyword Arguments
    ret = Addition(No2 = value1,No1 = value2);
    print("Addition is :",ret);


if __name__ == "__main__":
    main();