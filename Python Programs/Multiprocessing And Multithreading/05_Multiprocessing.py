import os
import multiprocessing

def Square(No):
    return No*No

def main():
    data = [5,3,1,4,8,2]
    result = list()
    for i in range(len(data)):
        #print(Square(data[i]))
        result.append(Square(data[i]))
    
    print("Result is :",result)

if __name__ == "__main__":
    main()