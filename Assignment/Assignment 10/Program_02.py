"""
Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc.
"""

import sys
import os

def ExtensionChanger(path):

	flag = os.path.isabs(path)
	if flag == False:
		path = os.path.abspath(path)

	exist = os.path.isdir(path)

	if exist:
		cnt = 0;
		for foldername, subfolder, filename in os.walk(path):
			for f in filename:
				if f.endswith(sys.argv[2]):
					base, ext = f.split(".")
					os.rename(foldername+"/"+f,foldername+"/"+base+sys.argv[3])
					print("Success.")
	else:
		print("Invalid path.")


def main():
	print("--- Assignment 10 ---\n")
	print("Application Name : ", sys.argv[0], "\n")

	if len(sys.argv)!=4:

		if sys.argv[1].lower() == '-h':
			print("Enter dictionary name and file extension. So that we can give you all files with that extension as an output.")
			print("Syntax      : python3 Program_02.py <Folder Name> <Extension of a file>")
			print("For Example : python3 Program_02.py Demo .txt .doc")
		else:
			print("Error : Invalid number of Arguments.")
			print("Please use -h for help")
			exit()

	try:
		
		ExtensionChanger(sys.argv[1])

	except Exception:

		print("Something is going wrong...")
		print(Exception)

	finally:

		print("\nThank you for using my application.")


if __name__ == '__main__':
	main()