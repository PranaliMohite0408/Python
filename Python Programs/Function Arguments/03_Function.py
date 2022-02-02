#Default Argument

def Area(radius,PI = 3.14):
    Ans = 0.0;
    Ans = PI * radius * radius
    return Ans

def main():
    print("Enter Radius of Circle :");
    value = float(input());
    
    ret = 0.0
    ret = Area(value)
    #ret = Area(value,7.10)
    #ret = Area(PI = 7.10, radius = value)
    
    print("Area of Circle is :",ret);
    

if __name__ == "__main__":
    main();