#! python3
# deleteUnneededFiles.py - walks through a folder tree  and searches for
# exceptionally large files or folders (> 100MB.)
# Prints these files with their absolute path to the screen.
# Colin McNicholl: 12/10/2017.

import os


def deleteUnneeded(folder):
	folder = os.path.abspath(folder)
	for folderName, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			fileSize = os.path.getsize(folderName + '/' + filename)
			if int(fileSize) < 10000000:
				continue
			#os.unlink(filename)  # commented out to protect against accidental deletion.
			print('Deleting ' + filename + '...')  # Print out to verify working correctly.
			
deleteUnneeded('C:\\Users\\Colin\\Documents')
print('Done')
			
