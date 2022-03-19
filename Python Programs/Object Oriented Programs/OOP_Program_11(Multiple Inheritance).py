class Base1:
    def __init__(self):
        print("Inside Base1..")
        
    def fun(self):
        print("fun of Bases1..")
        
class Base2:
    def __init__(self):
        print("Inside Base2..")
        
    def fun(self):
        print("fun of Base2..")

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside Derived...")

def main():
    dobj = Derived()
    dobj.fun()

if __name__ == "__main__":
    main()