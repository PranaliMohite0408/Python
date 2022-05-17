from sys import *


def main():
    print("Number of Command line arguments are :", len(argv))

    print("Name of Application is :", argv[0])

    print("Datatype of argument is :",type(argv[1]))

    print("Command line arguments are :")

    for data in argv:
        print(data)

    Ans = int(argv[1]) + int(argv[2])

    print("Addition is :",Ans)


if __name__ == "__main__":
    main()