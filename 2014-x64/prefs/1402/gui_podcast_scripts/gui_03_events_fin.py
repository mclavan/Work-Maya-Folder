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
	pm.button(command=button_pressed)
	pm.button(command=delete_history)
	pm.button(command=freeze_transforms)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

def button_pressed(*args):
	print('Button has been pressed.')

def delete_history(*args):
	pm.delete(ch=True)
	print('History Delete on Selected.')

def freeze_transforms(*args):
	pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	print('Transforms Frozen on Selected.')

