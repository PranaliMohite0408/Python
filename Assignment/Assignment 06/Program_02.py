"""
Write a program which contains one class named as BankAccount. BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5. 
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.
"""
class BankAccount:
    ROI = 10.5
    
    def __init__(self):
        self.Name = input("\nEnter Your Name =>")
        self.Amount = float(input("\nEnter Your Amount =>"))
        
    def Deposit(self):
        self.Deposit_Amount = float(input("\nEnter Your Deposit Amount =>"))
        self.Amount = self.Deposit_Amount + self.Amount
    
    def Withdraw(self):
        self.withdrawn_Amount = float(input("\nEnter Your withdrawn Amount =>"))
        self.Total_Amount = self.Amount - self.withdrawn_Amount
        
    def CalculateIntrest(self):
        self.Rate_of_Interest = self.Total_Amount * BankAccount.ROI
        
    def Display(self):
        print("\n********* Your Details *********")
        print("\nName =>",self.Name)
        print("Your Deposit Amount is =>",self.Deposit_Amount)
        print("Your Withdraw Amount is=>",self.withdrawn_Amount)
        print("Your Total Amount is =>",self.Total_Amount)
        print("ROT of Your Amount is =>",self.Rate_of_Interest)
        print("\n********* Thank You *********")
def main():
    Obj1 = BankAccount()
    Obj1.Deposit()
    Obj1.Withdraw()
    Obj1.CalculateIntrest()
    Obj1.Display()


if __name__ == "__main__":
    main()
