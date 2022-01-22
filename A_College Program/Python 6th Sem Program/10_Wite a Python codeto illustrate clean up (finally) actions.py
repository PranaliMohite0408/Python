x = int(input("Value of x: "))
y = int(input("Value of y: "))
def divide(x,y):
    try:
    #floor division: gives only fractional part as answer    
        result = x//y
    except ZeroDivisionError:
        print("Sorry !you are dividing by zero")
    else:
        print("Yeah! Your Answer is :",result)
    finally:
        print("I'm finally clause,alwalys raised !")
#Look at parameters and not the working of Program
divide(x,y)        
