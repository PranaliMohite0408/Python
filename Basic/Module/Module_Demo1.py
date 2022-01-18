import Addition_Module  

def main():
    print("Addition Application")
    
    print("Inside Module...",__name__)
    
    No1 = int(input("Enter First Number : "))
    
    No2 = int(input("Enter Second Number :"))
    
    Ans = Addition_Module.Addition(No1,No2)
    
    print("Addition is :",Ans)
	
if __name__ == "__main__":
	main()