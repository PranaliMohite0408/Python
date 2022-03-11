class Demo:
    A = 10          # Class Varibale

    def __init__(self):
        print("Inside constructor")
        self.B  = 20        # Instance Variable

    def fun_instance(self):     # instance method
        print("Inside instance method")
        print(self.B)
        print(self.A)
        print(Demo.A)       # this is the correct way to access class variable

    @classmethod
    def fun_class(cls):         # class method
        print("Inside class method")
        print(cls.A)
        print(Demo.A)
        # print(cls.B)

    @staticmethod
    def fun_static():       # static method
        print("Inside static method")
        print(Demo.A)
        # print(Demo.B)
        
    def __del__(self):
        print("Inside destructor")

def main():
    Demo.fun_static()

if __name__ == "__main__":
    main()

# Instane method
    #No decorator
    # self as a parameter
    # Call by the object name
    # Can access instance as well as class variable

# Class method
    # classmethod as a decorator
    # cls as a parameter
    # Call by the class name
    # Can acess only class variable

# static method
    # staticmethod as a decorator
    # No parameter
    # Call by the class name
    # Can acess class variable using class name