class Demo:
    A = 10                  #Class Variable
    
    def __init__(self):     
        self.B = 30          #Instance Variable
        
    def fun(self):          #Instance Method
        print("\nInside Instance Method Fun...")
        
    @classmethod
    def gun(cls):           #Class Method
        print("\nInside Class Method Gun... ")
        

def main():
    print("\nValue of Class Variable :",Demo.A)
    
    Demo.gun()
    
    obj1 = Demo()
    
    print("\nValue of Instance Variable :",obj1.B)
    obj1.fun()
        
        
if __name__ == "__main__":
    main()