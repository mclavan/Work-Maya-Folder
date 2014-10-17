'''
gui_04_pymelObjects.py 

How to Run:

import gui_04_pymelObjects
gui_04_pymelObjects.gui() 

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
	pm.checkBox(label='On / Off')

	'''
	pm.intField(min=2, value=2)
	pm.intField(min=2, value=4)
	pm.intField(min=2, value=2)
	'''

	pm.button(label='Check the Check', command=current_checkBox_value)
	pm.button(label='Create Lattice', command=create_lattice)
	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

def current_checkBox_value(*args):
	checkBox_value = 0
	print('Current Check Box Value: {0}'.format(checkBox_value))

def create_lattice(*args):
	lattice_x = 2
	lattice_y = 4
	lattice_z = 2
	print('Lattice Created: [{0}, {1}, {2}]'.format(lattice_x, lattice_y, lattice_z))
