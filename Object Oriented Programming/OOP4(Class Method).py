class Demo:
    A = 10                  #Class Variable    
    
    def __init__(self):        
        print("\nInside Constructor...")
        self.B = 20         #Instance Variable
    
    def fun_instance(self):
        print("\nInside Instance Method...")
        print(self.B)
        print(self.A)
        print(Demo.A)       #This is Correct Way to Access class Variable
        
    @classmethod
    def fun_class(cls):
        print("\nInside Class Method...")
        print(cls.A)
        print(Demo.A)
        
    @staticmethod   
    def fun_static():
        print("\nInside Static Method")
        
        
    def __del__(self):
        print("\nInside Destructor...")

def main():
        
    obj = Demo()            #Object Creation
    obj.fun_instance()
    print("\n")
    
    Demo.fun_class()
    
if __name__ == "__main__":
    main()