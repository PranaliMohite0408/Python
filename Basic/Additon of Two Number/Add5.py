def Addition(Value1,Value2):
	Result = Value1 + Value2
	return Result
	
def main():
	print("Addition Application....")
	
	No1 = int(input("Enter First Number:"))
	No2 = int(input("Enter Second Number:"))
	
	Ret = Addition(No1,No2)
	
	print("Addition of Two Number is:",Ret)
	
if __name__ == "__main__":
	main()

