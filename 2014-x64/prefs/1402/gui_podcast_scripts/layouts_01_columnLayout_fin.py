'''
layouts_01_columnLayout.py


How to Run:

import layouts_01_columnLayout

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window', width=200)

	# Layout Required
	# rowSpacing and columnOffset
	pm.columnLayout(rowSpacing=5, columnOffset=['both', 10])
	
	# GUI Components go here!
	pm.button(width=200)
	pm.button(width=200)
	pm.button(width=200)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))


# Create slider that will manipulate column layout settings




