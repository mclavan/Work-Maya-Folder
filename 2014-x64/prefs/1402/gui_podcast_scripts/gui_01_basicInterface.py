'''
gui_02_basicInterface.py


How to Run:

import gui_02_basicInterface
gui_02_basicInterface.gui()

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window')
	# with template:
	# Layout Required
	pm.columnLayout()
	
	# GUI Components go here!

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

