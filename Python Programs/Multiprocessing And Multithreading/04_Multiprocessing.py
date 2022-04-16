import os
import multiprocessing

def main():
    print("Number of Cores :",multiprocessing.cpu_count())

if __name__ == "__main__":
    main()