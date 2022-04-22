import os
import time

def CheckEvenOdd(x):
    print("PID is :",os.getpid())
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    print("Single process single thread application")
    print("PID of main process :",os.getpid())

    starttime = time.time()

    for i in range(0,8):
        time.sleep(2)
        ret = CheckEvenOdd(i)
        print('Input : {} results {}'.format(i, ret))

    print('Application took {} seconds'.format(time.time() - starttime))


if __name__ == "__main__":
    main()