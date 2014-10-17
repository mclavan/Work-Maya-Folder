'''
gui_02_components.py 

How to Run:

import gui_02_components
gui_02_components.gui() 

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window')

	# Layout Required
	pm.columnLayout()

	# GUI Components go here!
	# Basic

	# checkBox

	# sliders

	# check out separate podcast on groups.

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

