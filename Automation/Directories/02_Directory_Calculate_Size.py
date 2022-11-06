from sys import *
import os


def DirectoryWatcher(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filename in os.walk(path):
            print("Current Folder is : "+foldername)

            for subf in subfolder:
                print("Sub Folder of "+foldername+"is :"+subf)

            for filen in filename:
                print("File Inside "+foldername+"is :"+filen)
                if not filen.startswith("."):
                    print("With Size : ", os.path.getsize(filen))
                print(' ')
    else:
        print("Invalid Path")


def main():
    print("---------- Marvellous Infosystems ----------")

    print("Application Name : "+argv[0])

    if (len(argv) != 2):
        print("Error : Invalid Number of Arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to traverse specific directory and Display sizes of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of Input")

    except Exception:
        print("Error: Invalid Input")


if __name__ == "__main__":
    main()