'''
gui_03_buttonClicks.py


How to Run:

import gui_03_events
reload(gui_03_events)
gui_03_events.gui()

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
	pm.button(width=300, command=button_pressed)
	pm.button(width=300, command=delete_history)
	pm.button(width=300, command=freeze_transforms)

	pm.checkBox(label='On / Off', 
		changeCommand=freeze_transforms,
		onCommand=button_pressed,
		offCommand=delete_history)

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

def button_pressed(*args):
	print('Button has been pressed.')

def delete_history(*args):
	print('History Delete on Selected.')

def freeze_transforms(*args):
	# pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	print('Transforms Frozen on Selected.')

