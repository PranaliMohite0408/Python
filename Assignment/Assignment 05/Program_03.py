"""
Write a program which contains one class named as Arithmetic. Arithmetic class contains two instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0. There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division(). Accept method will accept value of Value1 and Value2 from user. 
Addition() method will perform addition of Value1 ,Value2 and return result. Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result. Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
"""
class Arithmetic:
    
    def __init__(self):
        Value1 = 0
        Value2 = 0
        
    def Accept(self):
        self.Value1 = int(input("\nEnter First Number =>"))
        self.Value2 = int(input("\nEnter Second Number =>"))
    
    def Addition(self):
        Add = self.Value1 + self.Value2
        print("\nAddition of Two Number is =>",Add)
        
    def Subtraction(self):
        Sub = self.Value1 - self.Value2
        print("\nSubtraction of Two Number is =>",Sub)
        
    def Multiplication(self):
        Mult = self.Value1 * self.Value2
        print("\nMultiplication of Two Number is =>",Mult)
        
def main():

    obj = Arithmetic()
    obj.Accept()
    obj.Addition()
    obj.Subtraction()
    obj.Multiplication()


if __name__ == "__main__":
    main()
