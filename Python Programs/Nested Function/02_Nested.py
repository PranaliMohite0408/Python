def Outer():            #0X100
    
    print("Inside Outer Function")
    
    def Inner():        #0X200
        print("Inside Inner Function")

    return Inner        #0X200

def main():
    
    func_Name = Outer() #its call to the outer function
    func_Name() #its call to the inner function
    
if __name__ == "__main__":
    main()