'''
Lesson - Functions - Part 2
functions_02.py

How to Run:

import functions_02
reload(functions_02)

'''

print 'Lesson Active - Function - Part 1'

import pymel.core as pm 

'''
# Function Template 

def function_name():
	print 'Function Executed.'

'''

def delete_history():
	'''

	import functions_02
	reload(functions_02)
	functions_02.delete_history()
	'''

	# Delete Command deletes objects in 3D space.
	#   The ch flag is for deleting construction history.
	pm.delete(ch=True)

	print 'History has been deleted on all selected objects.'

def unlock_and_show():
	'''
	Unlock and make keyable all channels of the first selected object. 

	import functions_02
	functions_02.unlock_and_show()
	'''

	# Get first selected.
	selected = pm.ls(selection=True)
	first_selected = selected[0]


	# Using first selected. 
	# Make translate, scale, and visibility unlocked and keyable.


	print 'First selected object has all channels shown.'

	print 'And more info.'





