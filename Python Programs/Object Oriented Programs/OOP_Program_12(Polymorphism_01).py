class Demo:
    def __init__(self):
        self.i = 10
        self.j = 20

    def Add(self,a):
        print("Inside Add With One Parameter")
        
    def Add(self,a,b):
        print("Inside Add with Two Parameter")

def main():
    obj = Demo()

if __name__ == "__main__":
    main()