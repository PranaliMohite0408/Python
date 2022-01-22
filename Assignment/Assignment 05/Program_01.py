"""
Write a program which contains one class named as Demo. Demo class contains two instance variables as no1 ,no2.
That class contains one class variable as Value.There are two instance methods of class as Fun and Gun which displays values of instance
variables. Initialise instance variable in init method by accepting the values from user. 
After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
"""

class Demo:
   
    Value = 0
    
    def _init__(self,no1,no2):
        self.no1 = 0
        self.no2 = 0
    
    def Fun(self):
        self.no1 = int(input("\nEnter First Number of Fun Method =>"))
        print(self.no1)
            
        self.no2 = int(input("\nEnter Second Number of Fun Method =>"))
        print(self.no2)
        
    
    def Gun(self):
        self.no1 = int(input("\nEnter First Number of Gun Method =>"))
        print(self.no1)
        
        self.no2 = int(input("\nEnter Second Number of Gun Method =>"))
        print(self.no2)

def main():
    
    Obj1 = Demo()
    Obj2 = Demo()
    
    print("Demonstration of Obj1")
    
    Obj1.Fun()
    Obj1.Gun()
    
    print("Demonstration Of Obj2")
    
    Obj2.Fun()
    Obj2.Gun()
    

if __name__ == "__main__":
    main()