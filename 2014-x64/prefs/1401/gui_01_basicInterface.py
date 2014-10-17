'''
gui_01_basicInterface.py


How to Run:

import gui_01_basicInterface
reload(gui_01_basicInterface)
gui_01_basicInterface.gui()

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window', width=300, height=300)
	pm.columnLayout()

	pm.button(label='Press Me', width=300)
	pm.button(label='Press Me', width=300)
	pm.button(label='Press Me', width=300)

	window_object.show()

	print('Window Created:')

