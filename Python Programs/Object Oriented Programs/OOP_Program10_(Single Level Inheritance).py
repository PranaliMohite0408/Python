class Base1:
    def __init__(self):
        print("Inside Base1..")
        self.A = 10
        
    def fun(self):
        print("fun of Bases1..")
        
class Base2:
    def __init__(self):
        print("Inside Base2..")
        self.B = 20
        
    def gun(self):
        print("gun of Base2..")

class Derived(Base1,Base2):
    def __init__(self):
        self.C = 30
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside Derived...")
        
    def sun(self):
        print("Inside sun of Derived...")


def main():
    dobj = Derived()


if __name__ == "__main__":
    main()