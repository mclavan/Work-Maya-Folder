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

	global on_off_checkBox, dx_field, dy_field, dz_field
	# GUI Components go here!
	on_off_checkBox = pm.checkBox(label='On / Off')

	# Integer Fields
	dx_field = pm.intField(min=2, value=2)
	dy_field = pm.intField(min=2, value=4)
	dz_field = pm.intField(min=2, value=2)
	

	pm.button(label='Check the Check', command=current_checkBox_value)
	pm.button(label='Create Lattice', command=create_lattice)
	pm.button(label='Reset Lattice Field', command=reset_lattice)
	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

def current_checkBox_value(*args):
	checkBox_value = on_off_checkBox.getValue()
	print('Current Check Box Value: {0}'.format(checkBox_value))

def create_lattice(*args):
	lattice_x = dx_field.getValue()
	lattice_y = dy_field.getValue()
	lattice_z = dz_field.getValue()
	print('Lattice Created: [{0}, {1}, {2}]'.format(lattice_x, lattice_y, lattice_z))


def reset_lattice(*args):
	dx_field.setValue(2)
	dy_field.setValue(4)
	dz_field.setValue(2)
	print('Lattice Fields Reset: [{0}, {1}, {2}]'.format(0, 0, 0))
