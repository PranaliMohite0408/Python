def main():

           #Python, PPA, LSP, Angular
           #  0  ,   1  ,  2  ,  3
    #fees = [12500,15000,21000,15500];
    fees = {"Python":12500,"PPA":15000,"LSP":21000,"Angular":15500};
    
    print(fees);
    
    print("Please enter batch name :");
    batch = input();
    
    print("Thank you for selecting:",batch);
    
    print("Fees are :",fees[batch]);
        


if __name__ == "__main__":
    main();