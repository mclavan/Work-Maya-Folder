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
	pm.button(label='Test Button')
	pm.text(label='Text Information', width=200)
	pm.separator(width=200)

	pm.checkBox(label='On and Off')
	pm.floatSliderGrp(label='Slider', field=True)


	window_object.show()

	print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))

'''
window_object = pm.window(title='Test Window')
window_object.show()
print('Window: {0} Created, type:{1}.'.format(window_object, type(window_object)))
'''

