'''
gui_03_buttonClicks.py


How to Run:

import gui_03_buttonClicks
gui_03_buttonClicks.gui()

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
	pm.button()
	pm.button()
	pm.button()

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

def button_pressed():
	print('Button has been pressed.')

def delete_history():
	print('History Delete on Selected.')

def freeze_transforms():
	print('Transforms Frozen on Selected.')

