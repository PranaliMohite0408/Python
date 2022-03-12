#Named Function
def Add(a,b):
    return a+b
 
 
#Lambda Function
AddX = lambda a,b : a+b

 
def main():
    ret = Add(10,20)
    print("Addition is :",ret)
    
    ret = AddX(11,20)
    print("Addition is :",ret)
    
    print(type(Add))
    print(type(AddX))
    print(type(lambda a,b : a+b))
    print(lambda a,b : a+b)
    
    
if __name__ == "__main__":
    main()