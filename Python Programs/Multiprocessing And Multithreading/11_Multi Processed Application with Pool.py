import os
import multiprocessing
import time


def CheckEvenOdd(x):
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"


def multiprocessing_func(x):
    time.sleep(2)
    print("PID is {} Input : {} results {}".format(os.getpid(), x, CheckEvenOdd(x)))


if __name__ == "__main__":
    print("Mult processed application with Pool")

    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func,range(0,8))
    pool.close
    endtime = time.time()

    print(f'That took {endtime - starttime} seconds')