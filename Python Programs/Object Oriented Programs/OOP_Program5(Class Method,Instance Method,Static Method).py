class Demo:
    A = 10          # Class Varibale

    def __init__(self):
        print("Inside constructor")
        self.B  = 20        # Instance Variable

    def fun_instance(self):     # instance method
        print("Inside instance method")

    @classmethod
    def fun_class(cls):         # class method
        print("Inside class method")

    @staticmethod
    def fun_static():       # static method
        print("Inside static method")

    def __del__(self):
        print("Inside destructor")

def main():
    Demo.fun_class()
    Demo.fun_static()

    obj = Demo()        # Object Creation
    obj.fun_instance()

    #obj.fun_static()
    #obj.fun_class()

if __name__ == "__main__":
    main()

# Instane method
    #No decorator
    # self as a parameter
    # Call by the object name

# Class method
    # classmethod as a decorator
    # cls as a parameter
    # Call by the class name (object is also allowed)

# static method
    # staticmethod as a decorator
    # No parameter
    # Call by the class name (object is also alloewed)