def main():

           #Python, PPA, LSP, Angular
           #  0  ,   1  ,  2  ,  3
    fees = [12500,15000,21000,15500];
    
    print(fees);
    
    print("Please enter batch name :");
    batch = input();
    
    print("Your entered batch name is :",batch);
    
    if batch == "PPA":
        print("Fees are :",fees[1]);
    elif batch == "LSP":
        print("Fees are :",fees[2]);
    elif batch == "Python":
        print("Fees are :",fees[0]);
    elif batch == "Angular":
        print("fees are :",fees[3]);
    else:
        print("There is no such batch in marvellous");
        


if __name__ == "__main__":
    main();