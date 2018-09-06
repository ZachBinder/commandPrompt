"""
Program: fileSystem.py
Author: Zach Binder

Provies a menu-driven tool for navigating a file system and gathering information on files.
"""
import os, os.path

QUIT = '7'
COMMANDS = ('1', '2','3','4','5','6','7')

MENU = """\n1 List the current directory
2 Move up
3 Move down
4 Number of files in a directory
5 Size of the directory in bytes
6 Search for a file name.
7 Quit the program.\n"""

def main():
	while True:
		print(os.getcwd())
		print(MENU)
		command = acceptCommand()
		runCommand(command)
		if command == QUIT:
			print("Have a splended remainder of your day!")
			break
def acceptCommand():
	"""Inputs and returns a legitmate command number"""
	command = input("Enter a number: ")
	if command in COMMANDS:
		return command
	else:
		print("Error: command not recognized")
		return acceptCommand()

def runCommand(command):
	"""Selects and runs a command based on the users menu choice"""
	if command == '1':
		listCurrentDir(os.getcwd())
	elif command == '2':
		moveUp()
	elif command == '3':
		moveDown(os.getcwd())
	elif command == '4':
		print("The total number of files is", countFiles(os.getcwd))
	elif command == '5':
		print("The total number of bytes is", countBytes(os.getcwd))
	elif command == '6':
		target = input("Enter the file name you are looking for: ")
		fileList = findFiles(target, os.getcwd())
		if not fileList:
			print("File not found")
		else:
			for f in fileList:
				print(f)

def listCurrentDir(dirName):
	"""Prints a list of the Current Working Directories contents."""
	lyst = os.listdir(dirName)
	for element in lyst:
		print(elements)

def moveUp():
	"""Move up to the parent directory unless the cwd is the root"""
	os.chdir("..")

def moveDown(currentDir):
	"""Moves down to the named subdirectory if it exists."""
	newDir = input("Enter the directory name: ")
	if os.path.exists(currentDir + os.sep + newDir) and os.path.isdir(newDir):
		os.chdir(newDir)
	else:
		print("ERROR: That name is not found.")

def countFiles(path):
	"""Returns the number of files in the cwd and all its subdirectories"""
	count = 0
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count += 1
		else:
			os.chdir(element)
			count += countedFiles(os.getcwd())
			os.chdir("..")
	return count

def countBytes(path):
	"""Returns the nunmber of bytes in the cwd and all its subdirectories"""
	count = 0
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			count += os.path.getsize(element)
		else:
			os.chdir(element)
			count += countBytes(os.getcwd())
			os.chdir("..")
	return count

def findFiles(target, path):
	"""Returns a list of the file names that contain the target string in the cwd and all its subdirectories"""
	files = []
	lyst = os.listdir(path)
	for element in lyst:
		if os.path.isfile(element):
			if target in element:
				files.append(path + os.sep + element)
			else:
				os.chdir(element)
				files.extend(findFiles(target, os.getcwd()))
				os.chdir("..")
	return files 

if __name__ == '__main__':
	main()