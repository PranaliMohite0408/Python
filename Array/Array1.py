import array as ARR

def main():
    print("Demonstration of Array in Python")

    data = ARR.array('i',[10,20,30,40])

    print(data)
    print("Length of array : ",len(data))
    print("Type is : ",type(data))

    print(data[0])
    print(data[1])

    print("Data from array")
    for i in range(len(data)):
            print(data[i])

    print("Second for loop")
    for no in data:
        print(no, end = "\t")

if __name__ == "__main__":
    main()