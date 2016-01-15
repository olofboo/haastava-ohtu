####################################
#Ohtuv   version control system    #
#       by Olli Bjorkqvist         #
#  HAS NO ERROR CONTROL IN PLACE!  #
####################################

from datetime import datetime
import os
import sys
import shutil
import glob

path_to_find = ".ohtuv"

#init - check if directory .ohtuv exists in path and create it if not
def init_repo():
	if not os.path.exists(path_to_find):
		os.makedirs(path_to_find)
	print("Initialization ok!")
	exit()

#find_repo - checks if path_to_find exists in path or in parent directories
#			 returns the path to it if found, or exits cleanly if not
def find_repo():
	if os.path.exists(path_to_find):
		return path_to_find
	while not os.path.exists(path_to_find):
		if os.path.abspath(path_to_find) == "/"+path_to_find:
			print("Directory " +path_to_find+ " cannot be found.")
			exit()
		return path_to_find

#save - save the file with stamp+filename into the first .ohtuv directory
#		example: 6.9.2015.15:34.filename.ext
def save_file(orig_file):
	stamp = datetime.strftime(datetime.now(), '%d.%m.%Y.%H:%M')
	#placeholder filename, should be using orig_file
	filename = stamp+"cocks.txt"
	path_to_save = find_repo()
	print("Saving: " + filename + " to " + path_to_save)
	savefile = os.path.join(path_to_save, filename)
	shutil.copy2(orig_file, savefile)
	exit()

#restore 	- find a list of files with matching filename and date. prompt
#			  which one to choose if multiple hits. copy chosen one to path
#			  as filename.ext
def restore_file(date, orig_file):
	path_to_load = find_repo()
	loadfile = os.path.join(path_to_load, date+"*"+orig_file)
	files = glob.glob(loadfile)
	for name in files:
		print str(files.index(name)) + " " + name
	choice = input("Please choose which version to restore (CTRL+C to cancel): ")
	restorefile = files[choice]
	print("Restoring: " + restorefile + " as " + orig_file)
	shutil.copy2(restorefile, orig_file)
	exit()

#placeholder stuff for testingses
#print(find_repo())
#restore_file("15.01.2016", "cocks.txt")
#save_file("cocks.txt")

def main():
	if sys.argv[1] == "init":
		init_repo()
	if sys.argv[1] == "save":
		save_file(sys.argv[2])
	if sys.argv[1] == "restore":
		restore_file(sys.argv[2], sys.argv[3])

if __name__ == '__main__':
	main()
