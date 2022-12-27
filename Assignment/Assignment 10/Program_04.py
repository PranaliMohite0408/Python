"""
Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp.
"""

import shutil;
import os;
import sys;

def FileCopier(src,dest,extension):

	flag = os.path.isabs(src);
	if flag == False:
		src = os.path.abspath(src)

	src_exist = os.path.isdir(src);
	
	flag = os.path.isabs(dest);
	if flag == False:
		dest = os.path.abspath(dest);

	if os.path.isdir(dest) == False:
		os.mkdir(dest);
		dest_exist = os.path.isdir(dest);
	else:
		dest_exist = False;
		print(dest+" already exist.");

	cnt = 0;

	if src_exist and dest_exist:
		for foldername, subfolder, filename in os.walk(src):
			for f in filename:
				if f.endswith(extension):
					cnt += 1;
					shutil.copy(foldername+"/"+f, dest);
	if cnt == 0 and dest_exist:
		print("Files with "+extension+" doesn't exist in "+src);
	elif dest_exist and src_exist:
		print("Files with "+extension+" copied over "+dest+" and file count is "+str(cnt));


def main():
	print("----------Assignment 10-----------");
	print("Application Name : ", sys.argv[0], "\n");

	if len(sys.argv)!=4 :

		if sys.argv[1].lower() == '-h':
			print("Enter src directory and Destination directory. It will copy mentioned src files to destination.");
			print("Syntax      : pytthon Program_04.py <SRC Folder Name> <DEST Folder Name> <Extension>");
			print("For Example : python Program_04.py Demo1 pyfiles .py");
		else:
			print("Error : invalid number of arguments.");
			print("Please use -h for help");
			exit();

	try:
		
		if len(sys.argv) == 4:	
			FileCopier(sys.argv[1],sys.argv[2],sys.argv[3]);

	except Exception:

		print("Something is going wrong...");
		print(Exception);

	finally:

		print("\nThank you for using my application.");


if __name__ == '__main__':
	main()