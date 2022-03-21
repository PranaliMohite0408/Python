class Base:
    def __init__(self):
        self.i =10
        self.j = 20
        
    def fun(self):
        print("Base Fun")
        
    def gun(self):
        print("Base Gun")
        
class Derived(Base):
    def __init__(self):
        self.a = 10
        self.b = 21
        
    def fun(self):
        print("Derived fun")
    
    def sun(self):
        print("Derived Sun")

def main():
    bobj = Base()
    dobj = Derived()

if __name__ == "__main__":
    main()