'''
critique_check.py
Michael Clavan

Description:

How to Run:

'''

import os
import glob


server_path = '/Volumes/cri1/Dropbox'
file_paths = glob.glob(os.path.join(server_path, '*.ma'))

class Student_Critique():
	def __init__(self, file_path):
		self.file_path = file_path

	def break_up(self):
		file_path, file_name = os.path.split(self.file_path) 


		self.name = os.path.split(file_name)

print file_paths

file_path, file_name = os.path.split(file_paths[0])
file_pieces = os.path.splitext(file_name)[0].split('_')[0:-3]
print file_pieces
print file_path, file_name


# I will need a list of all the students in the current class.  Then present the ones that are not on the list. 
# I will also like this tool to tell me students that I have critiqued in the previous classes.

# This means this will have to be exported to an external file.  Possibliy named under the class.
