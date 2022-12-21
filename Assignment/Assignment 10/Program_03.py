"""
Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.
Usage : DirectoryCopy.py “Demo” “Temp”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files from Demo to Temp.
"""

import shutil
import os
import sys

def FileCopier(src,dest):

	flag = os.path.isabs(src)
	if flag == False:
		src = os.path.abspath(src)

	src_exist = os.path.isdir(src)
	
	flag = os.path.isabs(dest)
	if flag == False:
		dest = os.path.abspath(dest)

	if os.path.isdir(dest) == False:
		os.mkdir(dest)
		dest_exist = os.path.isdir(dest)
	else:
		dest_exist = False
		print(dest+" already exist.")

	if src_exist and dest_exist:
		for foldername, subfolder, filename in os.walk(src):
			for f in filename:
				shutil.copy(foldername+"/"+f, dest)


def main():
	print("****Assignment10******");
	print("Application Name : ", sys.argv[0], "\n");

	if len(sys.argv)!=3 :

		if sys.argv[1].lower() == '-h':
			print("Enter src directory and Destination directory. It will copy src files to destination.");
			print("Syntax      : python3 Program_03.py <SRC Folder Name> <DEST Folder Name>");
			print("For Example : python3 Program_03.py Demo Demo1");
		else:
			print("Error : invalid number of arguments.");
			print("Please use -h for help");
			exit();

	try:
		
		if len(sys.argv) == 3:	
			FileCopier(sys.argv[1],sys.argv[2]);

	except Exception:

		print("Something is going wrong...");
		print(Exception);

	finally:

		print("\nThank you for using my application.");


if __name__ == '__main__':
	main()