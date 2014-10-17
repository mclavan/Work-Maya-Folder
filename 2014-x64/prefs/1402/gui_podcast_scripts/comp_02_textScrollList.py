'''
gui_01_window.py 

How to Run:

import gui_01_window
gui_01_window.gui() 

'''

import pymel.core as pm 

def gui():
	'''
	Interface function. 
	'''
	window_object = pm.window(title='Test Window')

	# Layout Required

	# GUI Components go here!

	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

