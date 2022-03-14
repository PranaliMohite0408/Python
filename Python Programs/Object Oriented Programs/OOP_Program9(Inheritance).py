class Base:
    
    def __init__(self):
        print("Inside Base Constructor")
        self.A = 10
        
    def fun(self):
        print("Base Fun")
    
################################################

class Derived(Base):
    
    def __init__(self):
        #Base.__init__(self)
        super().__init__()
        print("Inside Derived Constructor")
        self.B = 20
        
    def gun(self):
        print("Derived fun")
        
        
def main():
    
    dobj = Derived()
    dobj.fun()
    print(dobj.A)


if __name__ == "__main__":
    main()