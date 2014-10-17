'''
gui_04_inputs.py 

How to Run:

import gui_04_inputs
reload(gui_04_inputs)
gui_04_inputs.gui() 

'''

import pymel.core as pm 

def gui():
	global window_object
	window_object = pm.window(title='Test Window', width=200)

	# Layout Required
	pm.columnLayout()

	# GUI Components go here!
	# Check Box
	global on_off_checkBox
	on_off_checkBox = pm.checkBox(label='On / Off', changeCommand=get_checkBox_value)

	# Integer Fields
	global width_field, height_field
	width_field = pm.intField(min=5, max=600, value=300)
	height_field = pm.intField(min=5, max=600, value=300)
	pm.button(label='Resize Window', width=200, command=change_window_size)
	
	# Text Field
	pm.textField(text='Text Information')
	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))


'''
Getting Values
'''
def get_checkBox_value(*args):
	on_off_value = on_off_checkBox.getValue()
	print 'Check Box Value', on_off_value

'''
Manipulating the window. 
'''
# Window size
def change_window_size(*args):
	window_width = width_field.getValue()
	window_height = height_field.getValue()
	window_object.setWidth(window_width)
	window_object.setHeight(window_height)
	print 'Window Size Changed.'




