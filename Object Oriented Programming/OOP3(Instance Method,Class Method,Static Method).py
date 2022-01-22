class Demo:
    A = 10                  #Class Variable    
    
    def __init__(self):        
        print("\nInside Constructor...")
        self.B = 20         #Instance Variable
    
    def fun_instance(self):
        print("\nInside Instance Method...")
    
    @classmethod
    def fun_class(cls):
        print("\nInside Class Method...")
        
    @staticmethod   
    def fun_static():
        print("\nInside Static Method")
        
        
    def __del__(self):
        print("\nInside Destructor...")

def main():
    
    Demo.fun_class()
    Demo.fun_static()
    
    obj = Demo()            #Object Creation
    obj.fun_instance()
    
    #obj.fun_class()
    #obj.fun_static()
    
    
if __name__ == "__main__":
    main()