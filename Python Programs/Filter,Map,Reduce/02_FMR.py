from functools import reduce
    
CheckEven = lambda no : (no % 2 == 0)

Increment = lambda no : no + 2

Addition = lambda a,b : a + b

def main():
    
    data = [5,7,6,8,4]
    
    print("Original data :",data)
    
    #filter(fnction,list)
    newdata = list(filter(CheckEven,data))
    print("Data after filter :",newdata)
    
    #map(function,list)
    incrementdata = list(map(Increment,newdata))
    print("Data after map :",incrementdata)
    
    #reduce(function,list)
    ret = reduce(Addition,incrementdata)
    print("Data after reduce :",ret)


if __name__ == "__main__":
    main()