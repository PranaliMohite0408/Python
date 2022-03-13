class Demo:
    
    def __init__(self):
        
        self.A = 10
        self.__B = 20       #Private Variable of Class   Abstraction
        
    def fun(self):
        print("Inside fun")
        
        self.__gun()

    def __gun(self):            #Private Method of class
    
        print("Inside gun")
    
    
def main():
    
    obj = Demo()
    
    obj.fun()
    
    #obj.__gun()


if __name__ == "__main__":
    main()